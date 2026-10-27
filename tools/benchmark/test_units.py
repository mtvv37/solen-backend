#!/usr/bin/env python3
"""Unit tests for the detections fixed after the first real run."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crawl import features, find_product, first_offer, platform_of  # noqa: E402
from discover import candidates  # noqa: E402


def doc(ld, body=''):
    return ('<html><head><meta name="viewport" content="x"><script type="application/ld+json">'
            + json.dumps(ld) + '</script></head><body><h1>x</h1>' + body + '<p>' + 'text ' * 500 + '</p></body></html>')


# 1. ProductGroup (newer Shopify themes): offers live in the first variant
group = {'@context': 'https://schema.org', '@type': 'ProductGroup', 'name': 'Shoe',
         'aggregateRating': {'ratingValue': '4.8', 'reviewCount': '40'},
         'hasVariant': [{'@type': 'Product', 'offers': {'@type': 'Offer', 'price': '95', 'priceCurrency': 'USD'}}]}
f = features(doc(group), 'https://x.test/products/a')
assert f['ld_product'] and f['price'] and f['rating'] and f['currency'] == 'USD', f

# 2. Product inside @graph with a full schema.org type URL
graph = {'@graph': [{'@type': 'WebSite'}, {'@type': 'https://schema.org/Product', 'offers': [{'price': '5'}]}]}
assert first_offer(find_product(graph)).get('price') == '5'

# 3. Payment logos as inline SVG ids, not <img>; a PayPal script must NOT count
svg = '<svg><symbol id="icon-visa"></symbol></svg>'
assert features(doc({}, svg), 'u')['payment_logos'] is True
only_script = '<script>var s="https://www.paypal.com/sdk/js"</script>'
assert features(doc({}, only_script), 'u')['payment_logos'] is False
assert features(doc({}, '<p class="advisable">x</p>'), 'u')['payment_logos'] is False
assert features(doc({}, '<svg><title>Visa</title></svg>'), 'u')['payment_logos'] is True
w = features(doc({}, '<shop-pay-wallet-button></shop-pay-wallet-button>'), 'u')
assert w['wallet_buttons'] is True and w['payment_logos'] is False

# 4. Add to cart found through the Shopify cart form even when the button has no text
form = '<form action="/cart/add" method="post"><button type="submit">+</button></form>'
g = features(doc({}, form), 'u')
assert g['cta_found'] is True and g['cta_text'] is False and g['returns_near_cta'] is False

# 5. Platform detection: the word wp-content alone is no longer WooCommerce
assert platform_of('<link href="/wp-content/themes/x/style.css">') == 'other'
assert platform_of('<body class="woocommerce-page">') == 'woocommerce'
assert platform_of('<script src="https://cdn.shopify.com/s/x.js">') == 'shopify'

# 6. Link extraction for discovery: store kept, social and own host dropped
html = ('<a href="https://www.allbirds.com/?utm=1">a</a><a href="https://twitter.com/x">t</a>'
        '<a href="https://blog.example.com/p">own</a><a href="https://shop.brand.fr/">b</a>'
        '<a href="http://127.0.0.1/x">ip</a>')
assert candidates(html, 'blog.example.com') == ['allbirds.com', 'shop.brand.fr'], candidates(html, 'blog.example.com')

# 7. Tranco rows: cursor, skip list, junk lines
from discover_tranco import parse_rows  # noqa: E402
rows = "1,google.com\n2,somestore.com\n3,site.gov\nbad line\n4,other.fr\n5,third.com\n"
doms, nxt = parse_rows(rows, 1, 3)
assert doms == ['somestore.com', 'other.fr', 'third.com'] and nxt == 6, (doms, nxt)
doms2, nxt2 = parse_rows(rows, 4, 5)
assert doms2 == ['other.fr', 'third.com'] and nxt2 == 6, (doms2, nxt2)

# 8. Relative sitemap path in robots.txt (this crashed the first Tranco run), and error isolation
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import crawl


class R(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        h = self.headers.get('Host', '')
        if self.path == '/robots.txt':
            body, ct = 'User-agent: *\nSitemap: /sitemap.xml\n', 'text/plain'
        elif self.path == '/sitemap.xml':
            body, ct = ('<urlset>' + ''.join(f'<url><loc>http://{h}/products/p{i}</loc></url>' for i in range(3))
                        + '</urlset>'), 'text/xml'
        elif self.path.startswith('/products/p'):
            body, ct = doc({'@type': 'Product', 'offers': {'price': '9'}}), 'text/html'
        else:
            self.send_response(404)
            self.end_headers()
            return
        data = body.encode()
        self.send_response(200)
        self.send_header('Content-Type', ct)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


for k in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy'):
    os.environ.pop(k, None)
srv = ThreadingHTTPServer(('127.0.0.1', 0), R)
threading.Thread(target=srv.serve_forever, daemon=True).start()
dom = f'127.0.0.1:{srv.server_address[1]}'
rec, pages = crawl.safe_crawl(dom, 'http', 0.05, __import__('time').time() + 60)
assert rec['status'] == 'ok' and len([x for x in pages if x['ok']]) == 3, (rec, pages)
assert crawl.get('/sitemap.xml') == (0, '', '')


def boom(*a, **k):
    raise ValueError('boom')


real_crawl = crawl.crawl_domain
crawl.crawl_domain = boom
rec2, pages2 = crawl.safe_crawl('x.test', 'https', 0.05, 0)
assert rec2['status'] == 'error' and pages2 == [], rec2

# 9. Per-platform statistics: two platforms with enough stores get their own column,
#    a small one does not, and shares are computed inside each platform
import aggregate


def fake_pages(domain, platform, rating):
    return [{'domain': domain, 'url': f'https://{domain}/products/{i}', 'ok': True, 'v': 3, 'platform': platform,
             'rating': rating, 'cta_text': True, 'returns_near_cta': rating, 'imgs': 10, 'scripts': 5, 'bytes': 1000}
            for i in range(3)]


pages = []
for i in range(20):
    pages += fake_pages(f'a{i}.test', 'shopify', True)
for i in range(20):
    pages += fake_pages(f'b{i}.test', 'magento', False)
for i in range(3):
    pages += fake_pages(f'c{i}.test', 'wix', True)
st = aggregate.build(pages)
assert st['stores'] == 43 and set(st['by_platform']) == {'shopify', 'magento'}, st['by_platform'].keys()
assert st['by_platform']['shopify']['features']['rating']['pct'] == 100.0
assert st['by_platform']['magento']['features']['rating']['pct'] == 0.0
md = aggregate.to_markdown(st)
assert 'shopify (20)' in md and 'magento (20)' in md and 'wix' not in md.split('Platforms')[0]

# 10. www fallback when the bare domain does not answer at all
calls = []
real_get = crawl.get


def fake_get(url):
    calls.append(url)
    if url.startswith('https://www.only-www.test'):
        return (200, 'text/plain', 'User-agent: *\nDisallow: /nothing\n') if url.endswith('robots.txt') else (404, '', '')
    return 0, '', ''


crawl.get = fake_get
rec3, _ = real_crawl(domain := 'only-www.test', 'https', 0.0, __import__('time').time() + 30)
crawl.get = real_get
assert any(c.startswith('https://www.only-www.test/') for c in calls), calls
assert rec3['status'] != 'unreachable', rec3

# 11. queue size counts only domains still waiting
import tempfile
import discover_tranco
with tempfile.TemporaryDirectory() as d:
    open(os.path.join(d, 'seeds_discovered.txt'), 'w').write('a.com\nb.com\nc.com\n')
    open(os.path.join(d, 'domains.jsonl'), 'w').write(json.dumps({'domain': 'a.com'}) + '\n')
    assert discover_tranco.queue_size(d) == 2

# 12. Reference stores: read first, deeper, flagged, extra URLs honoured; stats show them next to the sample
rec4, pages4 = real_crawl(dom, 'http', 0.0, __import__('time').time() + 60, True, [f'http://{dom}/products/p1'])
assert rec4['ref'] is True and len([x for x in pages4 if x['ok']]) == 3 and all(x['ref'] for x in pages4), (rec4, pages4)
refs_found, ref_urls = crawl.load_references(os.path.dirname(os.path.abspath(__file__)))
assert 'helloboku.com' in refs_found and 'arntreal.com' in refs_found
assert ref_urls['helloboku.com'] == ['https://www.helloboku.com/products/bidet-boku'], ref_urls
assert crawl.host_key('https://www.Example.com/x?gclid=1') == 'example.com'
pages_r = []
for i in range(20):
    pages_r += fake_pages(f'a{i}.test', 'shopify', i % 2 == 0)
pages_r += fake_pages('refstore.test', 'shopify', True)
st2 = aggregate.build(pages_r, refs=['refstore.test', 'absent.test'], domain_status={'absent.test': 'blocked'})
assert list(st2['references']) == ['refstore.test'] and st2['references']['refstore.test']['practices']['rating'] is True
assert st2['references_not_measured'] == {'absent.test': 'blocked'}
md2 = aggregate.to_markdown(st2)
assert 'Reference stores' in md2 and 'refstore.test' in md2 and 'Not measured yet: absent.test (blocked)' in md2
print('UNIT TESTS PASSED')
