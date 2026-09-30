"""Solen social templates — 1200×675 X post visuals, Ink & Sun, dark/light.

Templates: audit_wireframe (a), audit_screenshot (b), audit_permission, key_number, journal, schema, table, chart.
Rule: a visual shows the information of the post (number, diagram, table, real capture) — never a restated quote.
All text is outlined from General Sans (set $SOLEN_FONTS to the local Fontshare folder; fonts are not in the repo).
Every function returns an SVG string. Main message: >= 48 px and <= 12 words (asserted).
"""
import base64, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "logo", "_src"))
from solenbrand import split_sun, outline_text  # noqa: E402

GS = os.path.join(os.environ.get("SOLEN_FONTS", ""), "general/GeneralSans_Complete/Fonts/TTF/GeneralSans-Variable.ttf")
W, H, M = 1200, 675, 72
HANDLE = "@thomzzss_"

MODES = {
    "dark": dict(bg="#0E1726", fg="#F6F5F1", accent="#F5A524", accent_text="#F5A524", muted="#8A8F98",
                 surface="#1B2740", line="#243049", ctrl="#F6F5F1"),
    "light": dict(bg="#F6F5F1", fg="#0E1726", accent="#F5A524", accent_text="#B45309", muted="#5B616B",
                  surface="#E7E5DE", line="#D5D9DE", ctrl="#0E1726"),
}
CTRL, VAR = split_sun(gap=0.05, lift=0.11)
CTRL32, VAR32 = split_sun(gap=0.08, lift=0.13)
MIN_MAIN, MAX_WORDS = 48, 12


# ------------------------------------------------------------------ primitives
def _words(s):
    return len(re.findall(r"[^\s→·=≠]+", s))


def check_main(text, size):
    assert size >= MIN_MAIN, f"main message {size}px < {MIN_MAIN}px"
    assert _words(text) <= MAX_WORDS, f"main message has {_words(text)} words (> {MAX_WORDS}): {text}"


ARROW = "→"   # not in General Sans: drawn as a vector arrow


def measure(s, size, weight, track=-0.015):
    parts = s.split(ARROW)
    w = sum(outline_text(GS, p, size, weight, track)[1] for p in parts if p)
    return w + (len(parts) - 1) * size * 0.9


def txt(s, size, weight, color, x, y, track=-0.015, anchor="start"):
    w = measure(s, size, weight, track)
    if anchor == "end":
        x -= w
    elif anchor == "middle":
        x -= w / 2
    out, cx = "", x
    parts = s.split(ARROW)
    for i, part in enumerate(parts):
        if part:
            d, pw, _ = outline_text(GS, part, size, weight, track)
            out += f'<path fill="{color}" transform="translate({cx:.1f} {y:.1f})" d="{d}"/>'
            cx += pw
        if i < len(parts) - 1:
            aw, ay, sw = size * 0.62, y - size * 0.34, max(2.5, size * 0.075)
            ax = cx + size * 0.14
            out += (f'<path d="M{ax:.1f} {ay:.1f} h{aw:.1f} m{-size * 0.2:.1f} {-size * 0.2:.1f} l{size * 0.2:.1f} {size * 0.2:.1f} '
                    f'l{-size * 0.2:.1f} {size * 0.2:.1f}" fill="none" stroke="{color}" stroke-width="{sw:.1f}" '
                    f'stroke-linecap="round" stroke-linejoin="round"/>')
            cx += size * 0.9
    return out, w


def wrap(s, size, weight, maxw, track=-0.015):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if cur and measure(trial, size, weight, track) > maxw:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    lines.append(cur)
    return lines


def block(s, size, weight, color, x, y, maxw, lh=1.15, track=-0.015):
    """Wrapped text; y = first baseline. Returns (svg, last_baseline, n_lines)."""
    out = ""
    lines = wrap(s, size, weight, maxw, track)
    for i, line in enumerate(lines):
        out += txt(line, size, weight, color, x, y + i * size * lh, track)[0]
    return out, y + (len(lines) - 1) * size * lh, len(lines)


