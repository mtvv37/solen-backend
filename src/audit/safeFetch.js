'use strict';
// Fetches external pages for the audit while refusing anything that could reach
// internal infrastructure (SSRF). Every hop is re-validated, and the IP checked
// is the IP the socket actually connects to (no DNS-rebinding window).
const http = require('http');
const https = require('https');
const dns = require('dns');
const net = require('net');

const DEFAULTS = {
  timeoutMs: 8000,
  maxBytes: 3 * 1024 * 1024,
  maxRedirects: 4,
  userAgent: 'SolenAuditBot/0.1 (+https://solen.app/bot)',
};

class SafeFetchError extends Error {
  constructor(code, message) {
    super(message);
    this.name = 'SafeFetchError';
    this.code = code;
  }
}

function ipv4ToInt(ip) {
  return ip.split('.').reduce((acc, part) => (acc << 8) + Number(part), 0) >>> 0;
}

const BLOCKED_V4 = [
  ['0.0.0.0', 8], ['10.0.0.0', 8], ['100.64.0.0', 10], ['127.0.0.0', 8],
  ['169.254.0.0', 16], ['172.16.0.0', 12], ['192.0.0.0', 24], ['192.0.2.0', 24],
  ['192.88.99.0', 24], ['192.168.0.0', 16], ['198.18.0.0', 15], ['198.51.100.0', 24],
  ['203.0.113.0', 24], ['224.0.0.0', 4], ['240.0.0.0', 4],
].map(([base, bits]) => [ipv4ToInt(base), bits === 0 ? 0 : (~0 << (32 - bits)) >>> 0]);

function isPublicIPv4(ip) {
  const n = ipv4ToInt(ip);
  return !BLOCKED_V4.some(([base, mask]) => (n & mask) === (base & mask));
}

function expandIPv6(ip) {
  let addr = ip.toLowerCase().split('%')[0];
  // Embedded IPv4 tail (e.g. ::ffff:1.2.3.4) -> two hex groups
  const v4 = addr.match(/(\d+\.\d+\.\d+\.\d+)$/);
  if (v4) {
    const n = ipv4ToInt(v4[1]);
    addr = addr.replace(v4[1], `${(n >>> 16).toString(16)}:${(n & 0xffff).toString(16)}`);
  }
  const [head, tail] = addr.split('::');
  const h = head ? head.split(':') : [];
  const t = tail !== undefined && tail !== '' ? tail.split(':') : [];
  const missing = addr.includes('::') ? 8 - h.length - t.length : 0;
  const groups = [...h, ...Array(missing).fill('0'), ...t].map((g) => parseInt(g || '0', 16));
  return groups.length === 8 ? groups : null;
}

function isPublicIPv6(ip) {
  const g = expandIPv6(ip);
  if (!g) return false;
  if (g.every((x) => x === 0)) return false; // ::
  if (g.slice(0, 7).every((x) => x === 0) && g[7] === 1) return false; // ::1
  // IPv4-mapped / IPv4-compatible / NAT64: judge the embedded IPv4
  const embeddedV4 = `${g[6] >> 8}.${g[6] & 255}.${g[7] >> 8}.${g[7] & 255}`;
  if (g.slice(0, 5).every((x) => x === 0) && (g[5] === 0xffff || g[5] === 0)) return isPublicIPv4(embeddedV4);
  if (g[0] === 0x64 && g[1] === 0xff9b) return isPublicIPv4(embeddedV4);
  if ((g[0] & 0xfe00) === 0xfc00) return false; // fc00::/7 unique local
  if ((g[0] & 0xffc0) === 0xfe80) return false; // fe80::/10 link local
  if ((g[0] & 0xff00) === 0xff00) return false; // multicast
  if (g[0] === 0x2001 && g[1] === 0x0db8) return false; // documentation
  if (g[0] === 0x2002) return isPublicIPv4(`${g[1] >> 8}.${g[1] & 255}.${g[2] >> 8}.${g[2] & 255}`); // 6to4
  return true;
}

function isPublicAddress(ip) {
  const family = net.isIP(ip);
  if (family === 4) return isPublicIPv4(ip);
  if (family === 6) return isPublicIPv6(ip);
  return false;
}

const BLOCKED_HOSTNAMES = /(^|\.)(localhost|local|internal|intranet|home|lan|corp|localdomain)$/i;

