# Solen — X header banners (@thomzzss_)

1500 × 500 px, dark mode, Ink & Sun. Source: `../logo/_src/build_x_banner.py` (text outlined from General Sans; set `SOLEN_FONTS` to the local font folder to rebuild).

| Variant | Upload file | Source | Preview |
|---|---|---|---|
| V1 · Text right | `banner-v1-text-right.png` | `.svg` | `preview-v1-text-right.png` |
| V2 · Big symbol, right | `banner-v2-big-symbol.png` | `.svg` | `preview-v2-big-symbol.png` |
| V3 · Minimal | `banner-v3-minimal.png` | `.svg` | `preview-v3-minimal.png` |

**Previews** darken what X may crop (outside the central 1500 × 360 band, y 70–430, red dashed lines) and simulate the round profile photo bottom-left (≈ 334 px diameter at banner scale, reaching up to y ≈ 322 — slightly higher than the 333 px planned in the brief, so text was kept above it).

**Colours**: background `#0E1726`, control half and text `#F6F5F1`, variant half and V1 secondary line `#F5A524` (8.8:1 on ink), V2 secondary line `#8A8F98` (5.5:1). Big background control half in V2: `#1B2740`.

**Copy**: "The self-optimizing commerce layer for Shopify." · "AI proposes. Reality decides. · Building in public". No figures, no promised results.

Note: the brief referenced `brand/BRAND.md`, `brand/tokens.css` and `brand/logo/final/`, which do not exist yet. Values are taken from the approved `brand/logo/b-v2/` (Ink & Sun).

## banner-v2/ — mobile-safe redo (replaces the banners above)

Rules: content in x 250–1250, y 190–430; background only above y 170; nothing where x < 450 and y > 300 (profile photo). Checked by assertions in `../logo/_src/build_x_banner_v2.py`.

| Variant | Upload file | Preview (iPhone + desktop) |
|---|---|---|
| A · One line + symbol sign-off + background texture | `banner-v2/banner-a-one-line.png` | `banner-v2/preview-a-one-line.png` |
| B · Symbol + two lines | `banner-v2/banner-b-two-lines.png` | `banner-v2/preview-b-two-lines.png` |

Headline 44 px General Sans 600, `#F6F5F1` on `#0E1726`. The "AI proposes…" line was dropped. The one-line headline is 972 px wide at 44 px: it only fits in the 1000 px safe zone if it sits above y 300 (avatar rule), so content cannot go lower in A.
