# Split sun — round 2 (refinement)

Comparison page: `index.html` (screenshot: `index.png`). Source: `../_src/build_b_refined.py`.

## 1. Lift and optical sizes

Lift = how far the variant half sits above the control half, as a % of the diameter. Gap = space between the halves.

| Cut | Used at | Gap | Lift |
|---|---|---|---|
| `lg` | ≥ 64 px | 5 % | 11 % |
| `s32` | 24–63 px | 8 % | 13 % |
| `s16` | < 24 px | 12 % | 15 % |

Lift test at 32 px (`lift-test-8/11/15.svg`): 8 % is barely visible; 11 % reads; 15 % starts to look broken at large sizes but is needed at 16 px.

## 2. Moving away from the generic ◐ (contrast / dark-mode icon)

| Option | Files | What changes | Verdict |
|---|---|---|---|
| O1 · Lift + size | `o1-lift-scale-*.svg` | Variant half 8 % larger | Reads as "grew", not "shifted". Still close to ◐ at 16 px in one colour. |
| O2 · Soft inner corners | `o2-soft-corners-*.svg` | Inner corners rounded (20 % of radius) | Most distinct in one colour; two deliberate pieces. Slightly softer, less "precise". |
| O3 · Two-tone | `o3-two-tone-*.svg` | Control grey, variant brand colour | Clearest story (control vs variant) and furthest from ◐. Depends on colour: the one-colour version falls back to the plain split. |

## 3. Palettes (round 2 proposals)

| Palette | Dark | Accent | Grey | Background |
|---|---|---|---|---|
| P1 · Ink & Amber | `#0E1726` | `#F5A524` | `#8A8F98` | `#F6F5F1` |
| P2 · Pine & Coral | `#0F4C4A` | `#FF6B4A` | `#93A3A1` | `#F4F7F6` |
| P3 · Graphite & Cobalt | `#1D2433` | `#2E5BFF` | `#8C93A1` | `#F5F6F8` |

The wordmark in this round is still the round-1 geometric monoline; it is replaced in `../b-v2/`.
