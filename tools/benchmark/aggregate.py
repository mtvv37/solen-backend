#!/usr/bin/env python3
"""Turn page-level features into store-level consensus statistics.

A store "has" a practice when at least 60% of its successfully fetched
sampled pages show it (and at least 2 pages were fetched). Output:
stats.json and stats.md. The counts in these files are the only numbers that
may be quoted publicly: every claim must come from here.
"""
import argparse
import json
import os
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone

BOOLS = [
    ('ld_product', 'Product structured data'),
    ('price', 'Price in structured data'),
    ('rating', 'Star rating in structured data'),
    ('return_policy_markup', 'Return policy in structured data'),
    ('shipping_markup', 'Shipping in structured data'),
    ('cta_found', 'Add to cart style button text'),
    ('returns_near_cta', 'Returns mentioned right after the button'),
    ('shipping_near_cta', 'Shipping or delivery mentioned right after the button'),
    ('free_shipping', 'Free shipping mentioned'),
    ('secure_checkout', 'Secure checkout wording'),
    ('guarantee', 'Guarantee wording'),
    ('payment_logos', 'Payment logos on the page'),
    ('viewport', 'Mobile viewport tag'),
]
NUMS = [('imgs', 'Images in the page'), ('scripts', 'Scripts in the page'), ('bytes', 'HTML size (bytes)')]


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        return [json.loads(x) for x in f if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', default='data')
    a = ap.parse_args()
    pages = [p for p in read_jsonl(os.path.join(a.data, 'pages.jsonl')) if p.get('ok')]
    by_domain = defaultdict(dict)  # latest page per url
    for p in pages:
        by_domain[p['domain']][p['url']] = p
    stores = {d: list(v.values()) for d, v in by_domain.items() if len(v) >= 2}

    feats = {}
    for key, label in BOOLS:
        have = sum(1 for ps in stores.values()
                   if sum(1 for p in ps if p.get(key)) / len(ps) >= 0.6)
        feats[key] = {'label': label, 'stores_with': have,
                      'pct': round(100 * have / len(stores), 1) if stores else None}
    nums = {}
    for key, label in NUMS:
        per_store = [statistics.median(p[key] for p in ps) for ps in stores.values()]
        nums[key] = {'label': label,
                     'median_across_stores': round(statistics.median(per_store)) if per_store else None}
    platforms = Counter(statistics.mode([p['platform'] for p in ps]) for ps in stores.values())
    stats = {
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'stores': len(stores),
        'pages': sum(len(ps) for ps in stores.values()),
        'features': feats,
        'numeric': nums,
        'platforms': dict(platforms),
    }
    with open(os.path.join(a.data, 'stats.json'), 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)
    lines = [f"# Benchmark ({stats['stores']} stores, {stats['pages']} product pages)",
             f"Generated {stats['generated_at']}. A store counts when at least 60% of its sampled pages show the practice.", '',
             '| Practice | Stores | Share |', '|---|---|---|']
    for key, _ in BOOLS:
        v = feats[key]
        lines.append(f"| {v['label']} | {v['stores_with']} | {v['pct']}% |")
    lines += ['', '| Measure | Median across stores |', '|---|---|']
    for key, _ in NUMS:
        v = nums[key]
        lines.append(f"| {v['label']} | {v['median_across_stores']} |")
    lines += ['', 'Platforms (most frequent per store): ' + ', '.join(f'{k} {v}' for k, v in platforms.most_common())]
    with open(os.path.join(a.data, 'stats.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
