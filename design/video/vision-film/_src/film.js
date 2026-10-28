// Solen product vision film: every frame is a pure function of time t (seconds).
const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const p = (t, a, b) => cl((t - a) / (b - a));
const eo = x => 1 - Math.pow(1 - cl(x), 3);
const eio = x => { x = cl(x); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
const back = x => { x = cl(x); const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
const lerp = (a, b, x) => a + (b - a) * x;
let seed = 11; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
const stage = document.getElementById('stage');
function el(tag, css, html, parent) {
  const e = document.createElement(tag);
  if (css) e.style.cssText = css;
  if (html != null) e.innerHTML = html;
  (parent || stage).appendChild(e);
  return e;
}
const G1 = '#7EF0A5', G2 = '#2BD07A', TXT = '#EEF5F0', MUT = '#9DB5A5', RED = '#FF5A5A';
const LOGO_PATHS = [
  'M17.47 0.00 L55.47 0.00 L45.47 11.00 L13.47 11.00 Z',
  'M65.47 0.00 L51.64 38.00 L42.82 32.00 L54.47 0.00 Z',
  'M48.00 48.00 L10.00 48.00 L20.00 37.00 L52.00 37.00 Z',
  'M0.00 48.00 L13.83 10.00 L22.65 16.00 L11.00 48.00 Z'];
const logoSvg = (w, fill = '#fff') => `<svg width="${w}" height="${w * 48 / 65.47}" viewBox="0 0 65.47 48"><g fill="${fill}">${LOGO_PATHS.map(d => `<path d="${d}"/>`).join('')}</g></svg>`;
const GLOW_DEFS = `<defs><filter id="glw" filterUnits="userSpaceOnUse" x="-200" y="-200" width="2400" height="1500"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1F9D5C" stop-opacity="0.25"/><stop offset="0.5" stop-color="#7EF0A5" stop-opacity="0.95"/><stop offset="1" stop-color="#1F9D5C" stop-opacity="0.25"/></linearGradient></defs>`;
const BG = 'radial-gradient(ellipse 75% 70% at 50% 50%, #0C2416 0%, #040A06 72%)';

function caption(root, text, bottom = 96) {
  return el('div', `position:absolute;left:0;right:0;bottom:${bottom}px;text-align:center;font:600 46px 'Inter Tight';letter-spacing:-0.02em;color:${TXT};opacity:0`, text, root);
}
function showIn(e, t, a, dur = 0.5, dy = 24) {
  const x = eo(p(t, a, a + dur)); e.style.opacity = x; e.style.transform = `translateY(${(1 - x) * dy}px)`; return x;
}
function stepLabel(root, text) {
  return el('div', `position:absolute;left:110px;top:90px;font:600 26px 'JetBrains Mono';color:${G1};letter-spacing:0.14em;opacity:0`, text, root);
}
// generic product page mockup
function pageMock(parent, css, o = {}) {
  const hue = o.hue || '#E9C9A0';
  const m = el('div', `position:absolute;background:#FBFAF7;border-radius:${o.r || 18}px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45);${css}`, '', parent);
  el('div', `position:absolute;left:0;right:0;top:0;height:52%;background:linear-gradient(140deg,${hue},#8C6A4A)`, '', m);
  el('div', 'position:absolute;left:30%;top:14%;width:40%;height:28%;border-radius:50%;background:rgba(255,255,255,.35);filter:blur(2px)', '', m);
  const body = el('div', 'position:absolute;left:8%;right:8%;top:56%;bottom:6%', '', m);
  if (o.title) el('div', `font:700 ${o.ts || 20}px 'Inter Tight';color:#16201A;letter-spacing:-0.02em;line-height:1.1`, o.title, body);
  else { el('div', 'height:9%;width:80%;background:#1c2620;border-radius:4px', '', body); }
  el('div', 'height:5%;width:55%;background:#c9cfca;border-radius:3px;margin-top:6%', '', body);
  el('div', 'height:5%;width:35%;background:#16201A;border-radius:3px;margin-top:5%', '', body);
  const btn = el('div', `margin-top:8%;height:16%;border-radius:999px;background:${o.btn || '#16201A'};display:flex;align-items:center;justify-content:center;color:#fff;font:600 ${o.bs || 13}px 'Inter Tight'`, o.btnText || '', body);
  m._body = body; m._btn = btn;
  return m;
}

const scenes = [];
function scene(dur, fade, build, draw) { scenes.push({ dur, fade, build, draw }); }

// ---------- placeholder for realistic AI shots ----------
function realistic(dur, n, desc) {
  scene(dur, [0.15, 0.15], r => {
    r.style.background = '#0b0d10';
    el('div', 'position:absolute;inset:0;background:repeating-linear-gradient(45deg,#0e1115 0 26px,#0b0d10 26px 52px)', '', r);
    el('div', `position:absolute;left:0;right:0;top:410px;text-align:center;font:600 28px 'JetBrains Mono';color:#6F8A78;letter-spacing:.14em`, `PLAN RÉALISTE ${n} · À GÉNÉRER`, r);
    el('div', `position:absolute;left:280px;right:280px;top:470px;text-align:center;font:500 42px 'Inter Tight';color:#C9D6CD;line-height:1.3`, desc, r);
  }, () => {});
}

// ---------- 1. Instagram feed on the phone ----------
scene(4.6, [0.2, 0.15], r => {
  r.style.background = 'radial-gradient(ellipse 55% 70% at 50% 45%, #16202c 0%, #05070a 72%)';
  r._glow = el('div', 'position:absolute;left:560px;top:40px;width:800px;height:1000px;background:radial-gradient(closest-side,rgba(140,170,255,.22),rgba(140,170,255,0))', '', r);
  const ph = el('div', 'position:absolute;left:725px;top:60px;width:470px;height:960px;border-radius:62px;background:#0a0a0a;box-shadow:0 0 0 3px #2b2b2b,0 50px 140px rgba(0,0,0,.7)', '', r);
  r._ph = ph;
  const scr = el('div', 'position:absolute;left:12px;top:12px;right:12px;bottom:12px;border-radius:50px;overflow:hidden;background:#000', '', ph);
  const feed = el('div', 'position:absolute;left:0;top:0;width:100%', '', scr); r._feed = feed;
  const SH = 936; r._sh = SH;
  const reels = [
    ['#ff7a59', '#7a2cff', '@jay.builds', '$41,280 in 30 days.<br>One product.', '48.2K'],
    ['#00c2a8', '#0052d4', '@ecomwithmia', 'Quit my 9–5<br>with one store', '112K'],
    ['#f7b733', '#fc4a1a', '@leo.dtc', 'Day 47: $12k today.<br>Not joking.', '9,804'],
    ['#ee0979', '#ff6a00', '@nora.sells', 'POV: your phone<br>won\'t stop buzzing', '231K'],
    ['#43cea2', '#185a9d', '@thestorekid', 'Passive income<br>is real.', '77.1K']];
  r._notifs = [];
  reels.forEach((d, i) => {
    const rc = el('div', `position:absolute;left:0;top:${i * SH}px;width:100%;height:${SH}px;background:linear-gradient(160deg,${d[0]},${d[1]});overflow:hidden`, '', feed);
    el('div', 'position:absolute;left:-60px;top:120px;width:320px;height:320px;border-radius:50%;background:rgba(255,255,255,.28);filter:blur(30px)', '', rc);
    el('div', 'position:absolute;right:-80px;top:380px;width:360px;height:360px;border-radius:50%;background:rgba(0,0,0,.25);filter:blur(40px)', '', rc);
    el('div', 'position:absolute;left:0;right:0;bottom:0;height:55%;background:linear-gradient(0deg,rgba(0,0,0,.65),rgba(0,0,0,0))', '', rc);
    el('div', `position:absolute;left:26px;top:58px;font:700 26px 'Inter Tight';color:#fff`, 'Reels', rc);
    el('div', `position:absolute;left:26px;right:90px;bottom:170px;font:800 46px 'Inter Tight';letter-spacing:-0.03em;line-height:1.05;color:#fff;text-shadow:0 4px 20px rgba(0,0,0,.4)`, d[3], rc);
    el('div', `position:absolute;left:26px;bottom:110px;display:flex;align-items:center;gap:12px;font:600 22px 'Inter Tight';color:#fff`, `<span style="width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.85);display:inline-block"></span>${d[2]}`, rc);
    [0, 1, 2].forEach(k => el('div', `position:absolute;right:22px;bottom:${330 - k * 96}px;width:48px;text-align:center;font:600 16px 'Inter Tight';color:#fff`, `<div style="width:44px;height:44px;margin:0 auto 6px;border-radius:50%;border:3px solid #fff"></div>${k === 0 ? d[4] : k === 1 ? '1,204' : 'Share'}`, rc));
    if (i === 3) {
      [['$64.00', '2 items'], ['$129.00', '1 item'], ['$38.50', '1 item'], ['$212.00', '3 items']].forEach((n, k) => {
        const nb = el('div', `position:absolute;left:18px;right:18px;top:120px;height:96px;border-radius:24px;background:rgba(245,245,245,.94);display:flex;align-items:center;gap:16px;padding:0 20px;box-sizing:border-box;box-shadow:0 10px 30px rgba(0,0,0,.25);opacity:0`,
          `<div style="width:56px;height:56px;border-radius:14px;background:#1f9d5c;flex:none"></div><div style="flex:1"><div style="font:700 22px 'Inter Tight';color:#111">New order</div><div style="font:500 20px 'Inter Tight';color:#444">${n[0]} · ${n[1]}</div></div><div style="font:500 17px 'Inter Tight';color:#777">now</div>`, rc);
        r._notifs.push(nb);
      });
    }
  });
}, (t, d, r) => {
  const flicks = [0.55, 1.2, 1.8];
  let s = 0; flicks.forEach(f => s += eio(p(t, f, f + 0.38)));
  r._feed.style.transform = `translateY(${-s * r._sh}px)`;
  r._notifs.forEach((nb, k) => {
    const a = 2.25 + k * 0.42; const x = back(p(t, a, a + 0.35));
    const after = r._notifs.length - 1 - k; // newer ones push older ones down
    let push = 0; for (let j = k + 1; j < r._notifs.length; j++) push += eo(p(t, 2.25 + j * 0.42, 2.25 + j * 0.42 + 0.3)) * 104;
    nb.style.opacity = cl(x * 1.2); nb.style.transform = `translateY(${(1 - x) * -60 + push}px) scale(${lerp(0.9, 1, cl(x))})`;
  });
  r._ph.style.transform = `scale(${lerp(1, 1.09, eio(p(t, 0, d)))}) rotate(${lerp(-2.5, 0, eio(p(t, 0, d)))}deg)`;
});

// ---------- 2. His own dashboard + echoes ----------
scene(6.2, [0.2, 0.7], r => {
  r.style.background = '#000';
  const scr = el('div', 'position:absolute;inset:0;background:#F3F4F6;transform-origin:1335px 300px', '', r); r._scr = scr;
  el('div', 'position:absolute;left:0;top:0;bottom:0;width:270px;background:#1E1F21', ['Home', 'Orders', 'Products', 'Customers', 'Analytics', 'Marketing', 'Discounts'].map((x, i) => `<div style="margin:${i ? 10 : 110}px 20px 0;padding:14px 18px;border-radius:12px;font:600 23px 'Inter Tight';color:${i === 4 ? '#fff' : '#a9adb3'};background:${i === 4 ? '#3a3b3e' : 'transparent'}">${x}</div>`).join(''), scr);
  el('div', `position:absolute;left:270px;right:0;top:0;height:78px;background:#fff;border-bottom:1px solid #e3e5e8;display:flex;align-items:center;padding:0 40px;font:700 24px 'Inter Tight';color:#222`, 'Jay\'s Store<div style="margin-left:60px;width:520px;height:42px;border-radius:12px;background:#f1f2f4"></div>', scr);
  el('div', `position:absolute;left:330px;top:120px;font:700 46px 'Inter Tight';letter-spacing:-0.02em;color:#111`, 'Analytics', scr);
  el('div', `position:absolute;left:332px;top:182px;font:500 22px 'Inter Tight';color:#6b7178`, 'Today · compared to yesterday', scr);
  const kp = [['Sessions', '2,481', '+12%', '#1a7f4b'], ['Orders', '3', '−1', '#b42318'], ['Conversion rate', '0.12%', '−0.04 pts', '#b42318'], ['Total sales', '$187.00', '−22%', '#b42318']];
  r._kv = [];
  kp.forEach((k, i) => {
    const c = el('div', `position:absolute;left:${330 + i * 385}px;top:232px;width:355px;height:175px;border-radius:18px;background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.06);padding:26px 28px;box-sizing:border-box`, `<div style="font:600 22px 'Inter Tight';color:#6b7178">${k[0]}</div>`, scr);
    const v = el('div', `margin-top:14px;font:800 56px 'Inter Tight';letter-spacing:-0.03em;color:#111`, k[1], c);
    el('div', `margin-top:6px;font:600 20px 'Inter Tight';color:${k[3]}`, k[2], c);
    r._kv.push(v); if (i === 2) r._conv = c;
  });
  const ch = el('div', 'position:absolute;left:330px;top:440px;width:1510px;height:540px;border-radius:18px;background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.06)', `<div style="position:absolute;left:30px;top:24px;font:600 22px 'Inter Tight';color:#6b7178">Sessions vs orders · last 30 days</div>`, scr);
  let sp = 'M40 400', op = 'M40 470';
  for (let i = 1; i <= 30; i++) { const x = 40 + i * 47; sp += ` L${x} ${400 - 60 * Math.sin(i * 1.3) - i * 7 - 40 * rnd()}`; op += ` L${x} ${470 - (i % 9 === 0 ? 14 : 2 * rnd())}`; }
  el('div', 'position:absolute;inset:0', `<svg width="1510" height="540"><path d="${sp}" fill="none" stroke="#7a9cc6" stroke-width="4"/><path d="${op}" fill="none" stroke="#d64545" stroke-width="4"/></svg>`, ch);
  r._vig = el('div', 'position:absolute;inset:0;background:radial-gradient(ellipse 60% 55% at 50% 45%,rgba(0,0,0,0) 30%,rgba(0,0,0,.85) 100%);opacity:0', '', r);
  r._ech = [['“So… how\'s your Shopify going?”', 150, 600, 0.7], ['“I\'m gonna launch my own brand.”', 860, 780, 2.0], ['“It\'s passive income, bro.”', 420, 160, 3.3]].map(e => {
    const w = el('div', `position:absolute;left:${e[1]}px;top:${e[2]}px;opacity:0`, '', r);
    [[-16, -6, .22, 6], [16, 8, .22, 6], [0, 0, 1, 0]].forEach(g => el('div', `position:absolute;left:${g[0]}px;top:${g[1]}px;white-space:nowrap;font:italic 600 56px 'Inter Tight';letter-spacing:-0.02em;color:#fff;opacity:${g[2]};filter:blur(${g[3]}px);text-shadow:0 4px 30px rgba(0,0,0,.8)`, e[0], w));
    w._t = e[3]; return w;
  });
}, (t, d, r) => {
  const z = eio(p(t, 0.8, 5.4));
  r._scr.style.transform = `scale(${lerp(1, 2.05, z)})`;
  r._scr.style.filter = `grayscale(${p(t, 4.6, 6)}) brightness(${lerp(1, 0.38, p(t, 0.8, 4))})`;
  const red = p(t, 1.6, 2.4);
  r._kv[2].style.color = `rgb(${Math.round(lerp(17, 210, red))},${Math.round(lerp(17, 40, red))},${Math.round(lerp(17, 40, red))})`;
  r._kv[2].style.transform = `scale(${1 + 0.05 * red * Math.max(0, Math.sin(t * 7))})`;
  r._kv[2].style.transformOrigin = 'left center';
  r._vig.style.opacity = p(t, 0.4, 2.0);
  r._ech.forEach(w => {
    const a = w._t, x = eo(p(t, a, a + 0.6)), out = p(t, a + 1.6, a + 2.4);
    w.style.opacity = x * lerp(1, 0.28, out);
    w.style.filter = `blur(${(1 - x) * 14 + out * 3}px)`;
    w.style.transform = `scale(${lerp(1.08, 1, x)})`;
  });
});


// ---------- 3. Solen arrives ----------
scene(4.8, [0.05, 0.25], r => {
  r.style.background = '#020503';
  r._bg = el('div', 'position:absolute;inset:0;background:radial-gradient(ellipse 50% 45% at 50% 46%,rgba(43,208,122,.22),rgba(0,0,0,0) 70%);opacity:0', '', r);
  el('div', 'position:absolute;inset:0', `<svg width="1920" height="1080">${GLOW_DEFS}<path id="sl" d="M-60 470 C 400 380 700 560 960 470 S 1500 380 1980 470" fill="none" stroke="url(#ln)" stroke-width="3" filter="url(#glw)" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>`, r);
  r._line = r.querySelector('#sl');
  const lg = el('div', 'position:absolute;left:830px;top:375px;width:260px;height:190px', `<svg width="260" height="190.6" viewBox="0 0 65.47 48" style="overflow:visible">${LOGO_PATHS.map((d, i) => `<path id="lp${i}" d="${d}" fill="#fff"/>`).join('')}</svg>`, r);
  r._lg = lg; r._lp = [0, 1, 2, 3].map(i => r.querySelector('#lp' + i));
  r._wm = el('div', `position:absolute;left:0;right:0;top:600px;text-align:center;font-family:'Archivo';font-stretch:125%;font-weight:800;font-size:110px;color:#fff;opacity:0`, 'Solen', r);
  r._q = el('div', `position:absolute;right:430px;top:640px;max-width:900px;padding:26px 36px;border-radius:30px 30px 8px 30px;background:rgba(126,240,165,.12);border:1.5px solid rgba(126,240,165,.45);font:500 44px 'Inter Tight';color:${TXT};opacity:0;white-space:nowrap`, '', r);
  r._a = el('div', `position:absolute;left:430px;top:790px;padding:26px 36px;border-radius:30px 30px 30px 8px;background:#EEF5F0;font:600 44px 'Inter Tight';color:#0B3D24;opacity:0;display:flex;align-items:center;gap:18px`, `${logoSvg(46, '#0B3D24')}Let me look at your store.`, r);
}, (t, d, r) => {
  r._line.setAttribute('stroke-dashoffset', 1 - eio(p(t, 0, 1.3)));
  r._bg.style.opacity = eo(p(t, 1.4, 2.2));
  const k = eo(p(t, 0.7, 1.55)), offs = [[0, -60], [60, 0], [0, 60], [-60, 0]];
  r._lp.forEach((pa, i) => { pa.setAttribute('transform', `translate(${offs[i][0] * (1 - k)} ${offs[i][1] * (1 - k)})`); pa.style.opacity = cl(k * 1.5); });
  const flash = Math.max(0, 1 - Math.abs(t - 1.65) / 0.35);
  const up = eio(p(t, 2.3, 2.9));
  r._lg.style.filter = `drop-shadow(0 0 ${10 + flash * 50}px rgba(126,240,165,${0.4 + flash * 0.6}))`;
  r._lg.style.transform = `translateY(${-up * 230}px) scale(${lerp(1, 0.62, up)})`;
  const w = eo(p(t, 1.55, 2.2));
  r._wm.style.opacity = w; r._wm.style.letterSpacing = `${lerp(0.25, -0.01, w)}em`;
  r._wm.style.transform = `translateY(${-up * 300}px) scale(${lerp(1, 0.62, up)})`;
  const q = 'Solen, why isn\'t my store selling?';
  const n = Math.floor(q.length * p(t, 2.8, 3.7));
  r._q.style.opacity = eo(p(t, 2.7, 2.95));
  r._q.innerHTML = q.slice(0, n) + `<span style="opacity:${n < q.length || Math.floor(t * 3) % 2 ? 1 : 0};color:${G1}">|</span>`;
  showIn(r._a, t, 3.9, 0.4, 30);
});

// ---------- 4. Scan: 1,500+ product pages ----------
scene(4.6, [0.2, 0.25], r => {
  r.style.background = BG;
  const svg = el('div', 'position:absolute;inset:0', `<svg width="1920" height="1080">${GLOW_DEFS}<g id="lines" fill="none" stroke="url(#ln)" stroke-width="1.6" filter="url(#glw)"></g></svg>`, r);
  r._lines = svg.querySelector('#lines');
  r._tiles = [];
  for (let i = 0; i < 64; i++) {
    const ang = rnd() * Math.PI * 2, rad = 1 + rnd() * 0.25, z = 0.45 + rnd() * 0.75;
    const sx = 960 + Math.cos(ang) * 1400, sy = 540 + Math.sin(ang) * 900;
    const hue = ['#E9C9A0', '#C9D8E9', '#E9B8C4', '#CDE9C9', '#E2D6F0', '#F0E2B8'][i % 6];
    const tl = pageMock(r, `left:0;top:0;width:96px;height:132px`, { hue, r: 10 });
    const ln = document.createElementNS('http://www.w3.org/2000/svg', 'path'); r._lines.appendChild(ln);
    r._tiles.push({ tl, ln, ang, rad, z, sx, sy, delay: rnd() * 0.7 });
  }
  r._shade = el('div', 'position:absolute;left:360px;top:250px;width:1200px;height:600px;background:radial-gradient(closest-side,rgba(4,10,6,.97) 55%,rgba(4,10,6,0))', '', r);
  r._num = el('div', `position:absolute;left:0;right:0;top:350px;text-align:center;font:800 190px 'Inter Tight';letter-spacing:-0.05em;color:${TXT}`, '', r);
  r._lab = el('div', `position:absolute;left:0;right:0;top:585px;text-align:center;font:600 46px 'Inter Tight';color:${MUT};opacity:0`, 'product pages studied', r);
  r._cap = caption(r, 'Solen reads your store against all of them.', 330); r._cap.style.fontSize = '40px';
}, (t, d, r) => {
  r._tiles.forEach(o => {
    const k = eo(p(t, o.delay, o.delay + 1.8));
    const a = o.ang + t * 0.07;
    const ex = 960 + Math.cos(a) * 700 * o.rad, ey = 540 + Math.sin(a) * 330 * o.rad;
    const x = lerp(o.sx, ex, k), y = lerp(o.sy, ey, k);
    o.tl.style.transform = `translate(${x - 48}px,${y - 66}px) scale(${o.z}) rotate(${(1 - k) * 30}deg)`;
    o.tl.style.opacity = cl(k * 1.4) * (0.55 + o.z * 0.4);
    o.ln.setAttribute('d', `M960 470 Q ${(960 + x) / 2 + 80} ${(470 + y) / 2 - 60} ${x} ${y}`);
    o.ln.style.opacity = 0.55 * p(t, o.delay + 1.0, o.delay + 1.8);
  });
  const v = Math.round(1500 * eio(p(t, 0.5, 2.8)));
  r._num.innerHTML = `<i class="g">${v.toLocaleString('en-US')}${t > 2.8 ? '+' : ''}</i>`;
  r._num.style.opacity = eo(p(t, 0.4, 0.8));
  showIn(r._lab, t, 1.0);
  showIn(r._cap, t, 2.6);
});

// ---------- 5. Observe: the leak ----------
scene(4.8, [0.2, 0.25], r => {
  r.style.background = BG;
  r._lab = stepLabel(r, '01 · OBSERVE');
  const tg = el('div', `position:absolute;left:760px;top:180px;width:400px;height:70px;border-radius:999px;background:rgba(255,255,255,.06);border:1px solid rgba(126,240,165,.3)`, '', r);
  r._knob = el('div', `position:absolute;left:5px;top:5px;width:195px;height:60px;border-radius:999px;background:${G1}`, '', tg);
  r._tgl = ['Desktop', 'Mobile'].map((x, i) => el('div', `position:absolute;left:${i * 200}px;width:200px;top:0;height:70px;display:flex;align-items:center;justify-content:center;font:600 26px 'Inter Tight'`, x, tg));
  const xs = [330, 750, 1170, 1590]; r._xs = xs;
  r._svg = el('div', 'position:absolute;inset:0', `<svg width="1920" height="1080">${GLOW_DEFS}<path id="p0" d="M330 520 L750 520" stroke="${G1}" stroke-width="4" filter="url(#glw)"/><path d="M750 520 L1590 520" stroke="${G1}" stroke-width="4" filter="url(#glw)" opacity=".75"/><g id="dots"></g></svg>`, r);
  r._p0 = r._svg.querySelector('#p0'); const dg = r._svg.querySelector('#dots');
  r._dots = [];
  for (let i = 0; i < 46; i++) { const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle'); c.setAttribute('r', 7); dg.appendChild(c); r._dots.push({ c, ph: rnd(), leak: i % 5 !== 0 }); }
  ['Product page', 'Cart', 'Checkout', 'Order'].forEach((n, i) => el('div', `position:absolute;left:${xs[i] - 150}px;top:465px;width:300px;height:110px;border-radius:28px;background:#0B1A11;border:1.5px solid rgba(126,240,165,.5);box-shadow:0 0 40px rgba(43,208,122,.25);display:flex;align-items:center;justify-content:center;font:700 32px 'Inter Tight';color:${TXT}`, n, r));
  r._call = el('div', `position:absolute;left:330px;top:690px;width:620px;padding:30px 36px;border-radius:24px;background:rgba(255,90,90,.08);border:1.5px solid ${RED};box-shadow:0 0 50px rgba(255,90,90,.25);opacity:0`, `<div style="font:600 22px 'JetBrains Mono';letter-spacing:.14em;color:${RED}">LEAK FOUND</div><div style="margin-top:12px;font:700 38px 'Inter Tight';color:${TXT}">Mobile · Product page → Cart</div><div style="margin-top:8px;font:500 28px 'Inter Tight';color:${MUT}">Most mobile visitors stop right here.</div>`, r);
  r._cap = caption(r, 'Observe. Solen finds where visitors drop.', 70);
}, (t, d, r) => {
  showIn(r._lab, t, 0.1);
  const m = eio(p(t, 1.0, 1.4));
  r._knob.style.transform = `translateX(${m * 195}px)`;
  r._tgl[0].style.color = m < .5 ? '#04130A' : MUT; r._tgl[1].style.color = m >= .5 ? '#04130A' : MUT;
  const red = p(t, 1.4, 1.9);
  r._p0.setAttribute('stroke', red > .5 ? RED : G1);
  r._dots.forEach(o => {
    const u = (t * 0.32 + o.ph) % 1; let x = 330 + u * 1260, y = 520, op = 1, col = G1;
    const leaking = o.leak && red > 0 && (t - (x - 330) / (1260 * 0.32)) > 1.4;
    if (leaking && x > 520) { const dx = Math.min(x - 520, 400); x = 520 + dx * 0.35; y = 520 + dx * dx * 0.004 + dx * 0.4; op = cl(1 - dx / 320); col = RED; }
    if (x < 330) op = 0;
    o.c.setAttribute('cx', x); o.c.setAttribute('cy', y); o.c.setAttribute('fill', col); o.c.setAttribute('opacity', op * eo(p(t, 0, 0.5)));
  });
  showIn(r._call, t, 2.0, 0.5, 20);
  showIn(r._cap, t, 2.8);
});

// ---------- 6. Propose: 100 hypotheses, 99 rejected ----------
const KEEP = 46;
scene(5.8, [0.2, 0.25], r => {
  r.style.background = BG;
  r._lab = stepLabel(r, '02 · PROPOSE');
  r._cards = [];
  for (let i = 0; i < 100; i++) {
    const row = Math.floor(i / 10), col = i % 10;
    const c = el('div', `position:absolute;left:${190 + col * 78}px;top:${230 + row * 58}px;width:64px;height:44px;border-radius:9px;background:rgba(126,240,165,.14);border:1.5px solid rgba(126,240,165,.55);box-sizing:border-box;padding:10px 9px`, '<div style="height:5px;width:80%;background:rgba(238,245,240,.6);border-radius:3px"></div><div style="height:5px;width:50%;margin-top:7px;background:rgba(238,245,240,.35);border-radius:3px"></div>', r);
    r._cards.push({ c, row, col });
  }
  const order = [...Array(100).keys()].filter(i => i !== KEEP).sort(() => rnd() - 0.5);
  order.forEach((i, k) => r._cards[i].rej = 1.3 + k * 0.021);
  r._side = el('div', 'position:absolute;left:1080px;top:230px;width:720px', '', r);
  r._n1 = el('div', `font:800 120px 'Inter Tight';letter-spacing:-0.04em;color:${TXT};line-height:1`, '100', r._side);
  el('div', `font:600 34px 'Inter Tight';color:${MUT};margin-top:6px`, 'hypotheses drafted', r._side);
  r._n2 = el('div', `font:800 120px 'Inter Tight';letter-spacing:-0.04em;color:${RED};line-height:1;margin-top:34px`, '0', r._side);
  el('div', `font:600 34px 'Inter Tight';color:${MUT};margin-top:6px`, 'rejected', r._side);
  r._rs = ['Touches your prices', 'Not supported by your data', 'Already tried', 'Too small to matter'].map(x => el('div', `margin-top:${x === 'Touches your prices' ? 34 : 12}px;font:500 30px 'Inter Tight';color:${TXT};opacity:0`, `<span style="color:${RED};font-weight:700">✕</span>&nbsp; ${x}`, r._side));
  r._big = el('div', `position:absolute;left:510px;top:270px;width:900px;padding:44px 52px;box-sizing:border-box;border-radius:30px;background:#0B1A11;border:2px solid ${G1};box-shadow:0 0 80px rgba(43,208,122,.35);opacity:0`,
    `<div style="font:600 24px 'JetBrains Mono';letter-spacing:.14em;color:${G1}">HYPOTHESIS · 1 OF 100</div>
     <div style="margin-top:18px;font:700 44px 'Inter Tight';letter-spacing:-0.02em;line-height:1.15;color:${TXT}">Mobile visitors don't see delivery &amp; returns before the button.</div>
     <div style="margin-top:22px;font:600 34px 'Inter Tight';color:${G1}">Change → show them right under “Add to cart”.</div>
     <div style="margin-top:26px;display:flex;gap:14px">${['Based on your data', 'Easy to apply', 'You approve'].map(x => `<span style="padding:10px 20px;border-radius:999px;border:1.5px solid rgba(126,240,165,.5);font:600 24px 'Inter Tight';color:${TXT}">${x}</span>`).join('')}</div>`, r);
  r._cap = caption(r, 'Drafts 100 ideas. Keeps the one your data supports.', 70);
}, (t, d, r) => {
  showIn(r._lab, t, 0.1);
  let rej = 0;
  const go = eio(p(t, 3.6, 4.3));
  r._cards.forEach((o, i) => {
    const a = eo(p(t, 0.05 + (o.row + o.col) * 0.035, 0.35 + (o.row + o.col) * 0.035));
    let s = lerp(0.3, 1, a), op = a, dy = 0;
    if (i === KEEP) {
      const g = p(t, 1.2, 1.5);
      o.c.style.background = `rgba(126,240,165,${0.14 + g * 0.6})`; o.c.style.boxShadow = `0 0 ${g * 30}px rgba(126,240,165,.8)`;
      const tx = lerp(0, 960 - (190 + o.col * 78 + 32), go), ty = lerp(0, 470 - (230 + o.row * 58 + 22), go);
      o.c.style.transform = `translate(${tx}px,${ty}px) scale(${lerp(1, 6, go)})`;
      o.c.style.opacity = 1 - p(t, 4.15, 4.35);
      return;
    }
    if (t > o.rej) { rej++; const k = eo(p(t, o.rej, o.rej + 0.25)); o.c.style.background = `rgba(120,130,125,${0.14})`; o.c.style.borderColor = `rgba(150,160,155,${0.5 - k * 0.3})`; op = lerp(1, 0.18, k); dy = k * 10; s *= lerp(1, 0.86, k); }
    o.c.style.opacity = op * (1 - go); o.c.style.transform = `translateY(${dy}px) scale(${s})`;
  });
  r._n2.textContent = rej;
  r._side.style.opacity = eo(p(t, 0.5, 0.9)) * (1 - go);
  r._rs.forEach((e, k) => showIn(e, t, 1.4 + k * 0.5, 0.35, 10));
  const b = eo(p(t, 4.2, 4.6)); r._big.style.opacity = b; r._big.style.transform = `scale(${lerp(0.94, 1, b)})`;
  showIn(r._cap, t, 4.6);
});

// ---------- 7. Test ----------
scene(4.8, [0.2, 0.25], r => {
  r.style.background = BG;
  r._lab = stepLabel(r, '03 · TEST');
  r._A = pageMock(r, 'left:520px;top:190px;width:330px;height:560px', { hue: '#E9C9A0', btn: '#16201A', btnText: 'Add to cart', bs: 18 });
  r._B = pageMock(r, 'left:1070px;top:190px;width:330px;height:560px', { hue: '#E9C9A0', btn: '#16201A', btnText: 'Add to cart', bs: 18 });
  r._hl = el('div', `margin-top:7%;padding:8px 10px;border-radius:10px;background:rgba(43,208,122,.18);border:1.5px solid ${G2};font:600 15px 'Inter Tight';color:#0B3D24;opacity:0`, 'Free delivery · 30-day returns', r._B._body);
  el('div', `position:absolute;left:520px;top:130px;width:330px;text-align:center;font:600 28px 'Inter Tight';color:${MUT}`, 'A · Current page', r);
  el('div', `position:absolute;left:1070px;top:130px;width:330px;text-align:center;font:600 28px 'Inter Tight';color:${G1}`, 'B · Proposed', r);
  const bar = el('div', 'position:absolute;left:460px;top:800px;width:1000px;height:22px;border-radius:999px;background:rgba(255,255,255,.12);overflow:hidden', '', r);
  r._bar = el('div', `position:absolute;right:0;top:0;bottom:0;width:0;background:${G1};box-shadow:0 0 20px ${G1}`, '', bar);
  r._bl = el('div', `position:absolute;left:460px;top:836px;width:1000px;display:flex;justify-content:space-between;font:600 26px 'Inter Tight';color:${MUT};opacity:0`, '<span>Control · 90% of traffic</span><span style="color:#7EF0A5">Test · 10%</span>', r);
  r._chips = ['Prices locked', 'Checkout untouched', 'Auto-stop if sales drop', 'You approve'].map((x, i) => el('div', `position:absolute;top:920px;left:${[300, 620, 990, 1420][i]}px;padding:14px 26px;border-radius:999px;border:1.5px solid rgba(126,240,165,.55);background:rgba(126,240,165,.08);font:600 28px 'Inter Tight';color:${TXT};opacity:0;white-space:nowrap`, `<span style="color:${G1}">✓</span>&nbsp; ${x}`, r));
}, (t, d, r) => {
  showIn(r._lab, t, 0.1);
  showIn(r._A, t, 0.1, 0.5, 30); showIn(r._B, t, 0.3, 0.5, 30);
  const h = eo(p(t, 0.9, 1.3)); r._hl.style.opacity = h; r._hl.style.boxShadow = `0 0 ${h * 24}px rgba(43,208,122,.6)`;
  r._bar.style.width = `${eio(p(t, 1.4, 2.1)) * 10}%`;
  showIn(r._bl, t, 1.6, 0.4, 10);
  r._chips.forEach((c, i) => { const x = back(p(t, 2.3 + i * 0.3, 2.65 + i * 0.3)); c.style.opacity = cl(x); c.style.transform = `scale(${lerp(0.7, 1, x)})`; });
});

// ---------- 8. Learn ----------
scene(4.8, [0.2, 0.25], r => {
  r.style.background = BG;
  r._lab = stepLabel(r, '04 · LEARN');
  const ch = el('div', 'position:absolute;left:150px;top:220px;width:900px;height:560px;border-radius:28px;background:rgba(255,255,255,.04);border:1px solid rgba(126,240,165,.25)', '', r);
  let a = 'M60 430', b = 'M60 430';
  for (let i = 1; i <= 14; i++) { const x = 60 + i * 56; a += ` L${x} ${430 - i * 4 - 14 * Math.sin(i * 1.7)}`; b += ` L${x} ${430 - i * (i > 5 ? 19 : 6) - 12 * Math.sin(i * 1.3)}`; }
  ch.innerHTML = `<svg width="900" height="560">${GLOW_DEFS}<path d="M60 470 L860 470" stroke="rgba(255,255,255,.15)" stroke-width="2"/><path id="la" d="${a}" fill="none" stroke="#7f8c85" stroke-width="5" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/><path id="lb" d="${b}" fill="none" stroke="${G1}" stroke-width="6" filter="url(#glw)" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>
  <div style="position:absolute;left:60px;top:30px;font:600 26px 'Inter Tight';color:${MUT}">Add to cart rate · <span style="color:#7f8c85">A</span> vs <span style="color:${G1}">B</span></div>`;
  r._la = ch.querySelector('#la'); r._lb = ch.querySelector('#lb');
  r._badge = el('div', `position:absolute;left:780px;top:250px;padding:16px 28px;border-radius:999px;background:${G1};font:700 30px 'Inter Tight';color:#04130A;opacity:0;box-shadow:0 0 40px rgba(126,240,165,.6)`, 'B wins · kept', r);
  const mem = el('div', 'position:absolute;left:1150px;top:220px;width:640px;height:560px;border-radius:28px;background:rgba(255,255,255,.04);border:1px solid rgba(126,240,165,.25);padding:40px;box-sizing:border-box', `<div style="font:600 24px 'JetBrains Mono';letter-spacing:.14em;color:${G1}">STORE MEMORY</div>`, r);
  r._mem = [['Delivery near the button', 'kept', G1], ['Sticky buy button', 'dropped', '#8a958f'], ['Reviews under the price', 'testing', '#F3C969']].map(m => el('div', `margin-top:30px;padding:24px 28px;border-radius:18px;background:rgba(255,255,255,.05);display:flex;justify-content:space-between;align-items:center;font:600 30px 'Inter Tight';color:${TXT};opacity:0`, `${m[0]}<span style="font:600 24px 'JetBrains Mono';color:${m[2]}">${m[1]}</span>`, mem));
  r._cap = caption(r, 'Every result makes the next idea better.', 120);
}, (t, d, r) => {
  showIn(r._lab, t, 0.1);
  r._la.setAttribute('stroke-dashoffset', 1 - eio(p(t, 0.3, 2.0)));
  r._lb.setAttribute('stroke-dashoffset', 1 - eio(p(t, 0.3, 2.0)));
  const b = back(p(t, 2.0, 2.4)); r._badge.style.opacity = cl(b); r._badge.style.transform = `scale(${lerp(0.6, 1, b)})`;
  r._mem.forEach((m, i) => showIn(m, t, 2.4 + i * 0.35, 0.4, 16));
  showIn(r._cap, t, 3.3);
});

// ---------- 9. Your pace ----------
scene(4.4, [0.2, 0.25], r => {
  r.style.background = BG;
  r._h = el('div', `position:absolute;left:0;right:0;top:150px;text-align:center;font:800 96px 'Inter Tight';letter-spacing:-0.04em;color:${TXT};opacity:0`, 'Your pace.', r);
  const tg = el('div', 'position:absolute;left:760px;top:300px;width:400px;height:70px;border-radius:999px;background:rgba(255,255,255,.06);border:1px solid rgba(126,240,165,.3)', '', r);
  r._knob = el('div', `position:absolute;left:5px;top:5px;width:195px;height:60px;border-radius:999px;background:${G1}`, '', tg);
  ['Daily', 'Weekly'].forEach((x, i) => el('div', `position:absolute;left:${i * 200}px;width:200px;top:0;height:70px;display:flex;align-items:center;justify-content:center;font:600 26px 'Inter Tight';color:${i ? MUT : '#04130A'}`, x, tg));
  const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], tips = ['Reviews higher', 'Delivery by the button', 'Shorter title', 'Size guide link', 'Bigger photos', 'Returns badge', 'FAQ block'];
  r._days = days.map((dn, i) => {
    const c = el('div', `position:absolute;left:${188 + i * 224}px;top:450px;width:200px;height:300px;border-radius:24px;background:rgba(255,255,255,.04);border:1px solid rgba(126,240,165,.25);opacity:0`, `<div style="margin:22px 0 0 22px;font:600 26px 'JetBrains Mono';color:${MUT}">${dn}</div>`, r);
    c._tip = el('div', `position:absolute;left:16px;right:16px;top:86px;padding:18px;border-radius:16px;background:rgba(126,240,165,.12);border:1px solid rgba(126,240,165,.45);font:600 24px 'Inter Tight';line-height:1.2;color:${TXT};opacity:0`, tips[i], c);
    c._btn = el('div', `position:absolute;left:16px;right:16px;bottom:18px;height:56px;border-radius:14px;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;font:700 24px 'Inter Tight';color:${TXT};opacity:0`, 'Approve', c);
    return c;
  });
  r._cur = el('div', 'position:absolute;left:0;top:0;opacity:0', '<svg width="44" height="54" viewBox="0 0 22 27"><path d="M2 2 L2 22 L7.5 17 L11 25 L14.5 23.5 L11 15.5 L18 15.5 Z" fill="#fff" stroke="#000" stroke-width="1.6" stroke-linejoin="round"/></svg>', r);
  r._cap = caption(r, 'One suggestion a day. Or a week. You decide.', 120);
}, (t, d, r) => {
  showIn(r._h, t, 0.05);
  r._days.forEach((c, i) => { showIn(c, t, 0.25 + i * 0.07, 0.35, 20); const x = back(p(t, 0.7 + i * 0.16, 1.0 + i * 0.16)); c._tip.style.opacity = cl(x); c._tip.style.transform = `scale(${lerp(0.7, 1, x)})`; c._btn.style.opacity = eo(p(t, 0.9 + i * 0.16, 1.2 + i * 0.16)); });
  const c = r._days[3], mv = eio(p(t, 1.9, 2.6));
  r._cur.style.opacity = eo(p(t, 1.8, 2.0));
  r._cur.style.transform = `translate(${lerp(1500, 188 + 3 * 224 + 120, mv)}px,${lerp(900, 450 + 300 - 50, mv)}px) scale(${t > 2.7 && t < 2.85 ? 0.85 : 1})`;
  if (t > 2.75) { c._btn.style.background = G1; c._btn.style.color = '#04130A'; c._btn.textContent = 'Approved ✓'; c.style.borderColor = G1; c.style.boxShadow = `0 0 50px rgba(126,240,165,${0.5 * (1 - p(t, 2.75, 3.6)) + 0.2})`; }
  else { c._btn.style.background = 'rgba(255,255,255,.08)'; c._btn.style.color = TXT; c._btn.textContent = 'Approve'; c.style.boxShadow = 'none'; }
  showIn(r._cap, t, 3.0);
});

// ---------- 10. The right page for each visitor ----------
scene(4.8, [0.2, 0.3], r => {
  r.style.background = BG;
  const heads = ['Built for long runs.', 'The gift they\'ll keep.', 'Welcome back.', 'New here? Start here.'];
  const labs = ['Runners', 'Gift buyers', 'Returning', 'First visit'];
  const hues = ['#C9D8E9', '#E9B8C4', '#E9C9A0', '#CDE9C9'];
  r._pg = heads.map((h, i) => {
    const m = pageMock(r, 'left:780px;top:220px;width:360px;height:600px', { hue: hues[i], title: h, ts: 30, btn: '#16201A', btnText: 'Add to cart', bs: 18 });
    m._lab = el('div', `position:absolute;left:780px;top:150px;width:360px;text-align:center;opacity:0`, `<span style="padding:10px 24px;border-radius:999px;background:rgba(126,240,165,.12);border:1.5px solid rgba(126,240,165,.55);font:600 26px 'Inter Tight';color:${TXT}">${labs[i]}</span>`, r);
    return m;
  });
  r._cap = caption(r, 'Each visitor sees the right page.', 110);
}, (t, d, r) => {
  const k = eio(p(t, 0.8, 1.9)); const xs = [-645, -215, 215, 645], rots = [-6, -2, 2, 6];
  r._pg.forEach((m, i) => {
    m.style.transform = `translateX(${xs[i] * k}px) rotate(${rots[i] * k * (1 - p(t, 2.2, 3))}deg) scale(${lerp(1, 0.92, k)})`;
    m.style.opacity = i === 2 ? eo(p(t, 0, 0.4)) : cl(k * 3);
    m._lab.style.transform = `translateX(${xs[i] * k}px)`; m._lab.style.opacity = eo(p(t, 1.9 + i * 0.12, 2.3 + i * 0.12));
  });
  r._pg[2].style.zIndex = 5;
  showIn(r._cap, t, 2.6);
});


// ---------- 11. Outro ----------
scene(5.4, [0.3, 0.6], r => {
  r.style.background = BG;
  const paths = ['M-40 300 C 300 180 600 420 960 300 S 1600 160 1960 260', 'M-40 820 C 360 940 640 700 980 820 S 1580 950 1960 800', 'M-40 560 C 400 500 600 640 960 560 S 1500 480 1960 560', 'M-40 150 C 500 260 900 60 1960 140', 'M-40 960 C 600 860 1100 1040 1960 930'];
  r._s = el('div', 'position:absolute;inset:0', `<svg width="1920" height="1080">${GLOW_DEFS}<g fill="none" stroke="url(#ln)" stroke-width="2.4" filter="url(#glw)">${paths.map(d => `<path d="${d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>`).join('')}</g></svg>`, r).querySelectorAll('path');
  el('div', 'position:absolute;left:360px;top:300px;width:1200px;height:480px;background:radial-gradient(closest-side,rgba(4,10,6,.95) 55%,rgba(4,10,6,0))', '', r);
  r._logo = el('div', `position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center;align-items:center;gap:30px;opacity:0`, `${logoSvg(130)}<span style="font-family:'Archivo';font-stretch:125%;font-weight:800;font-size:110px;color:#fff">Solen</span>`, r);
  r._t1 = el('div', `position:absolute;left:0;right:0;top:530px;text-align:center;font:700 64px 'Inter Tight';letter-spacing:-0.03em;color:${TXT};opacity:0`, 'The <i class="g">Self-Optimizing</i> E-commerce Layer.', r);
  r._t2 = el('div', `position:absolute;left:0;right:0;top:630px;text-align:center;font:500 38px 'Inter Tight';color:${MUT};opacity:0`, 'For Shopify stores · withsolen.com', r);
  r._t3 = el('div', `position:absolute;left:0;right:0;bottom:60px;text-align:center;font:500 22px 'JetBrains Mono';color:#6F8A78;opacity:0`, 'Product vision film. Features shown are in development.', r);
}, (t, d, r) => {
  r._s.forEach((pa, i) => pa.setAttribute('stroke-dashoffset', 1 - eio(p(t, i * 0.12, 1.4 + i * 0.12))));
  const l = eo(p(t, 0.5, 1.2)); r._logo.style.opacity = l; r._logo.style.transform = `scale(${lerp(0.9, 1, l)})`; r._logo.style.filter = `drop-shadow(0 0 ${30 * l}px rgba(126,240,165,.45))`;
  showIn(r._t1, t, 1.2); showIn(r._t2, t, 1.7); showIn(r._t3, t, 2.2, 0.5, 0);
});

// SVG ids (filters, gradients) must be unique: a url(#id) that resolves into a hidden scene renders nothing
function fixIds(root, k) {
  root.querySelectorAll('[id]').forEach(e => {
    const id = e.id, nid = id + '_' + k; e.id = nid;
    root.querySelectorAll('*').forEach(x => ['filter', 'stroke', 'fill'].forEach(a => { const v = x.getAttribute(a); if (v === `url(#${id})`) x.setAttribute(a, `url(#${nid})`); }));
  });
}
scenes.forEach((s, k) => { s.el = el('div', '', '', stage); s.el.className = 'scene'; s.build(s.el); fixIds(s.el, k); });
const TOTAL = scenes.reduce((a, s) => a + s.dur, 0);
window.TOTAL = TOTAL;
window.render = T => {
  let acc = 0;
  for (const s of scenes) {
    const on = T >= acc && T < acc + s.dur;
    s.el.style.display = on ? 'block' : 'none';
    if (on) {
      const lt = T - acc;
      s.el.style.opacity = Math.min(cl(lt / Math.max(s.fade[0], 1e-3)), cl((s.dur - lt) / Math.max(s.fade[1], 1e-3)));
      s.draw(lt, s.dur, s.el);
    }
    acc += s.dur;
  }
};
window.sceneTimes = () => { let acc = 0; return scenes.map(s => { const a = acc; acc += s.dur; return [a, acc]; }); };
render(0);
