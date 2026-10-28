# Solen — prompts Base44 pour construire le produit du film de vision

À coller dans le builder Base44, **un prompt à la fois**, dans l'ordre. Attendre que chaque étape fonctionne (critères « Done when ») avant de passer à la suivante.

Ce que montre le film et où chaque partie est construite :

| Dans le film | Étape | Statut aujourd'hui |
|---|---|---|
| L'identité de la boutique comprise par Solen | 1 · Store profile | À construire |
| « 1,500+ product pages studied » | 2 · Benchmark | Le robot existe (GitHub), pas branché à l'app |
| 01 · Observe : la fuite sur mobile | 3 · Leak detection v2 | Partiel (`findLeaks`) |
| 02 · Propose : 100 hypothèses, 99 rejetées, 1 gardée | 4 · Hypothesis engine | À construire |
| « One suggestion a day. Or a week. You decide. » + Approve | 5 · Cadence + inbox | À construire |
| 04 · Learn : mémoire de la boutique | 6 · Change log + memory | À construire |
| 03 · Test : A/B sur 10 % du trafic, garde-fous | 7 · Controlled A/B | Plus tard, derrière un interrupteur |
| Une page par type de visiteur | 8 · Vision | Pas maintenant |

Après les étapes 1 à 5, Solen fait déjà ce que promet le film jusqu'à « Approve » : comprendre la boutique, trouver la fuite, proposer une seule suggestion à la cadence choisie. C'est le premier produit vendable en abonnement (prix à décider et à tester).

---

## Prompt 0 — Contexte et règles (à coller en premier)

```
You are working on Solen, an existing Base44 app (do not create a new app).
Solen is the Self-Optimizing E-commerce Layer for Shopify stores. Loop: Observe → Understand → Propose → Test → Learn → Improve.
Philosophy: "AI proposes. Reality decides." Observation ≠ hypothesis ≠ experiment ≠ result.

What already exists and must keep working:
- Entities: Store, Session, DailyAggregate, Recommendation, AuditRequest, PilotApplication, Purchase, User.
- Backend functions: ingestEvents, rollupSessions, findLeaks, getStoreInsights, analyzeAudit, notifyPilotApplication, stripeWebhook, getDownloads.
- Workflows: SessionsRollup (nightly), PilotApplicationNotify.
- The free audit (/audit) and the tracking script (theme snippet).

Hard rules for every change I ask from now on:
1. Create a checkpoint before changing anything.
2. Never modify Stripe, stripeWebhook, Purchase, AuditRequest or PilotApplication unless I say so explicitly in that prompt.
3. Never publish. I review in preview first.
4. Never show invented numbers to merchants. Every number shown comes from the store's data or the benchmark, with its sample size. When data is too thin, say "Not enough data yet" instead of guessing.
5. Solen never changes prices, discounts, checkout, legal text or health claims, and never suggests doing so.
6. Every AI-written text is labelled as a suggestion, and the merchant approves before anything goes live.
7. At the end of each step, list: files changed, entities added or changed, how to test it in preview, and anything you could not do.

Reply only with "Ready" and a one-line summary of what you understood. Do not change anything yet.
```

---

## Prompt 1 — Store profile (l'identité de la boutique)

```
Step 1: Store profile.

Create an entity StoreProfile linked to Store (one per store):
- brand_name, store_url, category, target_customer, price_range (low/mid/premium), tone_of_voice (short text),
- key_products (list of {title, url}), shipping_policy_summary, returns_policy_summary,
- forbidden_words (list), forbidden_claims (list), notes,
- status: draft | validated, validated_at, source: auto | merchant.

Create a backend function draftStoreProfile(store_id):
- Fetch the store's own public pages (home, 3 product pages from /products.json or the sitemap, shipping and returns pages if linked). Respect robots.txt. Only the merchant's own store.
- Ask the LLM to fill the profile fields from that text only. Leave a field empty if the pages do not say it. Never invent policies.
- Save as status draft, source auto.

Add an onboarding screen "Your store, as Solen understands it":
- Shows the draft profile, every field editable, with a "Validate" button (status → validated).
- Explain in one line that Solen uses this profile so suggestions match the brand.

Done when: on a test store, the draft profile fills from real pages, empty fields stay empty, the merchant can edit and validate, and nothing else in the app changed.
```

