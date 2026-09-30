"""Build brand/posts/PLAN.md from docs/X_BUILD_IN_PUBLIC.md + the visual assignments below, and check the rules."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "docs", "X_BUILD_IN_PUBLIC.md")
OUT = os.path.join(ROOT, "brand", "posts", "PLAN.md")

THEMES = {"🔍": "Friction (audit)", "🛠": "Journal", "🎙": "Interviews", "💬": "Opinion", "📣": "Appel"}

# ---- parse the 90 posts
text = open(SRC).read()
posts = []
for day, body in re.findall(r"### Jour (\d+)\n(.*?)(?=\n### Jour |\n## |\Z)", text, re.S):
    for slot, emoji, post in re.findall(r"\*\*([ABC])\*\* (\S+)\n```\n(.*?)```", body, re.S):
        posts.append(dict(day=int(day), slot=slot, theme=THEMES.get(emoji, emoji), post=post.strip()))
assert len(posts) == 90, len(posts)

# ---- visual assignments: key "day+slot" -> (template, mode, text on visual, input)
SL = "« Source: Store Leads, 2026 » affiché sur le visuel — à vérifier par Thomas avant publication (TODO_INPUTS)"
WF = "AUDIT"
V = {
    "1A": ("journal", "dark", "Day 1. Prototype runs. 0 customers. Building in public.", "Capture réelle du prototype — visuel généré avec « SCREENSHOT HERE » (TODO_INPUTS)"),
    "1B": ("tableau", "dark", "Observation → hypothesis → test → result: one example.", "Exemple illustratif tiré de SOLEN_CONTEXT §3 (PDP mobile) ; ligne « result » = « not tested yet » — aucun résultat inventé"),
    "2A": ("audit", "dark", "Add-to-cart below the fold? I'd test moving it up.", WF),
    "2B": ("journal", "light", "Day 2. What the prototype does, and doesn't.", "Capture réelle du prototype — visuel généré avec « SCREENSHOT HERE » (TODO_INPUTS)"),
    "3A": ("chiffre", "dark", "2.87M live Shopify stores.", SL + " — mention sur le visuel : « Source: Store Leads, 2026 »"),
    "3B": ("tableau", "dark", "Sizing inputs: one sourced number, two guesses.", "Tableau : boutiques (Store Leads 2026) / part > 10k (5–15 %, hypothèse) / dépense (600–3 000 $, hypothèse)"),
    "3C": ("graphique", "dark", "TAM: $86M to $1.29B. A 15x range.", "Barres bas / central / haut (86 M$ · 430 M$ · 1,29 Md$), libellées « hypotheses »"),
    "4A": ("audit", "light", "Shipping cost only at checkout? I'd test showing it earlier.", WF),
    "5B": ("audit", "dark", "Hidden size options? I'd test visible swatches.", WF),
    "5C": ("schema", "dark", "What's built: script → API → database → analysis.", "Aucun (architecture réelle : tracking script → Express/Vercel → Supabase → heatmap + LLM)"),
    "6B": ("audit", "dark", "Reviews buried at the bottom? I'd test stars near the price.", WF),
    "6C": ("tableau", "dark", "Honest status: prototype yes, customers 0, revenue 0.", "État réel à confirmer le jour de publication (« 0 customers »)"),
    "7A": ("schema", "light", "Observation → Hypothesis → Test → Result", "—"),
    "8A": ("audit", "dark", "Return policy in the footer? I'd test it near the CTA.", WF),
    "8C": ("schema", "dark", "Where would you stop? 1 · 2 · 3 · 4", "Échelle d'autonomie en 4 marches (SOLEN_CONTEXT §22)"),
    "9B": ("audit", "dark", "Slow images on mobile? I'd test compression first.", WF),
    "10C": ("audit", "dark", "Hidden free-shipping threshold? I'd test a progress bar.", WF),
    "11A": ("chiffre", "dark", "~38% of live Shopify stores are in the US.", SL + " — mention sur le visuel : « Source: Store Leads, 2026 »"),
    "11B": ("audit", "light", "Size guide as a PDF? I'd test an inline drawer.", WF),
    "11C": ("tableau", "dark", "Pilot: what you get, what I ask.", "Deux colonnes reprises de l'offre (GTM_STRATEGY §4) ; « no promised uplift »"),
    "12C": ("audit", "dark", "Instant pop-up on mobile? I'd test a delay.", WF),
    "13B": ("audit", "dark", "No delivery date? I'd test showing one near the CTA.", WF),
    "15A": ("journal", "dark", "Day 15. What the prototype gets wrong.", "Capture réelle de la sortie de /analyze, sans données marchand — « SCREENSHOT HERE » (TODO_INPUTS)"),
    "15B": ("audit", "light", "Checkout button below upsells? I'd test pinning it.", WF),
    "17B": ("audit", "dark", "Out-of-stock but selectable? I'd test greying it out.", WF),
    "17C": ("tableau", "dark", "Five guardrails before any automated change.", "Checklist : control group · primary metric · stop rule · rollback · human sign-off"),
    "19A": ("schema", "light", "€190/month: a price hypothesis, tested in pilots.", "Échelle sans chiffres : outil gratuit ← Solen → agence (positionnement relatif, pas de prix concurrents inventés)"),
    "19B": ("audit", "dark", "Payment options hidden until checkout? I'd test icons earlier.", WF),
    "20A": ("audit", "dark", "No zoom, no scale? I'd test an in-hand photo.", WF),
    "20B": ("schema", "dark", "Heatmap: shows where people click, not why.", "Aucun (schéma deux colonnes : where / why)"),
    "21A": ("journal", "light", "Day 21. Tracking interviews, not followers.", "Aucun (titre seul, sans chiffres)"),
    "22A": ("schema", "dark", "Context → behavior → friction → hypothesis → change → result", "—"),
    "22B": ("audit", "dark", "Cookie banner covering the CTA? I'd test a compact one.", WF),
    "24A": ("tableau", "light", "Pilot report: observation, hypothesis, change, metric.", "Maquette vide du rapport (structure seulement, aucune donnée marchand)"),
    "24B": ("audit", "dark", "Motion matters but no video? I'd test a short clip.", WF),
    "25A": ("schema", "dark", "Watchers convert more. Cause or selection? Randomize.", "Schéma : groupe « regarde la vidéo » vs moitié tirée au hasard — aucun chiffre (le « 2x » du post est une citation typique, pas une donnée)"),
    "26B": ("audit", "dark", "Reviews without photos? I'd test photo reviews first.", WF),
    "27A": ("tableau", "dark", "Kill criteria, set before starting.", "Tableau signal → décision (GTM_STRATEGY §5)"),
    "28C": ("journal", "dark", "Day 28. 3 pilots. Honest notes. One decision.", "—"),
    "29C": ("tableau", "light", "Rank ideas: impact, confidence, effort.", "Grille 3 colonnes (exemple de notation illustratif, libellé comme tel)"),
}
AB = {k: "a" for k in ("5B", "6B", "9B", "10C", "11B", "12C", "13B", "15B", "17B", "19B", "20A", "22B", "24B", "26B")}
AB.update({"2A": "b", "4A": "b", "8A": "b"})
AB_SRC = {"2A": "theme-taste-demo.myshopify.com (démo officielle de thème Shopify) : bouton d'ajout au panier à 1 174 px, écran 844 px",
          "4A": "theme-craft-demo.myshopify.com : page panier « Taxes and shipping calculated at checkout »",
          "8A": "theme-refresh-demo.myshopify.com : infos retours uniquement dans le pied de page"}
AB_WHY = {"9B": "lenteur non visible sur une capture", "13B": "absence d'info difficile à montrer",
          "19B": "absence d'info difficile à montrer", "20A": "absence de zoom non visible sur une capture",
          "24B": "absence de vidéo difficile à montrer"}
LABEL = {"audit": "Audit annoté", "chiffre": "Chiffre clé", "journal": "Journal Day N", "graphique": "Graphique (données)",
         "schema": "Schéma (processus / architecture)", "tableau": "Tableau (comparaison / checklist)"}

# ---- checks
rows, prev_t, errors = [], None, []
for i, p in enumerate(posts, 1):
    k = f"{p['day']}{p['slot']}"
    v = V.get(k)
    t = v[0] if v else None
    if t and t == prev_t:
        errors.append(f"n°{i} ({k}) : même gabarit que le post précédent ({t})")
    if v and len(re.findall(r"[\w€$~%.,']+", v[2].replace("→", " ").replace("·", " "))) > 12:
        errors.append(f"n°{i} ({k}) : texte visuel > 12 mots")
    prev_t = t
    rows.append((p, i, k, v))
n_vis = sum(1 for r in rows if r[3])
n_light = sum(1 for r in rows if r[3] and r[3][1] == "light")
assert 30 <= n_vis <= 45, n_vis
assert not errors, errors

def first_line(s):
    return s.split("\n")[0].replace("|", "\\|")

md = [f"# Plan des visuels — 90 posts X\n",
      f"> À valider avant génération. Source des posts : `docs/X_BUILD_IN_PUBLIC.md`. Généré par `brand/posts/_src/make_plan.py`.\n",
      "## Résumé\n",
      f"- **{n_vis} visuels** sur 90 posts ({90 - n_vis} en texte seul), dans la fourchette 30–45.",
      f"- **Mode** : {n_vis - n_light} dark, {n_light} light (≈ 1 sur {round(n_vis / max(n_light, 1))}).",
      "- **Principe** : le visuel montre l'information du post (chiffre sourcé, graphique, schéma, tableau, capture réelle), jamais la phrase du post reformulée. Plus de gabarits « Citation » ni « Opinion ».",
      "- **Règles vérifiées par le script** : jamais deux posts consécutifs avec le même gabarit ; texte du visuel ≤ 12 mots.",
      "- **Lisibilité** : message principal ≥ 48 px sur 1200×675 (vérifié à la génération, étape 2).",
      "- **Aucune donnée inventée** : seuls chiffres = Store Leads 2026 (source secondaire, *à vérifier*), fourchettes du deck (présentées comme hypothèses), état réel du projet (0 client), prix hypothétique.\n",
      "| Gabarit | Nombre |", "|---|---|"]
from collections import Counter
for t, c in Counter(r[3][0] for r in rows if r[3]).most_common():
    md.append(f"| {LABEL[t]} | {c} |")
md += ["\n## Choix validés (29/09/2026)\n",
       "1. Kit de marque créé : `brand/BRAND.md`, `brand/tokens.css`, `brand/logo/final/`, gabarits dans `brand/templates/` (planche : `brand/templates/preview.html`).",
       "2. Audits **mixtes, à dominante (b)** : capture réelle d'une page produit Shopify publique via Playwright quand la friction y est vraiment visible, marque masquée (logo, nom, URL, photos produit reconnaissables floutés), annotations en hypothèses. Sinon (a) wireframe générique. Si aucune page publique ne montre la friction, repli sur (a). Gabarit « Audit — with permission » prévu pour les audits demandés par des marchands.",
       "3. Store Leads (n° 7 et 31) : gardés, avec « Source: Store Leads, 2026 » sur le visuel ; à vérifier par Thomas (TODO_INPUTS.md).",
       "4. N° 18 : « 0 customers » gardé ; à confirmer le jour de publication (TODO_INPUTS.md).",
       "5. N° 1, 5 et 43 : générés avec l'emplacement « SCREENSHOT HERE » ; captures réelles fournies par Thomas.\n",
       "## Tableau\n",
       "| Jour | N° | Post (1re ligne) | Thème | Visuel | Gabarit | Mode | Texte sur le visuel | Input requis |",
       "|---|---|---|---|---|---|---|---|---|"]
for p, i, k, v in rows:
    if v:
        t, mode, vt, inp = v
        lab = LABEL[t]
        if t == "audit":
            ab = AB[k]
            lab += " (b)" if ab == "b" else " (a)"
            inp = (f"Capture Playwright, marque floutée — {AB_SRC[k]}" if ab == "b" else
                   f"Aucun — wireframe générique ({AB_WHY.get(k, 'friction non trouvée sur les pages publiques testées')})")
        md.append(f"| {p['day']} | {i} | {first_line(p['post'])} | {p['theme']} | oui | {lab} | {mode} | {vt} | {inp} |")
    else:
        md.append(f"| {p['day']} | {i} | {first_line(p['post'])} | {p['theme']} | non | — | — | — | — |")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write("\n".join(md) + "\n")
todo = ["# Inputs à fournir ou vérifier avant publication\n",
        "| N° | Jour | Visuel | Ce qu'il faut | Statut |", "|---|---|---|---|---|"]
for p, i, k, v in rows:
    if not v:
        continue
    fname = f"jour-{p['day']:02d}-{p['slot'].lower()}.png"
    if "SCREENSHOT HERE" in v[3]:
        todo.append(f"| {i} | {p['day']} | `{fname}` | {v[3].split(' — ')[0]} : remplacer l'emplacement « SCREENSHOT HERE » | à fournir par Thomas |")
    elif k == "3B":
        todo.append(f"| {i} | {p['day']} | `{fname}` | Vérifier « 2.87M live Shopify stores » (1re ligne du tableau) sur storeleads.app | à vérifier par Thomas avant publication |")
    elif "Store Leads" in v[3]:
        todo.append(f"| {i} | {p['day']} | `{fname}` | Vérifier le chiffre « {v[2]} » sur storeleads.app (source actuelle : relais secondaire) | à vérifier par Thomas avant publication |")
    elif "confirmer" in v[3]:
        todo.append(f"| {i} | {p['day']} | `{fname}` | « {v[2]} » : vérifier que c'est toujours vrai | à confirmer le jour de publication |")
open(os.path.join(os.path.dirname(OUT), "TODO_INPUTS.md"), "w").write("\n".join(todo) + "\n")
print(f"{n_vis} visuals ({n_light} light) · wrote {OUT}")
