#!/usr/bin/env python3
"""Solen benchmark crawler.

Reads a list of e-commerce domains, samples a few public product pages per
domain from its sitemap, and stores FEATURES of each page (never page text or
images). Standard library only.

Good citizen rules, all enforced here:
- identifies itself with a clear User-Agent and a contact address
- reads robots.txt first and obeys it (including Crawl-delay)
- at most one request per domain every MIN_DELAY seconds
- a 401/403/captcha means "blocked": the domain is marked and left alone,
  never worked around
"""
import argparse
import gzip
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from urllib.robotparser import RobotFileParser

VERSION = 2  # bump when feature extraction changes: older records are crawled again
UA = 'SolenBot/0.1 (+https://withsolen.com; contact: withsolen@gmail.com)'
ROBOT_NAME = 'SolenBot'
MAX_BYTES = 2_500_000
TIMEOUT = 15
PAGES_PER_DOMAIN = 5

PRODUCT_RE = re.compile(
    r'/(products?|produits?|producto|artikel|item)/[^/?#]+|/p/[^/?#]+|-p-\d+', re.I)

CTA_RE = re.compile(
    r'add to (cart|bag|basket)|buy now|ajouter au (panier|sac)|acheter maintenant|'
    r'in den warenkorb|a[nñ]adir al carrito', re.I)
RETURN_RE = re.compile(r'return|refund|exchange|retour|rembours|r[uü]ckgabe|r[uü]cksendung|devoluci', re.I)
FREE_SHIP_RE = re.compile(
    r'free (shipping|delivery)|livraison (gratuite|offerte)|kostenlos(er)? versand|env[ií]o gratis', re.I)
SHIP_RE = re.compile(r'shipping|delivery|livraison|versand|env[ií]o', re.I)
SECURE_RE = re.compile(
    r'secure (checkout|payment)|paiement s[eé]curis[eé]|sichere zahlung|pago seguro', re.I)
GUARANTEE_RE = re.compile(
    r'guarantee|garantie|money.back|satisfait ou rembours|garant[ií]a', re.I)
PAY_RE = re.compile(r'visa|mastercard|paypal|apple.?pay|shop.?pay|klarna|amex|google.?pay', re.I)


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def get(url):
    """Returns (status, content_type, text). status 0 = network error."""
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip'})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as f:
            raw = f.read(MAX_BYTES)
            if raw[:2] == b'\x1f\x8b':
                raw = gzip.decompress(raw)
            return f.status, f.headers.get('Content-Type', ''), raw.decode('utf-8', 'ignore')
    except urllib.error.HTTPError as e:
        return e.code, '', ''
    except Exception:
        return 0, '', ''


def _is_type(d, names):
    t = d.get('@type')
    ts = t if isinstance(t, list) else [t]
    return any(isinstance(x, str) and x.rsplit('/', 1)[-1] in names for x in ts)


def find_product(d):
    """Finds a Product or ProductGroup node in JSON-LD (also inside @graph)."""
    if isinstance(d, list):
        for x in d:
            r = find_product(x)
            if r:
                return r
    elif isinstance(d, dict):
        if _is_type(d, ('Product', 'ProductGroup')):
            return d
        for k in ('@graph', 'mainEntity'):
            if k in d:
                r = find_product(d[k])
                if r:
                    return r
    return None


def first_offer(p):
    """Offer of a Product, or of the first variant of a ProductGroup."""
    o = p.get('offers') if p else None
    if not o and p and isinstance(p.get('hasVariant'), list) and p['hasVariant']:
        v = p['hasVariant'][0]
        o = v.get('offers') if isinstance(v, dict) else None
    if isinstance(o, list):
        o = o[0] if o else None
    return o if isinstance(o, dict) else {}


def jsonld_product(html):
    for m in re.finditer(
            r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.S | re.I):
        try:
            p = find_product(json.loads(m.group(1).strip()))
        except Exception:
            continue
        if p:
            return p
    return None


def visible_text(html):
    t = re.sub(r'<(script|style|noscript|svg)\b.*?</\1>', ' ', html, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).lower()[:200_000]


