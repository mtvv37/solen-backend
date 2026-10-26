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
print('UNIT TESTS PASSED')
