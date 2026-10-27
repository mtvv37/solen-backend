#!/usr/bin/env python3
"""Offline test: runs the crawler against a fake store on localhost.

Checks: robots.txt is obeyed, sitemap index is followed, 5 pages are sampled,
features are extracted, a blocked domain is marked and left alone, and the
aggregate step produces stats. Run: python3 tools/benchmark/test_local.py
"""
import json
import os
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
HITS = {}
PORT = {}


def page(i):
    ret = 'Free returns within 30 days.' if i % 2 == 0 else ''
    ld = {'@context': 'https://schema.org', '@type': 'Product', 'name': f'Item {i}',
          'image': ['a.jpg', 'b.jpg'],
          'offers': {'@type': 'Offer', 'price': '19.00', 'priceCurrency': 'EUR',
                     'availability': 'InStock'},
          'aggregateRating': {'ratingValue': '4.6', 'reviewCount': '120'}}
    filler = '<p>' + 'lorem ipsum ' * 300 + '</p>'
    return (f'<!doctype html><html><head><meta name="viewport" content="width=device-width">'
            f'<script type="application/ld+json">{json.dumps(ld)}</script></head><body>'
            f'<h1>Item {i}</h1><img src="visa.svg" alt="Visa"><button>Add to cart</button>'
            f'<p>{ret} Free shipping over 50.</p>{filler}</body></html>')


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        HITS[self.path] = HITS.get(self.path, 0) + 1
        host = self.headers.get('Host', '')
        base = f'http://{host}'
        if host.startswith('127.0.0.2'):  # a store that blocks robots
            self.send_response(403)
            self.end_headers()
            return
        if self.path == '/robots.txt':
            body = f'User-agent: *\nDisallow: /products/blocked/\nSitemap: {base}/sitemap_index.xml\n'
        elif self.path == '/sitemap_index.xml':
            body = (f'<sitemapindex><sitemap><loc>{base}/sitemap_pages_1.xml</loc></sitemap>'
                    f'<sitemap><loc>{base}/sitemap_products_1.xml</loc></sitemap></sitemapindex>')
        elif self.path == '/sitemap_products_1.xml':
            urls = [f'{base}/products/item-{i}' for i in range(8)] + [f'{base}/products/blocked/x']
            body = '<urlset>' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>'
        elif self.path == '/sitemap_pages_1.xml':
            body = f'<urlset><url><loc>{base}/pages/about</loc></url></urlset>'
        elif self.path.startswith('/products/item-'):
            body = page(int(self.path.rsplit('-', 1)[1]))
        else:
            self.send_response(404)
            self.end_headers()
            return
        data = body.encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html' if 'item-' in self.path else 'text/plain')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    srv = ThreadingHTTPServer(('0.0.0.0', 0), H)
    PORT['n'] = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    with tempfile.TemporaryDirectory() as tmp:
        seeds = os.path.join(tmp, 'seeds.txt')
        data = os.path.join(tmp, 'data')
        with open(seeds, 'w') as f:
            f.write(f"127.0.0.1:{PORT['n']}\n127.0.0.2:{PORT['n']}\n")
        env = dict(os.environ, NO_PROXY='*', no_proxy='*')
        for k in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy'):
            env.pop(k, None)
        r = subprocess.run([sys.executable, os.path.join(HERE, 'crawl.py'), '--seeds', seeds,
                            '--data', data, '--scheme', 'http', '--min-delay', '0.05', '--no-refs',
                            '--budget-min', '2'], capture_output=True, text=True, env=env)
        print(r.stdout, r.stderr)
        assert r.returncode == 0, 'crawler failed'
        pages = [json.loads(x) for x in open(os.path.join(data, 'pages.jsonl'))]
        doms = {json.loads(x)['domain']: json.loads(x) for x in open(os.path.join(data, 'domains.jsonl'))}
        ok = [p for p in pages if p['ok']]
        assert len(ok) == 5, f'expected 5 pages, got {len(ok)}'
        assert HITS.get('/products/blocked/x', 0) == 0, 'robots.txt Disallow was not obeyed'
        assert all(p['ld_product'] and p['price'] and p['rating'] and p['payment_logos'] and p['cta_found']
                   for p in ok), 'feature extraction failed'
        assert any(p['returns_near_cta'] for p in ok) and any(not p['returns_near_cta'] for p in ok)
        assert all(p['free_shipping'] and p['viewport'] and p['h1'] for p in ok)
        assert doms[f"127.0.0.1:{PORT['n']}"]['status'] == 'ok'
        assert doms[f"127.0.0.2:{PORT['n']}"]['status'] == 'blocked', 'blocked store not marked'
        # second run must not recrawl domains already done
        subprocess.run([sys.executable, os.path.join(HERE, 'crawl.py'), '--seeds', seeds, '--data', data,
                        '--scheme', 'http', '--min-delay', '0.05', '--no-refs'], capture_output=True, env=env)
        again = [json.loads(x) for x in open(os.path.join(data, 'pages.jsonl'))]
        assert len(again) == len(pages), 'domains were crawled twice'
        a = subprocess.run([sys.executable, os.path.join(HERE, 'aggregate.py'), '--data', data],
                           capture_output=True, text=True)
        print(a.stdout)
        stats = json.load(open(os.path.join(data, 'stats.json')))
        assert stats['stores'] == 1 and stats['pages'] == 5
        assert stats['features']['rating']['pct'] == 100.0
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