def platform_of(html):
    h = html[:400_000].lower()
    if 'cdn.shopify.com' in h or 'shopify.theme' in h:
        return 'shopify'
    if re.search(r'woocommerce[-_/]|/plugins/woocommerce', h):
        return 'woocommerce'
    if 'bigcommerce' in h:
        return 'bigcommerce'
    if 'demandware' in h or 'salesforce' in h:
        return 'sfcc'
    if 'mage/' in h or 'magento' in h:
        return 'magento'
    if 'wixstatic' in h:
        return 'wix'
    if 'squarespace' in h:
        return 'squarespace'
    return 'other'


def features(html, url):
    p = jsonld_product(html)
    offers = first_offer(p)
    rating = (p or {}).get('aggregateRating') or {}
    if not isinstance(rating, dict):
        rating = {}
    images = (p or {}).get('image')
    text = visible_text(html)
    cta = CTA_RE.search(text)
    cart_form = bool(re.search(r'action=["\'][^"\']*/cart/add|name=["\']add-to-cart|class=["\'][^"\']*single_add_to_cart', html, re.I))
    near = text[cta.start(): cta.start() + 1500] if cta else ''
    imgs = re.findall(r'<img\b[^>]*>', html, re.I)
    no_script = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.S | re.I)
    return {
        'v': VERSION,
        'url': url,
        'fetched_at': now(),
        'platform': platform_of(html),
        'bytes': len(html),
        'scripts': len(re.findall(r'<script\b', html, re.I)),
        'imgs': len(imgs),
        'viewport': bool(re.search(r'<meta[^>]+name=["\']viewport', html, re.I)),
        'h1': bool(re.search(r'<h1\b', html, re.I)),
        'ld_product': bool(p),
        'price': bool(offers.get('price') or offers.get('lowPrice')),
        'currency': offers.get('priceCurrency'),
        'availability': bool(offers.get('availability')),
        'rating': bool(rating.get('ratingValue')),
        'rating_count': rating.get('ratingCount') or rating.get('reviewCount'),
        'ld_images': (len(images) if isinstance(images, list) else 1) if images else 0,
        'return_policy_markup': bool(offers.get('hasMerchantReturnPolicy')),
        'shipping_markup': bool(offers.get('shippingDetails')),
        'cta_found': bool(cta) or cart_form,
        'cta_text': bool(cta),
        'returns_near_cta': bool(cta and RETURN_RE.search(near)),
        'shipping_near_cta': bool(cta and SHIP_RE.search(near)),
        'free_shipping': bool(FREE_SHIP_RE.search(text)),
        'secure_checkout': bool(SECURE_RE.search(text)),
        'guarantee': bool(GUARANTEE_RE.search(text)),
        'payment_logos': bool(PAY_RE.search(no_script)),
    }


def locs(xml):
    return re.findall(r'<loc>\s*([^<\s]+)\s*</loc>', xml)


def discover_products(sitemaps, delay, deadline):
    """Walk up to 6 sitemaps and return product-looking URLs."""
    queue, seen, urls = list(sitemaps[:5]), 0, []
    while queue and seen < 8 and len(urls) < 60 and time.time() < deadline:
        sm = queue.pop(0)
        seen += 1
        time.sleep(delay)
        status, _, xml = get(sm)
        if status != 200 or not xml:
            continue
        found = locs(xml)
        if '<sitemapindex' in xml:
            kids = sorted(found, key=lambda u: 'product' not in u.lower())
            queue = kids[:2] + queue
        elif 'product' in sm.lower() and not any(PRODUCT_RE.search(u) for u in found):
            urls += [u for u in found if not re.search(r'\.(jpg|jpeg|png|webp|gif)$', u, re.I)]
        else:
            urls += [u for u in found if PRODUCT_RE.search(u)]
    return urls