def symbol(x, y, box, c, small=False):
    k = box / 256
    a, b = (CTRL32, VAR32) if small else (CTRL, VAR)
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.4f})"><path fill="{c["ctrl"]}" d="{a}"/>'
            f'<path fill="{c["accent"]}" d="{b}"/></g>')


def footer(c):
    """Small lockup bottom-left + handle bottom-right."""
    box = 34
    _, _, mx = outline_text(GS, "x", 1000, 600)
    size = 0.5 * box / (mx["xh"] / 1000)
    d, w, m = outline_text(GS, "solen", size, 600, -0.025)
    y = H - M + 10 - box
    base = y + box / 2 + m["xh"] / 2
    out = symbol(M, y, box, c, small=True)
    out += f'<path fill="{c["fg"]}" transform="translate({M + box * 1.3:.1f} {base:.1f})" d="{d}"/>'
    out += txt(HANDLE, 22, 500, c["muted"], W - M, base, 0, "end")[0]
    return out


def label(s, c, x, y, color=None):
    return txt(s.upper(), 22, 600, color or c["accent_text"], x, y, 0.08)[0]


def frame(body, c, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" role="img" aria-label="{title}"><rect width="{W}" height="{H}" fill="{c["bg"]}"/>'
            f'{body}{footer(c)}</svg>')


def placeholder(x, y, w, h, c, text="SCREENSHOT HERE", r=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c["surface"]}" stroke="{c["accent"]}" '
            f'stroke-width="3" stroke-dasharray="14 10"/>' + txt(text, 30, 600, c["accent_text"], x + w / 2, y + h / 2 + 10, 0.04, "middle")[0])


def image(x, y, w, h, path, r=0):
    data = base64.b64encode(open(path, "rb").read()).decode()
    ext = "png" if path.lower().endswith("png") else "jpeg"
    cid = f"clip{abs(hash((x, y, w, h))) % 10**8}"
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'
            f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMin slice" clip-path="url(#{cid})" '
            f'xlink:href="data:image/{ext};base64,{data}"/>')


# ------------------------------------------------------------------ phone + wireframe
PX, PY, PW, PH = 110, 46, 290, 500          # phone frame (bottom at 546, clear of the footer)
SX, SY, SW, SH = PX + 14, PY + 14, PW - 28, PH - 28   # screen

# generic product page blocks, in screen coordinates (x, y, w, h)
BLOCKS = {
    "header": (0, 0, SW, 32),
    "gallery": (0, 40, SW, 200),
    "title": (16, 252, 190, 16),
    "price": (16, 278, 84, 16),
    "reviews": (112, 278, 118, 16),
    "variants": (16, 304, 230, 30),
    "cta": (16, 344, 230, 40),
    "delivery": (16, 394, 190, 12),
    "returns": (16, 414, 150, 12),
    "description": (16, 434, 230, 10),
}


