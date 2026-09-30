"""Round 2 — refine concept B (split sun): lift test, optical sizes, 3 differentiation options, 3 palettes.
Writes SVGs + index.html into brand/logo/b-refined/."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from solenbrand import split_sun, symbol_svg

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "b-refined")
os.makedirs(OUT, exist_ok=True)

INK, WHITE = "#111111", "#FFFFFF"
LIGHT_BG, DARK_BG = "#FFFFFF", "#0E1726"

# optical-size cuts: gap and lift grow as the mark gets smaller (fractions of the diameter)
CUTS = {"lg": dict(gap=0.05, lift=0.11), "s32": dict(gap=0.08, lift=0.13), "s16": dict(gap=0.12, lift=0.15)}

OPTIONS = {
    "o1-lift-scale": dict(label="O1 · Lift + size", note="Variant half is 8% larger and lifted: it reads as 'grew', not 'shifted'.", var_scale=1.08),
    "o2-soft-corners": dict(label="O2 · Soft inner corners", note="Inner corners rounded (20% of radius): two deliberate pieces, not a sliced circle.", rho=0.20),
    "o3-two-tone": dict(label="O3 · Two-tone", note="Control in neutral grey, variant in the brand colour: the comparison is carried by colour as well as position.", two_tone=True),
}

PALETTES = {
    "p1-ink-amber": dict(label="P1 · Ink & Amber", dark="#0E1726", accent="#F5A524", grey="#8A8F98", bg="#F6F5F1"),
    "p2-pine-coral": dict(label="P2 · Pine & Coral", dark="#0F4C4A", accent="#FF6B4A", grey="#93A3A1", bg="#F4F7F6"),
    "p3-graphite-cobalt": dict(label="P3 · Graphite & Cobalt", dark="#1D2433", accent="#2E5BFF", grey="#8C93A1", bg="#F5F6F8"),
}

def geom(opt, cut):
    p = dict(CUTS[cut])
    p["var_scale"] = opt.get("var_scale", 1.0)
    p["rho"] = opt.get("rho", 0.0)
    return split_sun(**p)

def cut_for(px):
    return "lg" if px >= 64 else ("s32" if px >= 24 else "s16")

def inline(paths, colors, px):
    s = symbol_svg(paths, colors)
    return s.replace('width="256" height="256"', f'width="{px}" height="{px}"')

# wordmark from round 1 (geometric monoline), extracted from the concept-B lockup
lock = open(os.path.join(ROOT, "concept-b-split-sun-lockup.svg")).read()
WM = re.search(r'(<g id="wordmark".*?</g>)', lock, re.S).group(1)
WM_W = float(re.search(r'viewBox="0 0 ([\d.]+) 256"', lock).group(1))

def lockup(paths, colors, word_color, h=64):
    sym = symbol_svg(paths, colors)
    inner = re.search(r'(<g id="symbol">.*?</g>)', sym, re.S).group(1)
    wm = WM.replace('stroke="#111111"', f'stroke="{word_color}"')
    w = WM_W
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} 256" height="{h}" width="{h * w / 256:.1f}">'
            f'<g transform="translate(0 35.84) scale(0.72)">{inner}</g>{wm}</svg>')

def colors_for(opt, pal, dark_bg):
    if opt.get("two_tone"):
        return (pal["grey"], pal["accent"])
    c = WHITE if dark_bg else INK
    return (c, c)

# ---------- files
for key, opt in OPTIONS.items():
    for cut in CUTS:
        cols = colors_for(opt, PALETTES["p1-ink-amber"], False)
        open(os.path.join(OUT, f"{key}-{cut}.svg"), "w").write(symbol_svg(geom(opt, cut), cols, title=f"Solen {opt['label']} ({cut})"))
for key, pal in PALETTES.items():
    for cut in CUTS:
        open(os.path.join(OUT, f"{key}-{cut}.svg"), "w").write(
            symbol_svg(geom({}, cut), (pal["grey"], pal["accent"]), title=f"Solen {pal['label']} ({cut})"))
for L in (0.08, 0.11, 0.15):
    open(os.path.join(OUT, f"lift-test-{int(L*100)}.svg"), "w").write(symbol_svg(split_sun(gap=0.05, lift=L), title=f"lift {L:.0%}"))

# ---------- page
def ladder(opt, pal, bg, dark):
    cells = []
    for px in (400, 64, 32, 16):
        cols = colors_for(opt, pal, dark)
        cells.append(f'<div class="cell"><div class="art" style="background:{bg}">{inline(geom(opt, cut_for(px)), cols, px)}</div><span>{px}px</span></div>')
    return "".join(cells)

def avatars(opt, pal, bg, dark):
    out = []
    for px in (200, 48):
        cols = colors_for(opt, pal, dark)
        sym = inline(geom(opt, cut_for(int(px * 0.62))), cols, int(px * 0.62))
        out.append(f'<div class="cell"><div class="avatar" style="width:{px}px;height:{px}px;background:{bg}">{sym}</div><span>X avatar {px}px</span></div>')
    return "".join(out)

def row(title, note, opt, pal):
    light_bg = pal["bg"] if opt.get("two_tone") else LIGHT_BG
    dark_bg = pal["dark"] if opt.get("two_tone") else DARK_BG
    word_l = pal["dark"] if opt.get("two_tone") else INK
    return f"""
