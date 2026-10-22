'use strict';
// Persistence for audits and leads. Uses the Supabase service-role key on the
// server only (tables have RLS on and no public policies). Falls back to an
// in-memory store when Supabase isn't configured (local dev, tests).
const { createClient } = require('@supabase/supabase-js');

function memoryStore() {
  const audits = new Map();
  const leads = [];
  const attempts = [];
  return {
    kind: 'memory',
    async insertAttempt(ipHash) { attempts.push({ ip_hash: ipHash, created_at: new Date().toISOString() }); },
    async countAttemptsSince(ipHash, sinceIso) {
      return attempts.filter((a) => a.ip_hash === ipHash && a.created_at >= sinceIso).length;
    },
    async insertAudit(row) { audits.set(row.id, { ...row, created_at: new Date().toISOString() }); },
    async getAudit(id) { return audits.get(id) || null; },
    async insertLead(row) { leads.push({ ...row, created_at: new Date().toISOString() }); },
    async countLeadsSince(ipHash, sinceIso) {
      return leads.filter((l) => l.ip_hash === ipHash && l.created_at >= sinceIso).length;
    },
    _leads: leads,
  };
}

function supabaseStore(url, key) {
  const db = createClient(url, key, { auth: { persistSession: false } });
  const check = ({ error }) => { if (error) throw new Error(`supabase: ${error.message}`); };
  return {
    kind: 'supabase',
    async insertAttempt(ipHash) { check(await db.from('audit_attempts').insert({ ip_hash: ipHash })); },
    async countAttemptsSince(ipHash, sinceIso) {
      const { count, error } = await db.from('audit_attempts').select('id', { count: 'exact', head: true }).eq('ip_hash', ipHash).gte('created_at', sinceIso);
      if (error) throw new Error(`supabase: ${error.message}`);
      return count || 0;
    },
    async insertAudit(row) { check(await db.from('audits').insert(row)); },
    async getAudit(id) {
      const { data, error } = await db.from('audits').select('*').eq('id', id).maybeSingle();
      if (error) throw new Error(`supabase: ${error.message}`);
      return data;
    },
    async insertLead(row) { check(await db.from('audit_leads').insert(row)); },
    async countLeadsSince(ipHash, sinceIso) {
      const { count, error } = await db.from('audit_leads').select('id', { count: 'exact', head: true }).eq('ip_hash', ipHash).gte('created_at', sinceIso);
      if (error) throw new Error(`supabase: ${error.message}`);
      return count || 0;
    },
  };
}

function createStore() {
  const url = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (url && key) return supabaseStore(url, key);
  if (process.env.NODE_ENV === 'production') throw new Error('SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set in production');
  return memoryStore();
}

module.exports = { createStore, memoryStore };
