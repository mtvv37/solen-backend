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
  
  const { data: clicks, error } = await supabase
    .from('events')
    .select('*')
    .eq('type', 'click')
    .order('created_at', { ascending: false })
    .limit(1000);

  if (error) return res.status(500).json({ error: error.message });

  const filtered = clicks.filter(c => {
    const p = typeof c.page === 'string' ? JSON.parse(c.page) : c.page;
    return p?.url === url;
  });

  const points = filtered.map(c => {
    const d = typeof c.data === 'string' ? JSON.parse(c.data) : c.data;
    return {
      x: d.pageX || d.x || 0,
      y: d.pageY || d.y || 0,
      pageHeight: d.pageHeight || 1000,
      viewportWidth: d.viewportWidth || 1440,
    };
  }).filter(p => p.x > 0 && p.y > 0);

  const width = 1440;
  const height = points.length > 0 ? Math.max(...points.map(p => p.pageHeight), 800) : 800;

  const html = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Solen Heatmap — ${url}</title>
  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body { background:#0C0D0F; font-family: system-ui; color: #E8EAF0; }
    .header { padding: 16px 24px; background:#13151A; border-bottom:1px solid #353A47; display:flex; align-items:center; gap:12px; }
    .logo { font-size:18px; font-weight:600; color:#F5A623; }
    .meta { font-size:13px; color:#6B7385; }
    .container { position:relative; margin: 24px auto; width:${width}px; }
    canvas { position:absolute; top:0; left:0; pointer-events:none; }
    .stats { padding: 16px 24px; display:flex; gap:24px; }
    .stat { background:#1C1F26; border:1px solid #353A47; border-radius:10px; padding:12px 16px; }
    .stat-val { font-size:24px; font-weight:600; color:#F5A623; }
    .stat-label { font-size:11px; color:#6B7385; margin-top:2px; }
    .empty { text-align:center; padding:80px; color:#6B7385; }
  </style>
</head>
<body>
  <div class="header">
    <span class="logo">Solen</span>
    <span class="meta">Heatmap — ${url} — ${filtered.length} clics</span>
  </div>
  <div class="stats">
    <div class="stat"><div class="stat-val">${filtered.length}</div><div class="stat-label">Clics totaux</div></div>
    <div class="stat"><div class="stat-val">${[...new Set(filtered.map(c=>c.session_id))].length}</div><div class="stat-label">Sessions</div></div>
    <div class="stat"><div class="stat-val">${url}</div><div class="stat-label">Page analysée</div></div>
  </div>
  ${points.length === 0 ? '<div class="empty">Pas encore assez de clics sur cette page. Navigue sur le store et reviens.</div>' : `
  <div class="container" style="height:${height}px">
    <canvas id="heatmap" width="${width}" height="${height}"></canvas>
  </div>
  <script>
    var points = ${JSON.stringify(points)};
    var canvas = document.getElementById('heatmap');
    var ctx = canvas.getContext('2d');
    
    points.forEach(function(p) {
      var gradient = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, 40);
      gradient.addColorStop(0, 'rgba(245, 166, 35, 0.8)');
      gradient.addColorStop(0.4, 'rgba(229, 83, 83, 0.4)');
      gradient.addColorStop(1, 'rgba(229, 83, 83, 0)');
      ctx.fillStyle = gradient;
      ctx.fillRect(p.x - 40, p.y - 40, 80, 80);
    });
  <\/script>`}
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
