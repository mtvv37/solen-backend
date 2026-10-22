'use strict';
// Maps failed checks to conversion "leaks" with a €/month range.
// Every number here is computed by code from explicit assumptions [hypothèse];
// the AI writer only phrases them and is not allowed to change them.

const DEFAULT_ASSUMPTIONS = {
  monthlyVisitors: 10000,
  conversionRate: 0.015,
  fallbackOrderValue: 50,
};

// Relative uplift ranges are Solen's internal orders of magnitude [hypothèse],
// not results from a study. They are shown to the merchant as such.
const CATALOG = {
  review_widget: { why: 'Sans avis visibles, le visiteur n’a que votre parole pour juger le produit.', title: 'Aucun avis client visible sur la fiche produit', uplift: [0.03, 0.08], fix: 'Afficher des avis (note + nombre) près du prix et du bouton d’achat.' },
  rating_shown: { why: 'Une note visible tôt aide le visiteur à se décider sans chercher plus loin.', title: 'La note moyenne n’est pas mise en avant', uplift: [0.01, 0.03], fix: 'Afficher la note étoilée sous le titre du produit.' },
  review_volume: { why: 'Quelques avis seulement rassurent moins qu’un volume qui montre que d’autres ont acheté.', title: 'Trop peu d’avis pour rassurer', uplift: [0.01, 0.03], fix: 'Relancer les clients après livraison pour collecter des avis.' },
  image_count: { why: 'En ligne, les photos remplacent l’essayage : peu de visuels laissent des questions sans réponse.', title: 'Trop peu de photos produit', uplift: [0.02, 0.05], fix: 'Viser 4 à 6 visuels : portés, détails, échelle, contexte.' },
  image_alt: { why: 'Les images sans description sont invisibles pour les lecteurs d’écran et moins bien référencées.', title: 'Images sans texte alternatif', uplift: [0.002, 0.01], fix: 'Décrire chaque image (accessibilité et référencement).' },
  description: { why: 'Une description courte laisse sans réponse les questions sur la matière, la taille ou l’usage.', title: 'Description produit trop courte', uplift: [0.01, 0.04], fix: 'Répondre aux questions avant achat : matière, taille, entretien, usage.' },
  price_clear: { why: 'Le prix n’est pas déclaré clairement dans le code de la page, ce qui gêne les moteurs et les comparateurs.', title: 'Prix difficile à lire pour les moteurs et les visiteurs', uplift: [0.01, 0.03], fix: 'Afficher clairement le prix et la devise, et les déclarer en données structurées.' },
  add_to_cart: { why: 'Nous n’avons pas trouvé de formulaire d’ajout au panier dans le code de la page.', title: 'Bouton d’ajout au panier non détecté', uplift: [0.05, 0.15], fix: 'Vérifier que le bouton « Ajouter au panier » est présent et fonctionnel.' },
  shipping_info: { why: 'Le coût et le délai de livraison sont parmi les premières questions avant d’acheter.', title: 'Délais et frais de livraison absents de la fiche', uplift: [0.02, 0.05], fix: 'Indiquer délai et coût de livraison près du bouton d’achat.' },
  returns_info: { why: 'Savoir qu’on peut renvoyer le produit réduit le risque perçu, surtout pour un premier achat.', title: 'Politique de retour invisible', uplift: [0.01, 0.04], fix: 'Mentionner les retours (délai, gratuité) sur la fiche produit.' },
  guarantee: { why: 'Une garantie visible rassure les visiteurs qui ne connaissent pas encore la marque.', title: 'Aucune garantie mise en avant', uplift: [0.005, 0.02], fix: 'Afficher la garantie ou le « satisfait ou remboursé ».' },
  secure_payment: { why: 'Une mention de paiement sécurisé rassure au moment de sortir sa carte.', title: 'Paiement sécurisé non signalé', uplift: [0.005, 0.015], fix: 'Ajouter une mention « paiement sécurisé » près du bouton d’achat.' },
  payment_icons: { why: 'Voir ses moyens de paiement habituels avant le panier évite une mauvaise surprise.', title: 'Moyens de paiement non affichés', uplift: [0.005, 0.02], fix: 'Afficher les logos des moyens de paiement acceptés.' },
  html_weight: { why: 'Une page lourde s’affiche plus lentement, surtout sur mobile en 4G.', title: 'Page produit lourde', uplift: [0.01, 0.03], fix: 'Alléger le thème et les sections inutilisées.' },
  script_count: { why: 'Chaque script ajoute du temps de chargement et des risques de conflit.', title: 'Trop de scripts chargés', uplift: [0.01, 0.03], fix: 'Supprimer les apps et scripts inutilisés.' },
  third_party: { why: 'Chaque app tierce charge son propre code et ralentit l’affichage.', title: 'Beaucoup de scripts tiers', uplift: [0.01, 0.03], fix: 'Faire l’inventaire des apps tierces et retirer les doublons.' },
  viewport: { why: 'Sans balise viewport, la page peut s’afficher en version bureau réduite sur mobile.', title: 'Page mal adaptée au mobile', uplift: [0.05, 0.1], fix: 'Déclarer un viewport mobile (balise meta viewport).' },
  cta_mobile: { why: 'D’après l’ordre du code, plusieurs photos passent avant le bouton d’achat : sur mobile, il est probablement sous la ligne de flottaison (estimation sans affichage de la page).', title: 'Bouton d’achat probablement trop bas sur mobile', uplift: [0.02, 0.06], fix: 'Tester un bouton plus haut ou un bouton collant sur mobile.' },
  variant_picker: { why: 'Une liste déroulante cache les tailles ou couleurs disponibles et ajoute un geste avant l’achat.', title: 'Tailles ou couleurs cachées dans une liste déroulante', uplift: [0.01, 0.04], fix: 'Tester des boutons ou pastilles visibles pour les variantes.' },
  dynamic_checkout: { why: 'Sans paiement express, chaque acheteur doit remplir tout le formulaire de commande.', title: 'Pas de paiement express', uplift: [0.01, 0.03], fix: 'Activer les boutons de paiement express (Shop Pay, Apple Pay…).' },
  quantity: { why: 'Sans sélecteur, acheter plusieurs exemplaires demande des allers-retours au panier.', title: 'Pas de sélecteur de quantité', uplift: [0.002, 0.01], fix: 'Ajouter un sélecteur de quantité si l’achat multiple a du sens.' },
  structured_data: { why: 'Les données produit incomplètes privent votre fiche d’informations enrichies dans Google.', title: 'Données produit structurées incomplètes', uplift: [0.005, 0.02], fix: 'Déclarer Product et Offer (prix, stock) en JSON-LD.' },
};

