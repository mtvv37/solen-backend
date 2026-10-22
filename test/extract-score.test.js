'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const path = require('path');
const { extractHome, extractProduct } = require('../src/audit/extract');
const { computeScore } = require('../src/audit/score');
const { buildLeaks, resolveAssumptions } = require('../src/audit/leaks');

const read = (f) => fs.readFileSync(path.join(__dirname, 'fixtures', f), 'utf8');
const home = extractHome(read('home.html'), 'https://maisonlune.fr/');
const good = extractProduct(read('product-good.html'), 'https://maisonlune.fr/products/robe-lin-sable');
const weak = extractProduct(read('product-weak.html'), 'https://maisonlune.fr/products/tee');

test('home: detects Shopify, viewport and the first product link (query stripped)', () => {
  assert.equal(home.isShopify, true);
  assert.equal(home.hasViewport, true);
  assert.equal(home.productUrl, 'https://maisonlune.fr/products/robe-lin-sable');
});

test('good product page: structured data, reviews, images, trust, cart', () => {
  assert.equal(good.name, 'Robe lin sable');
  assert.deepEqual(good.price, { value: 89, currency: 'EUR', visible: true });
  assert.equal(good.socialProof.ratingValue, 4.7);
  assert.equal(good.socialProof.reviewCount, 128);
  assert.ok(good.socialProof.widgets.includes('Judge.me'));
  assert.equal(good.images.count, 4, 'robe1_800x and the JSON-LD robe1 are the same image');
  assert.equal(good.images.withAlt, 4);
  assert.ok(good.description.words >= 80);
  assert.equal(good.cart.hasAddToCart, true);
  assert.equal(good.cart.likelyAboveFoldMobile, true);
  assert.equal(good.cart.variantPicker, 'buttons');
  assert.equal(good.cart.hasDynamicCheckout, true);
  assert.equal(good.cart.hasQuantity, true);
  assert.deepEqual({ ...good.trust, paymentIcons: good.trust.paymentIcons >= 3 }, { shipping: true, returns: true, guarantee: true, securePayment: true, paymentIcons: true });
  assert.deepEqual(good.weight.thirdPartyScriptHosts, ['static.klaviyo.com']);
});

test('weak product page: gaps are detected', () => {
  assert.equal(weak.structuredData.hasProduct, false);
  assert.equal(weak.price.value, null);
  assert.equal(weak.socialProof.widgets.length, 0);
  assert.equal(weak.images.count, 3);
  assert.equal(weak.images.withAlt, 0);
  assert.equal(weak.cart.imagesBeforeCart, 3);
  assert.equal(weak.cart.likelyAboveFoldMobile, false);
  assert.equal(weak.cart.variantPicker, 'dropdown');
  assert.equal(weak.hasViewport, false);
  assert.equal(weak.weight.thirdPartyScriptHosts.length, 7);
});

test('score is deterministic, bounded, and ranks the good page above the weak one', () => {
  const a = computeScore(home, good);
  const b = computeScore(home, good);
  assert.deepEqual(a, b);
  const w = computeScore(home, weak);
  for (const s of [a, w]) {
    assert.ok(s.score >= 0 && s.score <= 100);
    assert.equal(s.categories.reduce((t, c) => t + c.max, 0), 100);
    for (const c of s.categories) assert.ok(c.score >= 0 && c.score <= c.max, c.id);
  }
  assert.ok(a.score >= 90, `good page scored ${a.score}`);
  assert.ok(w.score <= 40, `weak page scored ${w.score}`);
});

test('leaks: top 5 by impact, € computed from stated assumptions marked [hypothèse]', () => {
  const { checks } = computeScore(home, weak);
  const assumptions = resolveAssumptions({}, weak);
  assert.equal(assumptions.monthlyVisitors, 10000);
  assert.equal(assumptions.averageOrderValue, 50);
  assert.ok(assumptions.notes.filter((n) => n.includes('[hypothèse]')).length >= 3);
  const leaks = buildLeaks(checks, assumptions);
  assert.equal(leaks.length, 5);
  assert.equal(leaks[0].id, 'review_widget');
  for (const l of leaks) {
    assert.ok(l.monthlyLossEur.low <= l.monthlyLossEur.high);
    assert.equal(l.estimate, true);
  }
  // 10 000 visitors × 1.5 % × 50 € = 7 500 €/month; reviews: 3–8 % → 225–600 €, rounded to the nearest 10
  assert.deepEqual(leaks[0].monthlyLossEur, { low: 230, high: 600 });
});

test('merchant inputs replace the default assumptions', () => {
  const a = resolveAssumptions({ monthlyVisitors: '25000', averageOrderValue: 70 }, good);
  assert.equal(a.monthlyVisitors, 25000);
  assert.equal(a.averageOrderValue, 70);
  assert.ok(a.notes[0].startsWith('Trafic mensuel indiqué'));
  const p = resolveAssumptions({}, good);
  assert.equal(p.averageOrderValue, 89);
});
