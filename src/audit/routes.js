'use strict';
const fs = require('fs');
const path = require('path');
const express = require('express');
const { runAudit, AuditError } = require('./service');
const { createStore } = require('./store');
const { newAuditId, isAuditId, unlockToken, verifyUnlockToken, hashIp, clientIp } = require('./tokens');
const { renderOgImage } = require('./og');
const { CATEGORIES } = require('./score');

const PUBLIC_DIR = path.join(__dirname, '..', '..', 'public', 'audit');
const AUDITS_PER_HOUR = 6; // attempts, successful or not
const UNLOCKS_PER_HOUR = 10;
const VISIBLE_LEAKS = 2;
const CONSENT_VERSION = 'audit-v0-2026-10';
const CONSENT_TEXT = 'J’accepte que Solen utilise mon email pour m’envoyer ce rapport et des conseils pour améliorer ma boutique. Désinscription possible à tout moment.';
const EMAIL_RE = /^[^\s@<>()[\]\\,;:"]{1,64}@[^\s@<>()[\]\\,;:"]{1,190}\.[a-z]{2,24}$/i;

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function toRow(id, ipHash, r) {
  return {
    id, ip_hash: ipHash, url: r.url, shop_domain: r.shopDomain, product_url: r.productUrl,
    product_name: r.productName, is_shopify: r.isShopify, score: r.score, categories: r.categories,
    checks: r.checks, summary: r.summary, leaks: r.leaks, assumptions: r.assumptions, writer: r.writer,
  };
}

function view(row, unlocked) {
  const leaks = (row.leaks || []).map((leak, i) => {
    if (unlocked || i < VISIBLE_LEAKS) return leak;
    return { locked: true, category: leak.category, categoryLabel: (CATEGORIES[leak.category] || {}).label || '' };
  });
  return {
    id: row.id,
    createdAt: row.created_at,
    shopDomain: row.shop_domain,
    productUrl: row.product_url,
    productName: row.product_name,
    isShopify: row.is_shopify,
    score: row.score,
    categories: row.categories,
    summary: row.summary,
    assumptions: row.assumptions,
    leaks,
    leakCount: (row.leaks || []).length,
    unlocked,
  };
}

function securityHeaders(res) {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.setHeader('Content-Security-Policy', [
    "default-src 'self'",
    "script-src 'self'",
    "style-src 'self' https://api.fontshare.com",
    'font-src https://cdn.fontshare.com',
    "img-src 'self' data:",
    "connect-src 'self'",
    "frame-ancestors 'none'",
    "base-uri 'none'",
    "form-action 'self'",
  ].join('; '));
}

function baseUrl(req) {
  if (process.env.PUBLIC_BASE_URL) return process.env.PUBLIC_BASE_URL.replace(/\/$/, '');
  const host = String(req.headers['x-forwarded-host'] || req.headers.host || 'localhost').replace(/[^a-z0-9.:-]/gi, '');
  const proto = req.headers['x-forwarded-proto'] === 'http' ? 'http' : 'https';
  return `${proto}://${host}`;
}