def wireframe(c, highlight, variant=None, highlight_box=None):
    """Generic product page on a phone. highlight = block name to circle in accent; variant tweaks the page."""
    g = f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="40" fill="none" stroke="{c["line"]}" stroke-width="4"/>'
    g += f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="28" fill="{c["surface"]}"/>'
    blocks = dict(BLOCKS)
    if variant == "cta_low":                    # tall gallery pushes the CTA below the fold
        blocks["gallery"] = (0, 40, SW, 340)
        for k in ("title", "price", "reviews", "variants", "delivery", "returns", "description"):
            blocks.pop(k)
        blocks["cta"] = (16, 400, 230, 40)
    spec = variant if isinstance(variant, dict) else {}
    for k in spec.get("remove", []):
        blocks.pop(k, None)
    blocks.update(spec.get("add", {}))
    for name, (x, y, w, h) in blocks.items():
        fill = c["line"]
        if name == "cta":
            fill = c["fg"]
        g += f'<rect x="{SX + x}" y="{SY + y}" width="{w}" height="{h}" rx="{min(8, h / 2)}" fill="{fill}"/>'
    if variant == "popup":
        g += f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="28" fill="#000" fill-opacity="0.45"/>'
        blocks["popup"] = (24, 130, SW - 48, 210)
        x, y, w, h = blocks["popup"]
        g += f'<rect x="{SX + x}" y="{SY + y}" width="{w}" height="{h}" rx="16" fill="{c["bg"]}" stroke="{c["line"]}" stroke-width="2"/>'
    if variant == "cookie":
        blocks["cookie"] = (0, 260, SW, SH - 260)
        x, y, w, h = blocks["cookie"]
        g += f'<rect x="{SX + x}" y="{SY + y}" width="{w}" height="{h}" rx="20" fill="{c["bg"]}" stroke="{c["line"]}" stroke-width="2"/>'
    if spec.get("panel"):
        x, y, w, h = spec["panel"]
        g += f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="28" fill="#000" fill-opacity="0.45"/>'
        g += f'<rect x="{SX + x}" y="{SY + y}" width="{w}" height="{h}" rx="18" fill="{c["bg"]}"/>'
        for name, (bx, by, bw, bh) in spec.get("panel_blocks", {}).items():
            fill = c["fg"] if name in spec.get("fg", []) else c["line"]
            g += f'<rect x="{SX + bx}" y="{SY + by}" width="{bw}" height="{bh}" rx="{min(8, bh / 2)}" fill="{fill}"/>'
        blocks.update(spec.get("panel_blocks", {}))
    if highlight or highlight_box:
        x, y, w, h = highlight_box or blocks[highlight]
        g += (f'<rect x="{SX + x - 8}" y="{SY + y - 8}" width="{w + 16}" height="{h + 16}" rx="12" fill="none" '
              f'stroke="{c["accent"]}" stroke-width="4"/>'
              f'<circle cx="{SX + x + w + 8}" cy="{SY + y - 8}" r="16" fill="{c["accent"]}"/>'
              + txt("1", 20, 600, "#0E1726", SX + x + w + 8, SY + y - 1, 0, "middle")[0])
    return g


def audit_text(c, number, message, note="Hypothesis, not a result.", extra=""):
    check_main(message, 52)
    x, maxw = 480, W - M - 480
    out = label(f"Friction worth testing #{number}", c, x, 170)
    b, last, _ = block(message, 52, 600, c["fg"], x, 250, maxw)
    out += b + txt(note, 26, 500, c["muted"], x, last + 62)[0] + extra
    return out


# ------------------------------------------------------------------ templates
def audit_wireframe(mode, number, message, highlight=None, variant=None, highlight_box=None):
    c = MODES[mode]
    return frame(wireframe(c, highlight, variant, highlight_box) + audit_text(c, number, message), c, f"Audit #{number}")


def _phone_with(c, content):
    return (f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="40" fill="none" stroke="{c["line"]}" stroke-width="4"/>'
            + content)


def _annot(c, box):
    """box in screen coordinates (x, y, w, h)."""
    x, y, w, h = box
    return (f'<rect x="{SX + x}" y="{SY + y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{c["accent"]}" stroke-width="4"/>'
            f'<circle cx="{SX + x + w}" cy="{SY + y}" r="16" fill="{c["accent"]}"/>'
            + txt("1", 20, 600, "#0E1726", SX + x + w, SY + y + 7, 0, "middle")[0])


