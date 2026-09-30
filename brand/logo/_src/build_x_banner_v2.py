"""X header banner v2 — mobile-safe. 1500×500, Ink & Sun. Writes brand/x/banner-v2/.
Rules: content in x 250–1250, y 190–430; nothing above y 170; empty where x < 450 and y > 300 (avatar).
Fonts are read from $SOLEN_FONTS (not stored in the repo)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from solenbrand import split_sun, outline_text

GS = os.path.join(os.environ["SOLEN_FONTS"], "general/GeneralSans_Complete/Fonts/TTF/GeneralSans-Variable.ttf")
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "x", "banner-v2"))
os.makedirs(OUT, exist_ok=True)

W, H = 1500, 500
INK, CREAM, AMBER = "#0E1726", "#F6F5F1", "#F5A524"
TEX_CTRL, TEX_VAR = "#131F33", "#1A2740"      # background texture: very low contrast (1.1–1.3:1 on ink)
LINE = "The self-optimizing commerce layer for Shopify."
SIZE = 44
SAFE = dict(x0=250, x1=1250, y0=190, y1=430)
CTRL, VAR = split_sun(gap=0.05, lift=0.11)


def sym(x, y, box, ctrl=CREAM, var=AMBER):
    k = box / 256
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.4f})">'
            f'<path fill="{ctrl}" d="{CTRL}"/><path fill="{var}" d="{VAR}"/></g>')


def text(s, x, y, size=SIZE, weight=600, color=CREAM):
    d, w, m = outline_text(GS, s, size, weight, -0.015)
    return f'<path fill="{color}" transform="translate({x:.1f} {y:.1f})" d="{d}"/>', w


def check(boxes):
    """boxes: list of (name, x0, y0, x1, y1) for important content."""
    for n, x0, y0, x1, y1 in boxes:
        assert x0 >= SAFE["x0"] and x1 <= SAFE["x1"] and y0 >= SAFE["y0"] and y1 <= SAFE["y1"], f"{n} outside safe zone"
        assert not (x0 < 450 and y1 > 300), f"{n} enters the avatar zone"


# ---- A · one line + symbol sign-off bottom-right + background texture
def variant_a():
    _, w = text(LINE, 0, 0)
    x = SAFE["x1"] - 12 - w                        # right-leaning inside the safe zone
    base = 282                                     # descenders stay above y = 300
    t, _ = text(LINE, x, base)
    box = 96
    sx, sy = x + w - box * 0.93, 318               # symbol aligned to the line's right edge
    check([("headline", x, base - 34, x + w, base + 11), ("symbol", sx, sy, sx + box, sy + box)])
    texture = sym(1000, -10, 520, TEX_CTRL, TEX_VAR)
    # wordmark-only sign-off ("solen", General Sans 600, tracking -2.5%), right-aligned under the line
    wd, ww, wm = outline_text(GS, "solen", 46, 600, -0.025)
    wx, wbase = x + w - ww, 368
    check([("wordmark", wx, wbase - wm["xh"] - 12, wx + ww, wbase)])
    word = f'<path fill="{AMBER}" transform="translate({wx:.1f} {wbase})" d="{wd}"/>'
    # full lockup sign-off (symbol + "solen"), same proportions as brand/logo/b-v2: x-height = 50% of the symbol box
    lb = 72
    _, _, mx = outline_text(GS, "x", 1000, 600)
    lsize = 0.50 * lb / (mx["xh"] / 1000)
    ld, lw, lm = outline_text(GS, "solen", lsize, 600, -0.025)
    lock_w = lb * 1.30 + lw
    lx, ly = x + w - lock_w, 318
    lbase = ly + lb / 2 + lm["xh"] / 2
    check([("lockup", lx, ly, lx + lock_w, ly + lb)])
    lock = sym(lx, ly, lb) + f'<path fill="{CREAM}" transform="translate({lx + lb * 1.30:.1f} {lbase:.1f})" d="{ld}"/>'
    return texture + t + sym(sx, sy, box), texture + t, texture + t + word, texture + t + lock


# ---- B · symbol left + headline on two lines
def variant_b():
    l1, l2 = "The self-optimizing commerce layer", "for Shopify."
    box, gap = 104, 46
    sx, sy = 300, 196
    tx = sx + box + gap                           # = 450: second line clears the avatar zone
    t1, w1 = text(l1, tx, 246)
    t2, w2 = text(l2, tx, 304)
    check([("symbol", sx, sy, sx + box, sy + box), ("line 1", tx, 212, tx + w1, 257), ("line 2", tx, 270, tx + w2, 315)])
    return sym(sx, sy, box) + t1 + t2


def banner(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Solen">'
            f'<rect width="{W}" height="{H}" fill="{INK}"/>{body}</svg>')


# ---- previews
def iphone(body, ox, oy):
    """iPhone profile: sides cropped 8%, top 35% under the UI, round avatar bottom-left."""
    cx0, cw = 120, 1260                           # 8% cropped on each side
    av_d = 250
    return (f'<g transform="translate({ox} {oy})">'
            f'<svg x="0" y="0" width="{cw}" height="{H}" viewBox="{cx0} 0 {cw} {H}"><rect x="{cx0}" width="{cw}" height="{H}" fill="{INK}"/>{body}</svg>'
            f'<rect width="{cw}" height="{H * 0.35:.0f}" fill="#000" fill-opacity="0.6"/>'
            f'<text x="60" y="58" font-family="-apple-system,Helvetica,Arial" font-size="34" font-weight="600" fill="#fff">9:41</text>'
            f'<circle cx="80" cy="130" r="30" fill="#000" fill-opacity="0.55"/><path d="M88 116 L74 130 L88 144" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{cw - 80}" cy="130" r="30" fill="#000" fill-opacity="0.55"/><circle cx="{cw - 84}" cy="126" r="11" stroke="#fff" stroke-width="5" fill="none"/><path d="M{cw - 76} 134 L{cw - 68} 142" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
            f'<rect y="{H}" width="{cw}" height="170" fill="#000"/>'
            f'<circle cx="{50 + av_d / 2}" cy="{H}" r="{av_d / 2 + 7}" fill="#000"/><circle cx="{50 + av_d / 2}" cy="{H}" r="{av_d / 2}" fill="{INK}"/>'
            + sym(50 + av_d / 2 - 80, H - 80, 160) +
            f'<text x="0" y="{H + 150}" font-family="-apple-system,Helvetica,Arial" font-size="26" fill="#8A8F98">iPhone profile · sides −8% · top 35% under UI</text></g>')


def desktop(body, ox, oy):
    r = 167
    return (f'<g transform="translate({ox} {oy})"><svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{INK}"/>{body}</svg>'
            f'<rect y="{H}" width="{W}" height="190" fill="#000"/>'
            f'<circle cx="{40 + r}" cy="{330 + r}" r="{r + 8}" fill="#000"/><circle cx="{40 + r}" cy="{330 + r}" r="{r}" fill="{INK}"/>'
            + sym(40 + r - 105, 330 + r - 105, 210) +
            f'<text x="0" y="{H + 170}" font-family="-apple-system,Helvetica,Arial" font-size="26" fill="#8A8F98">Desktop profile</text></g>')


def preview(body, name):
    ph = 40 + H + 170 + 40 + H + 190 + 40
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W + 80} {ph}" width="{W + 80}" height="{ph}">'
            f'<rect width="100%" height="100%" fill="#000"/>{iphone(body, 40 + 120, 40)}{desktop(body, 40, 40 + H + 170 + 40)}</svg>')


a_full, a_nologo, a_word, a_lock = variant_a()
for name, body in (("a-one-line", a_full), ("a-no-logo", a_nologo), ("a-wordmark", a_word), ("a-lockup", a_lock), ("b-two-lines", variant_b())):
    open(os.path.join(OUT, f"banner-{name}.svg"), "w").write(banner(body))
    open(os.path.join(OUT, f"preview-{name}.svg"), "w").write(preview(body, name))
print("wrote", OUT)
