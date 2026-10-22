'use strict';
const { safeFetch: defaultFetch, assertSafeUrl, SafeFetchError } = require('./safeFetch');
const { isAllowed } = require('./robots');
const { extractHome, extractProduct } = require('./extract');
const { computeScore } = require('./score');
const { buildLeaks, resolveAssumptions } = require('./leaks');
const { writeLeaks } = require('./writer');

class AuditError extends Error {
  constructor(code, message, status = 400) {
    super(message);
    this.name = 'AuditError';
    this.code = code;
    this.status = status;
  }
}

function normalizeInputUrl(raw) {
  const value = String(raw || '').trim();
  if (!value || value.length > 2048) throw new AuditError('INVALID_URL', 'Indiquez l’adresse de votre boutique.');
  const withScheme = /^[a-z][a-z0-9+.-]*:\/\//i.test(value) ? value : `https://${value}`;
  try {
    return assertSafeUrl(withScheme);
  } catch (err) {
    if (err instanceof SafeFetchError) throw new AuditError(err.code, err.message);
    throw err;
  }
}

async function fetchHtml(url, fetchImpl, label) {
  let res;
  try {
    res = await fetchImpl(url, { timeoutMs: 7000 });
  } catch (err) {
    if (err instanceof SafeFetchError) throw new AuditError(err.code, `${label} : ${err.message}`, 422);
    throw err;
  }
  if (res.status >= 400) throw new AuditError('HTTP_ERROR', `${label} : le site a répondu avec une erreur (${res.status}).`, 422);
  const type = String(res.headers['content-type'] || '');
  if (type && !/html/i.test(type)) throw new AuditError('NOT_HTML', `${label} : ce n’est pas une page web.`, 422);
  return res;
}

async function loadRobots(origin, fetchImpl) {
  try {
    const res = await fetchImpl(new URL('/robots.txt', origin), { timeoutMs: 4000, maxBytes: 256 * 1024, accept: 'text/plain,*/*;q=0.5' });
    if (res.status >= 400 && res.status < 500) return '';
    if (res.status >= 500) return null;
    return res.body;
  } catch {
    return null;
  }
}

function pathOf(url) {
  const u = new URL(url);
  return `${u.pathname}${u.search}`;
}

// input: { url, monthlyVisitors?, averageOrderValue? }
// deps: { fetch?, writerClient? } (injected in tests)
async function runAudit(input, deps = {}) {
  const fetchImpl = deps.fetch || defaultFetch;
  const start = normalizeInputUrl(input.url);
  const robots = await loadRobots(start.origin, fetchImpl);
  if (robots === null) throw new AuditError('ROBOTS_UNAVAILABLE', 'Le fichier robots.txt du site est indisponible : nous préférons ne pas analyser la boutique sans lui.', 422);

  const startsOnProduct = /\/products\/[^/]+/.test(start.pathname);
  const homeUrl = new URL('/', start.origin).toString();
  if (!isAllowed(robots, '/')) throw new AuditError('ROBOTS_DISALLOWED', 'Le robots.txt de ce site interdit l’analyse de la page d’accueil.', 422);

  const homeRes = await fetchHtml(homeUrl, fetchImpl, 'Page d’accueil');
  const home = extractHome(homeRes.body, homeRes.url);

  let productUrl = startsOnProduct ? (() => { const u = new URL(start); u.search = ''; u.hash = ''; return u.toString(); })() : home.productUrl;
  if (!productUrl) throw new AuditError('NO_PRODUCT', 'Aucune fiche produit trouvée depuis l’accueil. Collez directement l’adresse d’une page produit.', 422);
  if (new URL(productUrl).origin !== new URL(homeRes.url).origin && new URL(productUrl).origin !== start.origin) {
    throw new AuditError('NO_PRODUCT', 'La fiche produit trouvée est sur un autre site. Collez directement l’adresse d’une page produit.', 422);
  }
  if (!isAllowed(robots, pathOf(productUrl))) throw new AuditError('ROBOTS_DISALLOWED', 'Le robots.txt de ce site interdit l’analyse de cette fiche produit.', 422);

  const productRes = await fetchHtml(productUrl, fetchImpl, 'Fiche produit');
  const product = extractProduct(productRes.body, productRes.url);

  const { score, categories, checks } = computeScore(home, product);
  const assumptions = resolveAssumptions(input, product);
  const leaks = buildLeaks(checks, assumptions);
  const written = await writeLeaks({ score, leaks, product, client: deps.writerClient });

  return {
    url: start.toString(),
    shopDomain: new URL(homeRes.url).hostname,
    productUrl: productRes.url,
    productName: product.name,
    isShopify: home.isShopify || product.isShopify,
    score,
    categories,
    checks,
    summary: written.summary,
    leaks: written.leaks,
    writer: written.writer,
    assumptions,
  };
}

module.exports = { runAudit, normalizeInputUrl, AuditError };
