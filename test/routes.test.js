'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const path = require('path');
const express = require('express');
const { createAuditRouter } = require('../src/audit/routes');
const { memoryStore } = require('../src/audit/store');

const read = (f) => fs.readFileSync(path.join(__dirname, 'fixtures', f), 'utf8');
const PAGES = {
  'https://maisonlune.fr/robots.txt': { body: 'User-agent: *\nDisallow: /admin', type: 'text/plain' },
  'https://maisonlune.fr/': { body: read('home.html') },
  'https://maisonlune.fr/products/robe-lin-sable': { body: read('product-weak.html') },
  'https://blocked.fr/robots.txt': { body: 'User-agent: *\nDisallow: /', type: 'text/plain' },
};
async function fakeFetch(url) {
  const key = String(url);
  const page = PAGES[key];
  if (!page) return { url: key, status: 404, headers: { 'content-type': 'text/html' }, body: 'not found' };
  return { url: key, status: 200, headers: { 'content-type': page.type || 'text/html; charset=utf-8' }, body: page.body };
}

async function startApp() {
  const store = memoryStore();
  const app = express();
  app.use(express.json());
  app.use(createAuditRouter({ store, deps: { fetch: fakeFetch } }));
  const server = await new Promise((r) => { const s = app.listen(0, () => r(s)); });
  const base = `http://127.0.0.1:${server.address().port}`;
  const call = (p, opts = {}) => fetch(base + p, { ...opts, headers: { 'Content-Type': 'application/json', 'X-Real-IP': opts.ip || '203.0.113.7' } });
  return { server, store, call };
}

test('full flow: create, partial report, unlock with consent, token, share image', async () => {
  delete process.env.ANTHROPIC_API_KEY;
  const { server, store, call } = await startApp();
  try {
    const created = await call('/api/audits', { method: 'POST', body: JSON.stringify({ url: 'maisonlune.fr' }) });
    assert.equal(created.status, 201);
    const { id, reportUrl } = await created.json();
    assert.match(id, /^[A-Za-z0-9_-]{22}$/);
    assert.equal(reportUrl, `/r/${id}`);

    const partial = await (await call(`/api/audits/${id}`)).json();
    assert.equal(partial.unlocked, false);
    assert.equal(partial.leakCount, 5);
    assert.equal(partial.leaks.filter((l) => !l.locked).length, 2);
    assert.equal(partial.leaks.filter((l) => l.locked).length, 3);
    assert.equal(partial.leaks[2].title, undefined, 'locked leaks expose no content');
    assert.ok(partial.score >= 0 && partial.score <= 100);
    assert.equal(partial.shopDomain, 'maisonlune.fr');

    const noConsent = await call(`/api/audits/${id}/unlock`, { method: 'POST', body: JSON.stringify({ email: 'a@b.fr' }) });
    assert.equal(noConsent.status, 400);
    const badEmail = await call(`/api/audits/${id}/unlock`, { method: 'POST', body: JSON.stringify({ email: 'nope', consent: true }) });
    assert.equal(badEmail.status, 400);
    assert.equal(store._leads.length, 0);

    const unlocked = await call(`/api/audits/${id}/unlock`, { method: 'POST', body: JSON.stringify({ email: ' Founder@MaisonLune.fr ', consent: true }) });
    assert.equal(unlocked.status, 200);
    const { token, report } = await unlocked.json();
    assert.equal(report.unlocked, true);
    assert.ok(report.leaks.every((l) => !l.locked && l.title && l.monthlyLossEur));
    assert.equal(store._leads[0].email, 'founder@maisonlune.fr');
    assert.equal(store._leads[0].consent, true);
    assert.ok(store._leads[0].consent_text.length > 20);

    const withToken = await (await call(`/api/audits/${id}?t=${encodeURIComponent(token)}`)).json();
    assert.equal(withToken.unlocked, true);
    const forged = await (await call(`/api/audits/${id}?t=${encodeURIComponent(token.slice(0, -2) + 'xx')}`)).json();
    assert.equal(forged.unlocked, false);

    const page = await call(`/r/${id}`);
    assert.equal(page.status, 200);
    const html = await page.text();
    assert.match(html, new RegExp(`/api/audits/${id}/og.png`));
    assert.match(page.headers.get('content-security-policy'), /frame-ancestors 'none'/);

    const og = await call(`/api/audits/${id}/og.png`);
    assert.equal(og.status, 200);
    assert.equal(og.headers.get('content-type'), 'image/png');
    const png = Buffer.from(await og.arrayBuffer());
    assert.deepEqual([...png.subarray(0, 4)], [0x89, 0x50, 0x4e, 0x47]);
  } finally {
    server.close();
  }
});

test('refuses internal targets, respects robots.txt, 404s unknown ids, rate-limits per IP', async () => {
  const { server, call } = await startApp();
  try {
    const ssrf = await call('/api/audits', { method: 'POST', body: JSON.stringify({ url: 'http://169.254.169.254/latest/meta-data' }), ip: '198.51.100.1' });
    assert.equal(ssrf.status, 400);
    const robots = await call('/api/audits', { method: 'POST', body: JSON.stringify({ url: 'https://blocked.fr' }), ip: '198.51.100.1' });
    // failed attempts count too: 6 attempts per hour per IP, successful or not
    for (let i = 0; i < 4; i += 1) await call('/api/audits', { method: 'POST', body: JSON.stringify({ url: 'http://localhost' }), ip: '198.51.100.1' });
    assert.equal((await call('/api/audits', { method: 'POST', body: JSON.stringify({ url: 'http://localhost' }), ip: '198.51.100.1' })).status, 429);
    assert.equal(robots.status, 422);
    assert.match((await robots.json()).error, /robots\.txt/);
    assert.equal((await call('/api/audits/not-an-id')).status, 404);
    assert.equal((await call('/api/audits/AAAAAAAAAAAAAAAAAAAAAA')).status, 404);
    assert.equal((await call('/r/AAAAAAAAAAAAAAAAAAAAAA')).status, 404);

    const statuses = [];
    for (let i = 0; i < 7; i += 1) {
      statuses.push((await call('/api/audits', { method: 'POST', body: JSON.stringify({ url: 'maisonlune.fr' }), ip: '192.0.2.50' })).status);
    }
    assert.deepEqual(statuses, [201, 201, 201, 201, 201, 201, 429]);
  } finally {
    server.close();
  }
});
