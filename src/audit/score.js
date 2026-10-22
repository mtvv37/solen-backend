'use strict';
// Deterministic, weighted score out of 100. Same input, same score: no AI here.
// Thresholds are Solen's internal heuristics [hypothèse], not industry standards.

const CATEGORIES = {
  socialProof: { label: 'Preuve sociale', max: 20 },
  productPage: { label: 'Fiche produit', max: 25 },
  trust: { label: 'Réassurance', max: 20 },
  performance: { label: 'Poids de la page', max: 15 },
  mobile: { label: 'Mobile', max: 10 },
  checkout: { label: 'Accès au panier', max: 10 },
};

function tier(value, steps) {
  // steps: [[condition, points], ...] evaluated in order; first match wins
  for (const [ok, pts] of steps) if (ok(value)) return pts;
  return 0;
}

function computeScore(home, product) {
  const p = product;
  const checks = [];
  const add = (id, category, max, points, facts = {}) => checks.push({ id, category, max, points, passed: points >= max, facts });

  // Preuve sociale (20)
  add('review_widget', 'socialProof', 8, p.socialProof.widgets.length || p.structuredData.hasRating ? 8 : 0, { widgets: p.socialProof.widgets });
  add('rating_shown', 'socialProof', 6, p.socialProof.ratingValue ? 6 : 0, { ratingValue: p.socialProof.ratingValue });
  add('review_volume', 'socialProof', 6, tier(p.socialProof.reviewCount, [[(n) => n >= 10, 6], [(n) => n >= 1, 3]]), { reviewCount: p.socialProof.reviewCount });

  // Fiche produit (25)
  add('image_count', 'productPage', 7, tier(p.images.count, [[(n) => n >= 4, 7], [(n) => n >= 2, 4], [(n) => n >= 1, 1]]), { count: p.images.count });
  const altRatio = p.images.inPage ? p.images.withAlt / p.images.inPage : 0;
  add('image_alt', 'productPage', 3, p.images.inPage === 0 ? 0 : altRatio >= 0.8 ? 3 : altRatio >= 0.5 ? 1.5 : 0, { withAlt: p.images.withAlt, inPage: p.images.inPage });
  add('description', 'productPage', 6, tier(p.description.words, [[(n) => n >= 80, 6], [(n) => n >= 30, 3]]), { words: p.description.words });
  add('price_clear', 'productPage', 4, p.price.value !== null && p.price.visible ? 4 : p.price.visible ? 2 : 0, { price: p.price.value, currency: p.price.currency });
  add('add_to_cart', 'productPage', 5, p.cart.hasAddToCart ? 5 : 0);

  // Réassurance (20)
  add('shipping_info', 'trust', 5, p.trust.shipping ? 5 : 0);
  add('returns_info', 'trust', 5, p.trust.returns ? 5 : 0);
  add('guarantee', 'trust', 3, p.trust.guarantee ? 3 : 0);
  add('secure_payment', 'trust', 2, p.trust.securePayment ? 2 : 0);
  add('payment_icons', 'trust', 5, tier(p.trust.paymentIcons, [[(n) => n >= 3, 5], [(n) => n >= 1, 3]]), { paymentIcons: p.trust.paymentIcons });

  // Poids de la page (15)
  const kb = Math.round(p.weight.htmlBytes / 1024);
  add('html_weight', 'performance', 5, tier(kb, [[(n) => n < 300, 5], [(n) => n < 600, 3]]), { htmlKb: kb });
  add('script_count', 'performance', 5, tier(p.weight.scriptCount, [[(n) => n <= 40, 5], [(n) => n <= 70, 3]]), { scriptCount: p.weight.scriptCount });
  const tp = p.weight.thirdPartyScriptHosts.length;
  add('third_party', 'performance', 5, tier(tp, [[(n) => n <= 5, 5], [(n) => n <= 10, 3]]), { hosts: p.weight.thirdPartyScriptHosts });

  // Mobile (10)
  add('viewport', 'mobile', 4, p.hasViewport || home.hasViewport ? 4 : 0);
  add('cta_mobile', 'mobile', 4, p.cart.likelyAboveFoldMobile || p.cart.hasStickyCart ? 4 : 0, { imagesBeforeCart: p.cart.imagesBeforeCart, sticky: p.cart.hasStickyCart, estimate: true });
  add('variant_picker', 'mobile', 2, p.cart.variantPicker === 'dropdown' ? 0 : 2, { picker: p.cart.variantPicker });

  // Accès au panier (10)
  add('dynamic_checkout', 'checkout', 5, p.cart.hasDynamicCheckout ? 5 : 0);
  add('quantity', 'checkout', 2, p.cart.hasQuantity ? 2 : 0);
  add('structured_data', 'checkout', 3, p.structuredData.hasProduct && p.structuredData.hasOffer ? 3 : p.structuredData.hasProduct ? 1.5 : 0);

  const categories = Object.entries(CATEGORIES).map(([id, c]) => {
    const pts = checks.filter((k) => k.category === id).reduce((s, k) => s + k.points, 0);
    return { id, label: c.label, max: c.max, score: Math.round(pts * 10) / 10 };
  });
  const score = Math.round(categories.reduce((s, c) => s + c.score, 0));
  return { score, categories, checks };
}

module.exports = { computeScore, CATEGORIES };
