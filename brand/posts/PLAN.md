# Plan des visuels — 90 posts X

> À valider avant génération. Source des posts : `docs/X_BUILD_IN_PUBLIC.md`. Généré par `brand/posts/_src/make_plan.py`.

## Résumé

- **40 visuels** sur 90 posts (50 en texte seul), dans la fourchette 30–45.
- **Mode** : 31 dark, 9 light (≈ 1 sur 4).
- **Principe** : le visuel montre l'information du post (chiffre sourcé, graphique, schéma, tableau, capture réelle), jamais la phrase du post reformulée. Plus de gabarits « Citation » ni « Opinion ».
- **Règles vérifiées par le script** : jamais deux posts consécutifs avec le même gabarit ; texte du visuel ≤ 12 mots.
- **Lisibilité** : message principal ≥ 48 px sur 1200×675 (vérifié à la génération, étape 2).
- **Aucune donnée inventée** : seuls chiffres = Store Leads 2026 (source secondaire, *à vérifier*), fourchettes du deck (présentées comme hypothèses), état réel du projet (0 client), prix hypothétique.

| Gabarit | Nombre |
|---|---|
| Audit annoté | 17 |
| Tableau (comparaison / checklist) | 8 |
| Schéma (processus / architecture) | 7 |
| Journal Day N | 5 |
| Chiffre clé | 2 |
| Graphique (données) | 1 |

## Choix validés (29/09/2026)

1. Kit de marque créé : `brand/BRAND.md`, `brand/tokens.css`, `brand/logo/final/`, gabarits dans `brand/templates/` (planche : `brand/templates/preview.html`).
2. Audits **mixtes, à dominante (b)** : capture réelle d'une page produit Shopify publique via Playwright quand la friction y est vraiment visible, marque masquée (logo, nom, URL, photos produit reconnaissables floutés), annotations en hypothèses. Sinon (a) wireframe générique. Si aucune page publique ne montre la friction, repli sur (a). Gabarit « Audit — with permission » prévu pour les audits demandés par des marchands.
3. Store Leads (n° 7 et 31) : gardés, avec « Source: Store Leads, 2026 » sur le visuel ; à vérifier par Thomas (TODO_INPUTS.md).
4. N° 18 : « 0 customers » gardé ; à confirmer le jour de publication (TODO_INPUTS.md).
5. N° 1, 5 et 43 : générés avec l'emplacement « SCREENSHOT HERE » ; captures réelles fournies par Thomas.

## Tableau

