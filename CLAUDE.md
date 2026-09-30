# Solen backend

Solen — *The Self-Optimizing Commerce Layer*. B2B SaaS prototype that turns e-commerce visitor behavior into tested optimizations.

**Business context of reference: [`docs/SOLEN_CONTEXT.md`](docs/SOLEN_CONTEXT.md). Read it before any product, strategy or roadmap work.**

## Project stage (keep in mind for every task)

- Stage: **prototype / pre-validation (SEEK → COMMIT)**. Market, ICP, pricing, GTM and PMF are **not validated**.
- Philosophy: **AI proposes. Reality decides.** Observation ≠ hypothesis ≠ experiment ≠ result.
- Core loop: Observe → Understand → Propose → Test → Learn → Improve.
- Current product scope: **V1 — Intelligence** (analysis + recommendations, human-in-the-loop). V2–V4 (copilot, experimentation, autopilot) are vision, not current scope.
- Never present a hypothesis (differentiation vs. Amboras, experimentation-memory moat, 10k visitors/month threshold, personas) as a proven fact.
- Before building a significant feature, ask: *which hypothesis does this validate?* and *what evidence do we have?* Prefer cheap, fast experiments. "Do not build your way out of uncertainty."
- Autonomy must stay gradual and guarded: control/baseline, guardrails, kill switch, rollback; prices, promotions, checkout, legal and critical branding always need human validation.

## Code layout

- `index.js` — Express API deployed on Vercel (`vercel.json`), backed by Supabase (`events` table) and the Anthropic SDK.
  - `GET /health` — liveness.
  - `POST /events` — ingest tracked visitor events (`{ events: [...] }`).
  - `GET /heatmap?url=&device=` — click / scroll-milestone heatmap per device profile.
  - `GET /analyze` — LLM analysis of recent events into recommendations.
- Env vars: `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `ANTHROPIC_API_KEY`.
- `verzo-sales-agent/` — separate project (VERZO Studio sales agent) with its own `CLAUDE.md`; unrelated to Solen.
