'use strict';
// Turns raw HTML (no JavaScript rendering) into audit findings.
// Everything here is a static read of the page source: measures that depend on
// rendering (e.g. "visible without scrolling") are marked as estimates.
const cheerio = require('cheerio');

const REVIEW_WIDGETS = [
  ['Judge.me', /jdgm|judge\.me|judgeme/i],
  ['Yotpo', /yotpo/i],
  ['Loox', /loox/i],
  ['Okendo', /okendo/i],
  ['Stamped', /stamped\.io|stamped-/i],
  ['Reviews.io', /reviews\.io|reviewsio/i],
  ['Junip', /junip/i],
  ['Trustpilot', /trustpilot/i],
  ['Shopify Product Reviews', /\bspr-|shopify-product-reviews/i],
  ['Avis Vérifiés', /avis-verifies|netreviews/i],
];

const PAYMENT_RE = /\b(visa|mastercard|master card|american express|amex|paypal|apple pay|google pay|shop pay|carte bancaire|maestro|klarna|alma)\b/i;
const TRUST_PATTERNS = {
  shipping: /livraison|expédi|shipping|delivery|envoi (offert|gratuit)/i,
  returns: /retours?\b|rembours|échange|returns?\b|refund/i,
  guarantee: /garantie|garanti\b|guarantee|warranty|satisfait ou rembours/i,
  securePayment: /paiement (100 ?% )?sécuris|secure (payment|checkout)|ssl/i,
};

function isShopifyHtml(html) {
  return /cdn\.shopify\.com|Shopify\.theme|shopify-section|myshopify\.com|\/cdn\/shop\//i.test(html);
}

function textOf($) {
  const clone = $.root().clone();
  clone.find('script, style, noscript, template, svg').remove();
  return clone.text().replace(/\s+/g, ' ').trim();
}

function parseJsonLd($) {
  const items = [];
  $('script[type="application/ld+json"]').each((_, el) => {
    const raw = $(el).contents().text();
    try {
      const data = JSON.parse(raw);
      const queue = Array.isArray(data) ? [...data] : [data];
      while (queue.length) {
        const node = queue.shift();
        if (!node || typeof node !== 'object') continue;
        items.push(node);
        if (Array.isArray(node['@graph'])) queue.push(...node['@graph']);
      }
    } catch {
      /* invalid JSON-LD is ignored; it simply doesn't count as structured data */
    }
  });
  return items;
}

function typeIs(node, type) {
  const t = node['@type'];
  return Array.isArray(t) ? t.includes(type) : t === type;
}

function imageKey(src) {
  try {
    const u = new URL(src, 'https://x.invalid');
    const file = u.pathname.split('/').pop() || '';
    return file.replace(/_(\d+x\d*|\d*x\d+|pico|icon|thumb|small|compact|medium|large|grande|original|master)(?=[._@])/gi, '').replace(/@\dx/, '').toLowerCase();
  } catch {
    return src;
  }
}

function pageWeight($, html, pageUrl) {
  const host = (() => { try { return new URL(pageUrl).hostname; } catch { return ''; } })();
  const scripts = $('script');
  const externalHosts = new Set();
  scripts.each((_, el) => {
    const src = $(el).attr('src');
    if (!src) return;
    try {
      const h = new URL(src, pageUrl).hostname;
      if (h !== host && !/shopify(cdn)?\.com$|shopifysvc\.com$/.test(h)) externalHosts.add(h);
    } catch { /* ignore malformed src */ }
  });
  return {
    htmlBytes: Buffer.byteLength(html, 'utf8'),
    scriptCount: scripts.length,
    thirdPartyScriptHosts: [...externalHosts].sort(),
  };
}

