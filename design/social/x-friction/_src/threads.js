// Fils lumineux de la DA Solen : courbes de Catmull-Rom qui passent par des points donnés.
function drawThreads(threads) {
  const path = (p) => {
    let d = `M${p[0][0]} ${p[0][1]}`;
    for (let i = 0; i < p.length - 1; i++) {
      const p0 = p[i - 1] || p[i], p1 = p[i], p2 = p[i + 1], p3 = p[i + 2] || p2;
      d += ` C${p1[0] + (p2[0] - p0[0]) / 6} ${p1[1] + (p2[1] - p0[1]) / 6} ${p2[0] - (p3[0] - p1[0]) / 6} ${p2[1] - (p3[1] - p1[1]) / 6} ${p2[0]} ${p2[1]}`;
    }
    return d;
  };
  const g = document.getElementById('lines');
  for (const t of threads) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    el.setAttribute('d', path(t.p));
    el.setAttribute('stroke-opacity', t.o);
    g.appendChild(el);
  }
}