def audit_screenshot(mode, number, message, shot=None, box=(16, 700, 358, 56), vp=(390, 844), note=None):
    """(b) real public product page, brand masked (logo, name, URL, recognisable photos blurred before use).
    box = annotation in CSS px of the captured viewport (vp)."""
    c = MODES[mode]
    sh = PH - 28
    sw = sh * vp[0] / vp[1]
    cx = PX + PW / 2
    sx, sy = cx - sw / 2, PY + 14
    k = sw / vp[0]
    phone = (f'<rect x="{sx - 14:.1f}" y="{PY}" width="{sw + 28:.1f}" height="{PH}" rx="40" fill="none" '
             f'stroke="{c["line"]}" stroke-width="4"/>')
    content = image(sx, sy, sw, sh, shot, 24) if shot else placeholder(sx, sy, sw, sh, c, "SCREENSHOT", 24)
    bx, by, bw, bh = box
    ann = (f'<rect x="{sx + bx * k:.1f}" y="{sy + by * k:.1f}" width="{bw * k:.1f}" height="{bh * k:.1f}" rx="8" fill="none" '
           f'stroke="{c["accent"]}" stroke-width="4"/>'
           f'<circle cx="{sx + (bx + bw) * k:.1f}" cy="{sy + by * k:.1f}" r="16" fill="{c["accent"]}"/>'
           + txt("1", 20, 600, "#0E1726", sx + (bx + bw) * k, sy + by * k + 7, 0, "middle")[0])
    extra = txt(note, 24, 500, c["muted"], 480, 520)[0] if note else ""
    return frame(phone + content + ann + audit_text(c, number, message, note="Hypothesis, not a result. Public page, brand masked.", extra=extra),
                 c, f"Audit #{number}")


def audit_permission(mode, number, message, brand, shot=None, box=(16, 336, 230, 56)):
    """Merchant-requested audit: brand visible, 'Shared with permission'."""
    c = MODES[mode]
    content = image(SX, SY, SW, SH, shot, 28) if shot else placeholder(SX, SY, SW, SH, c, "SCREENSHOT", 28)
    badge = (f'<rect x="480" y="508" width="300" height="46" rx="23" fill="none" stroke="{c["accent"]}" stroke-width="2.5"/>'
             + txt("Shared with permission", 22, 600, c["accent_text"], 630, 539, 0.01, "middle")[0])
    extra = txt(brand, 26, 600, c["fg"], 480, 485)[0] + badge
    check_main(message, 52)
    x, maxw = 480, W - M - 480
    body = label(f"Audit · requested by the merchant", c, x, 170)
    b, last, _ = block(message, 52, 600, c["fg"], x, 250, maxw)
    body += b + txt("Hypotheses, not results.", 26, 500, c["muted"], x, last + 62)[0] + extra
    return frame(_phone_with(c, content) + _annot(c, box) + body, c, "Audit with permission")


def key_number(mode, number, caption, source=None, note=None):
    c = MODES[mode]
    check_main(caption, 52)
    out = txt(number, 200, 600, c["accent_text"], M, 290, -0.03)[0]
    b, last, _ = block(caption, 52, 600, c["fg"], M, 390, W - 2 * M)
    out += b
    if note:
        out += txt(note, 28, 500, c["muted"], M, last + 56)[0]
    if source:
        out += txt(source, 22, 500, c["muted"], M, 540)[0]
    return frame(out, c, number)


def journal(mode, day, title, shot=False, image_path=None):
    c = MODES[mode]
    check_main(title, 52)
    out = label(f"Day {day} · build log", c, M, 150)
    if shot or image_path:
        maxw = 470
        b, _, _ = block(title, 52, 600, c["fg"], M, 230, maxw)
        out += b
        sx, sy, sw, sh = 600, 110, 528, 400
        out += image(sx, sy, sw, sh, image_path, 14) if image_path else placeholder(sx, sy, sw, sh, c)
    else:
        b, _, _ = block(title, 64, 600, c["fg"], M, 250, W - 2 * M)
        out += b
    return frame(out, c, f"Day {day}")


