'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { isAllowed } = require('../src/audit/robots');

const SHOPIFY_LIKE = `
User-agent: *
Disallow: /admin
Disallow: /cart
Disallow: /checkout
Disallow: /*?*variant=*
Allow: /products/*?variant=public

User-agent: AhrefsBot
Disallow: /
`;

test('allows normal pages and blocks disallowed paths', () => {
  assert.equal(isAllowed(SHOPIFY_LIKE, '/'), true);
  assert.equal(isAllowed(SHOPIFY_LIKE, '/products/robe'), true);
  assert.equal(isAllowed(SHOPIFY_LIKE, '/admin/settings'), false);
  assert.equal(isAllowed(SHOPIFY_LIKE, '/products/robe?variant=12'), false);
  assert.equal(isAllowed(SHOPIFY_LIKE, '/products/x?variant=public'), true);
});

test('a group naming our bot overrides the * group', () => {
  const txt = 'User-agent: *\nDisallow:\n\nUser-agent: SolenAuditBot\nDisallow: /';
  assert.equal(isAllowed(txt, '/'), false);
  assert.equal(isAllowed('User-agent: *\nDisallow: /', '/products/a'), false);
});

test('empty or missing robots.txt allows everything; $ anchors', () => {
  assert.equal(isAllowed('', '/products/a'), true);
  assert.equal(isAllowed('User-agent: *\nDisallow: /*.json$', '/products/a.json'), false);
  assert.equal(isAllowed('User-agent: *\nDisallow: /*.json$', '/products/a.json?x=1'), true);
});
