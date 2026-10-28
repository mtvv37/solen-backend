# Solen — le prompt complet pour Base44

Un seul prompt à coller dans le builder Base44 de l'app Solen existante. Il décrit tout le produit voulu. Le prompt demande à Base44 de construire dans l'ordre et de s'arrêter après chaque phase pour que vous testiez en prévisualisation.

---

```
# SOLEN — FULL PRODUCT BRIEF

You are building Solen inside the EXISTING Base44 app (do not create a new app, do not delete existing features).
Read this whole brief before writing anything. Then build it phase by phase, in the order given in section 12.
After each phase: stop, list what you built, how I test it in preview, and what you could not do. Wait for my "go" before the next phase.

## 1. What Solen is

Solen is the self-optimizing commerce layer for Shopify stores.
It is installed on a merchant's store, understands the store's identity, watches how visitors behave, and continuously improves the store:
it finds where sales leak, proposes changes in the brand's own voice, tests them on a small share of traffic, keeps what works, rolls the winner out to the whole store, and remembers every result so the next idea is better.
It can also build a complete product page from scratch: the merchant drops a product, Solen studies how strong stores structure their pages, and drafts the page in the brand's style.

It runs always on, at the merchant's pace: one suggestion a day, one a week, or on demand.
The merchant stays in control: nothing goes live without their approval unless they explicitly allowed that type of change to run automatically.

Philosophy: "AI proposes. Reality decides."
Observation ≠ hypothesis ≠ experiment ≠ result. Every screen keeps these four apart.

Users:
- Merchant: a Shopify store owner or small team (1–10 people), already has traffic, no CRO agency, no developer.
- Admin: me (the founder). Manages the benchmark, plans, merchants, and sees all logs.

Language: the app works in English and French (merchant chooses). All merchant-facing copy exists in both.

## 2. Non-negotiable rules (apply to everything)

1. Never show an invented number. Every number comes from the store's own data or from the benchmark, with its sample size and date. When data is too thin, show "Not enough data yet" and explain what is missing.
2. Solen never changes or suggests changing: prices, discounts, promotions, checkout, payment, shipping costs, legal text, health or medical claims. These are filtered out in code, not only in the AI prompt.
3. No fake social proof: never generate reviews, ratings, testimonials, "bestseller" badges, stock counts or customer numbers.
4. Never copy text or images from another store. From other stores, Solen only learns structure (which sections exist, in which order, what is shown near the buy button), never wording or visuals.
5. Every AI-written text is shown as a suggestion. The merchant approves before it goes live, unless they turned on auto-apply for that exact change type (section 9), and even then a kill switch and one-click rollback always exist.
6. Visitor data is pseudonymized: random session id, no names, emails, typed text or IP stored. Respect consent: if the visitor refuses analytics, nothing is sent. Raw sessions are deleted after 90 days; only daily aggregates are kept.
7. One merchant's data is never used to benchmark or advise another merchant.
8. Do not modify Stripe, stripeWebhook, Purchase, AuditRequest or PilotApplication unless a phase below says so. Create a checkpoint before each phase. Never publish; I publish after review.
9. Results are labelled honestly: "Indicative" when there is no control group, "Proven" only for a finished controlled test with a clear difference.

## 3. Existing pieces to reuse (do not rebuild them from zero)

- Entities: Store, Session, DailyAggregate, Recommendation, AuditRequest, PilotApplication, Purchase, User.
- Functions: ingestEvents, rollupSessions, findLeaks, getStoreInsights, analyzeAudit, notifyPilotApplication, stripeWebhook, getDownloads.
- Workflows: SessionsRollup (nightly), PilotApplicationNotify.
- Free audit at /audit (score out of 100 + 3 fixes) and the tracking script installed in the Shopify theme.
- Stripe currently sells PDF guides only (/ai-videos). Solen subscriptions will use separate products (phase 8).

## 4. Installation and tracking

Today: the merchant pastes a Solen script in their Shopify theme. Keep this path and make it painless:
- Install screen with the snippet, copy button, a short video-style step list for Shopify (Online Store → Themes → Edit code → theme.liquid).
- "Check installation" button: pings the store and confirms events are arriving (show the last event received).
- The script sends: page view (path only), device, source (utm + referrer domain), country, scroll depth, repeated clicks, steps reached (product view, add to cart, checkout started, purchase with amount), and later experiment exposures (section 9).

Later (phase 9): a real Shopify app (OAuth install, Admin API with the minimum scopes, theme app extension to inject the script without code). Prepare the data model so Store can hold a Shopify connection (shop domain, access token stored as a secret, granted scopes, connected_at). Do not use the Shopify API to collect data for the benchmark.

## 5. Store identity (StoreProfile)

Solen must understand who the store is before proposing anything.

Entity StoreProfile (one per Store): brand_name, store_url, category, target_customer, price_range (low | mid | premium), tone_of_voice, brand_values, key_products [{title, url}], shipping_policy_summary, returns_policy_summary, guarantees, forbidden_words [], forbidden_claims [], visual_notes (colors, photo style), notes, status (draft | validated), source (auto | merchant), validated_at.

Function draftStoreProfile(store_id):
- Reads the merchant's own public pages: home, about, 3–5 product pages (from /products.json or the sitemap), shipping and returns pages. Respects robots.txt.
- The LLM fills the fields from that text only. Unknown fields stay empty. Never invent a policy.
- Saves as draft.

Screen "Your store, as Solen understands it": every field editable, "Validate" button. Suggestions only start once the profile is validated. The merchant can edit it at any time; changes apply to the next suggestions.

## 6. Benchmark intelligence ("what strong stores do")

A separate crawler (GitHub repo mtvv37/solen-backend, tools/benchmark) reads public product pages every night, obeys robots.txt, stores only features (never text or images) and writes stats.json: for each practice, the share of stores showing it, per platform, with sample sizes. It also has hand-picked reference stores.

Entity BenchmarkStat: practice_key, label, platform (all | shopify | woocommerce | other | french), stores_with, stores_measured, share_pct, snapshot_date, sample_note.
Entity BenchmarkReference: domain, practice_key, has_practice (yes | no | n/a), snapshot_date.

Admin page "Benchmark": paste stats.json → import a new snapshot (keep history). Show the table and the snapshot date.
Helper getBenchmark(practice_key, platform) used everywhere.

Display rule: "X% of the N stores in Solen's sample (snapshot DATE)". Always add: "Sample of public stores, mostly well-known brands. It shows what stores do, not what makes them sell."
Never write "what works" or "the best stores" as a fact.

## 7. Audit (free and paid)

Free audit (exists): keep it, and add 2–3 benchmark lines to the report ("Shipping info near the button: you don't; X% of the sample do").

Paid audit, one-shot, one product page (price set by me in settings, shown only once I set it):
- Inputs: product page URL + email + optional notes ("what we must not promise").
- Output (one page, web + PDF): score, the leaks found on the page, the 3–5 fixes ranked, ready-to-paste texts (title, subtitle/benefits, button text, FAQ ideas, shipping/returns block), a short roadmap to apply the same fixes to all product pages, and the benchmark lines used.
- Flow: payment → AI first draft → admin review queue (I read, edit, approve) → delivery email. Show a delivery clock: target 24 business hours, maximum 48. If 48 business hours pass without delivery, flag it for a full refund (I trigger the refund manually in Stripe).
- Each delivered audit is saved as an experiment record in the store memory (observation → hypothesis → proposed change), so it feeds Solen if the merchant later installs it.

## 8. The core loop: Observe → Propose → (Test) → Learn

### 8.1 Observe (leak detection)
Rewrite findLeaks:
- Funnel steps: product view → add to cart → checkout started → purchase, by device and by traffic source, for the last 7 and 28 days.
- For each step and segment: sessions, conversions, rate, 90% Wilson interval.
- Measurable only above a minimum of 200 sessions at the step entry (setting). Below: "not_enough_data", never ranked.
- Rank leaks by estimated lost conversions = sessions × (reference rate − segment rate). Label as "estimate".
- Entity Leak: store_id, period, step, segment, rate, ci_low, ci_high, sessions, estimated_lost, status (open | addressed).

### 8.2 Propose (hypothesis engine: many ideas, one suggestion)
Entity Hypothesis: store_id, leak_id, batch_id, text, change, target (page area or CSS selector, text-level only), status (drafted | rejected | kept), reject_reason, score, confidence (low | medium | high), evidence (numbers + sources), created_at.

Function generateHypotheses(store_id):
1. Inputs: validated StoreProfile, the top open Leak, related BenchmarkStat rows, store memory (8.4).
2. The LLM drafts up to 100 distinct hypotheses for that leak, each with a concrete change written in the brand's tone.
3. Code filters, in this order, saving the reason:
   - touches price, discount, checkout, legal, health → "Touches what Solen never changes"
   - forbidden word or claim from the profile → "Against your brand rules"
   - not linked to the leak's step or segment → "Not supported by your data"
   - already tried, refused or proven worse → "Already tried"
   - expected effect too small (rule shown in settings) → "Too small to matter"
4. Rank survivors by leak size × confidence. Keep exactly one. If none survive, say so.
5. Screen "How Solen chose this": real counts (drafted, rejected per reason, kept) and the kept hypothesis with its evidence.

### 8.3 Suggestions at the merchant's pace
Store fields: suggestion_cadence (daily | weekly | on_demand, default weekly), suggestion_day, paused.
Entity Suggestion: store_id, hypothesis_id, title, why (observation with numbers), change, ready_to_paste_text, status (new | approved | skipped | later | applied | auto_applied), decided_at, applied_at.

Scheduled workflow (daily): for each active store due by its cadence → findLeaks → generateHypotheses → one Suggestion → one email (title, why, change, link). Never more than one suggestion per period. "Get a suggestion now" button, max once a day.

Inbox screen: one card per suggestion: why (with numbers), the change, ready-to-paste text, buttons Approve / Skip / Later, and "Test it first" (if experiments are enabled, section 9). Approve shows how to apply it in Shopify manually, or applies it through the Shopify connection when available and allowed.

### 8.4 Learn (memory)
When a suggestion is applied (merchant confirms the date, or Solen applied it):
- After 14 days, compare the targeted step and segment, 14 days before vs after. Entity Result: suggestion_id, metric, before, after, intervals, verdict (better | worse | unclear), kind (indicative | proven).
- Indicative results only say better/worse when intervals do not overlap; otherwise "unclear".
Screen "Store memory": every past change with its verdict. Memory feeds generateHypotheses (no repeats, learns the brand's preferences from skipped suggestions).

## 9. Controlled tests and rollout (behind a per-store switch, off by default)

Entity Experiment: store_id, suggestion_id, target selector, control_text, variant_text, traffic_share (default 10%), status (draft | running | stopped | finished | rolled_out), start_at, min_sessions_per_arm, max_days, kill_switch, verdict.

Tracking script, only when the store's switch is on and an experiment runs:
- Assign each visitor once to control or variant (sticky random id), log an exposure event, replace only the text of the target element for the variant.
- Never touch prices, checkout, links, scripts or images. If anything fails or the kill switch is on, the original page shows.

Analysis:
- Fixed horizon: no verdict before min_sessions_per_arm and the planned duration.
- Sample ratio check: alert if the split is off.
- Guardrail: stop automatically if add-to-cart in the variant falls clearly below control.
- Verdict: winner | no difference | stopped, with intervals, kind "proven".

Rollout: when a variant wins, the merchant clicks "Roll out to all visitors" (or it happens automatically if they allowed auto-rollout for that change type). Rollout keeps a one-click rollback. Result goes to the store memory.

Autonomy settings (per store, per change type: text near the button, titles, benefit bullets, FAQ, shipping/returns block): suggest only (default) | test automatically | test and roll out automatically. Prices, checkout, legal and brand-critical changes can never be automated.

## 10. Product page generator (A to Z)

Screen "New product page":
- Inputs: product name, photos (upload), facts (materials, size, use, care…), price (entered by the merchant, never invented), optional 1–5 URLs of pages the merchant likes.
- Solen studies structure only: from the benchmark and from the given URLs it extracts which sections exist, their order, what sits near the buy button (reviews, shipping, returns, guarantees, payment marks), FAQ topics. Never text or images.
- Output: a full page draft in the brand's tone, by sections: title, subtitle, benefit bullets, description, specs, "what's in the box", shipping/returns block (from the store's own policies only), FAQ (answers only from facts given), suggested image order and alt texts.
- Each section editable, regenerate per section, "Explain why this structure" (benchmark lines used).
- Export: Shopify-ready product description HTML, plus copy buttons. When the Shopify connection exists: create the product as a draft in Shopify (never published by Solen).
- Every generated page can start an experiment against the current page later.

## 11. Personalized pages per audience (vision, build last, behind a switch)

Segments from tracking (new vs returning, source, device, country). For a product page, Solen proposes one variant per segment (text only), tested like any experiment, with the same guardrails. Off by default. Build it only after section 9 has run on real stores.

## 12. Build order (stop after each phase)

Phase 1 — Foundations: StoreProfile + draftStoreProfile + validation screen; install screen + "Check installation".
Phase 2 — Benchmark: BenchmarkStat, BenchmarkReference, admin import, getBenchmark, benchmark lines in the free audit.
Phase 3 — Observe: findLeaks v2 + Leak entity + dashboard card ("Biggest leak") with intervals and "Not enough data yet".
Phase 4 — Propose: Hypothesis entity, generateHypotheses with code filters, "How Solen chose this" screen.
Phase 5 — Pace: cadence settings, Suggestion entity, daily workflow, email, inbox with Approve / Skip / Later.
Phase 6 — Learn: Result entity, before/after analysis, store memory screen, memory fed back into phase 4.
Phase 7 — Page generator (section 10) with HTML export.
Phase 8 — Monetization: Solen plans as separate Stripe products (names and prices set by me in an admin settings page, nothing hardcoded), paid audit flow (section 7) with admin review queue. Only now may you touch Stripe-related code, and only to add Solen products, never to change the PDF products.
Phase 9 — Shopify app connection (OAuth, minimum scopes, theme app extension, product drafts via Admin API).
Phase 10 — Controlled tests and rollout (section 9), tested first on a demo store I own.
Phase 11 — Personalized pages (section 11).

Demo data: create one demo store flagged is_demo with seeded sessions (including a known mobile product-page → cart leak). Use it to test every phase. Never mix demo data with real stores and never count it in any real metric.

## 13. Screens summary (merchant side)

Home dashboard (biggest leak, latest suggestion, last result, data status) · Install · Store profile · Inbox (suggestions) · How Solen chose this · Store memory · Experiments (when enabled) · New product page · Audit (free / paid) · Settings (cadence, autonomy per change type, kill switch, language, billing).
Admin side: merchants list, benchmark import, audit review queue, plans and prices, logs (every AI call with its inputs and filters), global kill switch.

## 14. Definition of done for the whole product

- A real Shopify store can install Solen, validate its profile, and receive one useful suggestion per period, backed by its own numbers.
- Every number on screen can be traced to data or the benchmark, with sample size.
- No suggestion ever touches price, checkout, legal or health claims, and none contains fake social proof.
- The merchant can stop everything with one switch and roll back any applied change.
- The product page generator produces a complete draft from product facts without copying any other store.

Start now with a short summary of how you understood Solen (5 lines max) and the list of phase 1 tasks. Then build phase 1 and stop.
```

---

## Notes pour vous

- Si Base44 tronque ou mélange tout, recollez le même prompt et ajoutez à la fin « Continue with phase N only ».
- Les prix, les noms des formules et le moment d'activer l'automatisation restent vos décisions : le prompt demande à Base44 de les laisser configurables.
- Phase 9 (app Shopify) : la création d'une app publique passe par le programme partenaires de Shopify et sa validation. À vérifier avant d'y engager du temps.
