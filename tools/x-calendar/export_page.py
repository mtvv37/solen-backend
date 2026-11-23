"""Construit la page web du calendrier X (calendrier-x.html) à partir de posts.py et page.html.

Usage (depuis la racine du repo) : python3 tools/x-calendar/export_page.py
Les images sont publiées à côté de la page sous img/ (voir IMAGES).
"""
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from posts import BRANDS, C, D, FRICTIONS, REPLY, VISUALS, friction  # noqa: E402


def weight(s):
    """Comptage X : 1 pour les plages latines et la ponctuation courante, 2 pour le reste (emoji, €)."""
    n = 0
    for ch in s:
        o = ord(ch)
        n += 1 if (o <= 4351 or 8192 <= o <= 8205 or 8208 <= o <= 8223 or 8242 <= o <= 8247) else 2
    return n


EVENTS = {(11, 26): 'Thanksgiving (US)', (11, 27): 'Black Friday', (11, 30): 'Cyber Monday',
          (12, 24): 'Réveillon', (12, 25): 'Noël', (12, 26): 'Boxing Day', (12, 31): "Dernier jour de l'année"}
CHECK = {(12, 3): 'Vérifie ce jour-là : toujours 0 client payant ? Prix toujours à 19 € ?'}

# Chemin publié -> fichier du repo
IMAGES = {f'img/friction-{n}.png': f'design/social/x-friction/friction-{n}.png' for n in VISUALS}
IMAGES.update({
    'img/cta-form.png': 'design/social/x-friction/cta-form.png',
    'img/form-cover.png': 'design/social/form/cover.png',
    'img/form-share.png': 'design/social/form/share.png',
    'img/logo.png': 'design/social/avatar-01-blanc-sur-sapin.png',
})


def build():
    days = []
    start = dt.date(2026, 11, 19)
    for i in range(43):
        d = start + dt.timedelta(i)
        posts = []
        a = friction(28 + i, FRICTIONS[i])
        posts.append(dict(slot='A', time='9h', series='Shopify friction worth testing', num=28 + i, text=a, w=weight(a),
                          img=f'img/friction-{28 + i}.png' if 28 + i in VISUALS else None, reply=True))
        b = BRANDS[i % len(BRANDS)]
        posts.append(dict(slot='B', time='13h', series='Worth stealing', num=i + 1, brand=b[0], where=b[2], reply=True))
        c = C[i]
        if c is None:
            posts.append(dict(slot='C', time='18h', series='Bilan de la semaine', sunday=True))
        else:
            posts.append(dict(slot='C', time='18h', series=c[0], text=c[1], w=weight(c[1]), check=CHECK.get((d.month, d.day))))
        t = D.get((d.month, d.day))
        if t:
            posts.append(dict(slot='D', time='21h', series='Appel', text=t, w=weight(t)))
        for p in posts:
            assert p.get('w', 0) <= 280, (d, p['slot'])
        days.append(dict(date=d.isoformat(), event=EVENTS.get((d.month, d.day)), posts=posts))
    data = dict(days=days, reply=REPLY, reply_w=weight(REPLY.replace('[link]', 'x' * 23)),
                brands=[list(b) for b in BRANDS])
    page = open(os.path.join(HERE, 'page.html'), encoding='utf-8').read()
    payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    out = os.path.join(HERE, 'calendrier-x.html')
    open(out, 'w', encoding='utf-8').write(page.replace('__DATA__', payload))
    root = os.path.dirname(os.path.dirname(HERE))
    missing = [p for p in IMAGES.values() if not os.path.exists(os.path.join(root, p))]
    assert not missing, missing
    print(out, f'{len(payload)} octets de données,', sum(len(d['posts']) for d in days), 'posts,', len(IMAGES), 'images')


if __name__ == '__main__':
    build()