function extractHome(html, pageUrl) {
  const $ = cheerio.load(html);
  const base = new URL(pageUrl);
  let productUrl = null;
  $('a[href*="/products/"]').each((_, el) => {
    if (productUrl) return;
    try {
      const u = new URL($(el).attr('href'), base);
      if (u.hostname === base.hostname && /\/products\/[^/?#]+/.test(u.pathname)) {
        u.search = '';
        u.hash = '';
        productUrl = u.toString();
      }
    } catch { /* ignore */ }
  });
  const viewport = $('meta[name="viewport"]').attr('content') || '';
  return {
    url: pageUrl,
    isShopify: isShopifyHtml(html),
    title: $('title').first().text().trim().slice(0, 140),
    productUrl,
    hasViewport: /width\s*=\s*device-width/i.test(viewport),
    weight: pageWeight($, html, pageUrl),
  };
}

function extractProduct(html, pageUrl) {
  const $ = cheerio.load(html);
  const text = textOf($);
  const jsonLd = parseJsonLd($);
  const product = jsonLd.find((n) => typeIs(n, 'Product')) || null;

  // ---- price
  const offers = product && (Array.isArray(product.offers) ? product.offers[0] : product.offers);
  const ldPrice = offers ? Number(offers.price ?? offers.lowPrice) : NaN;
  const metaPrice = Number($('meta[property="product:price:amount"], meta[property="og:price:amount"]').attr('content'));
  const price = Number.isFinite(ldPrice) && ldPrice > 0 ? ldPrice : Number.isFinite(metaPrice) && metaPrice > 0 ? metaPrice : null;
  const currency = (offers && offers.priceCurrency) || $('meta[property="product:price:currency"], meta[property="og:price:currency"]').attr('content') || null;
  const visiblePrice = $('[class*="price"]').filter((_, el) => /\d/.test($(el).text())).length > 0;

  // ---- social proof
  const rating = product && product.aggregateRating;
  const ratingValue = rating ? Number(rating.ratingValue) : null;
  const reviewCount = rating ? Number(rating.reviewCount ?? rating.ratingCount) : null;
  const widgets = REVIEW_WIDGETS.filter(([, re]) => re.test(html)).map(([name]) => name);

  // ---- product images (gallery first, then any product image as fallback)
  const gallerySel = '[class*="product__media"] img, [class*="product-gallery"] img, [class*="product__photo"] img, [class*="product-single__photo"] img, [data-product-media] img, [class*="product-media"] img, media-gallery img';
  let imgs = $(gallerySel);
  if (!imgs.length) imgs = $('img').filter((_, el) => /\/products\/|\/files\//.test($(el).attr('src') || $(el).attr('data-src') || $(el).attr('srcset') || ''));
  const keys = new Map();
  imgs.each((_, el) => {
    const src = $(el).attr('src') || $(el).attr('data-src') || ($(el).attr('srcset') || '').split(/[ ,]/)[0];
    if (!src) return;
    const key = imageKey(src);
    const alt = ($(el).attr('alt') || '').trim();
    if (!keys.has(key)) keys.set(key, { alt });
    else if (alt && !keys.get(key).alt) keys.get(key).alt = alt;
  });
  const ldImages = product ? [].concat(product.image || []).map((i) => (typeof i === 'string' ? i : i && i.url)).filter(Boolean) : [];
  ldImages.forEach((src) => { const k = imageKey(src); if (!keys.has(k)) keys.set(k, { alt: '' , fromLd: true }); });
  const imageCount = keys.size;
  const domImages = [...keys.values()].filter((v) => !v.fromLd);
  const imagesWithAlt = domImages.filter((v) => v.alt.length > 0).length;

  // ---- description
  const descSel = '[class*="product__description"], [class*="product-single__description"], [class*="product-description"], [itemprop="description"], .product .rte';
  let description = '';
  $(descSel).each((_, el) => { const t = $(el).text().replace(/\s+/g, ' ').trim(); if (t.length > description.length) description = t; });
  if (!description && product && product.description) description = String(product.description).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  const descriptionWords = description ? description.split(' ').filter(Boolean).length : 0;

  // ---- add to cart and what sits before it
  const cartForm = $('form[action*="/cart/add"]').first();
  const hasAddToCart = cartForm.length > 0 && cartForm.find('button, input[type="submit"]').length > 0;
  let imagesBeforeCart = 0;
  if (cartForm.length) {
    const galleryNodes = new Set(imgs.toArray());
    for (const el of $('img, form[action*="/cart/add"]').toArray()) {
      if (el === cartForm.get(0)) break;
      if (galleryNodes.has(el)) imagesBeforeCart += 1;
    }
  }
  const variantSelects = cartForm.find('select[name="id"], select[name^="options"], select[id*="ption"]').length;
  const variantButtons = cartForm.find('input[type="radio"]').length + $('variant-radios, [class*="swatch"], [class*="variant-button"]').length;
  const hasDynamicCheckout = /shopify-payment-button|shopify-accelerated-checkout|dynamic-checkout/i.test(html);
  const hasStickyCart = $('[class*="sticky"]').filter((_, el) => /cart|atc|add/i.test($(el).attr('class') || '')).length > 0;

  // ---- trust
  const trust = Object.fromEntries(Object.entries(TRUST_PATTERNS).map(([k, re]) => [k, re.test(text)]));
  let paymentIcons = 0;
  $('[class*="payment"] svg, [class*="payment"] img, svg title, img[alt]').each((_, el) => {
    const label = `${$(el).attr('alt') || ''} ${$(el).text() || ''} ${$(el).attr('aria-labelledby') || ''}`;
    if (PAYMENT_RE.test(label)) paymentIcons += 1;
  });
  if (!paymentIcons && $('[class*="payment-icon"], [class*="icon--payment"], .payment-icons li').length) paymentIcons = $('[class*="payment-icon"], [class*="icon--payment"], .payment-icons li').length;

  const viewport = $('meta[name="viewport"]').attr('content') || '';

  return {
    url: pageUrl,
    isShopify: isShopifyHtml(html),
    name: (product && product.name) || $('h1').first().text().trim().slice(0, 140) || null,
    structuredData: {
      hasProduct: Boolean(product),
      hasOffer: Boolean(offers),
      hasRating: Boolean(rating),
    },
    price: { value: price, currency, visible: visiblePrice || price !== null },
    socialProof: {
      ratingValue: Number.isFinite(ratingValue) ? ratingValue : null,
      reviewCount: Number.isFinite(reviewCount) ? reviewCount : null,
      widgets,
    },
    images: { count: imageCount, withAlt: imagesWithAlt, inPage: domImages.length },
    description: { words: descriptionWords },
    cart: {
      hasAddToCart,
      imagesBeforeCart,
      // Estimate only: no rendering, so we infer from source order (most themes stack gallery above the buy box on mobile).
      likelyAboveFoldMobile: hasAddToCart && imagesBeforeCart <= 1,
      variantPicker: variantSelects > 0 && variantButtons === 0 ? 'dropdown' : variantButtons > 0 ? 'buttons' : 'none',
      hasDynamicCheckout,
      hasStickyCart,
      hasQuantity: cartForm.find('input[name="quantity"]').length > 0,
    },
    trust: { ...trust, paymentIcons },
    hasViewport: /width\s*=\s*device-width/i.test(viewport),
    weight: pageWeight($, html, pageUrl),
  };
}

module.exports = { extractHome, extractProduct, isShopifyHtml, imageKey };
