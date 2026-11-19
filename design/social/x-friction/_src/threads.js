// Traits de la DA Solen, comme la bannière X « réseau » : dégradé menthe au centre, estompé aux bouts, halo flou.
// drawThreads([[x,y], ...]) : chaque liste de points devient une courbe lisse (Catmull-Rom).
function drawThreads(threads) {
  const NS = 'http://www.w3.org/2000/svg';
  const svg = document.querySelector('svg.threads');
  svg.insertAdjacentHTML('afterbegin', `<defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="ln" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#1F9D5C" stop-opacity="0.25"/><stop offset="0.5" stop-color="#7EF0A5" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#1F9D5C" stop-opacity="0.25"/></linearGradient></defs>`);
  const g = document.createElementNS(NS, 'g');
  g.setAttribute('fill', 'none'); g.setAttribute('stroke', 'url(#ln)'); g.setAttribute('stroke-width', '2.4');
  g.setAttribute('stroke-linecap', 'round'); g.setAttribute('filter', 'url(#glow)');
  svg.appendChild(g);
  const path = (p) => {
    let d = `M${p[0][0]} ${p[0][1]}`;
    for (let i = 0; i < p.length - 1; i++) {
      const p0 = p[i - 1] || p[i], p1 = p[i], p2 = p[i + 1], p3 = p[i + 2] || p2;
      d += ` C${p1[0] + (p2[0] - p0[0]) / 6} ${p1[1] + (p2[1] - p0[1]) / 6} ${p2[0] - (p3[0] - p1[0]) / 6} ${p2[1] - (p3[1] - p1[1]) / 6} ${p2[0]} ${p2[1]}`;
    }
    return d;
  };
  for (const t of threads) {
    const el = document.createElementNS(NS, 'path');
    el.setAttribute('d', path(t.p || t));
    g.appendChild(el);
  }
}
