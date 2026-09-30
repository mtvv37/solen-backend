"""Round 3a — type study for the 'solen' wordmark next to the split-sun symbol.
Fonts are read from $SOLEN_FONTS (not stored in the repo). Writes brand/logo/b-v2/type-study/."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from solenbrand import split_sun, outline_text

FONTS_DIR = os.environ.get("SOLEN_FONTS", "")
FONTS = {
    "geist": ("Geist", "Geist.ttf"),
    "satoshi": ("Satoshi", "satoshi/Satoshi_Complete/Fonts/TTF/Satoshi-Variable.ttf"),
    "general-sans": ("General Sans", "general/GeneralSans_Complete/Fonts/TTF/GeneralSans-Variable.ttf"),
    "manrope": ("Manrope", "Manrope.ttf"),
}
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "b-v2", "type-study")
os.makedirs(OUT, exist_ok=True)

INK = "#111111"
SYM = 160            # symbol box height in the lockup
H = 200              # lockup height
XH_RATIO = 0.50      # x-height = 50% of the symbol box
TRACK = -0.025       # tighter letter-spacing (em)


def lockup(font_file, weight, text, color=INK, sym_colors=(INK, INK)):
    probe_d, probe_w, m = outline_text(font_file, "x", 1000, weight)
    size = XH_RATIO * SYM / (m["xh"] / 1000)
    d, w, m = outline_text(font_file, text, size, weight, TRACK)
    ctrl, var = split_sun()
    k = SYM / 256
    y0 = (H - SYM) / 2
    base = H / 2 + m["xh"] / 2          # centre the x-height on the symbol
    tx = SYM + 0.30 * SYM
    width = tx + w + 8
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.1f} {H}" width="{width:.1f}" height="{H}">'
           f'<g transform="translate(0 {y0}) scale({k})"><path fill="{sym_colors[0]}" d="{ctrl}"/><path fill="{sym_colors[1]}" d="{var}"/></g>'
           f'<path fill="{color}" transform="translate({tx:.1f} {base:.1f})" d="{d}"/></svg>')
    return svg, width


if __name__ == "__main__":
    rows = []
    for key, (label, rel) in FONTS.items():
        path = os.path.join(FONTS_DIR, rel)
        for weight in (500, 600):
            for text in ("solen", "Solen"):
                svg, w = lockup(path, weight, text)
                name = f"{key}-{weight}-{'lower' if text == 'solen' else 'title'}.svg"
                open(os.path.join(OUT, name), "w").write(svg)
                rows.append((label, weight, text, name))
    cells = "".join(
        f'<div class="c"><img src="{n}" height="72"><span>{l} {w} · {t} · tracking {TRACK:+.1%}</span></div>'
        for l, w, t, n in rows)
    open(os.path.join(OUT, "index.html"), "w").write(
        "<!doctype html><meta charset=utf-8><title>Solen type study</title><style>body{font:13px -apple-system,Arial;margin:32px;background:#fff}"
        ".g{display:grid;grid-template-columns:repeat(4,1fr);gap:28px 24px}.c{display:flex;flex-direction:column;gap:6px}.c span{color:#666}</style>"
        f"<h2>Type study — outlined, x-height = 50% of the symbol box</h2><div class=g>{cells}</div>")
    print("wrote", OUT)
