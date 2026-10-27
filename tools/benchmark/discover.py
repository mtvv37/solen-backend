#!/usr/bin/env python3
"""Finds candidate store domains in public roundup articles listed in sources.txt.

Reads each article once (robots.txt obeyed, same SolenBot identity as the crawler),
keeps the external domains it links to, and appends the new ones to
<data>/seeds_discovered.txt. A candidate is NOT assumed to be a store: crawl.py
checks it and records "no_products" when it is not. Standard library only.
"""
import argparse
import json
import os
import re
import sys
import time
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import ROBOT_NAME, get, now  # noqa: E402

SKIP_SUFFIXES = (
    'facebook.com', 'instagram.com', 'twitter.com', 'x.com', 'linkedin.com', 'youtube.com', 'youtu.be',
    'pinterest.com', 'tiktok.com', 'google.com', 'googleapis.com', 'gstatic.com', 'goo.gl', 'apple.com',
    'wikipedia.org', 'wordpress.com', 'wordpress.org', 'wp.com', 'gravatar.com', 'shopify.com',
    'myshopify.com', 'bigcommerce.com', 'woocommerce.com', 'magento.com', 'adobe.com', 'wix.com',
    'squarespace.com', 'medium.com', 'github.com', 'reddit.com', 'quora.com', 'amazon.com', 'ebay.com',
    'etsy.com', 'cloudflare.com', 'w3.org', 'schema.org', 'bit.ly', 'mailchimp.com', 'hubspot.com',
    'semrush.com', 'ahrefs.com', 'similarweb.com', 'builtwith.com', 'trustpilot.com', 'capterra.com',
    'g2.com', 'clutch.co', 'upwork.com', 'fiverr.com', 'paypal.com', 'stripe.com', 'klaviyo.com',
    'omnisend.com', 'hostinger.com', 'gempages.net', 'the4.co', 'meetanshi.com', 'drip.com', 'amasty.com',
    'trendtrack.io', 'ecomm.design', 'adnabu.com', 'whatmore.ai', 'digitiz.fr', 'lafabriquedunet.fr',
    'influencermarketinghub.com', 'mean.ceo', 'mockplus.com', 'ecommercefastlane.com', 'metrobi.com',
    'iab.com', 'ecomcrew.com', 'oberlo.com', 'wizishop.fr', 'elogic.co', 'sharethis.com', 'netsolutions.com',
    'vervaunt.com', 'ecommerceguide.com', 'contactpigeon.com', 'uxplanet.org', 'creativecommons.org',
    'tripadvisor.com', 'yelp.com', 'forbes.com', 'wsj.com', 'nytimes.com', 'techcrunch.com',
)


def candidates(html, own_host):
    out = []
    for h in re.findall(r'href=["\'](https?://[^"\'#\s]+)', html, re.I):
        host = (urlparse(h).hostname or '').lower()
        if host.startswith('www.'):
            host = host[4:]
        if not host or '.' not in host or re.fullmatch(r'[\d.]+', host):
            continue
        if host == own_host or own_host.endswith('.' + host) or host.endswith('.' + own_host):
            continue
        if any(host == s or host.endswith('.' + s) for s in SKIP_SUFFIXES):
            continue
        out.append(host)
    return list(dict.fromkeys(out))


def allowed(url):
    p = urlparse(url)
    rp = RobotFileParser()
    status, _, txt = get(f'{p.scheme}://{p.netloc}/robots.txt')
    if status in (401, 403):
        return False
    rp.parse(txt.splitlines() if status == 200 else [])
    return rp.can_fetch(ROBOT_NAME, url)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sources', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources.txt'))
    ap.add_argument('--data', default='data')
    ap.add_argument('--per-source', type=int, default=80)
    ap.add_argument('--max-new', type=int, default=500)
    a = ap.parse_args()
    os.makedirs(a.data, exist_ok=True)
    out_path = os.path.join(a.data, 'seeds_discovered.txt')
    log_path = os.path.join(a.data, 'discover_log.jsonl')
    known = set()
    if os.path.exists(out_path):
        known = {x.strip() for x in open(out_path, encoding='utf-8') if x.strip() and not x.startswith('#')}
    done = set()
    if os.path.exists(log_path):
        done = {json.loads(x)['source'] for x in open(log_path, encoding='utf-8') if x.strip()}
    srcs = [s.strip() for s in open(a.sources, encoding='utf-8') if s.strip() and not s.startswith('#')]
    new_total = 0
    for src in srcs:
        if src in done or new_total >= a.max_new:
            continue
        rec = {'source': src, 'at': now(), 'status': 'ok', 'found': 0, 'new': 0}
        try:
            if not allowed(src):
                rec['status'] = 'robots_disallow'
            else:
                time.sleep(1.5)
                st, ct, html = get(src)
                if st != 200 or 'html' not in ct.lower():
                    rec['status'] = f'http_{st}'
                else:
                    own = (urlparse(src).hostname or '').lower().removeprefix('www.')
                    found = candidates(html, own)[:a.per_source]
                    fresh = [d for d in found if d not in known]
                    with open(out_path, 'a', encoding='utf-8') as f:
                        for d in fresh:
                            f.write(d + '\n')
                    known.update(fresh)
                    rec['found'], rec['new'] = len(found), len(fresh)
                    new_total += len(fresh)
        except Exception as e:  # never let one article stop the run
            rec['status'] = 'error:' + str(e)[:60]
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(rec) + '\n')
        print(rec)
    print(f'{new_total} new candidate domains, {len(known)} known')


if __name__ == '__main__':
    main()
