#!/usr/bin/env python3
"""Adds the next slice of the Tranco popularity ranking to the crawl queue.

Tranco is a free research ranking of the most popular domains. Most of them
are not shops: that is fine, crawl.py classifies each candidate quickly
("no_products" for a non-shop) and the run summary shows the real hit rate.
A cursor in <data>/tranco_cursor.json remembers where the last run stopped,
so each night continues the list instead of starting again.
"""
import argparse
import io
import json
import os
import sys
import urllib.request
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import UA, now  # noqa: E402
from discover import SKIP_SUFFIXES  # noqa: E402

URL = 'https://tranco-list.eu/top-1m.csv.zip'  # redirects to the latest daily list
SKIP_TLDS = ('.gov', '.edu', '.mil', '.int', '.gov.uk', '.ac.uk')
MAX_ZIP = 80_000_000


def parse_rows(text, start, count):
    """Lines look like 'rank,domain'. Returns (domains, next_rank)."""
    out, nxt = [], start
    for line in text.splitlines():
        parts = line.strip().split(',')
        if len(parts) < 2 or not parts[0].isdigit():
            continue
        rank, dom = int(parts[0]), parts[1].strip().lower()
        if rank < start:
            continue
        if len(out) >= count:
            break
        nxt = rank + 1
        if any(dom == s or dom.endswith('.' + s) for s in SKIP_SUFFIXES) or dom.endswith(SKIP_TLDS):
            continue
        out.append(dom)
    return out, nxt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', default='data')
    ap.add_argument('--per-run', type=int, default=1500)
    ap.add_argument('--max-rank', type=int, default=200_000)
    a = ap.parse_args()
    os.makedirs(a.data, exist_ok=True)
    cur_path = os.path.join(a.data, 'tranco_cursor.json')
    out_path = os.path.join(a.data, 'seeds_discovered.txt')
    start = json.load(open(cur_path))['next_rank'] if os.path.exists(cur_path) else 1
    if start > a.max_rank:
        print('Tranco slice finished (max rank reached)')
        return
    req = urllib.request.Request(URL, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as f:
        raw = f.read(MAX_ZIP)
    z = zipfile.ZipFile(io.BytesIO(raw))
    text = z.read(z.namelist()[0]).decode('utf-8', 'ignore')
    doms, nxt = parse_rows(text, start, a.per_run)
    known = set()
    if os.path.exists(out_path):
        known = {x.strip() for x in open(out_path, encoding='utf-8') if x.strip()}
    fresh = [d for d in doms if d not in known]
    with open(out_path, 'a', encoding='utf-8') as f:
        for d in fresh:
            f.write(d + '\n')
    json.dump({'next_rank': nxt, 'updated_at': now()}, open(cur_path, 'w'))
    print(f'Tranco ranks {start} to {nxt - 1}: {len(fresh)} new candidate domains')


if __name__ == '__main__':
    main()
