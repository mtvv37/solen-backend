const express = require('express');
const cors = require('cors');
const { createClient } = require('@supabase/supabase-js');
const Anthropic = require('@anthropic-ai/sdk');

const app = express();
app.use(cors());
app.use(express.json({ limit: '1mb' }));

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

app.get('/health', (req, res) => {
  res.json({ status: 'Solen is alive', ts: new Date().toISOString() });
});

app.post('/events', async (req, res) => {
  const { events } = req.body;
  if (!events?.length) return res.status(400).json({ error: 'events required' });
  
const rows = events.map(e => ({
  type: e.type,
  session_id: e.sessionId,
  visitor_id: e.visitorId,
  timestamp: e.timestamp,
  page: e.page || e.url ? { url: e.url, pageType: e.pageType } : null,
  device: typeof e.device === 'string' ? { device: e.device } : e.device || null,
  data: e,
}));
  
  const { error } = await supabase.from('events').insert(rows);
  if (error) return res.status(500).json({ error: error.message });

  res.json({ ok: true, received: rows.length });
});


app.get('/heatmap', async (req, res) => {
  const url = req.query.url || '/';
  const device = req.query.device || 'desktop';

  const deviceProfiles = {
    desktop: { width: 1440, label: 'Desktop', foldHeight: 768 },
    tablet: { width: 768, label: 'Tablet', foldHeight: 1024 },
    mobile: { width: 390, label: 'Mobile', foldHeight: 844 },
  };
  const profile = deviceProfiles[device] || deviceProfiles.desktop;

  const { data: allEvents, error } = await supabase
    .from('events')
    .select('*')
    .in('type', ['click', 'scroll_milestone'])
    .order('created_at', { ascending: false })
    .limit(2000);

  if (error) return res.status(500).json({ error: error.message });

  const clicks = allEvents.filter(c => {
    const d = typeof c.data === 'string' ? JSON.parse(c.data) : c.data;
    return c.type === 'click' && d?.page?.url === url;
  });

  const scrollEvents = allEvents.filter(c => {
    const d = typeof c.data === 'string' ? JSON.parse(c.data) : c.data;
    return c.type === 'scroll_milestone' && d?.page?.url === url;
  });

  const points = clicks.map(c => {
    const d = typeof c.data === 'string' ? JSON.parse(c.data) : c.data;
    const scaleX = profile.width / (d.viewportWidth || 1440);
    return {
      x: Math.round((d.pageX || d.x || 0) * scaleX),
      y: Math.round(d.pageY || d.y || 0),
      pageHeight: d.pageHeight || 1000,
      rage: false,
    };
  }).filter(p => p.x > 0 && p.y > 0);

  const maxPageHeight = points.length > 0
    ? Math.max(...points.map(p => p.pageHeight), profile.foldHeight)
    : profile.foldHeight * 2;

  const scrollDepths = scrollEvents.map(s => {
    const d = typeof s.data === 'string' ? JSON.parse(s.data) : s.data;
    return d?.scrollPct || 0;
  });

  const avgScrollPct = scrollDepths.length > 0
    ? Math.round(scrollDepths.reduce((a, b) => a + b, 0) / scrollDepths.length)
    : 0;

  const avgScrollY = Math.round((avgScrollPct / 100) * (maxPageHeight - profile.foldHeight));

 const storeUrl = process.env.STORE_URL || '';
let screenshotBase64 = '';
if (storeUrl && process.env.SCREENSHOT_KEY) {
  try {
    const fetch2 = (await import('node-fetch')).default;
    const imgUrl = `https://api.screenshotone.com/take?url=${encodeURIComponent(storeUrl + url)}&viewport_width=${profile.width}&viewport_height=${maxPageHeight}&full_page=true&format=jpg&image_quality=50&access_key=${process.env.SCREENSHOT_KEY}`;
    const imgRes = await fetch2(imgUrl);
    if (imgRes.ok) {
      const buffer = await imgRes.buffer();
      screenshotBase64 = `data:image/jpeg;base64,${buffer.toString('base64')}`;
    }
  } catch(e) {
    console.error('[Solen] Screenshot error:', e.message);
  }
}
  const html = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Solen Heatmap — ${url}</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0;}
    body{background:#0A0B0D;color:#E2E5EF;font-family:system-ui,sans-serif;}
    .topbar{background:#111318;border-bottom:1px solid #2C303C;padding:10px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}
    .logo{font-size:16px;font-weight:600;color:#F5A623;flex-shrink:0;}
    .meta{font-size:12px;color:#5A6070;}
    .stats{display:flex;gap:10px;flex-wrap:wrap;padding:12px 20px;}
    .stat{background:#181B22;border:1px solid #2C303C;border-radius:8px;padding:8px 14px;}
    .stat-val{font-size:20px;font-weight:600;color:#F5A623;}
    .stat-label{font-size:10px;color:#5A6070;margin-top:1px;}
    .controls{display:flex;align-items:center;gap:8px;padding:0 20px 12px;flex-wrap:wrap;}
    .device-btn{background:#181B22;border:1px solid #2C303C;color:#8A93A8;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:12px;font-family:system-ui;transition:.15s;}
    .device-btn.active{background:#F5A62318;border-color:#F5A623;color:#F5A623;}
    .layer-btn{background:#181B22;border:1px solid #2C303C;color:#8A93A8;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:12px;font-family:system-ui;transition:.15s;}
    .layer-btn.active{background:#1FB8A015;border-color:#1FB8A0;color:#1FB8A0;}
    .sep{width:1px;height:24px;background:#2C303C;}
    .url-input{background:#181B22;border:1px solid #2C303C;color:#E2E5EF;padding:6px 12px;border-radius:6px;font-size:12px;width:200px;font-family:system-ui;}
    .go-btn{background:#F5A623;color:#0A0B0D;border:none;padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px;font-weight:600;font-family:system-ui;}
    .viewport-wrap{display:flex;justify-content:center;padding:0 20px 24px;overflow-x:auto;}
    .viewport{position:relative;background:#13151A;border:1px solid #2C303C;border-radius:8px;overflow:hidden;flex-shrink:0;}
    .iframe-bg{position:absolute;top:0;left:0;width:100%;height:100%;border:none;opacity:0.35;pointer-events:none;}
    .fold-line{position:absolute;left:0;right:0;border-top:2px dashed #F5A623;opacity:0.6;z-index:10;}
    .fold-label{position:absolute;right:8px;background:#F5A623;color:#0A0B0D;font-size:10px;font-weight:600;padding:2px 6px;border-radius:3px;z-index:11;transform:translateY(-50%);}
    .scroll-line{position:absolute;left:0;right:0;border-top:2px dashed #1FB8A0;opacity:0.7;z-index:10;}
    .scroll-label{position:absolute;right:8px;background:#1FB8A0;color:#0A0B0D;font-size:10px;font-weight:600;padding:2px 6px;border-radius:3px;z-index:11;transform:translateY(-50%);}
    .heatmap-canvas{position:absolute;top:0;left:0;pointer-events:none;z-index:5;}
    .empty{text-align:center;padding:60px 20px;color:#5A6070;font-size:13px;}
    .legend{display:flex;align-items:center;gap:16px;padding:0 20px 16px;flex-wrap:wrap;}
    .legend-item{display:flex;align-items:center;gap:6px;font-size:11px;color:#5A6070;}
    .legend-dot{width:12px;height:12px;border-radius:50%;}
  </style>
</head>
<body>
<div class="topbar">
  <span class="logo">Solen</span>
  <span class="meta">Heatmap — ${url} — ${clicks.length} clics — ${device}</span>
</div>

<div class="stats">
  <div class="stat"><div class="stat-val">${clicks.length}</div><div class="stat-label">Clics</div></div>
  <div class="stat"><div class="stat-val">${[...new Set(clicks.map(c=>c.session_id))].length}</div><div class="stat-label">Sessions</div></div>
  <div class="stat"><div class="stat-val">${avgScrollPct}%</div><div class="stat-label">Scroll moyen</div></div>
  <div class="stat"><div class="stat-val">${scrollEvents.length}</div><div class="stat-label">Events scroll</div></div>
</div>

<div class="controls">
  <a href="?url=${encodeURIComponent(url)}&device=desktop" class="device-btn ${device==='desktop'?'active':''}">🖥 Desktop</a>
  <a href="?url=${encodeURIComponent(url)}&device=tablet" class="device-btn ${device==='tablet'?'active':''}">📱 Tablet</a>
  <a href="?url=${encodeURIComponent(url)}&device=mobile" class="device-btn ${device==='mobile'?'active':''}">📱 Mobile</a>
  <div class="sep"></div>
  <button class="layer-btn active" id="btn-clicks" onclick="toggleLayer('clicks')">Clics</button>
  <button class="layer-btn" id="btn-scroll" onclick="toggleLayer('scroll')">Zone de scroll</button>
  <button class="layer-btn" id="btn-fold" onclick="toggleLayer('fold')">Above the fold</button>
  <div class="sep"></div>
  <input class="url-input" id="url-input" value="${url}" placeholder="/products/..." />
  <button class="go-btn" onclick="navigate()">Analyser</button>
</div>

<div class="legend">
  <div class="legend-item"><div class="legend-dot" style="background:#F5A623"></div>Zone de clics dense</div>
  <div class="legend-item"><div class="legend-dot" style="background:#F5A62340;border:1px dashed #F5A623"></div>Above the fold</div>
  <div class="legend-item"><div class="legend-dot" style="background:#1FB8A040;border:1px dashed #1FB8A0"></div>Scroll moyen (${avgScrollPct}%)</div>
</div>

<div class="viewport-wrap">
  <div class="viewport" id="viewport" style="width:${profile.width}px;height:${maxPageHeight}px;">
    ${screenshotBase64 ? `<img class="iframe-bg" src="${screenshotBase64}" style="width:100%;height:auto;position:absolute;top:0;left:0;opacity:0.35;" />` : ''}
    <div class="fold-line" id="fold-line" style="top:${profile.foldHeight}px;">
      <span class="fold-label" style="top:${profile.foldHeight}px;">Fold — ${profile.label}</span>
    </div>
    <div class="scroll-line" id="scroll-line" style="top:${profile.foldHeight + avgScrollY}px;display:none;">
      <span class="scroll-label" style="top:${profile.foldHeight + avgScrollY}px;">Scroll moyen ${avgScrollPct}%</span>
    </div>
    <canvas class="heatmap-canvas" id="heatmap" width="${profile.width}" height="${maxPageHeight}"></canvas>
    ${points.length === 0 ? `<div class="empty">Pas encore de clics sur cette page en mode ${profile.label}.<br>Navigue sur le store et reviens.</div>` : ''}
  </div>
</div>

<script>
var points = ${JSON.stringify(points)};
var layers = { clicks: true, scroll: false, fold: true };

var canvas = document.getElementById('heatmap');
var ctx = canvas.getContext('2d');

function drawHeatmap() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  if (!layers.clicks) return;
  points.forEach(function(p) {
    var r = 35;
    var g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, r);
    g.addColorStop(0, 'rgba(255,180,0,0.85)');
    g.addColorStop(0.3, 'rgba(245,100,35,0.5)');
    g.addColorStop(0.7, 'rgba(229,50,50,0.2)');
    g.addColorStop(1, 'rgba(229,50,50,0)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
    ctx.fill();
  });
}

function toggleLayer(name) {
  layers[name] = !layers[name];
  document.getElementById('btn-' + name).classList.toggle('active', layers[name]);
  if (name === 'scroll') document.getElementById('scroll-line').style.display = layers[name] ? 'block' : 'none';
  if (name === 'fold') document.getElementById('fold-line').style.display = layers[name] ? 'block' : 'none';
  if (name === 'clicks') drawHeatmap();
}

function navigate() {
  var url = document.getElementById('url-input').value;
  var device = '${device}';
  window.location.href = '?url=' + encodeURIComponent(url) + '&device=' + device;
}

document.getElementById('url-input').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') navigate();
});

drawHeatmap();
<\/script>
</body>
</html>`;

  res.setHeader('Content-Type', 'text/html');
  res.send(html);
});

app.get('/analyze', async (req, res) => {
  // Récupère les 500 derniers events
  const { data: events, error } = await supabase
    .from('events')
    .select('*')
    .order('created_at', { ascending: false })
    .limit(500);

  if (error) return res.status(500).json({ error: error.message });
  if (!events?.length) return res.status(400).json({ error: 'Pas assez de données' });

  // Agrège par type pour le prompt
  const summary = events.reduce((acc, e) => {
    acc[e.type] = (acc[e.type] || 0) + 1;
    return acc;
  }, {});

  const sessions = [...new Set(events.map(e => e.session_id))].length;
  const pages = [...new Set(events.map(e => e.page?.url).filter(Boolean))];
  const devices = events.reduce((acc, e) => {
    const d = e.device?.device || 'unknown';
    acc[d] = (acc[d] || 0) + 1;
    return acc;
  }, {});

  const prompt = `Tu es Solen, un agent IA spécialisé dans l'optimisation de la conversion e-commerce.

Voici les données comportementales collectées sur ce store :

- Sessions analysées : ${sessions}
- Events totaux : ${events.length}
- Types d'events : ${JSON.stringify(summary)}
- Pages visitées : ${pages.join(', ')}
- Répartition devices : ${JSON.stringify(devices)}

Exemples d'events récents :
${JSON.stringify(events.slice(0, 10), null, 2)}

Analyse ces données et produis un diagnostic structuré avec :
1. Les 3 principales frictions détectées
2. Pour chaque friction : ce qui se passe, pourquoi c'est un problème, et une variante concrète à tester
3. La priorité d'action (haute/moyenne/faible)

Réponds en français, de façon directe et actionnable. Tu es un agent qui agit, pas un outil qui observe.`;

  const message = await anthropic.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 1024,
    messages: [{ role: 'user', content: prompt }],
  });

  res.json({
    sessions,
    events: events.length,
    summary,
    diagnostic: message.content[0].text,
  });
});

module.exports = app;
