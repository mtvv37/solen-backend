"""Step 3 — contact sheet: the 90 posts in order, post text next to its visual (or 'texte seul'). Writes brand/posts/index.html."""
import html, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
POSTS_DIR = os.path.join(ROOT, "brand", "posts")
text = open(os.path.join(ROOT, "docs", "X_BUILD_IN_PUBLIC.md")).read()
plan = open(os.path.join(POSTS_DIR, "PLAN.md")).read()
todo = open(os.path.join(POSTS_DIR, "TODO_INPUTS.md")).read()
todo_n = {int(m) for m in re.findall(r"^\| (\d+) \|", todo, re.M)}
rows = {int(m[1]): m for m in re.findall(r"^\| (\d+) \| (\d+) \| .*? \| (.*?) \| (oui|non) \| (.*?) \| (.*?) \|", plan, re.M)}
THEMES = {"🔍": "Friction", "🛠": "Journal", "🎙": "Interviews", "💬": "Opinion", "📣": "Appel"}

cards, n = [], 0
for day, body in re.findall(r"### Jour (\d+)\n(.*?)(?=\n### Jour |\n## |\Z)", text, re.S):
    for slot, emoji, post in re.findall(r"\*\*([ABC])\*\* (\S+)\n```\n(.*?)```", body, re.S):
        n += 1
        d = int(day)
        img = f"jour-{d:02d}-{slot.lower()}.png"
        has = os.path.exists(os.path.join(POSTS_DIR, img))
        tpl = rows[n][4] if n in rows else ""
        mode = rows[n][5] if n in rows else ""
        flag = '<span class="todo">input requis — voir TODO_INPUTS.md</span>' if n in todo_n else ""
        vis = (f'<a href="{img}"><img src="{img}" loading="lazy"></a><div class="meta">{html.escape(tpl)} · {mode} {flag}</div>'
               if has else '<div class="textonly">texte seul</div>')
        cards.append(f'<article><div class="left"><div class="head">Jour {d} · {slot} · n° {n} · {THEMES.get(emoji, emoji)} '
                     f'<span class="len">{len(post.strip())} car.</span></div><pre>{html.escape(post.strip())}</pre></div>'
                     f'<div class="right">{vis}</div></article>')
assert n == 90, n
page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solen — 90 posts X, relecture</title><style>
body{{font:15px/1.5 -apple-system,Helvetica,Arial,sans-serif;background:#0E1726;color:#F6F5F1;margin:0;padding:32px}}
h1{{margin:0 0 4px;font-size:26px}} .sub{{color:#8A8F98;margin:0 0 24px}}
article{{display:grid;grid-template-columns:minmax(0,1fr) 480px;gap:24px;background:#141F33;border-radius:12px;padding:18px 20px;margin-bottom:14px}}
.head{{font-size:12px;color:#F5A524;font-weight:600;letter-spacing:.03em;margin-bottom:8px}} .len{{color:#8A8F98;font-weight:400;margin-left:6px}}
pre{{white-space:pre-wrap;font:15px/1.5 -apple-system,Helvetica,Arial,sans-serif;margin:0}}
img{{width:100%;border-radius:8px;display:block}} .meta{{font-size:12px;color:#8A8F98;margin-top:6px}}
.todo{{color:#F5A524;font-weight:600;margin-left:6px}}
.textonly{{height:100%;min-height:80px;display:flex;align-items:center;justify-content:center;border:1px dashed #243049;border-radius:8px;color:#8A8F98;font-size:13px}}
@media (max-width:900px){{article{{grid-template-columns:1fr}}}}
</style></head><body>
<h1>90 posts X — relecture</h1>
<p class="sub">Dans l'ordre de publication. {sum(1 for c in cards if 'img src' in c)} visuels, {sum(1 for c in cards if 'texte seul' in c)} posts en texte seul. Plan : PLAN.md · inputs : TODO_INPUTS.md.</p>
{''.join(cards)}
</body></html>"""
open(os.path.join(POSTS_DIR, "index.html"), "w").write(page)
print("wrote index.html")
