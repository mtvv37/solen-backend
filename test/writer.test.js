'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { writeLeaks, MODEL } = require('../src/audit/writer');

const leaks = [
  { id: 'review_widget', title: 'Aucun avis client visible sur la fiche produit', fix: 'Afficher des avis.', facts: {}, monthlyLossEur: { low: 230, high: 600 } },
  { id: 'cta_mobile', title: 'Bouton d’achat probablement trop bas sur mobile', fix: 'Tester un bouton collant.', facts: { estimate: true }, monthlyLossEur: { low: 150, high: 450 } },
];
const product = { name: 'T-shirt' };

function fakeClient(payload, extra = {}) {
  const calls = [];
  return {
    calls,
    beta: { messages: { create: async (req) => { calls.push(req); return { stop_reason: 'end_turn', content: [{ type: 'text', text: JSON.stringify(payload) }], ...extra }; } } },
  };
}

test('uses Claude text, keeps code-owned numbers, sends the expected request', async () => {
  const client = fakeClient({ summary: 'Page correcte, la preuve sociale manque.', leaks: [
    { id: 'review_widget', explanation: 'Aucun avis n’apparaît près du prix.', test: 'Ajoutez la note sous le titre.' },
    { id: 'cta_mobile', explanation: 'Le bouton semble arriver après la galerie.', test: 'Testez un bouton collant.' },
  ] });
  const out = await writeLeaks({ score: 40, leaks, product, client });
  assert.equal(out.writer, 'claude');
  assert.equal(out.leaks[0].explanation, 'Aucun avis n’apparaît près du prix.');
  assert.deepEqual(out.leaks[0].monthlyLossEur, { low: 230, high: 600 });
  const req = client.calls[0];
  assert.equal(req.model, MODEL);
  assert.equal(req.fallbacks, 'default');
  assert.deepEqual(req.betas, ['server-side-fallback-2026-07-01']);
  assert.equal(req.output_config.format.type, 'json_schema');
  assert.equal('temperature' in req, false);
});

test('a leak text containing € or % is replaced by the template', async () => {
  const client = fakeClient({ summary: 'Résumé.', leaks: [
    { id: 'review_widget', explanation: 'Vous perdez 500 € par mois.', test: 'Ajoutez des avis.' },
    { id: 'cta_mobile', explanation: 'Le bouton est bas.', test: 'Gain de 10 %.' },
  ] });
  const out = await writeLeaks({ score: 40, leaks, product, client });
  assert.match(out.leaks[0].explanation, /^Aucun avis client visible/);
  assert.equal(out.leaks[1].test, 'Tester un bouton collant.');
});

test('refusal, invalid JSON or API error fall back to templates', async () => {
  const refusal = { beta: { messages: { create: async () => ({ stop_reason: 'refusal', content: [] }) } } };
  const broken = { beta: { messages: { create: async () => ({ stop_reason: 'end_turn', content: [{ type: 'text', text: '{oops' }] }) } } };
  const failing = { beta: { messages: { create: async () => { throw new Error('network'); } } } };
  for (const client of [refusal, broken, failing]) {
    const out = await writeLeaks({ score: 40, leaks, product, client });
    assert.equal(out.writer, 'template');
    assert.equal(out.leaks.length, 2);
    assert.ok(out.summary.length > 10);
  }
});

test('without an API key and no client, templates are used (no network)', async () => {
  const saved = process.env.ANTHROPIC_API_KEY;
  delete process.env.ANTHROPIC_API_KEY;
  try {
    const out = await writeLeaks({ score: 80, leaks, product });
    assert.equal(out.writer, 'template');
  } finally {
    if (saved !== undefined) process.env.ANTHROPIC_API_KEY = saved;
  }
});