---

## Prompt 2 — Benchmark (« 1,500+ product pages studied »)

```
Step 2: Benchmark data inside the app.

Context: a separate crawler (GitHub repo mtvv37/solen-backend, tools/benchmark) measures practices on public product pages every night and writes stats.json (shares of stores showing each practice, per platform, with sample sizes).

Create an entity BenchmarkStat:
- practice_key, label, platform (all | shopify | woocommerce | other | french), stores_with, stores_measured, share_pct, snapshot_date, sample_note.

Create an admin-only page "Benchmark import":
- A text area where I paste stats.json, a button "Import" that replaces the current snapshot (keep previous snapshots by snapshot_date).
- Show the imported table and the snapshot date.

Create a helper getBenchmark(practice_key, platform) used by later steps.
Whenever a benchmark number is shown to a merchant, show it as: "X% of the N stores in Solen's sample (snapshot DATE)". Add the note: "Sample of public stores, mostly known brands. Shows what stores do, not what makes them sell."

Done when: I can paste stats.json, the table shows the same numbers as the file, and getBenchmark returns them with the sample size.
```

---

## Prompt 3 — Leak detection v2 (01 · Observe)

```
Step 3: Make findLeaks reliable.

Rewrite findLeaks so that, for a store and a period (last 7 and last 28 days):
- It computes the funnel steps (product view → add to cart → checkout started → purchase) by device (mobile/desktop) and by traffic source.
- For each step and segment it returns: sessions, conversions, rate, and a 90% confidence interval (Wilson).
- A segment is "measurable" only above a minimum of 200 sessions at the step entry (make this a setting). Below it, return "not_enough_data" and never rank it.
- It ranks leaks by estimated lost conversions = sessions × (reference rate − segment rate), where the reference is the store's other device or its 28-day average. Label this as an estimate.
- It saves the top leak per store in a new entity Leak (store_id, period, step, segment, rate, ci_low, ci_high, sessions, estimated_lost, status: open | addressed).

Show it on the dashboard as one card: "Biggest leak: Mobile · product page → cart", the rate with its interval, the session count, and "estimate" next to the lost conversions.

Done when: with seeded demo data (a separate demo store flagged is_demo, never mixed with real stores) the leak found is the one I seeded, and a store with little traffic shows "Not enough data yet".
```

---

## Prompt 4 — Hypothesis engine (02 · Propose : 100 → 1)

```
Step 4: Hypothesis engine.

Create an entity Hypothesis:
- store_id, leak_id, batch_id, text (what we believe), change (what to change on the page), target (selector or page area, text only),
- status: drafted | rejected | kept, reject_reason, score, confidence (low/medium/high), evidence (the numbers used, with sources), created_at.

Create a backend function generateHypotheses(store_id):
1. Inputs: the validated StoreProfile, the open Leak, the relevant BenchmarkStat rows, and the store memory (step 6, empty for now).
2. Ask the LLM for up to 100 distinct hypotheses for that leak, in the brand's tone, each with a concrete change. The LLM writes text only.
3. Filter in code, in this order, and record the reason for each rejection:
   - touches price, discount, checkout, legal or health claims → "Touches what Solen never changes"
   - uses a forbidden word or claim from the profile → "Against your brand rules"
   - not linked to the leak's step or segment → "Not supported by your data"
   - same as a past hypothesis that was tried or refused → "Already tried"
   - very small expected effect (rule you define and show me) → "Too small to matter"
4. Rank the remaining ones by leak size × confidence. Keep exactly one (status kept). If none survive, keep none and say so.
5. Save every hypothesis with its status so the screen can show the real counts.

Add a screen "How Solen chose this suggestion": the real counts (drafted, rejected by reason, kept) and the kept hypothesis with its evidence. Never show a count that did not happen.

Done when: on the demo store, the counts on screen match the Hypothesis records, a hypothesis mentioning a discount is always rejected, and the kept one cites the leak numbers.
```