def chart(mode, title, kind, items, highlight=None, note=None):
    """kind: 'flow' (boxes + arrows), 'columns' (boxes, no arrows), 'list' (numbered rows), 'range' (bars with values).
    items: list of labels; for 'range' a list of (label, value, display)."""
    c = MODES[mode]
    check_main(title, 52)
    out, last, _ = block(title, 52, 600, c["fg"], M, 150, W - 2 * M)
    top = last + 60
    if kind in ("flow", "columns"):
        n = len(items)
        gap = 36 if kind == "flow" else 20
        bw = (W - 2 * M - gap * (n - 1)) / n
        bh = 120
        size = 26 if bw > 150 else 22
        for i, it in enumerate(items):
            x = M + i * (bw + gap)
            hi = highlight is not None and i == highlight
            out += (f'<rect x="{x:.1f}" y="{top}" width="{bw:.1f}" height="{bh}" rx="16" '
                    f'fill="{c["accent"] if hi else c["surface"]}" stroke="{c["line"]}" stroke-width="2"/>')
            lines = wrap(it, size, 600, bw - 24)
            for j, ln in enumerate(lines):
                yy = top + bh / 2 + (j - (len(lines) - 1) / 2) * size * 1.15 + size * 0.35
                out += txt(ln, size, 600, "#0E1726" if hi else c["fg"], x + bw / 2, yy, 0, "middle")[0]
            if kind == "flow" and i < n - 1:
                ax = x + bw + 8
                out += (f'<path d="M{ax:.1f} {top + bh / 2} h{gap - 16} m-8 -8 l8 8 l-8 8" fill="none" '
                        f'stroke="{c["accent"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    elif kind == "list":
        for i, it in enumerate(items):
            y = top + i * 56
            out += (f'<circle cx="{M + 18}" cy="{y}" r="18" fill="{c["accent"]}"/>'
                    + txt(str(i + 1), 20, 600, "#0E1726", M + 18, y + 7, 0, "middle")[0]
                    + txt(it, 30, 500, c["fg"], M + 56, y + 10)[0])
    elif kind == "range":
        vmax = max(v for _, v, _ in items)
        for i, (lab, v, disp) in enumerate(items):
            y = top + i * 78
            bw = (W - 2 * M - 360) * v / vmax
            hi = highlight is not None and i == highlight
            out += txt(lab, 26, 500, c["muted"], M, y + 34)[0]
            out += f'<rect x="{M + 170}" y="{y}" width="{max(bw, 6):.1f}" height="48" rx="8" fill="{c["accent"] if hi else c["line"]}"/>'
            out += txt(disp, 30, 600, c["fg"], M + 190 + bw, y + 35)[0]
    if note:
        out += txt(note, 22, 500, c["muted"], M, 548)[0]
    return frame(out, c, title)


def _arrow(c, x1, y1, x2, y2):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 12 * math.cos(a - 0.5), y2 - 12 * math.sin(a - 0.5)
    kx, ky = x2 - 12 * math.cos(a + 0.5), y2 - 12 * math.sin(a + 0.5)
    return (f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} M{hx:.1f} {hy:.1f} L{x2:.1f} {y2:.1f} L{kx:.1f} {ky:.1f}" '
            f'fill="none" stroke="{c["accent"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')


def _node(c, x, y, w, h, label, hi=False, size=24):
    out = (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="14" '
           f'fill="{c["accent"] if hi else c["surface"]}" stroke="{c["line"]}" stroke-width="2"/>')
    lines = wrap(label, size, 600, w - 20)
    for j, ln in enumerate(lines):
        yy = y + h / 2 + (j - (len(lines) - 1) / 2) * size * 1.15 + size * 0.35
        out += txt(ln, size, 600, "#0E1726" if hi else c["fg"], x + w / 2, yy, 0, "middle")[0]
    return out


