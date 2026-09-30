"""Shared helpers for the Solen split-sun identity: symbol geometry, text outlining, WCAG contrast.

Font files are NOT stored in the repo (Fontshare FFL forbids redistribution); pass their paths in.
"""
import math

# ---------------------------------------------------------------- symbol geometry
def _f(v):
    return f"{round(v, 2):g}"


def half(cx, cy, r, side, rho=0.0):
    """Half disc with its flat edge on x=cx. side=-1 bulges left (control), +1 right (variant).
    rho = radius of the rounded inner corners (0 = sharp)."""
    sweep = 0 if side < 0 else 1
    if rho <= 0:
        return (f"M{_f(cx)} {_f(cy - r)} A{_f(r)} {_f(r)} 0 0 {sweep} {_f(cx)} {_f(cy + r)} Z")
    fx = cx + side * rho
    dy = math.sqrt((r - rho) ** 2 - rho ** 2)
    k = r / (r - rho)
    t1_top, t1_bot = (cx, cy - dy), (cx, cy + dy)
    t2_top = (cx + (fx - cx) * k, cy - dy * k)
    t2_bot = (cx + (fx - cx) * k, cy + dy * k)
    return (f"M{_f(t1_top[0])} {_f(t1_top[1])}"
            f" A{_f(rho)} {_f(rho)} 0 0 {sweep} {_f(t2_top[0])} {_f(t2_top[1])}"
            f" A{_f(r)} {_f(r)} 0 0 {sweep} {_f(t2_bot[0])} {_f(t2_bot[1])}"
            f" A{_f(rho)} {_f(rho)} 0 0 {sweep} {_f(t1_bot[0])} {_f(t1_bot[1])} Z")


def split_sun(gap=0.05, lift=0.10, var_scale=1.0, rho=0.0, box=256, fill_ratio=0.875):
    """Return (control_path, variant_path) for a split disc centred in a box×box canvas.
    gap, lift: fractions of the control diameter. var_scale: variant radius / control radius.
    rho: inner-corner radius as a fraction of the control radius."""
    # unit geometry with control radius 1
    g, L, s = gap * 2, lift * 2, var_scale
    w = 1 + g + s                      # width in control radii
    top = min(-1, -L - s)              # control centre at y=0, variant centre at y=-L
    bot = max(1, -L + s)
    h = bot - top
    R = fill_ratio * box / max(w, h)   # control radius in px
    ox = box / 2 - (w * R) / 2 + R     # control centre x
    oy = box / 2 - ((top + bot) / 2) * R
    cxl = ox                           # flat edge of control half = its centre x
    cxr = cxl + g * R
    return (half(cxl, oy, R, -1, rho * R), half(cxr, oy - L * R, s * R, +1, rho * R * s))


def symbol_svg(paths, colors=("#111111", "#111111"), box=256, title="Solen symbol", bg=None):
    ctrl, var = paths
    bgr = f'<rect width="{box}" height="{box}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {box} {box}" width="{box}" height="{box}" '
            f'role="img" aria-labelledby="title"><title id="title">{title}</title>{bgr}'
            f'<g id="symbol"><path id="control" fill="{colors[0]}" d="{ctrl}"/>'
            f'<path id="variant" fill="{colors[1]}" d="{var}"/></g></svg>')


# ---------------------------------------------------------------- text outlining
def outline_text(font_path, text, size, weight=None, tracking=0.0):
    """Return (svg_path_d, advance_width_px, metrics) for `text` set at `size` px, baseline at y=0.
    tracking: extra spacing in em (e.g. -0.02). Uses HarfBuzz shaping (kerning) when available."""
    from fontTools.ttLib import TTFont
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen

    font = TTFont(font_path)
    if "fvar" in font and weight is not None:
        from fontTools.varLib import instancer
        font = instancer.instantiateVariableFont(font, {"wght": weight}, inplace=False)
    upm = font["head"].unitsPerEm
    scale = size / upm
    gs = font.getGlyphSet()
    try:
        import uharfbuzz as hb
        blob = hb.Blob.from_file_path(font_path)
        face = hb.Face(blob)
        hbf = hb.Font(face)
        if weight is not None:
            hbf.set_variations({"wght": weight})
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(hbf, buf, {"kern": True, "liga": False})
        order = font.getGlyphOrder()
        glyphs = [(order[i.codepoint], p.x_advance, p.x_offset) for i, p in zip(buf.glyph_infos, buf.glyph_positions)]
    except Exception:
        cmap = font.getBestCmap()
        glyphs = [(cmap[ord(c)], font["hmtx"][cmap[ord(c)]][0], 0) for c in text]
    x = 0.0
    parts = []
    for i, (name, adv, xoff) in enumerate(glyphs):
        pen = SVGPathPen(gs, ntos=lambda v: f"{round(v, 2):g}")
        gs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x + xoff * scale, 0)))
        parts.append(pen.getCommands())
        x += adv * scale
        if i < len(glyphs) - 1:
            x += tracking * size
    os2 = font["OS/2"]
    metrics = {"xh": os2.sxHeight * scale, "cap": os2.sCapHeight * scale}
    return " ".join(parts), x, metrics


# ---------------------------------------------------------------- WCAG
def _lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_):
    h = hex_.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def wcag(ratio):
    if ratio >= 7:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    if ratio >= 3:
        return "AA large / UI"
    return "Fail"
