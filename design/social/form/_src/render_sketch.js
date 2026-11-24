// Rend les deux schémas en PNG (2400 x 1600, net sur mobile). Usage : node render_sketch.js <dossier node_modules>
// Dépendances : npm i roughjs@4.6.6 @fontsource/caveat@5.0.8 (dans le dossier passé en argument).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const nm = path.resolve(process.argv[2]);
  const src = fs.readFileSync(path.join(__dirname, 'sketch.html'), 'utf8')
    .replace('ROUGH_URL', 'file://' + path.join(nm, 'roughjs/bundled/rough.js'))
    .replace('FONT_URL', 'file://' + path.join(nm, '@fontsource/caveat/files/caveat-latin-600-normal.woff2'));
  const tmp = path.join(nm, '..', 'sketch.built.html');
  fs.writeFileSync(tmp, src);
  const b = await chromium.launch();
  const SIZES = { without: [1200, 800], with: [1200, 800], compare: [1400, 1100] };
  for (const scene of Object.keys(SIZES)) {
    const [w, h] = SIZES[scene];
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await p.goto('file://' + tmp + '#' + scene);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(200);
    const out = path.join(__dirname, '..', scene === 'compare' ? 'with-vs-without-solen.png' : `${scene}-solen.png`);
    await p.locator('#c').screenshot({ path: out });
    console.log(out);
    await p.close();
  }
  await b.close();
})();
