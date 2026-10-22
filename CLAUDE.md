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

- `index.js` — Express app deployed on Vercel through `api/index.js` (`vercel.json` rewrites everything to it), backed by Supabase and the Anthropic SDK. `npm test` runs the suite, `npm run dev` serves locally.
  - `/audit/`, `/r/:id`, `/api/audits*` — free conversion audit V0 (`src/audit/`, UI in `public/audit/`, schema in `supabase/migrations/`). See `docs/AUDIT_V0.md`. Numbers are computed by code from stated assumptions; Claude only writes the French text.
  - `GET /health` — liveness.
  - `POST /events` — ingest tracked visitor events (`{ events: [...] }`).
  - `GET /heatmap?url=&device=` — click / scroll-milestone heatmap per device profile.
  - `GET /analyze` — LLM analysis of recent events into recommendations.
- Env vars: see `.env.example`.
- `verzo-sales-agent/` — separate project (VERZO Studio sales agent) with its own `CLAUDE.md`; unrelated to Solen.
