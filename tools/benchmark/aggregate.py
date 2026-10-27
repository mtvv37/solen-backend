#!/usr/bin/env python3
"""Turn page-level features into store-level consensus statistics, overall and per platform.

A store "has" a practice when at least 60% of its successfully fetched sampled pages
show it (and at least 2 pages were fetched). Output: stats.json and stats.md. The counts
in these files are the only numbers that may be quoted publicly: every claim must come
from here. Platforms with fewer than MIN_PLATFORM stores are not reported separately,
because a share over so few stores means nothing.
"""
import argparse
import json
import os
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone

MIN_PLATFORM = 15
BOOLS = [
    ('ld_product', 'Product structured data'),
    ('price', 'Price in structured data'),
    ('rating', 'Star rating in structured data'),
    ('return_policy_markup', 'Return policy in structured data'),
    ('shipping_markup', 'Shipping in structured data'),
    ('cta_found', 'Add to cart button or cart form found'),
    ('cta_text', 'Add to cart style button text'),
    ('returns_near_cta', 'Returns mentioned right after the button'),
    ('shipping_near_cta', 'Shipping or delivery mentioned right after the button'),
    ('free_shipping', 'Free shipping mentioned'),
    ('secure_checkout', 'Secure checkout wording'),
    ('guarantee', 'Guarantee wording'),
    ('payment_logos', 'Card or PayPal brand marks on the page'),
    ('wallet_buttons', 'Wallet payment (Shop Pay, Apple Pay, Google Pay) on the page'),
    ('viewport', 'Mobile viewport tag'),
]
NUMS = [('imgs', 'Images in the page'), ('scripts', 'Scripts in the page'), ('bytes', 'HTML size (bytes)')]
NEAR = ('returns_near_cta', 'shipping_near_cta')  # only meaningful where the button text was found


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        return [json.loads(x) for x in f if x.strip()]


def has(ps, key):
    return sum(1 for p in ps if p.get(key)) / len(ps) >= 0.6


def summarize(stores):
    """stores: {domain: [page features]} -> counts and shares for every practice."""
    feats = {}
    for key, label in BOOLS:
        pool = [ps for ps in stores.values() if has(ps, 'cta_text')] if key in NEAR else list(stores.values())
        have = sum(1 for ps in pool if has(ps, key))
        feats[key] = {'label': label, 'stores_with': have, 'stores_measured': len(pool),
                      'pct': round(100 * have / len(pool), 1) if pool else None}
    nums = {}
    for key, label in NUMS:
        per_store = [statistics.median(p[key] for p in ps) for ps in stores.values()]
        nums[key] = {'label': label,
                     'median_across_stores': round(statistics.median(per_store)) if per_store else None}
    return {'stores': len(stores), 'pages': sum(len(ps) for ps in stores.values()),
            'features': feats, 'numeric': nums}


