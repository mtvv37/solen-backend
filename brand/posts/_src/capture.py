"""Capture the 3 public pages where a friction was verified (see probe_pages.py), mask the brand, save to brand/posts/_captures/.
Mask = Gaussian blur on logo / store name, product photos and cart item images. No personal data entered."""
import json, os
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_captures")
os.makedirs(OUT, exist_ok=True)
VP, DPR = dict(width=390, height=844), 2
UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
      "Version/17.0 Mobile/15E148 Safari/604.1")
MASK_SEL = ["header .header__heading", "header .header__heading-logo", "header a[href='/'] img", "header [class*='logo']",
            ".product__media img", ".product-media-container img", "product-media img", ".product__media-list img",
            ".cart-item__image", ".cart-item__media img", "footer .footer__content-bottom-wrapper .footer__copyright",
            "footer [class*='copyright']", "main img", "footer img", "footer svg", "footer a[href='/']",
            "footer [class*='logo']", "[class*='card__media']"]

BOXES_JS = """(sels) => {
  const out = [];
  for (const s of sels) for (const el of document.querySelectorAll(s)) {
    const r = el.getBoundingClientRect();
    if (r.width > 4 && r.height > 4 && r.bottom > 0 && r.top < window.innerHeight) out.push([r.left, r.top, r.width, r.height]);
  }
  return out;
}"""

TEXT_BOX_JS = """(re) => {
  const rx = new RegExp(re, 'i');
  let best = null;
  for (const el of document.querySelectorAll('main *, footer *')) {
    const t = (el.innerText || '').trim();
    if (!t || !rx.test(t)) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) continue;
    if (!best || t.length < best.len) best = {el, len: t.length};
  }
  if (!best) return null;
  best.el.scrollIntoView({block: 'center'});
  const r = best.el.getBoundingClientRect();
  return [r.left, r.top, r.width, r.height];
}"""


def mask(png, boxes):
    im = Image.open(png).convert("RGB")
    for x, y, w, h in boxes:
        x0, y0 = max(0, int(x * DPR)), max(0, int(y * DPR))
        x1, y1 = min(im.width, int((x + w) * DPR)), min(im.height, int((y + h) * DPR))
        if x1 > x0 and y1 > y0:
            region = im.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(22))
            im.paste(region, (x0, y0))
    im.save(png)


meta = {}
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    ctx = b.new_context(viewport=VP, device_scale_factor=DPR, is_mobile=True, has_touch=True, user_agent=UA)

    # 1 · CTA below the fold: first screen of a product page
    pg = ctx.new_page()
    pg.goto("https://theme-taste-demo.myshopify.com/products/gatsby", wait_until="networkidle", timeout=60000)
    cta = pg.evaluate("""() => { const b = document.querySelector('form[action*="/cart/add"] button[type="submit"], button[name="add"]');
                                 return Math.round(b.getBoundingClientRect().top + window.scrollY); }""")
    f = os.path.join(OUT, "audit-01-cta-below-fold.png")
    pg.screenshot(path=f)
    mask(f, pg.evaluate(BOXES_JS, MASK_SEL))
    meta["01"] = dict(file=f, box=[6, 806, 378, 34], cta_top=cta, note=f"Add-to-cart starts at {cta}px; the first screen ends at 844px.")
    pg.close()

    # 2 · Shipping only at checkout: cart page note
    pg = ctx.new_page()
    pg.goto("https://theme-craft-demo.myshopify.com/products/ceramic-carafe", wait_until="networkidle", timeout=60000)
    pg.click('form[action*="/cart/add"] button[type="submit"], button[name="add"]')
    pg.wait_for_timeout(1500)
    pg.goto("https://theme-craft-demo.myshopify.com/cart", wait_until="networkidle", timeout=60000)
    box = pg.evaluate(TEXT_BOX_JS, "shipping calculated at check")
    pg.wait_for_timeout(400)
    box = pg.evaluate(TEXT_BOX_JS, "shipping calculated at check")
    f = os.path.join(OUT, "audit-02-shipping-at-checkout.png")
    pg.screenshot(path=f)
    mask(f, pg.evaluate(BOXES_JS, MASK_SEL))
    meta["02"] = dict(file=f, box=[box[0] - 6, box[1] - 6, box[2] + 12, box[3] + 12])
    pg.close()

    # 5 · Return policy only in the footer
    pg = ctx.new_page()
    pg.goto("https://theme-refresh-demo.myshopify.com/products/shampoo-2", wait_until="networkidle", timeout=60000)
    box = pg.evaluate(TEXT_BOX_JS, "refund|return")
    pg.wait_for_timeout(400)
    box = pg.evaluate(TEXT_BOX_JS, "refund|return")
    f = os.path.join(OUT, "audit-05-returns-in-footer.png")
    pg.screenshot(path=f)
    mask(f, pg.evaluate(BOXES_JS, MASK_SEL))
    meta["05"] = dict(file=f, box=[box[0] - 6, box[1] - 6, box[2] + 12, box[3] + 12])
    pg.close()
    b.close()

json.dump(meta, open(os.path.join(OUT, "captures.json"), "w"), indent=1)
print(json.dumps(meta, indent=1))
