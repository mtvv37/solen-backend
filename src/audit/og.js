'use strict';
// Share image (1200x630 PNG) for a report: satori (layout -> SVG) then resvg (SVG -> PNG).
// Inter is used for the text; the Solen wordmark comes from the outlined brand SVG.
const fs = require('fs');
const path = require('path');
const satori = require('satori').default || require('satori');
const { Resvg } = require('@resvg/resvg-js');

let fontsCache = null;
function fonts() {
  if (!fontsCache) {
    // Literal paths so Vercel's file tracer bundles exactly these three files.
    const files = {
      400: require.resolve('@fontsource/inter/files/inter-latin-400-normal.woff'),
      600: require.resolve('@fontsource/inter/files/inter-latin-600-normal.woff'),
      700: require.resolve('@fontsource/inter/files/inter-latin-700-normal.woff'),
    };
    const load = (w) => fs.readFileSync(files[w]);
    fontsCache = [
      { name: 'Inter', data: load(400), weight: 400, style: 'normal' },
      { name: 'Inter', data: load(600), weight: 600, style: 'normal' },
      { name: 'Inter', data: load(700), weight: 700, style: 'normal' },
    ];
  }
  return fontsCache;
}

let lockupCache = null;
function lockup() {
  if (!lockupCache) {
    const svg = fs.readFileSync(path.join(__dirname, '..', '..', 'public', 'audit', 'lockup-dark.svg'));
    lockupCache = `data:image/svg+xml;base64,${svg.toString('base64')}`;
  }
  return lockupCache;
}

const h = (type, style, children) => ({ type, props: { style, children } });

function scoreColor(score) {
  if (score >= 75) return '#7BC88F';
  if (score >= 50) return '#F5A524';
  return '#F07A5F';
}

async function renderOgImage({ domain, score, leakCount }) {
  const tree = h('div', {
    width: '100%', height: '100%', boxSizing: 'border-box', display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
    background: '#0E1726', color: '#F6F5F1', padding: '64px 72px', fontFamily: 'Inter',
  }, [
    { type: 'img', props: { src: lockup(), width: 210, height: 72 } },
    h('div', { display: 'flex', alignItems: 'flex-end', gap: 48 }, [
      h('div', { display: 'flex', alignItems: 'baseline' }, [
        h('div', { fontSize: 180, fontWeight: 700, lineHeight: 0.9, color: scoreColor(score), letterSpacing: '-0.04em' }, String(score)),
        h('div', { fontSize: 56, fontWeight: 600, color: '#8A8F98', marginLeft: 12 }, '/100'),
      ]),
      h('div', { display: 'flex', flexDirection: 'column', marginBottom: 24, maxWidth: 560 }, [
        h('div', { fontSize: 26, fontWeight: 600, color: '#F5A524', letterSpacing: '0.06em', textTransform: 'uppercase' }, 'Audit de conversion'),
        h('div', { fontSize: 44, fontWeight: 600, marginTop: 10, lineHeight: 1.15 }, domain.length > 28 ? `${domain.slice(0, 27)}…` : domain),
        h('div', { fontSize: 28, color: '#8A8F98', marginTop: 14 }, `${leakCount} fuite${leakCount > 1 ? 's' : ''} de conversion détectée${leakCount > 1 ? 's' : ''}`),
      ]),
    ]),
  ]);
  const svg = await satori(tree, { width: 1200, height: 630, fonts: fonts() });
  return new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
}

module.exports = { renderOgImage };
