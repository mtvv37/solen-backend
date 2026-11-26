"""Génère les visuels X de la série « Friction Shopify à tester » (1200 x 675, même format que brand/posts/).

Mise en page du premier lot : téléphone annoté à gauche, texte à droite, logo en bas à gauche, compte en bas à droite.
DA de la bannière X verte. Rendu : node render.js <html...> (Playwright).
Usage : python3 gen_frictions.py  -> écrit _src/friction-NN.html
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

ICONS = {
 'tag': '<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.4"/>',
 'percent': '<line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
 'bag': '<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'check': '<path d="M20 6L9 17l-5-5"/>',
 'card': '<rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/>',
 'help': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 0 1 4.8 1c0 1.7-2.3 2.2-2.3 3.5"/><circle cx="12" cy="17" r=".6"/>',
 'box': '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><line x1="12" y1="13" x2="12" y2="21"/>',
 'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 'truck': '<rect x="1" y="6" width="14" height="10" rx="1"/><path d="M15 9h4l3 3v4h-7"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
 'gift': '<rect x="3" y="8" width="18" height="13" rx="1"/><line x1="12" y1="8" x2="12" y2="21"/><path d="M3 12h18"/><path d="M12 8c-2-4-6-4-6-1.5S9 8 12 8c3 0 6-1 6-1.5S14 4 12 8z"/>',
 'heart': '<path d="M20.8 5.6a5 5 0 0 0-7.1 0L12 7.3l-1.7-1.7a5 5 0 0 0-7.1 7.1L12 21.5l8.8-8.8a5 5 0 0 0 0-7.1z"/>',
 'ruler': '<rect x="2" y="7" width="20" height="10" rx="2"/><path d="M6 7v4M10 7v3M14 7v4M18 7v3"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
 'phone': '<rect x="7" y="2" width="10" height="20" rx="2"/><line x1="11" y1="18" x2="13" y2="18"/>',
 'lock': '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'filter': '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
 'refresh': '<path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 4v7h-7"/>',
}

# ---------- éléments de l'écran du téléphone ----------
def mk(html, inline=False):
    return f'<div class="mk{" in" if inline else ""}">{html}<i class="bd">1</i></div>'
def nav(): return '<div class="nav"></div>'
def img(h=196): return f'<div class="img" style="height:{h}px"></div>'
def title(): return '<div class="bar"></div><div class="bar s"></div>'
def price(now, was='', mark=False):
    inner = f'<span class="now">{now}</span>' + (f'<span class="was">{was}</span>' if was else '')
    return f'<div class="price">{mk(inner, True) if mark else inner}</div>'
def btn(t='Ajouter au panier', ghost=False): return f'<div class="btn{" ghost" if ghost else ""}">{t}</div>'
def bart(): return '<div class="bar t"></div>'
def head(t, right='×'): return f'<div class="head"><b>{t}</b><span>{right}</span></div>'
def banner(t): return f'<div class="banner">{t}</div>'
def item(price_t, was=''):
    return f'<div class="item"><div class="th"></div><div class="lines"><div class="bar"></div><div class="bar s"></div></div><b>{price_t}{f" <s>{was}</s>" if was else ""}</b></div>'
def row(l, r, strong=False): return f'<div class="rw{" st" if strong else ""}"><span>{l}</span><b>{r}</b></div>'
def note(t, cls=''): return f'<div class="nt {cls}">{t}</div>'
def field(label, value=''): return f'<div class="fd"><span>{label}</span><div>{value}</div></div>'
def opt(label, right='', on=False): return f'<div class="op{" on" if on else ""}"><i></i><span>{label}</span><b>{right}</b></div>'
def sizes(labels): return '<div class="sz">' + ''.join(f'<span>{s}</span>' for s in labels) + '</div>'
def card(price_t, chip='', quick=False):
    return (f'<div class="cd"><div class="ci">{f"<em>{chip}</em>" if chip else ""}</div><div class="bar"></div>'
            f'<b>{price_t}</b>{"<u>+ Ajout rapide</u>" if quick else ""}</div>')
def grid(cards): return '<div class="gr">' + ''.join(cards) + '</div>'
def timer(label, t): return f'<div class="tm"><span>{label}</span><b>{t}</b></div>'
def toggle(label, right, on=True): return f'<div class="tg{" on" if on else ""}"><i></i><span>{label}</span><b>{right}</b></div>'
def chips(labels): return '<div class="ch">' + ''.join(f'<span>{c}</span>' for c in labels) + '</div>'
def links(items, marked): return '<div class="ln">' + ''.join(mk(f'<span>{t}</span>') if t == marked else f'<span>{t}</span>' for t in items) + '</div>'
def gap(h): return f'<div style="height:{h}px"></div>'

SPECS = [  # en français depuis le 26/11/2026, un visuel par angle de friction (voir tools/x-calendar/posts.py)
 dict(n=28, icons=['tag', 'percent', 'bag'],
      h1='Prix barré<br>pour <i>-5 %</i> ? Je<br>testerais le prix seul.',
      screen=[nav(), img(), title(), price('38 €', '40 €', mark=True), btn(), bart()]),
 dict(n=29, icons=['percent', 'tag', 'bag'],
      h1='Remise visible<br><i>qu\'au paiement</i> ?<br>Je testerais le panier.',
      screen=[head('Ton panier (2)'), banner('BLACK FRIDAY · CODE BLACK30'), item('60 €'), item('25 €'),
              mk(row('Sous-total', '85 €', True)), note('Réductions calculées au paiement'), btn('Paiement')]),
 dict(n=30, icons=['card', 'bag', 'check'],
      h1='Apple Pay<br>sur la fiche ? Je<br>testerais <i>le panier</i>.',
      screen=[nav(), img(104), title(), price('39 €'), btn(), mk(btn('Apple Pay', True) + gap(4) + btn('Shop Pay', True))]),
 dict(n=31, icons=['clock', 'eye', 'check'],
      h1='Un timer qui<br><i>repart à zéro</i> ? Je<br>testerais une vraie date.',
      screen=[nav(), img(158), title(), price('49 €'), mk(timer("Fin de l'offre dans", '00:14:59')), btn()]),
 dict(n=32, icons=['tag', 'filter', 'percent'],
      h1='Badge <i>Promo</i>,<br>mais pas ta taille ?<br>Je testerais le dire.',
      screen=[head('Soldes', '≡'), grid([card('dès 29 €', 'PROMO'), card('dès 35 €', 'PROMO')]),
              mk(opt('XS', '29 €') + opt('M', '49 €', True)), btn()]),
 dict(n=33, icons=['tag', 'help', 'bag'],
      h1='Code refusé<br><i>sans dire pourquoi</i> ?<br>Je testerais la raison.',
      screen=[head('Ton panier (1)'), item('42 €', '60 €'), gap(4),
              mk('<div class="code"><div>BLACK10</div><span>Appliquer</span></div><div class="nt q">Code non valide</div>'),
              row('Sous-total', '42 €', True), btn('Paiement')]),
 dict(n=34, icons=['box', 'percent', 'tag'],
      h1='« 2 achetés, -10 % »<br><i>absent du panier</i> ?<br>Je testerais l\'y mettre.',
      screen=[head('Ton panier (1)'), item('25 €'), mk('<div class="empty">Plus un mot sur « 2 achetés, -10 % »</div>'),
              row('Sous-total', '25 €', True), btn('Paiement')]),
 dict(n=35, icons=['shield', 'check', 'bag'],
      h1='Protection<br><i>cochée d\'office</i> ?<br>Je testerais décochée.',
      screen=[head('Ton panier (2)'), item('55 €'), item('20 €'), mk(toggle('Protection de livraison', '2,95 €')),
              row('Sous-total', '77,95 €', True), btn('Paiement')]),
 dict(n=36, icons=['chat', 'eye', 'bag'],
      h1='Le chat <i>sur</i><br><i>le bouton</i> ? Je<br>testerais de l\'enlever.',
      screen=[nav(), img(), title(), price('39 €'), '<div class="rel">' + btn() + '<div class="chat"><svg viewBox="0 0 24 24">' + ICONS['chat'] + '</svg><i class="bd">1</i></div></div>', bart()]),
 dict(n=37, icons=['ruler', 'bag', 'check'],
      h1='L\'ajout rapide<br><i>prend le XS</i> ? Je<br>testerais de demander.',
      screen=[head('Sweats', '≡'), grid([card('59 €', quick=True), card('59 €', quick=True)]),
              mk('<div class="toast"><svg viewBox="0 0 24 24">' + ICONS['check'] + '</svg>Ajouté au panier : taille XS</div>'), grid([card('49 €'), card('49 €')])]),
 dict(n=39, icons=['mail', 'percent', 'eye'],
      h1='Pop-up fermée,<br><i>code perdu</i> ?<br>Je testerais un onglet.',
      screen=[nav(), img(), title(), price('39 €'), btn(),
              '<div class="dim"></div><div class="pop"><div class="px">' + mk('<span>×</span>', True) + '</div><b>-10 %</b><p>sur ta première commande</p>'
              '<div class="fx">Email</div><div class="btn">Recevoir mon code</div></div>']),
 dict(n=40, icons=['truck', 'gift', 'clock'],
      h1='« 3 à 5 jours<br>ouvrés » <i>en décembre</i> ?<br>Je testerais une date.',
      screen=[nav(), img(170), title(), price('45 €'), btn(), mk(note('Expédié sous 3 à 5 jours ouvrés', 'ship'))]),
 dict(n=41, icons=['gift', 'bag', 'heart'],
      h1='Le <i>prix dans</i><br><i>le colis</i> ? Je testerais<br>« C\'est un cadeau ».',
      screen=[head('Ton panier (2)'), item('48 €'), item('32 €'), mk('<div class="empty">Pas de facture sans prix, pas de message</div>'),
              row('Sous-total', '80 €', True), btn('Paiement')]),
 dict(n=42, icons=['truck', 'percent', 'check'],
      h1='Livraison offerte,<br>puis <i>plus offerte</i> ?<br>Je testerais le seuil.',
      screen=[head('Livraison', ''), row('Sous-total', '52 €'), row('Code -10 %', '-5,20 €'), gap(2),
              mk(opt('Standard', '4,95 €', True)), note('Livraison offerte dès 50 €'), btn('Continuer')]),
 dict(n=44, icons=['ruler', 'eye', 'check'],
      h1='Tes avis disent<br><i>« taille petit »</i> ?<br>Je testerais de l\'écrire.',
      screen=[nav(), img(120), title(), price('65 €'), mk(sizes(['XS', 'S', 'M', 'L', 'XL'])), note('★★★★☆ « Taille petit, prenez au-dessus »'), btn()]),
 dict(n=46, icons=['globe', 'card', 'tag'],
      h1='Un prix à<br><i>49,37 €</i> ? Je<br>testerais l\'arrondi.',
      screen=[nav(), img(), title(), price('49,37 €', mark=True), btn(), bart()]),
 dict(n=47, icons=['globe', 'box', 'card'],
      h1='Douane payée<br><i>à la livraison</i> ? Je<br>testerais droits inclus.',
      screen=[head('Récapitulatif', ''), item('120 €'), row('Sous-total', '120 €'), row('Livraison', '8 €'),
              mk(row('Douane', 'À la livraison')), row('Total', '128 €', True), btn('Payer')]),
 dict(n=48, icons=['phone', 'lock', 'check'],
      h1='Téléphone exigé,<br><i>sans dire pourquoi</i> ?<br>Je testerais le dire.',
      screen=[head('Contact', ''), field('Email', 'sam@mail.com'), field('Adresse', '12 rue du Marché'),
              mk(field('Téléphone (obligatoire)', '')), btn('Continuer')]),
 dict(n=54, icons=['gift', 'clock', 'bag'],
      h1='Le 22 décembre,<br>la carte cadeau<br><i>dans le footer</i> ?',
      screen=[nav(), img(120), '<div class="ft">', note('Aide', 'lbl'), links(['Contact', 'Livraison', 'Retours', 'Cartes cadeaux', 'Notre histoire'], 'Cartes cadeaux'), '</div>']),
 dict(n=58, icons=['box', 'tag', 'percent'],
      h1='Un lot <i>sans</i><br><i>prix unitaire</i> ? Je<br>testerais 9,67 € la paire.',
      screen=[nav(), img(170), title(), mk(opt('1 paire', '12 €') + opt('3 paires', '29 €', True)), btn()]),
 dict(n=59, icons=['refresh', 'card', 'check'],
      h1='Abonnement<br><i>coché pour toi</i> ? Je<br>testerais l\'inverse.',
      screen=[nav(), img(160), title(), mk(opt('Abonnement -15 %', '34 €', True)), opt('Achat unique', '40 €'), btn()]),
 dict(n=65, icons=['filter', 'ruler', 'tag'],
      h1='Filtre <i>taille M</i>,<br>mais M épuisé ?<br>Je testerais le stock.',
      screen=[head('Soldes', '≡'), mk(chips(['Taille : M', 'Prix', 'Couleur'])), grid([card('29 €', 'ÉPUISÉ'), card('39 €', 'PROMO')]), grid([card('24 €', 'ÉPUISÉ'), card('45 €', 'PROMO')])]),
]

PAGE = open(os.path.join(HERE, 'friction.tpl.html'), encoding='utf-8').read()

def tile(name, x, y, rot):
    # Tuiles légèrement penchées, comme sur la bannière.
    return f'<div class="tile" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"><svg viewBox="0 0 24 24">{ICONS[name]}</svg></div>'

for s in SPECS:
    tiles = tile(s['icons'][0], 452, 84, -5) + tile(s['icons'][1], 1128, 96, 6) + tile(s['icons'][2], 1010, 470, -4)
    html = (PAGE.replace('{{N}}', str(s['n'])).replace('{{H1}}', s['h1'])
                .replace('{{SCREEN}}', '\n'.join(s['screen'])).replace('{{TILES}}', tiles))
    with open(os.path.join(HERE, f"friction-{s['n']}.html"), 'w', encoding='utf-8') as f:
        f.write(html)
print(len(SPECS), 'pages:', ' '.join(str(s['n']) for s in SPECS))