const fmt = (n) => new Intl.NumberFormat('fr-FR', { maximumFractionDigits: 0 }).format(n).replace(/\u202f|\u00a0/g, ' ');

function resolveAssumptions(input, product) {
  const visitors = Number(input.monthlyVisitors);
  const aov = Number(input.averageOrderValue);
  const notes = [];
  const monthlyVisitors = Number.isFinite(visitors) && visitors > 0 ? Math.round(visitors) : DEFAULT_ASSUMPTIONS.monthlyVisitors;
  notes.push(Number.isFinite(visitors) && visitors > 0 ? `Trafic mensuel indiqué : ${fmt(monthlyVisitors)} visiteurs.` : `Trafic mensuel supposé : ${fmt(monthlyVisitors)} visiteurs [hypothèse].`);
  const conversionRate = DEFAULT_ASSUMPTIONS.conversionRate;
  notes.push(`Taux de conversion supposé : ${(conversionRate * 100).toFixed(1).replace('.', ',')} % [hypothèse].`);
  let averageOrderValue;
  if (Number.isFinite(aov) && aov > 0) {
    averageOrderValue = aov;
    notes.push(`Panier moyen indiqué : ${fmt(aov)} €.`);
  } else if (product.price.value) {
    averageOrderValue = product.price.value;
    notes.push(`Panier moyen supposé égal au prix du produit audité : ${fmt(product.price.value)} ${product.price.currency && product.price.currency !== 'EUR' ? product.price.currency : '€'} [hypothèse].`);
  } else {
    averageOrderValue = DEFAULT_ASSUMPTIONS.fallbackOrderValue;
    notes.push(`Panier moyen supposé : ${averageOrderValue} € [hypothèse].`);
  }
  notes.push('Gains relatifs par fuite : ordres de grandeur internes à Solen, non issus d’une étude [hypothèse]. Les fuites ne s’additionnent pas.');
  const monthlyRevenue = monthlyVisitors * conversionRate * averageOrderValue;
  return { monthlyVisitors, conversionRate, averageOrderValue, monthlyRevenue, notes };
}

function roundEuro(n) {
  if (n < 100) return Math.round(n / 5) * 5;
  if (n < 1000) return Math.round(n / 10) * 10;
  return Math.round(n / 50) * 50;
}

function buildLeaks(checks, assumptions) {
  return checks
    .filter((c) => !c.passed && CATALOG[c.id])
    .map((c) => {
      const entry = CATALOG[c.id];
      const severity = (c.max - c.points) / c.max; // 1 = fully missing, 0.5 = partial
      const low = roundEuro(assumptions.monthlyRevenue * entry.uplift[0] * severity);
      const high = roundEuro(assumptions.monthlyRevenue * entry.uplift[1] * severity);
      return {
        id: c.id,
        category: c.category,
        title: entry.title,
        why: entry.why,
        fix: entry.fix,
        facts: c.facts,
        estimate: true,
        monthlyLossEur: { low, high },
        upliftRange: entry.uplift,
        sortKey: (entry.uplift[0] + entry.uplift[1]) / 2 * severity,
      };
    })
    .sort((a, b) => b.sortKey - a.sortKey)
    .slice(0, 5)
    .map(({ sortKey, ...rest }) => rest);
}

module.exports = { buildLeaks, resolveAssumptions, CATALOG, DEFAULT_ASSUMPTIONS };
