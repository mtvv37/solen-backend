'use strict';
const crypto = require('crypto');

const DEV_SECRET = 'dev-only-secret-change-me';

function secret(name) {
  const value = process.env[name];
  if (value) return value;
  if (process.env.NODE_ENV === 'production') throw new Error(`${name} must be set in production`);
  return DEV_SECRET;
}

function newAuditId() {
  return crypto.randomBytes(16).toString('base64url'); // 22 chars, 128 bits
}

const ID_RE = /^[A-Za-z0-9_-]{22}$/;
const isAuditId = (id) => typeof id === 'string' && ID_RE.test(id);

function unlockToken(auditId) {
  return crypto.createHmac('sha256', secret('AUDIT_TOKEN_SECRET')).update(`unlock:${auditId}`).digest('base64url');
}

function verifyUnlockToken(auditId, token) {
  if (typeof token !== 'string' || !token) return false;
  const expected = Buffer.from(unlockToken(auditId));
  const given = Buffer.from(token);
  return expected.length === given.length && crypto.timingSafeEqual(expected, given);
}

function hashIp(ip) {
  return crypto.createHmac('sha256', secret('AUDIT_IP_SALT')).update(String(ip || 'unknown')).digest('hex');
}

function clientIp(req) {
  const real = req.headers['x-real-ip'];
  if (typeof real === 'string' && real) return real.trim();
  const fwd = req.headers['x-forwarded-for'];
  if (typeof fwd === 'string' && fwd) return fwd.split(',')[0].trim();
  return (req.socket && req.socket.remoteAddress) || 'unknown';
}

module.exports = { newAuditId, isAuditId, unlockToken, verifyUnlockToken, hashIp, clientIp };
