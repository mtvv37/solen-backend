# Solen — brand kit (v1, 29/09/2026)

Approved direction: **split sun**, palette **Ink & Sun**, wordmark **General Sans 600**. Tokens: [`tokens.css`](tokens.css). Logo files: [`logo/final/`](logo/final/). Social templates: [`templates/`](templates/). History of the exploration: `logo/` (rounds 1, b-refined, b-v2).

## Idea

A disc — the *sol* in Solen — split into **control** and **variant**; the variant half sits one measured step higher. It stands for the product's stance: compare, measure, then decide. *AI proposes. Reality decides.*

## Logo

| File | Use |
|---|---|
| `logo/final/lockup-dark.svg` / `lockup-light.svg` | Default: symbol + wordmark, on dark / light backgrounds |
| `logo/final/symbol-{dark,light}-lg.svg` | Symbol ≥ 64 px |
| `logo/final/symbol-{dark,light}-s32.svg` | Symbol 24–63 px (wider gap, more lift) |
| `logo/final/symbol-{dark,light}-s16.svg` | Symbol < 24 px, favicon |
| `logo/final/x-avatar-{dark,light}.svg` | Profile picture (400 × 400) |
| `logo/final/wordmark.svg` | Wordmark alone, when the symbol is already present nearby |

- **Colours in the symbol**: control half = ink on light backgrounds, cream on dark backgrounds; variant half = amber, always.
- **Clear space**: the width of the gap × 4 (≈ one quarter of the symbol) on every side.
- **Minimum size**: symbol 16 px (use the `s16` cut); lockup 24 px high.
- **Don't**: recolour the halves, swap them (variant must be on the right and higher), align them (the offset is the idea), add effects, set the wordmark in another font.

## Colour

| Token | Hex | Use | Contrast |
|---|---|---|---|
| Ink | `#0E1726` | Dark background, text on light | 16.5:1 on cream |
| Cream | `#F6F5F1` | Light background, text on dark | 16.5:1 on ink |
| Amber | `#F5A524` | Variant half, accents and text **on dark** | 8.8:1 on ink · **1.9:1 on cream — never text on light** |
| Amber text | `#B45309` | Amber for text **on light** | 4.6:1 on cream (AA) |
| Grey | `#8A8F98` | Secondary text on dark | 5.5:1 on ink · decorative only on light |
| Grey text (light) | `#5B616B` | Secondary text on light | 5.7:1 on cream |
| Ink 2 / Ink 3 | `#1B2740` / `#243049` | Surfaces, wireframes, textures on dark | decorative |
| Cream 2 / Cream 3 | `#E7E5DE` / `#D5D9DE` | Surfaces, wireframes on light | decorative |

Full WCAG table: `logo/b-v2/wcag.md`.

## Typography

**General Sans** (Indian Type Foundry, via Fontshare, ITF Free Font License: free for commercial use, logos and trademarks; the font files must not be redistributed, so they are not in this repo).

- Headlines: 600, tracking −2 %. Body and labels: 500. Wordmark: 600, lowercase, tracking −2.5 %, outlined.
- Social visuals (1200 × 675): main message ≥ 48 px, ≤ 12 words; secondary ≥ 22 px.

## Voice

- Evidence over hype. Observation ≠ hypothesis ≠ result.
- Write "I'd test…", never "+X % conversion". No figures without a source; unverified figures are labelled.
- Plain words. Avoid "AI agent", "revolutionize", "autopilot", "guaranteed".

## X account (@thomzzss_)

- Banner: `x/banner-v2/banner-a-lockup.png` (mobile-safe, see `x/README.md`).
- Avatar: `logo/final/x-avatar-dark.svg`.
- Post visuals: `templates/` (8 templates, dark by default, about 1 in 4 light).

## Social templates (`templates/solen_templates.py`)

Rule: a visual shows the information of the post (sourced number, diagram, table, chart, real capture) — never the post's sentence restated as a quote.

| Template | Function | When |
|---|---|---|
| Audit — (a) wireframe | `audit_wireframe` | A friction shown on a generic product page |
| Audit — (b) public page | `audit_screenshot` | A real public page where the friction is visible; brand masked (logo, name, URL, recognisable photos) |
| Audit — with permission | `audit_permission` | A merchant asked for the audit; brand visible, "Shared with permission" |
| Key number | `key_number` | One sourced number (source + year on the visual) |
| Journal Day N | `journal` | Build log, with a real screenshot or a "SCREENSHOT HERE" slot |
| Diagram | `schema` | Process or architecture: `flow` (left to right) or `loop` |
| Table | `table` | Comparison, statuses, checklist (`check_col`) |
| Chart | `chart` | Data: `range` bars (also `flow`, `columns`, `list`) |

Preview of all templates: `templates/preview.html` (`preview.png`). Rebuild: `SOLEN_FONTS=<font folder> python templates/build_examples.py`.
