"""Probe public Shopify theme-demo product pages on a mobile viewport and report which frictions are really present.
No personal data is entered; pages are read-only except adding one item to a cart to read the cart page."""
import json, sys
from playwright.sync_api import sync_playwright

STORES = {
    "theme-dawn-demo": ["puff-olive-leaf", "studio-denim"],
    "theme-sense-demo": ["natural-bamboo-hairbrush-ecofriendly", "10-free-nontoxic-nailpolish-frenchpink"],
    "theme-craft-demo": ["ceramic-carafe", "flatware-set-polished-silver"],
    "theme-refresh-demo": ["shampoo-2"],
    "theme-studio-demo": ["willow"],
    "theme-taste-demo": ["gatsby"],
}
VP = dict(width=390, height=844)

JS = """() => {
  const q = s => document.querySelector(s);
  const add = q('form[action*="/cart/add"] button[type="submit"], button[name="add"]');
  const r = add ? add.getBoundingClientRect() : null;
  const selects = document.querySelectorAll('form[action*="/cart/add"] select, variant-selects select, .product-form__input select');
  const main = (q('main') || document.body).innerText.toLowerCase();
  const footer = (q('footer') || {innerText: ''}).innerText.toLowerCase();
  const productInfo = (q('.product__info-container, .product__info-wrapper, product-info, .product-single__meta') || {innerText: ''}).innerText.toLowerCase();
  return {
    cta_top: r ? Math.round(r.top + window.scrollY) : null,
    variant_selects: selects.length,
    return_in_product_info: /return|refund/.test(productInfo),
    refund_in_footer: /refund|return/.test(footer),
    shipping_note_in_product: /shipping calculated at checkout|shipping/.test(productInfo),
    reviews_widget: !!q('[class*="review"], [id*="review"]'),
  };
}"""

out = {}
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(viewport=VP, device_scale_factor=2, is_mobile=True, has_touch=True,
                        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
    for store, handles in STORES.items():
        for h in handles:
            url = f"https://{store}.myshopify.com/products/{h}"
            pg = ctx.new_page()
            try:
                pg.goto(url, wait_until="networkidle", timeout=45000)
                m = pg.evaluate(JS)
                m["cta_below_fold"] = m["cta_top"] is not None and m["cta_top"] > VP["height"]
                # cart page text (add one item, read /cart)
                try:
                    pg.click('form[action*="/cart/add"] button[type="submit"], button[name="add"]', timeout=5000)
                    pg.wait_for_timeout(1500)
                    pg.goto(f"https://{store}.myshopify.com/cart", wait_until="networkidle", timeout=30000)
                    t = pg.inner_text("main").lower()
                    m["cart_shipping_at_checkout"] = "shipping calculated at checkout" in t or "shipping calculated at check" in t
                except Exception as e:
                    m["cart_shipping_at_checkout"] = f"err {type(e).__name__}"
                out[url] = m
            except Exception as e:
                out[url] = {"error": str(e)[:120]}
            pg.close()
    b.close()
print(json.dumps(out, indent=1))