| Jour | N° | Post (1re ligne) | Thème | Visuel | Gabarit | Mode | Texte sur le visuel | Input requis |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | I'm building Solen in public. | Journal | oui | Journal Day N | dark | Day 1. Prototype runs. 0 customers. Building in public. | Capture réelle du prototype — visuel généré avec « SCREENSHOT HERE » (TODO_INPUTS) |
| 1 | 2 | Rule I'm setting for Solen from day one: | Opinion | oui | Tableau (comparaison / checklist) | dark | Observation → hypothesis → test → result: one example. | Exemple illustratif tiré de SOLEN_CONTEXT §3 (PDP mobile) ; ligne « result » = « not tested yet » — aucun résultat inventé |
| 1 | 3 | If you run a Shopify store: what was the last change you made to your product page, and how did you know if it worked? | Interviews | non | — | — | — | — |
| 2 | 4 | Shopify friction worth testing #1: | Friction (audit) | oui | Audit annoté (b) | dark | Add-to-cart below the fold? I'd test moving it up. | Capture Playwright, marque floutée — theme-taste-demo.myshopify.com (démo officielle de thème Shopify) : bouton d'ajout au panier à 1 174 px, écran 844 px |
| 2 | 5 | What Solen's prototype does today: | Journal | oui | Journal Day N | light | Day 2. What the prototype does, and doesn't. | Capture réelle du prototype — visuel généré avec « SCREENSHOT HERE » (TODO_INPUTS) |
| 2 | 6 | Free offer this week: send me your Shopify store link and I'll reply with 3 mobile frictions I'd test, with the reasoning. | Appel | non | — | — | — | — |
| 3 | 7 | Sizing Solen's market, part 1: | Journal | oui | Chiffre clé | dark | 2.87M live Shopify stores. | « Source: Store Leads, 2026 » affiché sur le visuel — à vérifier par Thomas avant publication (TODO_INPUTS) — mention sur le visuel : « Source: Store Leads, 2026 » |
| 3 | 8 | Sizing, part 2. The two numbers I'm guessing: | Journal | oui | Tableau (comparaison / checklist) | dark | Sizing inputs: one sourced number, two guesses. | Tableau : boutiques (Store Leads 2026) / part > 10k (5–15 %, hypothèse) / dépense (600–3 000 $, hypothèse) |
| 3 | 9 | Sizing, part 3. Result: a TAM between $86M and $1.29B, ~$430M in the middle. | Journal | oui | Graphique (données) | dark | TAM: $86M to $1.29B. A 15x range. | Barres bas / central / haut (86 M$ · 430 M$ · 1,29 Md$), libellées « hypotheses » |
| 4 | 10 | Shopify friction worth testing #2: | Friction (audit) | oui | Audit annoté (b) | light | Shipping cost only at checkout? I'd test showing it earlier. | Capture Playwright, marque floutée — theme-craft-demo.myshopify.com : page panier « Taxes and shipping calculated at checkout » |
| 4 | 11 | Most small e-commerce teams don't lack data. | Opinion | non | — | — | — | — |
| 4 | 12 | How I'm running merchant interviews: | Interviews | non | — | — | — | — |
| 5 | 13 | Why I'm not building a dashboard: | Opinion | non | — | — | — | — |
| 5 | 14 | Shopify friction worth testing #3: | Friction (audit) | oui | Audit annoté (a) | dark | Hidden size options? I'd test visible swatches. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 5 | 15 | Looking for a technical cofounder. | Appel | oui | Schéma (processus / architecture) | dark | What's built: script → API → database → analysis. | Aucun (architecture réelle : tracking script → Express/Vercel → Supabase → heatmap + LLM) |
| 6 | 16 | Interview question I rely on: | Interviews | non | — | — | — | — |
| 6 | 17 | Shopify friction worth testing #4: | Friction (audit) | oui | Audit annoté (a) | dark | Reviews buried at the bottom? I'd test stars near the price. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 6 | 18 | Honest status, week 1: | Journal | oui | Tableau (comparaison / checklist) | dark | Honest status: prototype yes, customers 0, revenue 0. | État réel à confirmer le jour de publication (« 0 customers ») |
| 7 | 19 | Most "AI CRO" pitches skip a step. | Opinion | oui | Schéma (processus / architecture) | light | Observation → Hypothesis → Test → Result | — |
| 7 | 20 | What I'm deliberately not doing yet: | Journal | non | — | — | — | — |
| 7 | 21 | Question for Shopify founders: | Interviews | non | — | — | — | — |
| 8 | 22 | Shopify friction worth testing #5: | Friction (audit) | oui | Audit annoté (b) | dark | Return policy in the footer? I'd test it near the CTA. | Capture Playwright, marque floutée — theme-refresh-demo.myshopify.com : infos retours uniquement dans le pied de page |
| 8 | 23 | Solen v0 architecture, no magic: | Journal | non | — | — | — | — |
| 8 | 24 | Autonomy ladder I'm testing with merchants: | Interviews | oui | Schéma (processus / architecture) | dark | Where would you stop? 1 · 2 · 3 · 4 | Échelle d'autonomie en 4 marches (SOLEN_CONTEXT §22) |
| 9 | 25 | Something I'm unsure about: the traffic threshold. | Journal | non | — | — | — | — |
| 9 | 26 | Shopify friction worth testing #6: | Friction (audit) | oui | Audit annoté (a) | dark | Slow images on mobile? I'd test compression first. | Aucun — wireframe générique (lenteur non visible sur une capture) |
| 9 | 27 | Things that should always stay human, in my view: | Opinion | non | — | — | — | — |
| 10 | 28 | I studied how Tally reportedly grew to millions in ARR, bootstrapped. Core loop: a "Made with Tally" badge every respondent sees. | Opinion | non | — | — | — | — |
| 10 | 29 | So what replaces a viral badge for an invisible product? | Opinion | non | — | — | — | — |
| 10 | 30 | Shopify friction worth testing #7: | Friction (audit) | oui | Audit annoté (a) | dark | Hidden free-shipping threshold? I'd test a progress bar. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 11 | 31 | Why Europe first for Solen, not the US: | Journal | oui | Chiffre clé | dark | ~38% of live Shopify stores are in the US. | « Source: Store Leads, 2026 » affiché sur le visuel — à vérifier par Thomas avant publication (TODO_INPUTS) — mention sur le visuel : « Source: Store Leads, 2026 » |
| 11 | 32 | Shopify friction worth testing #8: | Friction (audit) | oui | Audit annoté (a) | light | Size guide as a PDF? I'd test an inline drawer. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 11 | 33 | Pilot offer I'm testing: | Appel | oui | Tableau (comparaison / checklist) | dark | Pilot: what you get, what I ask. | Deux colonnes reprises de l'offre (GTM_STRATEGY §4) ; « no promised uplift » |
| 12 | 34 | Everything Solen recommends gets reviewed by me before a merchant sees it. | Journal | non | — | — | — | — |
| 12 | 35 | Uncomfortable truth: many small stores don't have enough traffic to A/B test every idea. | Opinion | non | — | — | — | — |
| 12 | 36 | Shopify friction worth testing #9: | Friction (audit) | oui | Audit annoté (a) | dark | Instant pop-up on mobile? I'd test a delay. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 13 | 37 | What I ask instead of "would you pay for this?": | Interviews | non | — | — | — | — |
| 13 | 38 | Shopify friction worth testing #10: | Friction (audit) | oui | Audit annoté (a) | dark | No delivery date? I'd test showing one near the CTA. | Aucun — wireframe générique (absence d'info difficile à montrer) |
| 13 | 39 | Warning for anyone testing in November: | Opinion | non | — | — | — | — |
| 14 | 40 | How I describe Solen in one line right now: | Journal | non | — | — | — | — |
| 14 | 41 | Shopify friction worth testing #11: | Friction (audit) | non | — | — | — | — |
| 14 | 42 | Shopify founders: what's the one metric you check every morning? | Interviews | non | — | — | — | — |
| 15 | 43 | What the prototype gets wrong today, openly: | Journal | oui | Journal Day N | dark | Day 15. What the prototype gets wrong. | Capture réelle de la sortie de /analyze, sans données marchand — « SCREENSHOT HERE » (TODO_INPUTS) |
| 15 | 44 | Shopify friction worth testing #12: | Friction (audit) | oui | Audit annoté (a) | light | Checkout button below upsells? I'd test pinning it. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 15 | 45 | Still looking for a technical cofounder. | Appel | non | — | — | — | — |
| 16 | 46 | My market sizing has one solid number and two guesses. I published it anyway. | Opinion | non | — | — | — | — |
| 16 | 47 | Shopify friction worth testing #13: | Friction (audit) | non | — | — | — | — |
| 16 | 48 | Interview ask: I'm talking to Shopify founders and e-commerce leads for 20 minutes. | Appel | non | — | — | — | — |
| 17 | 49 | Some bet on rebuilding e-commerce from scratch around AI. | Opinion | non | — | — | — | — |
| 17 | 50 | Shopify friction worth testing #14: | Friction (audit) | oui | Audit annoté (a) | dark | Out-of-stock but selectable? I'd test greying it out. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 17 | 51 | Guardrails any automated optimization should have: | Opinion | oui | Tableau (comparaison / checklist) | dark | Five guardrails before any automated change. | Checklist : control group · primary metric · stop rule · rollback · human sign-off |
| 18 | 52 | Why the first pilots will be done by hand: | Journal | non | — | — | — | — |
| 18 | 53 | Shopify friction worth testing #15: | Friction (audit) | non | — | — | — | — |
| 18 | 54 | Question for CRO people: | Interviews | non | — | — | — | — |
| 19 | 55 | Pricing hypothesis I'll test with pilots: ~€190/month. | Journal | oui | Schéma (processus / architecture) | light | €190/month: a price hypothesis, tested in pilots. | Échelle sans chiffres : outil gratuit ← Solen → agence (positionnement relatif, pas de prix concurrents inventés) |
| 19 | 56 | Shopify friction worth testing #16: | Friction (audit) | oui | Audit annoté (a) | dark | Payment options hidden until checkout? I'd test icons earlier. | Aucun — wireframe générique (absence d'info difficile à montrer) |
| 19 | 57 | What building in public means for me: | Opinion | non | — | — | — | — |
| 20 | 58 | Shopify friction worth testing #17: | Friction (audit) | oui | Audit annoté (a) | dark | No zoom, no scale? I'd test an in-hand photo. | Aucun — wireframe générique (absence de zoom non visible sur une capture) |
| 20 | 59 | Heatmaps show where people click. They don't show why. | Opinion | oui | Schéma (processus / architecture) | dark | Heatmap: shows where people click, not why. | Aucun (schéma deux colonnes : where / why) |
| 20 | 60 | Open offer, still running: send me your Shopify store link, get 3 mobile frictions I'd test, with the reasoning. | Appel | non | — | — | — | — |
| 21 | 61 | Three weeks of posting about a product with 0 paying customers. | Journal | oui | Journal Day N | light | Day 21. Tracking interviews, not followers. | Aucun (titre seul, sans chiffres) |
| 21 | 62 | Shopify friction worth testing #18: | Friction (audit) | non | — | — | — | — |
| 21 | 63 | Interview question I find most revealing: | Interviews | non | — | — | — | — |
| 22 | 64 | The learning-loop idea behind Solen, stated as a hypothesis: | Journal | oui | Schéma (processus / architecture) | dark | Context → behavior → friction → hypothesis → change → result | — |
| 22 | 65 | Shopify friction worth testing #19: | Friction (audit) | oui | Audit annoté (a) | dark | Cookie banner covering the CTA? I'd test a compact one. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 22 | 66 | Solo founder math: every hour on code is an hour not talking to merchants. | Journal | non | — | — | — | — |
| 23 | 67 | "Best practices" are other people's hypotheses that worked in their context. | Opinion | non | — | — | — | — |
| 23 | 68 | Shopify friction worth testing #20: | Friction (audit) | non | — | — | — | — |
| 23 | 69 | If you work at a Shopify agency or do CRO freelance: | Interviews | non | — | — | — | — |
| 24 | 70 | What a Solen pilot report looks like (structure only): | Journal | oui | Tableau (comparaison / checklist) | light | Pilot report: observation, hypothesis, change, metric. | Maquette vide du rapport (structure seulement, aucune donnée marchand) |
| 24 | 71 | Shopify friction worth testing #21: | Friction (audit) | oui | Audit annoté (a) | dark | Motion matters but no video? I'd test a short clip. | Aucun — wireframe générique (absence de vidéo difficile à montrer) |
| 24 | 72 | Consent isn't a later problem for Solen. | Opinion | non | — | — | — | — |
| 25 | 73 | A claim you'll often hear: "Visitors who watch the video convert 2x more." | Opinion | oui | Schéma (processus / architecture) | dark | Watchers convert more. Cause or selection? Randomize. | Schéma : groupe « regarde la vidéo » vs moitié tirée au hasard — aucun chiffre (le « 2x » du post est une citation typique, pas une donnée) |
| 25 | 74 | Shopify friction worth testing #22: | Friction (audit) | non | — | — | — | — |
| 25 | 75 | Cofounder search, honest version: | Appel | non | — | — | — | — |
| 26 | 76 | The question I use to pick Solen's first customers: | Journal | non | — | — | — | — |
| 26 | 77 | Shopify friction worth testing #23: | Friction (audit) | oui | Audit annoté (a) | dark | Reviews without photos? I'd test photo reviews first. | Aucun — wireframe générique (friction non trouvée sur les pages publiques testées) |
| 26 | 78 | What would make you trust a recommendation from software about your store? | Interviews | non | — | — | — | — |
| 27 | 79 | Kill criteria I set before starting, so I can't move the goalposts: | Journal | oui | Tableau (comparaison / checklist) | dark | Kill criteria, set before starting. | Tableau signal → décision (GTM_STRATEGY §5) |
| 27 | 80 | Shopify friction worth testing #24: | Friction (audit) | non | — | — | — | — |
| 27 | 81 | Pilot spots open for Shopify stores with 20k+ visitors/month. | Appel | non | — | — | — | — |
| 28 | 82 | "We know what to fix, we just never get to it" is a different problem from "we don't know what to fix". | Opinion | non | — | — | — | — |
| 28 | 83 | Shopify friction worth testing #25: | Friction (audit) | non | — | — | — | — |
| 28 | 84 | Reminder to myself at the end of month one: | Journal | oui | Journal Day N | dark | Day 28. 3 pilots. Honest notes. One decision. | — |
| 29 | 85 | What I'd build first if pilots confirm the problem: | Journal | non | — | — | — | — |
| 29 | 86 | Shopify friction worth testing #26: | Friction (audit) | non | — | — | — | — |
| 29 | 87 | Every store has more ideas to test than capacity to test them. | Opinion | oui | Tableau (comparaison / checklist) | light | Rank ideas: impact, confidence, effort. | Grille 3 colonnes (exemple de notation illustratif, libellé comme tel) |
| 30 | 88 | 30 days of posting about Solen. What stays the same: | Opinion | non | — | — | — | — |
| 30 | 89 | Shopify friction worth testing #27: | Friction (audit) | non | — | — | — | — |
| 30 | 90 | If you've read along this month: thank you. | Appel | non | — | — | — | — |
