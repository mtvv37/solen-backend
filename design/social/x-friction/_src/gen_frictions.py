"""Génère les visuels X de la série « Shopify friction worth testing » (1200 x 675, même format que brand/posts/).

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
def btn(t='Add to cart', ghost=False): return f'<div class="btn{" ghost" if ghost else ""}">{t}</div>'
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
            f'<b>{price_t}</b>{"<u>+ Quick add</u>" if quick else ""}</div>')
def grid(cards): return '<div class="gr">' + ''.join(cards) + '</div>'
def timer(label, t): return f'<div class="tm"><span>{label}</span><b>{t}</b></div>'
def toggle(label, right, on=True): return f'<div class="tg{" on" if on else ""}"><i></i><span>{label}</span><b>{right}</b></div>'
def chips(labels): return '<div class="ch">' + ''.join(f'<span>{c}</span>' for c in labels) + '</div>'
def links(items, marked): return '<div class="ln">' + ''.join(mk(f'<span>{t}</span>') if t == marked else f'<span>{t}</span>' for t in items) + '</div>'
def gap(h): return f'<div style="height:{h}px"></div>'

SPECS = [
 dict(n=28, icons=['tag', 'percent', 'bag'],
      h1='Sale price <i>alone</i>?<br>I\'d test the original<br>price next to it.',
      screen=[nav(), img(), title(), price('€39', mark=True), btn(), bart()]),
 dict(n=29, icons=['percent', 'tag', 'bag'],
      h1='Discount only<br><i>at checkout</i>? I\'d test<br>it in the cart.',
      screen=[head('Your cart (2)'), banner('BLACK FRIDAY · 30% OFF'), item('€60'), item('€25'),
              mk(row('Subtotal', '€85', True)), note('Discounts applied at checkout'), btn('Checkout')]),
 dict(n=30, icons=['card', 'bag', 'check'],
      h1='One checkout button?<br>I\'d test <i>express pay</i><br>in the cart.',
      screen=[head('Your cart (2)'), item('€45'), item('€30'), row('Subtotal', '€75', True), gap(6), mk(btn('Checkout')), note('Taxes and shipping at checkout')]),
 dict(n=31, icons=['clock', 'eye', 'check'],
      h1='A timer that <i>restarts</i><br>on reload? I\'d test<br>a real deadline.',
      screen=[nav(), img(158), title(), price('€49'), mk(timer('Offer ends in', '00:14:59')), btn()]),
 dict(n=32, icons=['tag', 'filter', 'percent'],
      h1='Full-price items<br>on the <i>Sale</i> page?<br>I\'d test sale items only.',
      screen=[head('Sale', '≡'), grid([card('€42', 'SALE'), card('€35', 'SALE')]), mk(grid([card('€80'), card('€65')]))]),
 dict(n=33, icons=['tag', 'help', 'bag'],
      h1='Does my code work<br>on <i>sale</i> items? I\'d test<br>saying it in the cart.',
      screen=[head('Your cart (1)'), item('€42', '€60'), gap(4),
              mk('<div class="code"><div>Discount code</div><span>Apply</span></div><div class="nt q">Does it work on sale items?</div>'),
              row('Subtotal', '€42', True), btn('Checkout')]),
 dict(n=34, icons=['box', 'percent', 'tag'],
      h1='Bundle offer<br>in <i>small print</i>? I\'d test<br>the saving in euros.',
      screen=[nav(), img(164), title(), price('€25'), mk(note('Buy 2, save 10%. Conditions apply.', 'tiny')), btn(), bart()]),
 dict(n=35, icons=['shield', 'check', 'bag'],
      h1='Protection added<br><i>by default</i>? I\'d test<br>it unchecked.',
      screen=[head('Your cart (2)'), item('€55'), item('€20'), mk(toggle('Shipping protection', '€2.95')),
              row('Subtotal', '€77.95', True), btn('Checkout')]),
 dict(n=36, icons=['chat', 'eye', 'bag'],
      h1='Chat bubble on<br><i>Add to cart</i>? I\'d test<br>moving it up.',
      screen=[nav(), img(), title(), price('€39'), '<div class="rel">' + btn() + '<div class="chat"><svg viewBox="0 0 24 24">' + ICONS['chat'] + '</svg><i class="bd">1</i></div></div>', bart()]),
 dict(n=37, icons=['ruler', 'bag', 'check'],
      h1='Quick add <i>picks a size</i><br>for you? I\'d test<br>asking first.',
      screen=[head('Hoodies', '≡'), grid([card('€59', quick=True), card('€59', quick=True)]),
              mk('<div class="toast"><svg viewBox="0 0 24 24">' + ICONS['check'] + '</svg>Added to cart: size S</div>'), grid([card('€49'), card('€49')])]),
 dict(n=39, icons=['mail', 'percent', 'eye'],
      h1='Close the pop-up,<br><i>lose the code</i>?<br>I\'d test a small tab.',
      screen=[nav(), img(), title(), price('€39'), btn(),
              '<div class="dim"></div><div class="pop"><div class="px">' + mk('<span>×</span>', True) + '</div><b>Get 10% off</b><p>your first order</p>'
              '<div class="fx">Email</div><div class="btn">Get my code</div></div>']),
 dict(n=40, icons=['truck', 'gift', 'clock'],
      h1='Will it arrive<br><i>by Christmas</i>? I\'d test<br>an order-by date.',
      screen=[nav(), img(170), title(), price('€45'), btn(), mk(note('Ships in 3 to 5 business days', 'ship'))]),
 dict(n=41, icons=['gift', 'bag', 'heart'],
      h1='No gift option<br><i>before checkout</i>?<br>I\'d test a gift toggle.',
      screen=[head('Your cart (2)'), item('€48'), item('€32'), mk('<div class="empty">No gift wrap, no gift message</div>'),
              row('Subtotal', '€80', True), btn('Checkout')]),
 dict(n=42, icons=['truck', 'clock', 'check'],
      h1='Shipping options<br><i>without dates</i>?<br>I\'d test delivery days.',
      screen=[head('Shipping', ''), field('Address', '12 Market Street'), gap(2),
              mk(opt('Standard', '€4.95', True) + opt('Express', '€9.95')), btn('Continue to payment')]),
 dict(n=44, icons=['ruler', 'eye', 'check'],
      h1='Sizes, but<br><i>no fit info</i>? I\'d test<br>the model\'s size.',
      screen=[nav(), img(162), title(), price('€65'), mk(sizes(['XS', 'S', 'M', 'L', 'XL'])), btn()]),
 dict(n=46, icons=['globe', 'card', 'tag'],
      h1='Dollars for<br><i>European</i> visitors?<br>I\'d test local currency.',
      screen=[nav(), img(), title(), price('$49.00 USD', mark=True), btn(), bart()]),
 dict(n=47, icons=['globe', 'box', 'card'],
      h1='Duties paid<br><i>on delivery</i>? I\'d test<br>duties included.',
      screen=[head('Order summary', ''), item('€120'), row('Subtotal', '€120'), row('Shipping', '€8'),
              mk(row('Duties', 'Paid on delivery')), row('Total', '€128', True), btn('Pay now')]),
 dict(n=48, icons=['phone', 'lock', 'check'],
      h1='Phone number<br><i>required</i>, no reason?<br>I\'d test saying why.',
      screen=[head('Contact', ''), field('Email', 'sam@mail.com'), field('Address', '12 Market Street'),
              mk(field('Phone (required)', '')), btn('Continue')]),
 dict(n=54, icons=['gift', 'clock', 'bag'],
      h1='Gift cards<br><i>in the footer</i>? I\'d test<br>them in the menu.',
      screen=[nav(), img(120), '<div class="ft">', note('Help', 'lbl'), links(['Contact', 'Shipping', 'Returns', 'Gift cards', 'Our story'], 'Gift cards'), '</div>']),
 dict(n=58, icons=['box', 'tag', 'percent'],
      h1='Packs <i>without</i><br><i>a unit price</i>? I\'d test<br>€9.67 per pair.',
      screen=[nav(), img(170), title(), mk(opt('1 pair', '€12') + opt('3 pairs', '€29', True)), btn()]),
 dict(n=59, icons=['refresh', 'card', 'check'],
      h1='Subscription<br><i>picked for you</i>?<br>I\'d test one-time first.',
      screen=[nav(), img(160), title(), mk(opt('Subscribe and save 15%', '€34', True)), opt('One-time purchase', '€40'), btn()]),
 dict(n=65, icons=['filter', 'ruler', 'tag'],
      h1='Sale page with<br><i>no size filter</i>?<br>I\'d test one.',
      screen=[head('Sale', '≡'), mk(chips(['Category', 'Price', 'Color'])), grid([card('€29', 'SALE'), card('€39', 'SALE')]), grid([card('€24', 'SALE'), card('€45', 'SALE')])]),
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
