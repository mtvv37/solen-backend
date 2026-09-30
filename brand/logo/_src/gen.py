"""Generate Solen logo concepts (black-first) into brand/logo/."""
import math, os

OUT = "/Users/thomasmetivier/solen-backend/brand/logo"
os.makedirs(OUT, exist_ok=True)
INK = "#111111"

def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return round(cx + r * math.cos(a), 2), round(cy + r * math.sin(a), 2)

def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-labelledby="title">\n  <title id="title">{title}</title>\n{body}\n</svg>\n')

# ---------- Concept A: Open spiral (abstract) ----------
# One continuous stroke built from tangent semicircles whose radius grows each half-turn:
# a loop that never returns to the same place — each pass ends a step further out.
def concept_a():
    k = 1.3                                  # scale baked into geometry
    sw, d, r1 = 22 * k, 18 * k, 40 * k
    r2, r3 = r1 + d, r1 + 2 * d
    ang = -35
    # raw bbox with centre c=(0,0), c2=(-d,0), then shift so the bbox is centred on 128
    minx = -d - r2 - sw / 2
    maxx = r3 * math.cos(math.radians(ang)) + sw / 2
    miny, maxy = -r3 - sw / 2, r2 + sw / 2
    ox, oy = 128 - (minx + maxx) / 2, 128 - (miny + maxy) / 2
    c, c2 = (ox, oy), (ox - d, oy)
    ex, ey = pt(*c, r3, ang)
    f = lambda v: round(v, 2)
    path = (f"M{f(c[0]-r1)} {f(c[1])} A{f(r1)} {f(r1)} 0 0 1 {f(c[0]+r1)} {f(c[1])}"
            f" A{f(r2)} {f(r2)} 0 0 1 {f(c2[0]-r2)} {f(c2[1])}"
            f" A{f(r3)} {f(r3)} 0 0 1 {ex} {ey}")
    return (f'  <g id="symbol" fill="none" stroke="{INK}" stroke-width="{f(sw)}" stroke-linecap="round">\n'
            f'    <path d="{path}"/>\n  </g>')

# ---------- Concept B: Split sun (abstract, A/B) ----------
# A disc (Sol) split into control and variant; the variant half sits one step (16) higher.
def concept_b():
    r, gap, lift = 88, 12, 16
    lx = 128 - gap / 2
    rx = 128 + gap / 2
    ly = 128 + lift / 2
    ry = 128 - lift / 2
    left = f"M{lx} {ly - r} A{r} {r} 0 0 0 {lx} {ly + r} Z"
    right = f"M{rx} {ry - r} A{r} {r} 0 0 1 {rx} {ry + r} Z"
    return (f'  <g id="symbol" fill="{INK}">\n    <path d="{left}"/>\n    <path d="{right}"/>\n  </g>')

# ---------- Concept C: S-trace (letterform) ----------
# A monoline S drawn as one trajectory (two tangent arcs), set in motion by a detached dot:
# the observation that starts the path.
def concept_c():
    k = 1.2
    f = lambda v: round(v, 2)
    r, sw = 40 * k, 28 * k
    X = lambda x: 128 + k * (x - 134.9)      # recentre horizontally (optical bbox of the drawing)
    tc, bc = (X(128), 128 - 40 * k), (X(128), 128 + 40 * k)
    x1, y1 = pt(*tc, r, -60)
    x2, y2 = pt(*bc, r, 140)
    d = f"M{x1} {y1} A{f(r)} {f(r)} 0 1 0 {f(tc[0])} 128 A{f(r)} {f(r)} 0 1 1 {x2} {y2}"
    dx, dy = pt(*tc, r, 5)
    return (f'  <g id="symbol">\n    <path d="{d}" fill="none" stroke="{INK}" stroke-width="{f(sw)}" stroke-linecap="round"/>\n'
            f'    <circle cx="{dx}" cy="{dy}" r="{f(sw/2)}" fill="{INK}"/>\n  </g>')

# ---------- Shared geometric wordmark "solen" (monoline, exploration) ----------
def wordmark(x0):
    w = 18                       # stroke
    top, bot = 87, 169           # centerline x-height band (baseline 178)
    cy, R = 128, 41
    parts = []
    # s
    rs = (bot - top) / 4
    scx = x0 + rs + w / 2
    t1 = (scx, top + rs); b1 = (scx, bot - rs)
    sx1, sy1 = pt(*t1, rs, -30); sx2, sy2 = pt(*b1, rs, 150)
    parts.append(f"M{sx1} {sy1} A{rs} {rs} 0 1 0 {scx} {cy} A{rs} {rs} 0 1 1 {sx2} {sy2}")
    x = scx + rs + w / 2
    # o
    ocx = x + 18 + w / 2 + R
    parts.append(f"M{ocx - R} {cy} A{R} {R} 0 1 1 {ocx + R} {cy} A{R} {R} 0 1 1 {ocx - R} {cy} Z")
    x = ocx + R + w / 2
    # l
    lx = x + 22 + w / 2
    parts.append(f"M{lx} 52 V{bot}")
    x = lx + w / 2
    # e
    ecx = x + 22 + w / 2 + R
    ex, ey = pt(ecx, cy, R, 40)
    parts.append(f"M{ecx - R} {cy} H{ecx + R} A{R} {R} 0 1 0 {ex} {ey}")
    x = ecx + R + w / 2
    # n
    n1 = x + 20 + w / 2
    n2 = n1 + 2 * R
    parts.append(f"M{n1} {top} V{bot} M{n1} {cy} A{R} {R} 0 0 1 {n2} {cy} V{bot}")
    right = n2 + w / 2
    g = (f'  <g id="wordmark" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">\n'
         + "\n".join(f'    <path d="{d}"/>' for d in parts) + "\n  </g>")
    return g, right

def lockup(symbol_body, title):
    s = 0.72
    sym = f'  <g transform="translate(0 {round((256 - 256 * s) / 2, 2)}) scale({s})">\n{symbol_body}\n  </g>'
    wm, right = wordmark(256 * s + 36)
    return svg(round(right + 8), 256, title, sym + "\n" + wm)

for key, name, fn in [("a", "open-spiral", concept_a), ("b", "split-sun", concept_b), ("c", "s-trace", concept_c)]:
    body = fn()
    open(f"{OUT}/concept-{key}-{name}.svg", "w").write(svg(256, 256, f"Solen symbol, concept {key.upper()}", body))
    open(f"{OUT}/concept-{key}-{name}-lockup.svg", "w").write(lockup(body, f"Solen logo, concept {key.upper()}"))
print("ok")
