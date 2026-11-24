import sys, datetime as dt
sys.path.insert(0, sys.argv[1])
from posts import FRICTIONS, C, D, BRANDS, VISUALS, REPLY, RESERVE, START, friction
from ws_long import EXAMPLE as WS_EXAMPLE, TEMPLATE as WS_TEMPLATE
from ws_posts import WS

def weight(s):
    # Comptage X : 1 pour les plages latines/ponctuation, 2 pour le reste (emoji, €...).
    n = 0
    for ch in s:
        o = ord(ch)
        n += 1 if (o <= 4351 or 8192 <= o <= 8205 or 8208 <= o <= 8223 or 8242 <= o <= 8247) else 2
    return n

start = dt.date(*START)
days = [start + dt.timedelta(d) for d in range(len(C))]
assert days[-1] == dt.date(2026, 12, 31) and len(FRICTIONS) == len(C) + len(RESERVE)
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
    if i < len(WS):
        ws = WS[i]
        out.append(f"**B · 13h · Worth stealing #{i+1} · {ws['brand']}** ({len(ws['text'])} caractères, X Premium)\n```\n{ws['text']}\n```\nImage : ta capture {ws['brand']}.\n")
    else:
        out.append(f"**B · 13h · Worth stealing #{i+1}** : capture à m'envoyer. Idée pour décembre : guide cadeaux, date limite pour Noël, emballage cadeau, carte cadeau, retours prolongés, soldes.\n")
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
head = f"""# Solen : 3 posts X par jour, du 24 novembre au 31 décembre 2026

> Version 1.5, 24/11/2026 : Worth stealing complet (38 posts), réécrit en ton parlé, 900 caractères maximum, puces en tiret. Version 1.4, 23/11/2026 : départ décalé au mardi 24 novembre (rien n'a été posté avant). Frictions #28 à #65 jusqu'au 31 décembre, #66 à #70 en réserve pour janvier. 22 visuels de friction, visuel d'appel au formulaire, liste de marques ; sans tiret ni emoji, selon `design/social/RULES.md`. En anglais. Tous les posts font 280 caractères au plus (compteur X, les emoji et « € » comptent double).
> Suite de [`X_BUILD_IN_PUBLIC.md`](X_BUILD_IN_PUBLIC.md). Objectif : obtenir des appels 1:1 et des réponses au formulaire, pas des abonnés.

## Mode d'emploi

- **A · 9h : Shopify friction worth testing**, #28 à #70. La série qui fait le plus réagir. Finit par « Follow for more. » 22 posts sur 43 ont un visuel (`design/social/x-friction/`), en priorité ceux sur l'argent.
- **B · 13h : Worth stealing**, nouvelle série en format long (X Premium). Tu m'envoies la capture d'une fonctionnalité d'un site, j'écris le post. 900 caractères maximum, puces en tiret, finit par « Follow for more. »
- **C · 18h : question, demande d'échange, opinion ou journal.** Le dimanche : le bilan chiffré de la semaine, écrit avec tes vrais chiffres.
- **D · 21h, {len(D)} jours sur {len(C)} : un 4e post, uniquement un appel vers le formulaire.** Surtout les lundis, mercredis et vendredis où le post C n'en est pas déjà un. Avec les {sum(1 for c in C if c and c[0] == 'Appel')} appels en C : {len(D) + sum(1 for c in C if c and c[0] == 'Appel')} appels, plus le lien en réponse sous chaque post A et B.
- **« Comment "form" »** : réponds en message privé avec le lien à chaque personne qui commente.
- **Sous chaque post A et B**, ta première réponse : ce texte, avec le visuel `design/social/x-friction/cta-form.png`. Remplace `[link]` par le lien Tally.
  ```
{{REPLY_BLOCK}}
  ```
- **« Link below »** dans un post C : le lien du formulaire va en première réponse, jamais dans le post.

## Worth stealing : le format long

Une capture, un nom de marque, ce qui marche, une chose qu'on testerait. Au-delà de 280 caractères, X demande un compte Premium ;
le fil coupe après quelques lignes avec « Show more », donc la marque et la fonctionnalité tiennent dans les deux premières lignes.

Le gabarit :

```
{WS_TEMPLATE}
```

Un exemple rempli ({len(WS_EXAMPLE)} caractères ; la marque reste entre crochets, le vrai post ne décrit que ce qu'on voit sur la capture) :

```
{WS_EXAMPLE}
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
reserve = '\n\n## En réserve pour janvier\n\nCes frictions ne tiennent plus avant le 31 décembre.\n\n' + '\n'.join(
    f"**Friction #{n}** ({weight(friction(n, FRICTIONS[n - 28]))}/280)\n```\n{friction(n, FRICTIONS[n - 28])}\n```\n" for n in RESERVE)
open(sys.argv[2], 'w', encoding='utf-8').write(head + '\n'.join(out) + reserve + '\n')
assert nd == len(D), (nd, len(D))
print('ok, max weight', maxw, '| D posts', nd)
