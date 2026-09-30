"""Round 3b — split sun v2: General Sans 600 wordmark (outlined), two palettes, X avatar + post cards, WCAG.
Fonts are read from $SOLEN_FONTS (not stored in the repo). Writes brand/logo/b-v2/."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from solenbrand import split_sun, outline_text, contrast, wcag

FONTS_DIR = os.environ["SOLEN_FONTS"]
GS = os.path.join(FONTS_DIR, "general/GeneralSans_Complete/Fonts/TTF/GeneralSans-Variable.ttf")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "b-v2")
os.makedirs(OUT, exist_ok=True)

WEIGHT, TRACK = 600, -0.025
CUTS = {"lg": dict(gap=0.05, lift=0.11), "s32": dict(gap=0.08, lift=0.13), "s16": dict(gap=0.12, lift=0.15)}

PALETTES = {
    "ink-sun": dict(label="Ink & Sun", dark="#0E1726", accent="#F5A524", bg="#F6F5F1", grey="#8A8F98",
                    text_accent="#B45309", light="#F6F5F1"),
    "teal-coral": dict(label="Teal & Coral", dark="#0F4C4A", accent="#FF6B4A", bg="#F4F7F6", grey="#93A3A1",
                       text_accent="#B93A1F", light="#F4F7F6"),
}

def cut_for(px):
    return "lg" if px >= 64 else ("s32" if px >= 24 else "s16")

def sym_colors(pal, on_dark):
    # control = dark on light backgrounds; on dark backgrounds the control flips to the light neutral
    return (pal["light"] if on_dark else pal["dark"], pal["accent"])

def symbol(pal, on_dark, cut="lg", px=256, bg=None):
    c, v = split_sun(**CUTS[cut])
    cc, vc = sym_colors(pal, on_dark)
    bgr = f'<rect width="256" height="256" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="{px}" height="{px}" role="img" aria-label="Solen">'
            f'{bgr}<path fill="{cc}" d="{c}"/><path fill="{vc}" d="{v}"/></svg>')

# ---- wordmark (outlined) + lockup geometry
_, _, _m = outline_text(GS, "x", 1000, WEIGHT)
SYM, H = 160, 200
SIZE = 0.50 * SYM / (_m["xh"] / 1000)
WM_D, WM_W, WM_M = outline_text(GS, "solen", SIZE, WEIGHT, TRACK)

def lockup_group(pal, on_dark, x=0, y=0, scale=1.0):
    c, v = split_sun(**CUTS["lg"])
    cc, vc = sym_colors(pal, on_dark)
    word = pal["light"] if on_dark else pal["dark"]
    k = SYM / 256
    base = H / 2 + WM_M["xh"] / 2
    tx = SYM * 1.30
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({scale})">'
            f'<g transform="translate(0 {(H - SYM) / 2}) scale({k})"><path fill="{cc}" d="{c}"/><path fill="{vc}" d="{v}"/></g>'
            f'<path fill="{word}" transform="translate({tx:.1f} {base:.1f})" d="{WM_D}"/></g>')

LOCK_W = SYM * 1.30 + WM_W + 4

def lockup_svg(pal, on_dark, h=H, bg=None):
    bgr = f'<rect width="{LOCK_W:.1f}" height="{H}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LOCK_W:.1f} {H}" height="{h}" width="{h * LOCK_W / H:.1f}" role="img" aria-label="Solen">'
            f'{bgr}{lockup_group(pal, on_dark)}</svg>')

def wordmark_svg(color):
    base = WM_M["xh"] + (SIZE * 0.25)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WM_W + 4:.1f} {H}" role="img" aria-label="solen">'
            f'<path fill="{color}" transform="translate(0 {H / 2 + WM_M["xh"] / 2:.1f})" d="{WM_D}"/></svg>')

# ---- X post card (1200×675), text outlined
def text_path(text, size, weight, color, x, y, track=-0.01):
    d, w, _ = outline_text(GS, text, size, weight, track)
    return f'<path fill="{color}" transform="translate({x} {y})" d="{d}"/>', w

def card(pal, on_dark):
    bg = pal["dark"] if on_dark else pal["bg"]
    fg = pal["light"] if on_dark else pal["dark"]
    acc_text = pal["accent"] if on_dark else pal["text_accent"]
    muted = pal["grey"]
    t1, _ = text_path("Observation is not a result.", 64, 600, fg, 96, 330)
    t2, _ = text_path("AI proposes. Reality decides.", 40, 500, acc_text, 96, 400)
    t3, _ = text_path("Building Solen in public", 26, 500, muted if on_dark else "#5B616B", 96, 590)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="1200" height="675">'
            f'<rect width="1200" height="675" fill="{bg}"/>'
            f'{lockup_group(pal, on_dark, 96, 72, 0.42)}{t1}{t2}{t3}'
            f'<g transform="translate(1004 500) scale(0.42)">{symbol_inner(pal, on_dark)}</g></svg>')

def symbol_inner(pal, on_dark):
    c, v = split_sun(**CUTS["lg"])
    cc, vc = sym_colors(pal, on_dark)
    return f'<path fill="{cc}" d="{c}"/><path fill="{vc}" d="{v}"/>'

# ---- write files
for key, pal in PALETTES.items():
    for dark in (False, True):
        mode = "dark" if dark else "light"
        for cut in CUTS:
            open(os.path.join(OUT, f"symbol-{key}-{mode}-{cut}.svg"), "w").write(symbol(pal, dark, cut))
        open(os.path.join(OUT, f"lockup-{key}-{mode}.svg"), "w").write(lockup_svg(pal, dark))
        open(os.path.join(OUT, f"x-card-{key}-{mode}.svg"), "w").write(card(pal, dark))
        open(os.path.join(OUT, f"x-avatar-{key}-{mode}.svg"), "w").write(
            symbol(pal, dark, "lg", 400, bg=pal["dark"] if dark else pal["bg"]))
open(os.path.join(OUT, "wordmark-solen-general-sans-600.svg"), "w").write(wordmark_svg("#111111"))

# ---- WCAG table
def pairs(p):
    return [
        ("Dark text on background", p["dark"], p["bg"], "body text, wordmark"),
        ("Light text on dark", p["light"], p["dark"], "reversed text, wordmark"),
        ("Accent on background", p["accent"], p["bg"], "symbol only — never text"),
        ("Text-safe accent on background", p["text_accent"], p["bg"], "links, highlights on light"),
        ("Accent on dark", p["accent"], p["dark"], "highlights on dark"),
        ("Dark on accent", p["dark"], p["accent"], "button label on accent"),
        ("Grey on background", p["grey"], p["bg"], "decorative only"),
        ("Grey on dark", p["grey"], p["dark"], "secondary text on dark"),
    ]

def swatch(c):
    return f'<span class="sw" style="background:{c}"></span>{c}'

wcag_html = ""
wcag_md = []
for key, p in PALETTES.items():
    rows = ""
    wcag_md.append(f"\n**{p['label']}**\n\n| Use | Foreground | Background | Ratio | WCAG |\n|---|---|---|---|---|")
    for name, fg, bg, use in pairs(p):
        r = contrast(fg, bg)
        rows += (f"<tr><td>{name}<br><small>{use}</small></td><td>{swatch(fg)}</td><td>{swatch(bg)}</td>"
                 f"<td>{r:.2f}:1</td><td class='{'bad' if r < 3 else ('mid' if r < 4.5 else 'ok')}'>{wcag(r)}</td></tr>")
        wcag_md.append(f"| {name} ({use}) | `{fg}` | `{bg}` | {r:.2f}:1 | {wcag(r)} |")
    wcag_html += f"<h3>{p['label']}</h3><table><tr><th>Use</th><th>Foreground</th><th>Background</th><th>Ratio</th><th>WCAG</th></tr>{rows}</table>"
open(os.path.join(OUT, "wcag.md"), "w").write("# WCAG contrast — Solen palettes v2\n" + "\n".join(wcag_md) + "\n")

# ---- page
def band(pal, dark):
    bg = pal["dark"] if dark else pal["bg"]
    cells = "".join(f'<div class="cell"><div class="art">{symbol(pal, dark, cut_for(px), px)}</div><span>{px}px</span></div>'
                    for px in (400, 64, 32, 16))
    av = "".join(f'<div class="cell"><div class="avatar" style="width:{px}px;height:{px}px;background:{bg}">'
                 f'{symbol(pal, dark, cut_for(int(px * 0.62)), int(px * 0.62))}</div><span>X avatar {px}px</span></div>'
                 for px in (200, 48))
    lk = f'<div class="cell"><div class="art">{lockup_svg(pal, dark, 72)}</div><span>lockup</span></div>'
    return f'<div class="band {"dark" if dark else ""}" style="background:{bg}">{cells}{av}{lk}</div>'

sections = ""
for key, p in PALETTES.items():
    sections += (f'<section><h2>{p["label"]}</h2><p class="note">dark {p["dark"]} · accent {p["accent"]} · background {p["bg"]}'
                 f' · grey {p["grey"]} · text-safe accent {p["text_accent"]}. Control half = dark (light neutral on dark backgrounds), variant half = accent.</p>'
                 f'{band(p, False)}{band(p, True)}'
                 f'<div class="cards"><div class="cell"><img src="x-card-{key}-light.svg" width="600"><span>X post card 1200×675 · light</span></div>'
                 f'<div class="cell"><img src="x-card-{key}-dark.svg" width="600"><span>X post card 1200×675 · dark</span></div></div></section>')

html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Solen — split sun v2</title>
<style>
body{{font:14px/1.45 -apple-system,Helvetica,Arial,sans-serif;color:#111;background:#F3F3F1;margin:0;padding:40px 48px}}
h1{{font-size:30px;margin:0 0 4px}} h2{{font-size:20px;margin:0 0 2px}} h3{{margin:18px 0 8px}} .sub,.note{{color:#555;margin:0 0 14px}}
section{{background:#fff;border-radius:14px;padding:24px 28px;margin:0 0 28px}}
.band{{display:flex;flex-wrap:wrap;gap:22px;align-items:flex-end;padding:20px;border-radius:10px;margin:0 0 10px}}
.band.dark span{{color:#B8C2CC}} .cell{{display:flex;flex-direction:column;align-items:center;gap:6px}} .cell span{{font-size:11px;color:#666}}
.art{{display:flex;align-items:center;justify-content:center}} .avatar{{border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 1px rgba(128,128,128,.25)}}
.cards{{display:flex;gap:20px;margin-top:14px;flex-wrap:wrap}} .cards img{{border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,.15)}}
table{{border-collapse:collapse;width:100%;font-size:13px}} td,th{{text-align:left;padding:7px 10px;border-bottom:1px solid #eee}} small{{color:#777}}
.sw{{display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;margin-right:6px;box-shadow:0 0 0 1px rgba(0,0,0,.15)}}
.ok{{color:#1a7f37;font-weight:600}} .mid{{color:#9a6700;font-weight:600}} .bad{{color:#cf222e;font-weight:600}}
.type img{{height:64px}}
</style></head><body>
<h1>Solen — split sun v2</h1>
<p class="sub">Wordmark: General Sans Semibold (600), lowercase, tracking −2.5%, outlined. x-height = 50% of the symbol box to match its optical weight.</p>
<section class="type"><h2>Typography</h2><p class="note">Chosen: General Sans 600 lowercase. Full study (Geist, Satoshi, General Sans, Manrope · 500/600 · lowercase/Title case) in <code>type-study/</code>.</p>
<div class="cards"><div class="cell"><img src="type-study/general-sans-600-lower.svg"><span>General Sans 600 · chosen</span></div>
<div class="cell"><img src="type-study/geist-600-lower.svg"><span>Geist 600</span></div><div class="cell"><img src="type-study/satoshi-600-lower.svg"><span>Satoshi 600</span></div>
<div class="cell"><img src="type-study/manrope-600-lower.svg"><span>Manrope 600</span></div><div class="cell"><img src="type-study/general-sans-600-title.svg"><span>General Sans 600 · Title case</span></div></div></section>
{sections}
<section><h2>WCAG contrast (text uses)</h2><p class="note">AA = 4.5:1 for body text, 3:1 for large text (≥ 24px, or 18.66px bold) and UI graphics.</p>{wcag_html}</section>
</body></html>"""
open(os.path.join(OUT, "index.html"), "w").write(html)
print("wrote", OUT)
