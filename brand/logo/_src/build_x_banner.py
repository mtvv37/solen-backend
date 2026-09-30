"""X (Twitter) header banners for Solen — 1500×500, Ink & Sun, dark mode. Writes brand/x/.
Fonts are read from $SOLEN_FONTS (not stored in the repo)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from solenbrand import split_sun, outline_text

FONTS_DIR = os.environ["SOLEN_FONTS"]
GS = os.path.join(FONTS_DIR, "general/GeneralSans_Complete/Fonts/TTF/GeneralSans-Variable.ttf")
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "x"))
os.makedirs(OUT, exist_ok=True)

W, H = 1500, 500
INK, CREAM, AMBER, GREY = "#0E1726", "#F6F5F1", "#F5A524", "#8A8F98"
SAFE_TOP, SAFE_BOT = 70, 430                 # central band kept on every screen
DEAD = dict(x1=400, y0=333)                  # avatar overlap: x < 400 and y > 333
HEAD = ["The self-optimizing commerce", "layer for Shopify."]
SUB = "AI proposes. Reality decides. · Building in public"

CTRL, VAR = split_sun(gap=0.05, lift=0.11)   # 256 box, large cut


def sym(x, y, size, ctrl=CREAM, var=AMBER):
    k = size / 256
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.4f})">'
            f'<path fill="{ctrl}" d="{CTRL}"/><path fill="{var}" d="{VAR}"/></g>')


def text(s, size, weight, color, x, y, track=-0.015):
    d, w, m = outline_text(GS, s, size, weight, track)
    return f'<path fill="{color}" transform="translate({x:.1f} {y:.1f})" d="{d}"/>', w, m


# lockup = symbol + outlined "solen" (same proportions as brand/logo/b-v2: x-height = 50% of symbol box, tracking −2.5%)
_, _, _m = outline_text(GS, "x", 1000, 600)
def lockup(x, y, sym_box):
    size = 0.50 * sym_box / (_m["xh"] / 1000)
    d, w, m = outline_text(GS, "solen", size, 600, -0.025)
    base = y + sym_box / 2 + m["xh"] / 2
    tx = x + sym_box * 1.30
    return (sym(x, y, sym_box) + f'<path fill="{CREAM}" transform="translate({tx:.1f} {base:.1f})" d="{d}"/>',
            sym_box * 1.30 + w)


def svg(body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="{title}"><rect width="{W}" height="{H}" fill="{INK}"/>{body}</svg>')


# ---- V1 · lockup left, text right
def v1():
    lk, lw = lockup(96, 150, 110)
    size = 46
    l1, w1, _ = text(HEAD[0], size, 600, CREAM, 0, 0)
    l2, w2, _ = text(HEAD[1], size, 600, CREAM, 0, 0)
    s1, ws, _ = text(SUB, 22, 500, AMBER, 0, 0)
    right = W - 96
    x = right - max(w1, w2, ws)
    assert x > 96 + lw + 60, "text collides with lockup"
    body = lk
    body += text(HEAD[0], size, 600, CREAM, x, 208)[0]
    body += text(HEAD[1], size, 600, CREAM, x, 264)[0]
    body += text(SUB, 22, 500, AMBER, x, 318)[0]
    return body


# ---- V2 · big symbol in the background, right; text left (kept above the avatar, which reaches y≈322)
def v2():
    big = sym(1000, -40, 580, ctrl="#1B2740", var=AMBER)
    lk, lw = lockup(96, 78, 64)
    size = 44
    body = big + lk
    body += text(HEAD[0], size, 600, CREAM, 96, 206)[0]
    body += text(HEAD[1], size, 600, CREAM, 96, 260)[0]
    body += text(SUB, 21, 500, GREY, 96, 298)[0]
    return body


# ---- V3 · minimal: symbol + headline only (two lines)
def v3():
    size = 46
    _, w1, m = text(HEAD[0], size, 600, CREAM, 0, 0)
    _, w2, _ = text(HEAD[1], size, 600, CREAM, 0, 0)
    box, gap = 170, 52
    total = box + gap + max(w1, w2)
    x0 = max(430, (W - total) / 2 + 60)       # clear of the avatar, balanced to the right
    assert x0 + total <= W - 80, "v3 overflows"
    y_mid = 225
    body = sym(x0, y_mid - box / 2, box)
    tx = x0 + box + gap
    body += text(HEAD[0], size, 600, CREAM, tx, y_mid - 8)[0]
    body += text(HEAD[1], size, 600, CREAM, tx, y_mid - 8 + 56)[0]
    return body, x0 + total


VARIANTS = {"v1-text-right": v1(), "v2-big-symbol": v2(), "v3-minimal": v3()[0]}

# ---- preview overlays: mobile crop band + profile photo
AVATAR_R, AVATAR_C = 167, (207, 497)         # ≈ X desktop avatar (134 px on a 600 px wide banner) × 2.5
def preview(body, title):
    ov = (f'<rect x="0" y="0" width="{W}" height="{SAFE_TOP}" fill="#000" fill-opacity="0.55"/>'
          f'<rect x="0" y="{SAFE_BOT}" width="{W}" height="{H - SAFE_BOT}" fill="#000" fill-opacity="0.55"/>'
          f'<line x1="0" y1="{SAFE_TOP}" x2="{W}" y2="{SAFE_TOP}" stroke="#E5484D" stroke-width="2" stroke-dasharray="10 8"/>'
          f'<line x1="0" y1="{SAFE_BOT}" x2="{W}" y2="{SAFE_BOT}" stroke="#E5484D" stroke-width="2" stroke-dasharray="10 8"/>'
          f'<circle cx="{AVATAR_C[0]}" cy="{AVATAR_C[1]}" r="{AVATAR_R + 8}" fill="#000"/>'
          f'<circle cx="{AVATAR_C[0]}" cy="{AVATAR_C[1]}" r="{AVATAR_R}" fill="{INK}"/>'
          + sym(AVATAR_C[0] - 105, AVATAR_C[1] - 105, 210))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H + 90}" width="{W}" height="{H + 90}">'
            f'<rect width="{W}" height="{H + 90}" fill="#000"/><rect width="{W}" height="{H}" fill="{INK}"/>{body}{ov}</svg>')

for k, body in VARIANTS.items():
    open(os.path.join(OUT, f"banner-{k}.svg"), "w").write(svg(body, f"Solen X banner {k}"))
    open(os.path.join(OUT, f"preview-{k}.svg"), "w").write(preview(body, k))
print("wrote", OUT)
