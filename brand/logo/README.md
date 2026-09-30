# Solen — logo concepts (round 1)

Status: **concepts for review**, black only, not final. Overview: `concepts.png`.

## Brief (as understood)

- **What**: B2B SaaS that turns Shopify visitor behavior into tested store improvements — "The Self-Optimizing Commerce Layer".
- **Audience**: e-commerce founders, growth managers, CRO agencies.
- **Adjectives**: precise, calm, trustworthy — evidence over hype.
- **Avoid**: flashy "AI" (sparkles, brains, gradients), category clichés (upward arrows, bar charts, eyes, magnifiers, carts, refresh arrows, infinity loops — already used by Arduino, Fedora, Flux, Squarespace…).
- **Idea to explore**: a continuous loop (Observe → Test → Learn).

## Concepts

### A — Open spiral · abstract
`concept-a-open-spiral.svg`, `concept-a-open-spiral-lockup.svg`

**Idea:** one loop that never returns to the same place — each pass ends a step further out.
- Built from three tangent semicircles whose radius grows by a fixed step: the "learning" is literally in the geometry (a constant, measured increment, not an explosion).
- One continuous stroke, no break: calm and deliberate.
- Risk: spirals read as generic ("vortex", "snail", a "6" or "@" at a glance). Needs a very disciplined system to feel ownable.

### B — Split sun · abstract
`concept-b-split-sun.svg`, `concept-b-split-sun-lockup.svg`

**Idea:** a disc — the "sol" in Solen — split into control and variant; the variant half sits one measured step higher.
- The most direct image of an A/B test, without charts or arrows.
- Strongest silhouette of the three: holds up at 16 px, as a favicon and in one colour.
- Risk: the offset may read as "broken" or "misaligned" rather than "measured"; and it implies the variant always wins, which contradicts "reality decides".

### C — S-trace · letterform ← recommended
`concept-c-s-trace.svg`, `concept-c-s-trace-lockup.svg`

**Idea:** an S drawn as one trajectory, set in motion by a single detached point — the observation.
- Links directly to the name, so it builds recognition for Solen rather than for a generic concept.
- The point before the path encodes the philosophy: an observation comes first, then the path is drawn; the point stays separate from the line (observation ≠ result).
- Quiet, monoline, no effect: reads as a tool, not as hype.
- Risk: the loop idea is implicit (a path) rather than explicit (a cycle). At 16 px the dot gets small; a small-size cut with a larger dot will be needed.

**Recommendation:** C. It is the only concept that is both tied to the name and free of a category cliché, and its one detail (the separate point) carries the "evidence over hype" stance. B is the strongest backup if you want the testing idea to be more explicit.

## Wordmark (shared, exploration)

`solen` in lowercase, constructed geometrically (circles and straight strokes, no font), monoline 18/256, round terminals. The same wordmark is used in the three lockups so the symbols are compared fairly.

## Technical notes

- All files are hand-built SVG, one colour (#111111), no text, no raster, no filter.
- Concepts A, C and the wordmark use **strokes**: they must be expanded to filled outlines (in Figma/Illustrator) before the final master files.
- The overview sheet (`concepts.png`) crops the left edge of the large S in concept C; the SVG file itself is not cropped (checked by rendering it alone).
- Tests run: SVG audit (98–100/100, heuristic), render at 512 px, 64/32/16 px sizes on the sheet. Not yet run: one-colour/reversed sheet, shelf test against competitors, colour.
- No trademark clearance: a professional search is needed before adopting any mark.
- `_src/gen.py` regenerates every SVG; `_iterations/` keeps the first versions of A and C (A v1 read as a loading spinner and was replaced).