// Validates the URL itself (scheme, credentials, port, obvious internal names).
// Address checks happen at connect time in the lookup hook.
function assertSafeUrl(input, { allowAnyPortForTests = false, isAllowedAddress = isPublicAddress } = {}) {
  let url;
  try {
    url = input instanceof URL ? input : new URL(String(input));
  } catch {
    throw new SafeFetchError('INVALID_URL', "Cette adresse n'est pas une URL valide.");
  }
  if (url.protocol !== 'http:' && url.protocol !== 'https:') {
    throw new SafeFetchError('BLOCKED_SCHEME', 'Seules les adresses http et https sont acceptées.');
  }
  if (url.username || url.password) {
    throw new SafeFetchError('BLOCKED_CREDENTIALS', 'Les adresses avec identifiants ne sont pas acceptées.');
  }
  if (url.port && !['80', '443'].includes(url.port) && !allowAnyPortForTests) {
    throw new SafeFetchError('BLOCKED_PORT', 'Seuls les ports standards (80 et 443) sont acceptés.');
  }
  const host = url.hostname.replace(/^\[|\]$/g, '').replace(/\.$/, '');
  if (!host || BLOCKED_HOSTNAMES.test(host) || !host.includes('.') && !net.isIP(host)) {
    throw new SafeFetchError('BLOCKED_HOST', 'Cette adresse ne pointe pas vers un site public.');
  }
  if (net.isIP(host) && !isAllowedAddress(host)) {
    throw new SafeFetchError('BLOCKED_ADDRESS', 'Cette adresse ne pointe pas vers un site public.');
  }
  return url;
}

function makeLookup(isAllowedAddress) {
  return (hostname, options, callback) => {
    dns.lookup(hostname, { all: true, verbatim: true }, (err, addresses) => {
      if (err) return callback(err);
      const list = Array.isArray(addresses) ? addresses : [{ address: addresses, family: net.isIP(addresses) }];
      if (!list.length || list.some((a) => !isAllowedAddress(a.address))) {
        return callback(new SafeFetchError('BLOCKED_ADDRESS', 'Cette adresse ne pointe pas vers un site public.'));
      }
      const chosen = list[0];
      if (options && options.all) return callback(null, [chosen]);
      return callback(null, chosen.address, chosen.family);
    });
  };
}

function requestOnce(url, opts) {
  return new Promise((resolve, reject) => {
    const lib = url.protocol === 'https:' ? https : http;
    const host = url.hostname.replace(/^\[|\]$/g, '');
    if (net.isIP(host) && !opts.isAllowedAddress(host)) {
      return reject(new SafeFetchError('BLOCKED_ADDRESS', 'Cette adresse ne pointe pas vers un site public.'));
    }
    const req = lib.request(url, {
      method: 'GET',
      lookup: makeLookup(opts.isAllowedAddress),
      headers: {
        'User-Agent': opts.userAgent,
        Accept: opts.accept || 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.5',
        'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.7',
        'Accept-Encoding': 'identity',
      },
      timeout: opts.timeoutMs,
    });
    const deadline = setTimeout(() => req.destroy(new SafeFetchError('TIMEOUT', 'Le site a mis trop de temps à répondre.')), opts.timeoutMs);
    req.on('timeout', () => req.destroy(new SafeFetchError('TIMEOUT', 'Le site a mis trop de temps à répondre.')));
    req.on('error', (err) => { clearTimeout(deadline); reject(err); });
    req.on('response', (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        clearTimeout(deadline);
        res.resume();
        return resolve({ redirect: res.headers.location, status: res.statusCode });
      }
      const declared = Number(res.headers['content-length'] || 0);
      if (declared > opts.maxBytes) {
        clearTimeout(deadline);
        res.destroy();
        return reject(new SafeFetchError('TOO_LARGE', 'La page est trop lourde pour être analysée.'));
      }
      const chunks = [];
      let size = 0;
      res.on('data', (chunk) => {
        size += chunk.length;
        if (size > opts.maxBytes) {
          clearTimeout(deadline);
          res.destroy();
          return reject(new SafeFetchError('TOO_LARGE', 'La page est trop lourde pour être analysée.'));
        }
        chunks.push(chunk);
      });
      res.on('end', () => {
        clearTimeout(deadline);
        resolve({
          status: res.statusCode,
          headers: res.headers,
          body: Buffer.concat(chunks).toString('utf8'),
          bytes: size,
        });
      });
      res.on('error', (err) => { clearTimeout(deadline); reject(err); });
    });
    req.end();
  });
}

// Returns { url, status, headers, body, bytes }. Throws SafeFetchError on any refusal.
async function safeFetch(input, options = {}) {
  const opts = { ...DEFAULTS, isAllowedAddress: isPublicAddress, ...options };
  let url = assertSafeUrl(input, opts);
  for (let hop = 0; hop <= opts.maxRedirects; hop += 1) {
    let res;
    try {
      res = await requestOnce(url, opts);
    } catch (err) {
      if (err instanceof SafeFetchError) throw err;
      throw new SafeFetchError('NETWORK', "Impossible de joindre ce site.");
    }
    if (res.redirect) {
      let next;
      try { next = new URL(res.redirect, url); } catch { throw new SafeFetchError('BAD_REDIRECT', 'Redirection invalide.'); }
      url = assertSafeUrl(next, opts);
      continue;
    }
    return { url: url.toString(), ...res };
  }
  throw new SafeFetchError('TOO_MANY_REDIRECTS', 'Trop de redirections.');
}

module.exports = { safeFetch, assertSafeUrl, isPublicAddress, SafeFetchError };
