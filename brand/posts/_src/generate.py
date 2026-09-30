"""Step 2 — generate the 40 post visuals (1200×675 PNG) into brand/posts/, named jour-DD-x.png.
Content follows brand/posts/PLAN.md. Requires $SOLEN_FONTS. Audit (b) captures come from _captures/ (see capture.py)."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(POSTS, "..", "templates"))
import solen_templates as T  # noqa: E402

CAP = json.load(open(os.path.join(POSTS, "_captures", "captures.json")))
shot = lambda k: os.path.join(POSTS, "_captures", os.path.basename(CAP[k]["file"]))
SH = T.SH
INPUTS = os.path.join(POSTS, "inputs")


def inp(key):
    """Real screenshot dropped by Thomas in brand/posts/inputs/jour-DD-x.png (or .jpg), if present."""
    day, slot = int(key[:-1]), key[-1].lower()
    for ext in ("png", "jpg", "jpeg"):
        f = os.path.join(INPUTS, f"jour-{day:02d}-{slot}.{ext}")
        if os.path.exists(f):
            return f
    return None

VISUALS = {
    # ---- day 1
    "1A": lambda: T.journal("dark", 1, "Prototype runs. 0 customers. Building in public.", shot=True, image_path=inp("1A")),
    "1B": lambda: T.table("dark", "Observation → hypothesis → test → result: one example.", ["Step", "Statement"],
                          [["Observation", "Mobile visitors rarely reach the CTA."], ["Hypothesis", "The CTA sits too low."],
                           ["Test", "Higher CTA vs control."], ["Result", "Not tested yet."]], col_w=[260, 796], highlight_row=3),
    "2A": lambda: T.audit_screenshot("dark", 1, "Add-to-cart below the fold? I'd test moving it up.", shot("01"), CAP["01"]["box"],
                                     note="Add-to-cart starts at 1,174px. Screen: 844px."),
    "2B": lambda: T.journal("light", 2, "What the prototype does, and doesn't.", shot=True, image_path=inp("2B")),
    "3A": lambda: T.key_number("dark", "2.87M", "live Shopify stores.", source="Source: Store Leads, 2026"),
    "3B": lambda: T.table("dark", "Sizing inputs: one sourced number, two guesses.", ["Input", "Value", "Status"],
                          [["Live Shopify stores", "2.87M", "Sourced · Store Leads, 2026"],
                           ["Share with 10k+ visitors/month", "5–15%", "Guess"],
                           ["Yearly spend on CRO tools", "$600–3,000", "Guess"]], col_w=[440, 220, 396], size=25),
    "3C": lambda: T.chart("dark", "TAM: $86M to $1.29B. A 15x range.", "range",
                          [("Low", 86, "$86M"), ("Central", 430, "$430M"), ("High", 1290, "$1.29B")], highlight=1,
                          note="Bottom-up estimate. Two of three inputs are unverified guesses."),
    # ---- days 4–8
    "4A": lambda: T.audit_screenshot("light", 2, "Shipping cost only at checkout? I'd test showing it earlier.", shot("02"), CAP["02"]["box"]),
    "5B": lambda: T.audit_wireframe("dark", 3, "Hidden size options? I'd test visible swatches.", "variants"),
    "5C": lambda: T.schema("dark", "What's built: script → API → database → analysis.",
                           ["Tracking script", "API (Vercel)", "Events (Supabase)", "Heatmaps + LLM analysis"], "flow", highlight=3,
                           note="Not built yet: multi-store, consent, experiments."),
    "6B": lambda: T.audit_wireframe("dark", 4, "Reviews buried at the bottom? I'd test stars near the price.",
                                    variant={"remove": ["reviews"], "add": {"reviews_bottom": (16, 434, 230, 10)}}, highlight="reviews_bottom"),
    "6C": lambda: T.table("dark", "Honest status: prototype yes, customers 0, revenue 0.", ["", "Week 1"],
                          [["Prototype", "Runs"], ["Customers", "0"], ["Revenue", "0"], ["Cofounder", "Not yet"]], col_w=[360, 696]),
    "7A": lambda: T.schema("light", "Observation → Hypothesis → Test → Result",
                           ["Mobile users scroll less", "Move the CTA up", "Controlled test vs control", "Only now: a result"],
                           "flow", highlight=2, note="The step most pitches skip is the test."),
    "8A": lambda: T.audit_screenshot("dark", 5, "Return policy in the footer? I'd test it near the CTA.", shot("05"), CAP["05"]["box"],
                                     note="Returns info found only in the footer."),
    "8C": lambda: T.schema("dark", "Where would you stop? 1 · 2 · 3 · 4",
                           ["1 · Flag problems", "2 · Draft changes, you approve", "3 · Run controlled tests", "4 · Deploy under strict rules"], "flow"),
    # ---- days 9–13
    "9B": lambda: T.audit_wireframe("dark", 6, "Slow images on mobile? I'd test compression first.", "gallery"),
    "10C": lambda: T.audit_wireframe("dark", 7, "Hidden free-shipping threshold? I'd test a progress bar.", "delivery"),
    "11A": lambda: T.key_number("dark", "~38%", "of live Shopify stores are in the US.", source="Source: Store Leads, 2026"),
    "11B": lambda: T.audit_wireframe("light", 8, "Size guide as a PDF? I'd test an inline drawer.",
                                     variant={"remove": ["reviews"], "add": {"sizeguide": (150, 278, 96, 16)}}, highlight="sizeguide"),
    "11C": lambda: T.table("dark", "Pilot: what you get, what I ask.", ["You get", "I ask"],
                           [["Weekly friction report", "Install a script"], ["Heatmaps per device", "30 min per week"],
                            ["A weekly call", "Honest feedback"]], col_w=[528, 528],
                           note="4 weeks. Free for the first 3 stores. No promised uplift."),
    "12C": lambda: T.audit_wireframe("dark", 9, "Instant pop-up on mobile? I'd test a delay.", "popup", variant="popup"),
    "13B": lambda: T.audit_wireframe("dark", 10, "No delivery date? I'd test showing one near the CTA.",
                                     variant={"remove": ["delivery"]}, highlight_box=(16, 392, 190, 16)),
    # ---- days 15–19
    "15A": lambda: T.journal("dark", 15, "What the prototype gets wrong.", shot=True, image_path=inp("15A")),
    "15B": lambda: T.audit_wireframe("light", 12, "Checkout button below upsells? I'd test pinning it.",
                                     variant={"panel": (60, 0, T.SW - 60, SH),
                                              "panel_blocks": {"item": (76, 40, 170, 56), "upsell1": (76, 116, 170, 110),
                                                               "upsell2": (76, 240, 170, 110), "checkout": (76, 400, 170, 40)},
                                              "fg": ["checkout"]}, highlight="checkout"),
    "17B": lambda: T.audit_wireframe("dark", 14, "Out-of-stock but selectable? I'd test greying it out.", "variants"),
    "17C": lambda: T.table("dark", "Five guardrails before any automated change.", None,
                           [["yes", "A control group"], ["yes", "One primary metric, plus secondary checks"], ["yes", "A stop rule"],
                            ["yes", "Instant rollback"], ["yes", "Human sign-off for sensitive changes"]],
                           col_w=[70, 986], check_col=0, primary_col=1),
    "19A": lambda: T.schema("light", "€190/month: a price hypothesis, tested in pilots.",
                            ["Free heatmap tool", "Solen · €190/month (hypothesis)", "CRO agency"], "columns", highlight=1,
                            note="Relative positioning only. No competitor prices shown."),
    "19B": lambda: T.audit_wireframe("dark", 16, "Payment options hidden until checkout? I'd test icons earlier.",
                                     variant={"remove": ["delivery"]}, highlight_box=(16, 392, 230, 16)),
    # ---- days 20–24
    "20A": lambda: T.audit_wireframe("dark", 17, "No zoom, no scale? I'd test an in-hand photo.", "gallery"),
    "20B": lambda: T.schema("dark", "Heatmap: shows where people click, not why.",
                            ["Where they click: the heatmap shows it.", "Why they click: needs a test."],
                            "columns", highlight=1),
    "21A": lambda: T.journal("light", 21, "Tracking interviews, not followers."),
    "22A": lambda: T.schema("dark", "Context → behavior → friction → hypothesis → change → result",
                            ["Context", "Behavior", "Friction", "Hypothesis", "Change", "Result"], "loop", highlight=5,
                            note="The learning loop is a hypothesis, not a proven moat."),
    "22B": lambda: T.audit_wireframe("dark", 19, "Cookie banner covering the CTA? I'd test a compact one.", "cookie", variant="cookie"),
    "24A": lambda: T.table("light", "Pilot report: observation, hypothesis, change, metric.",
                           ["Observation", "Hypothesis", "Change to test", "Metric"],
                           [["Friction 1", "", "", ""], ["Friction 2", "", "", ""], ["Friction 3", "", "", ""]],
                           col_w=[264, 264, 264, 264], note="No 'expected uplift' column. On purpose."),
    "24B": lambda: T.audit_wireframe("dark", 21, "Motion matters but no video? I'd test a short clip.", "gallery"),
    # ---- days 25–29
    "25A": lambda: T.schema("dark", "Watchers convert more. Cause or selection? Randomize.",
                            ["Observed: viewers vs non-viewers. Motivated buyers may self-select.",
                             "Test: show the video to a random half. Groups are comparable."], "columns", highlight=1),
    "26B": lambda: T.audit_wireframe("dark", 23, "Reviews without photos? I'd test photo reviews first.", "reviews"),
    "27A": lambda: T.table("dark", "Kill criteria, set before starting.", ["If…", "Then…"],
                           [["No concrete pain stories in interviews", "Change segment"],
                            ["Pilots act on no recommendation", "Rethink the product"],
                            ["Zero paying pilots after 90 days", "Back to research"]], col_w=[660, 396]),
    "28C": lambda: T.journal("dark", 28, "3 pilots. Honest notes. One decision."),
    "29C": lambda: T.table("light", "Rank ideas: impact, confidence, effort.", ["Idea", "Impact", "Confidence", "Effort"],
                           [["Show shipping cost earlier", "High", "Medium", "Low"], ["Move the CTA up", "High", "Medium", "Low"],
                            ["Add a product video", "Medium", "Low", "High"]], col_w=[456, 200, 200, 200],
                           note="Illustrative scoring, not data."),
}

RENDER = os.path.expanduser("~/.claude/skills/logo-design/scripts/render_png.py")
os.makedirs(os.path.join(POSTS, "_svg"), exist_ok=True)
only = set(sys.argv[1:])
for key, fn in VISUALS.items():
    if only and key not in only:
        continue
    day, slot = int(key[:-1]), key[-1].lower()
    name = f"jour-{day:02d}-{slot}"
    svg_path = os.path.join(POSTS, "_svg", name + ".svg")
    open(svg_path, "w").write(fn())
    subprocess.run(["python3", RENDER, svg_path, "-o", os.path.join(POSTS, name + ".png"), "--width", "1200", "--height", "675"],
                   check=True, capture_output=True)
    print("wrote", name)