def schema(mode, title, nodes, kind="flow", highlight=None, note=None):
    """Process / architecture diagram. kind: 'flow' (left to right) or 'loop' (nodes on a ring, last returns to first)."""
    import math
    c = MODES[mode]
    check_main(title, 52)
    out, last, _ = block(title, 52, 600, c["fg"], M, 150, W - 2 * M)
    if kind == "flow":
        n, gap = len(nodes), 40
        bw = (W - 2 * M - gap * (n - 1)) / n
        top, bh = last + 70, 130
        for i, lab in enumerate(nodes):
            x = M + i * (bw + gap)
            out += _node(c, x, top, bw, bh, lab, i == highlight, 24 if bw > 150 else 21)
            if i < n - 1:
                out += _arrow(c, x + bw + 6, top + bh / 2, x + bw + gap - 6, top + bh / 2)
    elif kind == "columns":
        n, gap = len(nodes), 24
        bw = (W - 2 * M - gap * (n - 1)) / n
        top, bh = last + 60, 170
        for i, lab in enumerate(nodes):
            out += _node(c, M + i * (bw + gap), top, bw, bh, lab, i == highlight, 26)
    else:  # loop
        n = len(nodes)
        cx, cy, rx, ry = W / 2, last + 150, 360, 100
        bw, bh = 190, 64
        pts = [(cx + rx * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + ry * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]
        for i in range(n):
            (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
            dx, dy = x2 - x1, y2 - y1
            L = math.hypot(dx, dy)
            sx = x1 + dx / L * 105
            sy = y1 + dy / L * 40
            ex = x2 - dx / L * 105
            ey = y2 - dy / L * 40
            out += _arrow(c, sx, sy, ex, ey)
        for i, (x, y) in enumerate(pts):
            out += _node(c, x - bw / 2, y - bh / 2, bw, bh, nodes[i], i == highlight, 22)
    if note:
        out += txt(note, 22, 500, c["muted"], M, 548)[0]
    return frame(out, c, title)


def _check(c, x, y, ok=True):
    if ok:
        return (f'<path d="M{x} {y} l8 8 l16 -18" fill="none" stroke="{c["accent"]}" stroke-width="4" '
                f'stroke-linecap="round" stroke-linejoin="round"/>')
    return f'<rect x="{x}" y="{y - 12}" width="22" height="22" rx="5" fill="none" stroke="{c["muted"]}" stroke-width="2.5"/>'


def table(mode, title, header, rows, col_w=None, highlight_row=None, check_col=None, note=None, size=26, primary_col=0):
    """Comparison table or checklist. header: list of column titles (or None); rows: list of lists of strings.
    check_col: index of a column rendered as a check mark ('yes'/'no' cells)."""
    c = MODES[mode]
    check_main(title, 52)
    out, last, _ = block(title, 52, 600, c["fg"], M, 150, W - 2 * M)
    ncol = len(rows[0])
    col_w = col_w or [(W - 2 * M) / ncol] * ncol
    y = last + 56
    rh = 58 if len(rows) <= 5 else 50
    if header:
        x = M
        for j, h in enumerate(header):
            out += txt(h.upper(), 20, 600, c["accent_text"], x + 14, y + 20, 0.06)[0]
            x += col_w[j]
        y += 36
    for i, row in enumerate(rows):
        if highlight_row == i:
            out += f'<rect x="{M}" y="{y}" width="{W - 2 * M}" height="{rh}" rx="10" fill="{c["surface"]}"/>'
        out += f'<line x1="{M}" y1="{y + rh}" x2="{W - M}" y2="{y + rh}" stroke="{c["line"]}" stroke-width="2"/>'
        x = M
        for j, cell in enumerate(row):
            if check_col == j:
                out += _check(c, x + 14, y + rh / 2 - 2, cell == "yes")
            else:
                prim = j == primary_col
                out += txt(cell, size, 600 if prim else 500, c["fg"] if prim else c["muted"], x + 14, y + rh / 2 + size * 0.35)[0]
            x += col_w[j]
        y += rh
    if note:
        out += txt(note, 22, 500, c["muted"], M, 548)[0]
    return frame(out, c, title)
