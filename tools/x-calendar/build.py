import sys, datetime as dt
sys.path.insert(0, sys.argv[1])
from posts import FRICTIONS, C, D, BRANDS, VISUALS, REPLY, friction

def weight(s):
    # Comptage X : 1 pour les plages latines/ponctuation, 2 pour le reste (emoji, €...).
    n = 0
    for ch in s:
        o = ord(ch)
        n += 1 if (o <= 4351 or 8192 <= o <= 8205 or 8208 <= o <= 8223 or 8242 <= o <= 8247) else 2
    return n

start = dt.date(2026, 11, 19)
days = [start + dt.timedelta(d) for d in range(43)]
assert days[-1] == dt.date(2026, 12, 31) and len(FRICTIONS) == 43 and len(C) == 43
JOURS = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
MOIS = {11: 'novembre', 12: 'décembre'}
EVENTS = {dt.date(2026,11,26): 'Thanksgiving (US)', dt.date(2026,11,27): 'Black Friday', dt.date(2026,11,30): 'Cyber Monday',
          dt.date(2026,12,24): 'Réveillon', dt.date(2026,12,25): 'Noël', dt.date(2026,12,26): 'Boxing Day', dt.date(2026,12,31): 'Dernier jour de l\'année'}
CHECK = {dt.date(2026,12,3): 'Vérifie le jour même : toujours 0 client payant ? Prix toujours à 19 € ?'}
errors, maxw, nd = [], 0, 0
out = []
for i, d in enumerate(days):
    if d.weekday() == 0 or i == 0:
        out.append(f"\n## Semaine du {d.day} {MOIS[d.month]}\n")
    title = f"### {JOURS[d.weekday()].capitalize()} {d.day} {MOIS[d.month]}" + (f" · {EVENTS[d]}" if d in EVENTS else '')
    out.append(title + "\n")
    a = friction(28 + i, FRICTIONS[i]); wa = weight(a); maxw = max(maxw, wa)
    if wa > 280: errors.append(f"A #{28+i}: {wa}")
    vis = f"\nVisuel : `design/social/x-friction/friction-{28+i}.png`\n" if 28 + i in VISUALS else "\nSans visuel.\n"
    out.append(f"**A · 9h · Friction #{28+i}** ({wa}/280)\n```\n{a}\n```{vis}")
    b = BRANDS[i % len(BRANDS)]
    out.append(f"**B · 13h · Worth stealing #{i+1}** : envoie-moi ta capture, j'écris le post. Suggestion : {b[0]} ({b[2]}).\n")
    c = C[i]
    if c is None:
        assert d.weekday() == 6, d
        out.append("**C · 18h · Bilan de la semaine** : envoie-moi tes chiffres (réponses au formulaire, appels, abonnés), je l'écris.\n")
    else:
        wc = weight(c[1]); maxw = max(maxw, wc)
        if wc > 280: errors.append(f"C {d}: {wc}")
        note = f"\n> {CHECK[d]}\n" if d in CHECK else ''
        out.append(f"**C · 18h · {c[0]}** ({wc}/280)\n```\n{c[1]}\n```\n{note}")
    dtext = D.get((d.month, d.day))
    if dtext:
        assert not (c and c[0] == 'Appel'), d
        wd = weight(dtext); maxw = max(maxw, wd)
        if wd > 280: errors.append(f"D {d}: {wd}")
        out.append(f"**D · 21h · Appel** ({wd}/280)\n```\n{dtext}\n```\n")
        nd += 1
if errors:
    print('TOO LONG:', *errors, sep='\n'); sys.exit(1)
assert all((c is None) == (d.weekday() == 6) for c, d in zip(C, days))

brand_rows = '\n'.join(f"| {n} | {cat} | {w} |" for n, cat, w in BRANDS)
wr = weight(REPLY.replace('[link]', 'x' * 23))
assert wr <= 280, wr
assert sorted(VISUALS) == VISUALS and len(VISUALS) == 22
head = f"""# Solen : 3 posts X par jour, du 19 novembre au 31 décembre 2026

> Version 1.3, 19/11/2026 (22 visuels de friction, visuel d'appel au formulaire, liste de marques ; sans tiret ni emoji, selon `design/social/RULES.md`). En anglais. Tous les posts font 280 caractères au plus (compteur X, les emoji et « € » comptent double).
> Suite de [`X_BUILD_IN_PUBLIC.md`](X_BUILD_IN_PUBLIC.md). Objectif : obtenir des appels 1:1 et des réponses au formulaire, pas des abonnés.

## Mode d'emploi

- **A · 9h : Shopify friction worth testing**, #28 à #70. La série qui fait le plus réagir. Finit par « Follow for more. » 22 posts sur 43 ont un visuel (`design/social/x-friction/`), en priorité ceux sur l'argent.
- **B · 13h : Worth stealing**, nouvelle série. Tu m'envoies la capture d'une fonctionnalité d'un site, j'écris le post. Finit par « Follow for more. »
- **C · 18h : question, demande d'échange, opinion ou journal.** Le dimanche : le bilan chiffré de la semaine, écrit avec tes vrais chiffres.
- **D · 21h, 14 jours sur 43 : un 4e post, uniquement un appel vers le formulaire.** Les lundis, mercredis et vendredis où le post C n'en est pas déjà un. Avec les 8 appels en C : 22 appels en 6 semaines, plus le lien en réponse sous chaque post A et B.
- **« Comment "form" »** : réponds en message privé avec le lien à chaque personne qui commente.
- **Sous chaque post A et B**, ta première réponse : ce texte, avec le visuel `design/social/x-friction/cta-form.png`. Remplace `[link]` par le lien Tally.
  ```
{{REPLY_BLOCK}}
  ```
- **« Link below »** dans un post C : le lien du formulaire va en première réponse, jamais dans le post.

## Worth stealing : le format

Une capture, un nom de marque, ce qui marche, une chose qu'on testerait.

```
Worth stealing #1: [Brand]'s [feature].

Why it works:
· [what the shopper sees]
· [the question it answers]
· [the friction it removes]

What I'd test: [one idea, framed as a test]

Follow for more.
```

**Règles**
- On parle de ce qu'on voit sur la capture, jamais des résultats de la marque : pas de « +20 % de conversion », on ne les connaît pas.
- « What I'd test », jamais « they should ». Ce n'est pas une critique.
- On ne refait pas une fonctionnalité déjà décortiquée par un autre compte (par exemple le sticky add-to-cart de Comfrt).
- On n'écrit « on Shopify » que si on l'a vérifié.

## Marques à décortiquer

Des marques e-commerce dans l'esprit de Gymshark, Boku, Arntreal, Fincut et Holy. Pour chacune, où regarder en premier ; si rien ne ressort, prends une autre fonctionnalité ou une autre marque. Pour Fincut et Holy, envoie-moi les liens : je n'ai pas pu vérifier de quelles marques il s'agit.

| Marque | Catégorie | Où regarder |
|---|---|---|
{brand_rows}

## Calendrier
"""
head = head.replace('{REPLY_BLOCK}', '\n'.join('  ' + l if l else '' for l in REPLY.split('\n')))
open(sys.argv[2], 'w', encoding='utf-8').write(head + '\n'.join(out) + '\n')
assert nd == len(D), (nd, len(D))
print('ok, max weight', maxw, '| D posts', nd)