def crawl_domain(domain, scheme, min_delay, deadline):
    rec = {'v': VERSION, 'domain': domain, 'checked_at': now(), 'status': 'ok',
           'platform': None, 'pages': 0}
    if time.time() > deadline:
        rec['status'] = 'skipped_budget'
        return rec, []
    base = f'{scheme}://{domain}'
    status, _, robots = get(base + '/robots.txt')
    if status in (401, 403):
        rec['status'] = 'blocked'
        return rec, []
    if status == 0 or status >= 500:
        rec['status'] = 'unreachable'
        return rec, []
    rp = RobotFileParser()
    rp.parse(robots.splitlines() if status == 200 else [])
    if not rp.can_fetch(ROBOT_NAME, base + '/'):
        rec['status'] = 'robots_disallow'
        return rec, []
    delay = max(min_delay, min(10.0, float(rp.crawl_delay(ROBOT_NAME) or 0)))
    sitemaps = list(dict.fromkeys((rp.site_maps() or []) +
                                  [base + '/sitemap.xml', base + '/sitemap_index.xml']))
    urls = [u for u in dict.fromkeys(discover_products(sitemaps, delay, deadline))
            if rp.can_fetch(ROBOT_NAME, u)]
    if not urls:
        rec['status'] = 'no_products'
        return rec, []
    rng = random.Random(domain)
    sample = rng.sample(urls, min(PAGES_PER_DOMAIN, len(urls)))
    pages = []
    for u in sample:
        if time.time() > deadline:
            break
        time.sleep(delay)
        st, ct, html = get(u)
        if st in (401, 403, 429):
            rec['status'] = 'blocked'
            break
        if st != 200 or 'html' not in ct.lower() or len(html) < 2000:
            pages.append({'v': VERSION, 'domain': domain, 'url': u, 'ok': False, 'http': st})
            continue
        f = features(html, u)
        f.update({'domain': domain, 'ok': True, 'http': st})
        pages.append(f)
        rec['platform'] = rec['platform'] or f['platform']
    rec['pages'] = sum(1 for p in pages if p['ok'])
    if rec['status'] == 'ok' and rec['pages'] == 0:
        rec['status'] = 'no_pages'
    return rec, pages


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def append_jsonl(path, rows):
    with open(path, 'a', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seeds', default=os.path.join(os.path.dirname(__file__), 'seeds.txt'))
    ap.add_argument('--data', default='data')
    ap.add_argument('--batch', type=int, default=40)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--min-delay', type=float, default=1.5)
    ap.add_argument('--budget-min', type=float, default=35)
    ap.add_argument('--scheme', default='https')
    ap.add_argument('--recheck-days', type=int, default=60)
    a = ap.parse_args()

    os.makedirs(a.data, exist_ok=True)
    seed_files = [a.seeds, os.path.join(a.data, 'seeds_discovered.txt')]
    seeds = [s.strip().lower() for path in seed_files if os.path.exists(path)
             for s in open(path, encoding='utf-8') if s.strip() and not s.startswith('#')]
    state = {r['domain']: r for r in read_jsonl(os.path.join(a.data, 'domains.jsonl'))}

    def due(d):
        r = state.get(d)
        if not r or r.get('v', 1) < VERSION:
            return True
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(r['checked_at'])).days
        return age >= a.recheck_days

    pending = [d for d in dict.fromkeys(seeds) if due(d)][:a.batch]
    deadline = time.time() + a.budget_min * 60
    print(f'{len(seeds)} seeds, {len(pending)} to crawl now')

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        results = list(ex.map(lambda d: crawl_domain(d, a.scheme, a.min_delay, deadline), pending))

    recs = [r for r, _ in results if r['status'] != 'skipped_budget']
    pages = [p for _, ps in results for p in ps]
    append_jsonl(os.path.join(a.data, 'domains.jsonl'), recs)
    append_jsonl(os.path.join(a.data, 'pages.jsonl'), pages)

    by_status = {}
    for r in recs:
        by_status[r['status']] = by_status.get(r['status'], 0) + 1
    all_domains = [r for r in read_jsonl(os.path.join(a.data, 'domains.jsonl')) if r.get('v', 1) >= VERSION]
    all_pages = [p for p in read_jsonl(os.path.join(a.data, 'pages.jsonl')) if p.get('v', 1) >= VERSION]
    summary = {
        'run_at': now(),
        'domains_processed': len(recs),
        'by_status': by_status,
        'pages_ok': sum(1 for p in pages if p['ok']),
        'pages_failed': sum(1 for p in pages if not p['ok']),
        'total_domains_with_pages': len({r['domain'] for r in all_domains if r['pages'] > 0}),
        'total_pages_ok': sum(1 for p in all_pages if p['ok']),
        'seeds_left': len([d for d in seeds if due(d) and d not in {r['domain'] for r in recs}]),
    }
    with open(os.path.join(a.data, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    sys.exit(main())
