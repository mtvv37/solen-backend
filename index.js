const express = require('express');
const cors = require('cors');
const { createClient } = require('@supabase/supabase-js');

const app = express();
app.use(cors());
app.use(express.json({ limit: '1mb' }));

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);

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
    page: e.page || null,
    device: e.device || null,
    data: e,
  }));

  const { error } = await supabase.from('events').insert(rows);
  if (error) {
    console.error('[Solen] Erreur insert:', error.message);
    return res.status(500).json({ error: error.message });
  }

  console.log(`[Solen] ${rows.length} events stockés`);
  res.json({ ok: true, received: rows.length });
});

module.exports = app;