<section><h2>{title}</h2><p class="note">{note}</p>
<div class="band" style="background:{light_bg}">{ladder(opt, pal, light_bg, False)}{avatars(opt, pal, light_bg, False)}
<div class="cell"><div class="art" style="background:{light_bg}">{lockup(geom(opt, 'lg'), colors_for(opt, pal, False), word_l)}</div><span>with wordmark</span></div></div>
<div class="band dark" style="background:{dark_bg}">{ladder(opt, pal, dark_bg, True)}{avatars(opt, pal, dark_bg, True)}
<div class="cell"><div class="art" style="background:{dark_bg}">{lockup(geom(opt, 'lg'), colors_for(opt, pal, True), WHITE)}</div><span>with wordmark</span></div></div>
</section>"""

contrast_icon = ('<svg viewBox="0 0 256 256" width="{px}" height="{px}"><circle cx="128" cy="128" r="104" fill="none" stroke="#111" stroke-width="16"/>'
                 '<path d="M128 24 A104 104 0 0 1 128 232 Z" fill="#111"/></svg>')

lift_cells = "".join(
    f'<div class="cell"><div class="art">{inline(split_sun(gap=0.08, lift=L), (INK, INK), 400)}</div><span>lift {int(L*100)}% · 400px</span></div>'
    f'<div class="cell"><div class="art">{inline(split_sun(gap=0.08, lift=L), (INK, INK), 32)}</div><span>lift {int(L*100)}% · 32px</span></div>'
    for L in (0.08, 0.11, 0.15))

html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Solen — split sun, round 2</title>
<style>
body{{font:14px/1.45 -apple-system,Helvetica,Arial,sans-serif;color:#111;background:#F3F3F1;margin:0;padding:40px 48px}}
h1{{font-size:30px;margin:0 0 4px}} h2{{font-size:19px;margin:0 0 2px}} .sub,.note{{color:#555;margin:0 0 14px}}
section{{background:#fff;border-radius:14px;padding:24px 28px;margin:0 0 28px}}
.band{{display:flex;flex-wrap:wrap;gap:22px;align-items:flex-end;padding:20px;border-radius:10px;margin:0 0 10px}}
.band.dark span{{color:#B8C2CC}}
.cell{{display:flex;flex-direction:column;align-items:center;gap:6px}} .cell span{{font-size:11px;color:#666}}
.art{{display:flex;align-items:center;justify-content:center;padding:4px}}
.avatar{{border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 1px rgba(128,128,128,.25)}}
.row{{display:flex;gap:28px;align-items:flex-end;flex-wrap:wrap}}
</style></head><body>
<h1>Solen — split sun, round 2</h1>
<p class="sub">Black first, then colour. Small sizes use optical cuts (gap 5% → 8% → 12%, lift 11% → 13% → 15% of the diameter).</p>
<section><h2>1 · Lift test (gap 8%)</h2><p class="note">The offset has to read at 32px. 8% disappears; 15% starts to look broken. Chosen: 11% at large sizes, 13% at 32px, 15% at 16px.</p><div class="row">{lift_cells}</div></section>
<section><h2>2 · The problem to avoid</h2><p class="note">The generic “contrast / dark mode” icon ◐. Every option below must not read as this.</p>
<div class="row"><div class="cell"><div class="art">{contrast_icon.format(px=120)}</div><span>generic ◐</span></div><div class="cell"><div class="art">{contrast_icon.format(px=32)}</div><span>32px</span></div><div class="cell"><div class="art">{contrast_icon.format(px=16)}</div><span>16px</span></div></div></section>
{''.join(row(o['label'], o['note'], o, PALETTES['p1-ink-amber']) for o in OPTIONS.values())}
<h1 style="margin-top:40px">Palettes (two-tone: control = neutral grey, variant = brand colour)</h1>
<p class="sub">Calm B2B palettes, no AI purple. Wordmark in the palette's dark colour.</p>
{''.join(row(p['label'], f"dark {p['dark']} · accent {p['accent']} · grey {p['grey']} · background {p['bg']}", dict(two_tone=True), p) for p in PALETTES.values())}
</body></html>"""
open(os.path.join(OUT, "index.html"), "w").write(html)
print("wrote", OUT)
