const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json({ limit: '1mb' }));

app.get('/health', (req, res) => {
  res.json({ status: 'Solen is alive', ts: new Date().toISOString() });
});

app.post('/events', (req, res) => {
  const { events } = req.body;
  if (!events?.length) return res.status(400).json({ error: 'events required' });
  console.log(`[Solen] ${events.length} events reçus`);
  events.forEach(e => console.log(`  → ${e.type} | ${e.page?.url}`));
  res.json({ ok: true, received: events.length });
});

module.exports = app;