---

## Prompt 5 — Cadence, inbox, Approve (« Your pace »)

```
Step 5: One suggestion at a time, at the merchant's pace.

Add to Store: suggestion_cadence (daily | weekly | on_demand, default weekly), suggestion_day (for weekly), paused (boolean).

Create an entity Suggestion: store_id, hypothesis_id, title, why (observation with numbers), change, ready_to_paste_text, status: new | approved | skipped | later | applied, decided_at, applied_at.

Create a scheduled workflow (daily) that, for each store not paused and due according to its cadence:
- runs findLeaks then generateHypotheses,
- turns the kept hypothesis into one Suggestion,
- sends one email: title, why, the change, a link to the inbox. Never more than one suggestion per period.
On demand: a "Get a suggestion now" button with the same logic, limited to once per day.

Create the inbox screen: one card per suggestion with Approve, Skip, Later. Approve copies the ready-to-paste text and shows how to apply it in Shopify (manual today). A toggle Daily / Weekly / On demand at the top.

Done when: on the demo store, changing the cadence changes when suggestions arrive, there is never more than one per period, and Approve/Skip/Later update the status.
```

---

## Prompt 6 — Change log et mémoire (04 · Learn)

```
Step 6: Learn from what the merchant did.

When a suggestion is marked "applied" (the merchant confirms the change is live, with the date):
- Compare the targeted step and segment over the 14 days before and the 14 days after (once 14 days have passed).
- Save a Result entity: suggestion_id, metric, before (rate, sessions), after (rate, sessions), interval for both, verdict: better | worse | unclear.
- Label every result "Indicative: no control group, other things changed too". Only call it better or worse when the intervals do not overlap; otherwise "unclear".

Create a "Store memory" screen: list of past suggestions with their verdict. Feed this memory into generateHypotheses (already-tried rule and as context for the LLM).

Done when: on demo data with a seeded improvement the verdict is "better", with overlapping intervals it is "unclear", and generateHypotheses no longer proposes something already tried.
```

---

## Prompt 7 — A/B contrôlé (03 · Test) — plus tard, derrière un interrupteur

À ne lancer qu'après plusieurs boutiques actives sur les étapes 1 à 6, et en le testant d'abord sur une boutique de démonstration qui vous appartient.

```
Step 7: Controlled tests, behind a feature flag (off by default, per store).

Create an entity Experiment: store_id, suggestion_id, target selector, control_text, variant_text, traffic_share (default 10%), status: draft | running | stopped | finished, start_at, min_sessions, max_days, kill_switch.

Extend the tracking script:
- Only when the store's flag is on and an experiment is running: assign each visitor once to control or variant (sticky, by random id), log an "exposure" event, and replace only the text of the target element for the variant. Never touch price, checkout, scripts, links or images.
- If the script fails or the kill switch is on, show the original page.

Analysis function:
- Fixed horizon: decide only after min_sessions per arm and the planned duration. No peeking verdicts.
- Sample ratio check: alert if the split is off.
- Guardrail: stop the test automatically if add-to-cart in the variant drops clearly below control.
- Verdict: winner | no difference | stopped, with intervals. The merchant decides to keep the winner.

Done when: on my own demo store, assignment is sticky, the split matches the share, the kill switch restores the page immediately, and a seeded drop triggers the automatic stop.
```

---

## Étape 8 — Une page par type de visiteur

Pas de prompt pour l'instant : c'est la vision du film. On en reparle quand l'étape 7 a tourné sur de vraies boutiques.

---

## Avant de vendre l'abonnement

- Le site doit dire ce qui existe vraiment (Lot 1 et la section « Aujourd'hui / Bientôt / Vision »).
- Le prix, le paiement Solen (séparé des PDF) et les conditions sont des décisions à prendre par le fondateur.
- Les étapes 3 à 6 utilisent les données de navigation des visiteurs : la politique de confidentialité doit le dire, et la purge à 90 jours doit rester appliquée.
