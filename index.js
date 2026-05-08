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
