'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const http = require('http');
const { safeFetch, assertSafeUrl, isPublicAddress } = require('../src/audit/safeFetch');

test('refuses non-http schemes, credentials, odd ports and internal names', () => {
  for (const url of ['file:///etc/passwd', 'ftp://example.com', 'javascript:alert(1)', 'gopher://x.com',
    'http://user:pass@example.com', 'http://example.com:8080/', 'http://localhost/', 'http://foo.local/',
    'http://intranet/', 'http://metadata.internal/', 'not a url']) {
    assert.throws(() => assertSafeUrl(url), (e) => e.name === 'SafeFetchError', url);
  }
});

test('refuses private, loopback, link-local and metadata IP literals', () => {
  for (const url of ['http://127.0.0.1/', 'http://10.1.2.3/', 'http://172.16.0.1/', 'http://192.168.1.1/',
    'http://169.254.169.254/latest/meta-data', 'http://0.0.0.0/', 'http://100.64.0.1/', 'http://[::1]/',
    'http://[fd00::1]/', 'http://[fe80::1]/', 'http://[::ffff:127.0.0.1]/', 'http://[::ffff:a9fe:a9fe]/',
    'http://2130706433/', 'http://0x7f000001/', 'http://017700000001/']) {
    assert.throws(() => assertSafeUrl(url), (e) => e.name === 'SafeFetchError', url);
  }
});

test('isPublicAddress classifies addresses', () => {
  assert.equal(isPublicAddress('8.8.8.8'), true);
  assert.equal(isPublicAddress('23.227.38.65'), true);
  assert.equal(isPublicAddress('2606:4700::1111'), true);
  for (const ip of ['127.0.0.1', '10.0.0.1', '169.254.169.254', '192.168.0.10', '::1', '::', 'fc00::1', '::ffff:10.0.0.1', '64:ff9b::a00:1', '2002:7f00:1::1', 'nonsense']) {
    assert.equal(isPublicAddress(ip), false, ip);
  }
});

test('accepts normal public URLs', () => {
  assert.equal(assertSafeUrl('https://maboutique.fr/products/x').hostname, 'maboutique.fr');
});

function serve(handler) {
  return new Promise((resolve) => {
    const server = http.createServer(handler).listen(0, '127.0.0.1', () => resolve(server));
  });
}
// Test-only: allow exactly the local test server address, nothing else.
const onlyLoopback = (ip) => ip === '127.0.0.1';
const dns = require('dns');
const realLookup = dns.lookup;

test('blocks the connection when a public-looking hostname resolves to a private IP', async () => {
  dns.lookup = (host, opts, cb) => (host === 'rebind.example.com' ? cb(null, [{ address: '127.0.0.1', family: 4 }]) : realLookup(host, opts, cb));
  try {
    await assert.rejects(safeFetch('http://rebind.example.com/'), (e) => e.code === 'BLOCKED_ADDRESS');
  } finally {
    dns.lookup = realLookup;
  }
});

const internal = require('../src/audit/safeFetch');

test('redirect chain, size limit and timeout are enforced (local server, test hook)', async () => {
  let hits = 0;
  const big = 'x'.repeat(2048);
  const server = await serve((req, res) => {
    hits += 1;
    if (req.url === '/to-private') { res.writeHead(301, { Location: 'http://192.168.1.1/' }); return res.end(); }
    if (req.url === '/big') { res.writeHead(200, { 'Content-Type': 'text/html' }); return res.end(big); }
    if (req.url === '/slow') { setTimeout(() => { res.writeHead(200); res.end('late'); }, 1500); return undefined; }
    if (req.url === '/loop') { res.writeHead(302, { Location: '/loop' }); return res.end(); }
    res.writeHead(200, { 'Content-Type': 'text/html' });
    return res.end('<p>ok</p>');
  });
  const { port } = server.address();
  const base = `http://127.0.0.1:${port}`;
  const opts = { isAllowedAddress: onlyLoopback, allowAnyPortForTests: true };
  try {
    const ok = await internal.safeFetch(`${base}/`, opts);
    assert.equal(ok.status, 200);
    assert.match(ok.body, /ok/);
    await assert.rejects(internal.safeFetch(`${base}/to-private`, opts), (e) => e.code === 'BLOCKED_ADDRESS');
    await assert.rejects(internal.safeFetch(`${base}/big`, { ...opts, maxBytes: 1000 }), (e) => e.code === 'TOO_LARGE');
    await assert.rejects(internal.safeFetch(`${base}/slow`, { ...opts, timeoutMs: 300 }), (e) => e.code === 'TIMEOUT');
    await assert.rejects(internal.safeFetch(`${base}/loop`, opts), (e) => e.code === 'TOO_MANY_REDIRECTS');
    assert.ok(hits >= 5);
  } finally {
    server.close();
  }
});
