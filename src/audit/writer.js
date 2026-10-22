'use strict';
// Claude phrases the leaks in French. Numbers stay owned by the code:
// the prompt forbids figures in € or %, and any leak text that contains them
// is replaced by the deterministic template.
const Anthropic = require('@anthropic-ai/sdk');

const MODEL = 'claude-opus-5-5';

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['summary', 'leaks'],
  properties: {
    summary: { type: 'string' },
    leaks: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['id', 'explanation', 'test'],
        properties: {
          id: { type: 'string' },
          explanation: { type: 'string' },
          test: { type: 'string' },
        },
      },
    },
  },
};

const SYSTEM = `Tu rédiges un audit de conversion pour une boutique Shopify, en français, pour son ou sa propriétaire.
Règles :
- Tu reçois des constats mesurés par un script sur le code source de deux pages (accueil et une fiche produit). Tu ne vois pas la boutique.
- N'écris aucun montant en euros ni aucun pourcentage : les chiffres sont affichés à part par le logiciel.
- Chaque constat est une observation, pas une preuve. Formule les causes comme des hypothèses et propose un test, jamais une promesse de résultat.
- Si un constat est marqué "estimate", dis que c'est une estimation faite sans afficher la page.
- Ton direct, concret, sans jargon ni superlatifs. Vouvoiement.
- explanation : 2 phrases maximum, ce qui a été vu et pourquoi ça peut freiner l'achat.
- test : 1 phrase, ce que vous testeriez en premier.
- summary : 2 phrases maximum sur l'état général de la page.`;

function templateText(leak) {
  return {
    id: leak.id,
    explanation: leak.why || `${leak.title}.`,
    test: leak.fix,
  };
}

function templateSummary(score) {
  if (score >= 75) return 'La fiche produit couvre l’essentiel. Les gains restants viennent de détails à tester un par un.';
  if (score >= 50) return 'La fiche produit a des bases correctes, mais plusieurs freins à l’achat restent visibles.';
  return 'Plusieurs éléments qui rassurent et guident l’acheteur manquent sur cette fiche produit.';
}

const FORBIDDEN = /€|\beur(os)?\b|%|pour ?cent/i;

function mergeWritten(leaks, written) {
  const byId = new Map((written.leaks || []).map((w) => [w.id, w]));
  return leaks.map((leak) => {
    const w = byId.get(leak.id);
    const ok = w && typeof w.explanation === 'string' && typeof w.test === 'string'
      && !FORBIDDEN.test(w.explanation) && !FORBIDDEN.test(w.test)
      && w.explanation.length <= 600 && w.test.length <= 300;
    return { ...leak, ...(ok ? { explanation: w.explanation.trim(), test: w.test.trim() } : templateText(leak)), id: leak.id };
  });
}

// client is injectable for tests. Returns { summary, leaks, writer: 'claude' | 'template' }.
async function writeLeaks({ score, leaks, product, client } = {}) {
  const fallback = () => ({ summary: templateSummary(score), leaks: leaks.map((l) => ({ ...l, ...templateText(l) })), writer: 'template' });
  const anthropic = client || (process.env.ANTHROPIC_API_KEY ? new Anthropic({ timeout: 25000, maxRetries: 0 }) : null);
  if (!anthropic || !leaks.length) return fallback();

  const facts = {
    score,
    produit: product.name,
    constats: leaks.map((l) => ({ id: l.id, titre: l.title, piste: l.fix, details: l.facts, estimate: l.id === 'cta_mobile' })),
  };
  try {
    const response = await anthropic.beta.messages.create({
      model: MODEL,
      max_tokens: 4000,
      betas: ['server-side-fallback-2026-07-01'],
      fallbacks: 'default',
      system: SYSTEM,
      output_config: { effort: 'low', format: { type: 'json_schema', schema: SCHEMA } },
      messages: [{ role: 'user', content: `Constats (JSON) :\n${JSON.stringify(facts)}` }],
    });
    if (response.stop_reason === 'refusal' || response.stop_reason === 'max_tokens') return fallback();
    const text = response.content.filter((b) => b.type === 'text').map((b) => b.text).join('');
    const parsed = JSON.parse(text);
    const summary = typeof parsed.summary === 'string' && !FORBIDDEN.test(parsed.summary) ? parsed.summary.trim() : templateSummary(score);
    return { summary, leaks: mergeWritten(leaks, parsed), writer: 'claude' };
  } catch (err) {
    if (process.env.NODE_ENV !== 'test') console.error('[audit] writer fallback:', err && err.message);
    return fallback();
  }
}

module.exports = { writeLeaks, mergeWritten, templateSummary, MODEL };