def build(pages, min_platform=MIN_PLATFORM, refs=(), domain_status=None):
    by_domain = defaultdict(dict)  # latest page per url
    for p in pages:
        by_domain[p['domain']][p['url']] = p
    stores = {d: list(v.values()) for d, v in by_domain.items() if len(v) >= 2}
    platform_of = {d: statistics.mode([p['platform'] for p in ps]) for d, ps in stores.items()}
    groups = defaultdict(dict)
    for d, ps in stores.items():
        groups[platform_of[d]][d] = ps
    out = summarize(stores)
    out['generated_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    out['platforms'] = dict(Counter(platform_of.values()))
    out['by_platform'] = {p: summarize(g) for p, g in sorted(groups.items(), key=lambda kv: -len(kv[1]))
                          if len(g) >= min_platform}
    refs = set(refs)
    out['references'] = {
        d: {'pages': len(ps), 'platform': platform_of[d],
            'practices': {key: (has(ps, key) if key not in NEAR or has(ps, 'cta_text') else None)
                          for key, _ in BOOLS}}
        for d, ps in stores.items() if d in refs}
    status = domain_status or {}
    out['references_not_measured'] = {d: status.get(d, 'not crawled yet') for d in sorted(refs - set(stores))}
    return out


def to_markdown(stats):
    cols = ['all'] + list(stats['by_platform'])
    heads = [f"all ({stats['stores']})"] + [f"{p} ({stats['by_platform'][p]['stores']})" for p in stats['by_platform']]
    lines = [f"# Benchmark ({stats['stores']} stores, {stats['pages']} product pages)",
             f"Generated {stats['generated_at']}. A store counts when at least 60% of its sampled pages show the practice. "
             f"Platforms with fewer than {MIN_PLATFORM} stores are not shown on their own.", '',
             '| Practice | ' + ' | '.join(heads) + ' |', '|---|' + '---|' * len(cols)]

    def part(c):
        return stats if c == 'all' else stats['by_platform'][c]

    for key, label in BOOLS:
        cells = []
        for c in cols:
            v = part(c)['features'][key]
            cells.append('n/a' if v['pct'] is None else f"{v['pct']}%")
        lines.append(f'| {label} | ' + ' | '.join(cells) + ' |')
    lines += ['', '| Median across stores | ' + ' | '.join(heads) + ' |', '|---|' + '---|' * len(cols)]
    for key, label in NUMS:
        lines.append(f'| {label} | ' + ' | '.join(str(part(c)['numeric'][key]['median_across_stores']) for c in cols) + ' |')
    near = stats['features']['returns_near_cta']
    lines += ['', f"Near-the-button shares only count stores where the button text was found "
              f"({near['stores_measured']} of {stats['stores']} overall).",
              'Platforms (most frequent per store): ' + ', '.join(f'{k} {v}' for k, v in
                                                                 sorted(stats['platforms'].items(), key=lambda kv: -kv[1]))]
    refs = stats.get('references', {})
    missing = stats.get('references_not_measured', {})
    if refs or missing:
        names = list(refs)
        lines += ['', '## Reference stores (picked by hand, not a statistical group)',
                  'Each column shows what that store does on at least 60% of its pages. The sample column is the share of '
                  'all stores above. "n/a" means the button text was not found, so the near-the-button check is not possible.', '']
        if names:
            lines += ['| Practice | Sample | ' + ' | '.join(f"{n} ({refs[n]['pages']} pages)" for n in names) + ' |',
                      '|---|---|' + '---|' * len(names)]
            for key, label in BOOLS:
                sample = stats['features'][key]['pct']
                cells = ['n/a' if refs[n]['practices'][key] is None else ('yes' if refs[n]['practices'][key] else 'no')
                         for n in names]
                lines.append(f'| {label} | {sample}% | ' + ' | '.join(cells) + ' |')
        for d, st in missing.items():
            lines.append(f'Not measured yet: {d} ({st}).')
    return '\n'.join(lines) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', default='data')
    a = ap.parse_args()
    pages = [p for p in read_jsonl(os.path.join(a.data, 'pages.jsonl')) if p.get('ok') and p.get('v', 1) >= 3]
    here = os.path.dirname(os.path.abspath(__file__))
    ref_path = os.path.join(here, 'references.txt')
    refs = [x.strip().lower() for x in open(ref_path, encoding='utf-8') if x.strip() and not x.startswith('#')] \
        if os.path.exists(ref_path) else []
    status = {}
    for r in read_jsonl(os.path.join(a.data, 'domains.jsonl')):
        status[r['domain']] = r['status']
    stats = build(pages, refs=refs, domain_status=status)
    with open(os.path.join(a.data, 'stats.json'), 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)
    md = to_markdown(stats)
    with open(os.path.join(a.data, 'stats.md'), 'w', encoding='utf-8') as f:
        f.write(md)
    print(md)


if __name__ == '__main__':
    main()
