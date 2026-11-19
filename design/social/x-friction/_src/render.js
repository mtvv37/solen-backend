// Rendu PNG des pages HTML (Playwright). Usage : node render.js <largeur> <hauteur> <page.html>...
// Le PNG est écrit dans le dossier parent, sous le même nom. Signale tout débordement.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [w, h, ...files] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  for (const f of files) {
    await page.goto('file://' + path.resolve(f));
    await page.evaluate(() => document.fonts.ready);
    const issues = await page.evaluate(() => {
      const out = [];
      const s = document.querySelector('.screen');
      if (s && s.scrollHeight > s.clientHeight + 1) out.push(`écran déborde de ${s.scrollHeight - s.clientHeight}px`);
      const h1 = document.querySelector('h1'), sub = document.querySelector('.sub'), note = document.querySelector('.note');
      if (sub && note && sub.getBoundingClientRect().bottom > note.getBoundingClientRect().top - 8) out.push('le titre touche la note');
      if (h1 && h1.getBoundingClientRect().right > 1140) out.push('titre trop large');
      return out;
    });
    const out = path.join(path.dirname(path.resolve(f)), '..', path.basename(f).replace(/\.html$/, '.png'));
    await page.locator('#c').screenshot({ path: out });
    console.log(path.basename(out), issues.length ? 'PROBLÈME: ' + issues.join(', ') : 'ok');
  }
  await browser.close();
})();