function createAuditRouter(options = {}) {
  const router = express.Router();
  let store = options.store || null;
  const getStore = () => { if (!store) store = createStore(); return store; };
  const deps = options.deps || {};
  const hourAgo = () => new Date(Date.now() - 3600 * 1000).toISOString();

  const reportTemplate = () => fs.readFileSync(path.join(PUBLIC_DIR, 'report.html'), 'utf8');

  router.use('/audit', (req, res, next) => { securityHeaders(res); next(); }, express.static(PUBLIC_DIR, { index: 'index.html', maxAge: '1h' }));

  router.post('/api/audits', async (req, res) => {
    try {
      const ipHash = hashIp(clientIp(req));
      const db = getStore();
      if ((await db.countAttemptsSince(ipHash, hourAgo())) >= AUDITS_PER_HOUR) {
        return res.status(429).json({ error: 'Vous avez lancé beaucoup d’audits en peu de temps. Réessayez dans une heure.' });
      }
      await db.insertAttempt(ipHash);
      const body = req.body || {};
      const result = await runAudit({ url: body.url, monthlyVisitors: body.monthlyVisitors, averageOrderValue: body.averageOrderValue }, deps);
      const id = newAuditId();
      await db.insertAudit(toRow(id, ipHash, result));
      return res.status(201).json({ id, reportUrl: `/r/${id}` });
    } catch (err) {
      if (err instanceof AuditError) return res.status(err.status).json({ error: err.message, code: err.code });
      console.error('[audit] create failed:', err);
      return res.status(500).json({ error: 'L’audit n’a pas pu aboutir. Réessayez dans quelques minutes.' });
    }
  });

  router.get('/api/audits/:id', async (req, res) => {
    if (!isAuditId(req.params.id)) return res.status(404).json({ error: 'Rapport introuvable.' });
    try {
      const row = await getStore().getAudit(req.params.id);
      if (!row) return res.status(404).json({ error: 'Rapport introuvable.' });
      res.setHeader('Cache-Control', 'no-store');
      return res.json(view(row, verifyUnlockToken(row.id, req.query.t)));
    } catch (err) {
      console.error('[audit] read failed:', err);
      return res.status(500).json({ error: 'Impossible de charger ce rapport.' });
    }
  });

  router.post('/api/audits/:id/unlock', async (req, res) => {
    if (!isAuditId(req.params.id)) return res.status(404).json({ error: 'Rapport introuvable.' });
    const { email, consent } = req.body || {};
    const cleanEmail = String(email || '').trim().toLowerCase();
    if (cleanEmail.length > 254 || !EMAIL_RE.test(cleanEmail)) return res.status(400).json({ error: 'Cette adresse email ne semble pas valide.' });
    if (consent !== true) return res.status(400).json({ error: 'Cochez la case de consentement pour recevoir le rapport complet.' });
    try {
      const db = getStore();
      const row = await db.getAudit(req.params.id);
      if (!row) return res.status(404).json({ error: 'Rapport introuvable.' });
      const ipHash = hashIp(clientIp(req));
      if ((await db.countLeadsSince(ipHash, hourAgo())) >= UNLOCKS_PER_HOUR) {
        return res.status(429).json({ error: 'Trop de demandes en peu de temps. Réessayez dans une heure.' });
      }
      await db.insertLead({
        audit_id: row.id, email: cleanEmail, consent: true, consent_text: CONSENT_TEXT,
        consent_version: CONSENT_VERSION, consented_at: new Date().toISOString(), ip_hash: ipHash,
      });
      return res.json({ token: unlockToken(row.id), report: view(row, true) });
    } catch (err) {
      console.error('[audit] unlock failed:', err);
      return res.status(500).json({ error: 'Impossible d’enregistrer votre demande. Réessayez.' });
    }
  });

  router.get('/api/audits/:id/og.png', async (req, res) => {
    if (!isAuditId(req.params.id)) return res.status(404).end();
    try {
      const row = await getStore().getAudit(req.params.id);
      if (!row) return res.status(404).end();
      const png = await renderOgImage({ domain: row.shop_domain, score: row.score, leakCount: (row.leaks || []).length });
      res.setHeader('Content-Type', 'image/png');
      res.setHeader('Cache-Control', 'public, max-age=86400, immutable');
      return res.end(png);
    } catch (err) {
      console.error('[audit] og failed:', err);
      return res.status(500).end();
    }
  });

  router.get('/r/:id', async (req, res) => {
    securityHeaders(res);
    const notFound = () => res.status(404).type('html').send(reportTemplate()
      .replace(/{{OG_TITLE}}/g, 'Rapport introuvable · Solen')
      .replace(/{{OG_DESCRIPTION}}/g, 'Ce rapport n’existe pas ou a été supprimé.')
      .replace(/{{OG_IMAGE}}/g, '')
      .replace(/{{CANONICAL}}/g, ''));
    if (!isAuditId(req.params.id)) return notFound();
    try {
      const row = await getStore().getAudit(req.params.id);
      if (!row) return notFound();
      const base = baseUrl(req);
      const title = `${row.shop_domain} : ${row.score}/100 à l’audit de conversion Solen`;
      const desc = `${(row.leaks || []).length} fuites de conversion détectées sur la fiche produit. Faites l’audit gratuit de votre boutique Shopify.`;
      res.setHeader('Cache-Control', 'public, max-age=300');
      return res.type('html').send(reportTemplate()
        .replace(/{{OG_TITLE}}/g, escapeHtml(title))
        .replace(/{{OG_DESCRIPTION}}/g, escapeHtml(desc))
        .replace(/{{OG_IMAGE}}/g, escapeHtml(`${base}/api/audits/${row.id}/og.png`))
        .replace(/{{CANONICAL}}/g, escapeHtml(`${base}/r/${row.id}`)));
    } catch (err) {
      console.error('[audit] report page failed:', err);
      return res.status(500).type('text').send('Erreur');
    }
  });

  return router;
}

module.exports = { createAuditRouter, view, CONSENT_TEXT, CONSENT_VERSION, VISIBLE_LEAKS };
