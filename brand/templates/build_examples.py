"""Render one filled example per template, dark + light, and a contact sheet (preview.html / preview.png)."""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import solen_templates as T

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples")
os.makedirs(OUT, exist_ok=True)
EX = [
    ("1-audit-wireframe", "Audit — (a) generic wireframe",
     lambda m: T.audit_wireframe(m, 4, "Reviews buried at the bottom? I'd test stars near the price.", "reviews")),
    ("2-audit-screenshot", "Audit — (b) real public page, brand masked",
     lambda m: T.audit_screenshot(m, 1, "Add-to-cart below the fold? I'd test moving it up.")),
    ("3-audit-permission", "Audit — with permission",
     lambda m: T.audit_permission(m, 0, "Shipping cost only at checkout? I'd test showing it earlier.", "Merchant brand name")),
    ("4-key-number", "Chiffre clé",
     lambda m: T.key_number(m, "2.87M", "live Shopify stores.", source="Source: Store Leads, 2026")),
    ("5-journal", "Journal Day N",
     lambda m: T.journal(m, 15, "What the prototype gets wrong.", shot=True)),
    ("6-schema", "Schéma (processus / architecture)",
     lambda m: T.schema(m, "How the prototype works today.", ["Tracking script", "API (Vercel)", "Events (Supabase)", "LLM analysis"], "flow", highlight=3,
                        note="No experiments, no multi-store yet.")),
    ("6b-schema-loop", "Schéma — boucle",
     lambda m: T.schema(m, "The learning loop, as a hypothesis.", ["Context", "Behavior", "Friction", "Hypothesis", "Change", "Result"], "loop", highlight=5)),
    ("7-table", "Tableau (comparaison / checklist)",
     lambda m: T.table(m, "One example, four different statements.", ["Step", "Statement"],
                       [["Observation", "Mobile visitors rarely reach the CTA."], ["Hypothesis", "The CTA sits too low."],
                        ["Test", "Higher CTA vs control."], ["Result", "Not tested yet."]], col_w=[260, 796], highlight_row=3)),
    ("8-chart", "Graphique (données)",
     lambda m: T.chart(m, "Market size: a 15x range.", "range",
                       [("Low", 86, "$86M"), ("Central", 430, "$430M"), ("High", 1290, "$1.29B")], highlight=1,
                       note="Bottom-up TAM. Two of three inputs are unverified assumptions.")),
]
RENDER = os.path.expanduser("~/.claude/skills/logo-design/scripts/render_png.py")
cards = ""
for key, name, fn in EX:
    row = f'<h2>{name}</h2><div class="row">'
    for mode in ("dark", "light"):
        base = os.path.join(OUT, f"{key}-{mode}")
        open(base + ".svg", "w").write(fn(mode))
        subprocess.run(["python3", RENDER, base + ".svg", "-o", base + ".png", "--width", "1200", "--height", "675"],
                       check=True, capture_output=True)
        row += f'<figure><img src="examples/{key}-{mode}.png"><figcaption>{mode}</figcaption></figure>'
    cards += row + "</div>"
html = ("<!doctype html><meta charset=utf-8><title>Solen templates</title><style>"
        "body{font:14px -apple-system,Arial;background:#E9E8E4;margin:32px 40px;color:#111}h1{margin:0 0 4px}"
        "h2{font-size:17px;margin:26px 0 8px}.row{display:flex;gap:18px}figure{margin:0}img{width:600px;border-radius:8px;"
        "box-shadow:0 1px 3px rgba(0,0,0,.2)}figcaption{font-size:12px;color:#666;margin-top:4px}</style>"
        "<h1>Solen — social templates (1200×675)</h1><p>One filled example per template, dark and light. "
        "All examples use real or placeholder content only.</p>" + cards)
open(os.path.join(os.path.dirname(OUT), "preview.html"), "w").write(html)
print("ok")
