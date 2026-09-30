// Solen — Market sizing & GTM deck (MBB style). Output: docs/Solen_Market_GTM.pptx
const pptxgen = require("pptxgenjs");
const path = require("path");

const OUT = process.argv[2] || path.join(__dirname, "Solen_Market_GTM.pptx");

// ---------- Palette (Solen heatmap teal + ink) ----------
const INK = "0E1A24";     // titles, dark slides
const TEAL = "1FB8A0";    // Solen accent (from heatmap UI)
const TEAL_D = "12806F";  // darker teal for text on white
const SLATE = "5B6B78";   // secondary text
const MIST = "EEF3F5";    // card tint
const LINE = "C9D3D9";
const AMBER = "E0A030";   // "à vérifier" flag
const RED = "C8553D";
const WHITE = "FFFFFF";
const FONT = "Arial";

// ---------- Data (every figure is sourced or labelled as hypothesis) ----------
const SL_TOTAL = 2865709;          // Store Leads, live Shopify stores, 03/07/2026
const SL_US = 1088283, SL_CA = 121955, SL_UK = 197736, SL_AU = 119745, SL_IN = 114995;
const NA = SL_US + SL_CA;          // 1,210,238
const REST = SL_TOTAL - NA;        // allocated with regional merchant split 31/16/5 (secondary source, to verify)
const EMEA = Math.round(REST * 31 / 52);
const APAC = Math.round(REST * 16 / 52);
const LATAM = REST - EMEA - APAC;
const REG = [
  { k: "Amérique du Nord", n: NA },
  { k: "Europe (EMEA)", n: EMEA },
  { k: "APAC", n: APAC },
  { k: "LatAm", n: LATAM },
];
const SCEN = {
  bas: { share: 0.05, spend: 600 },
  central: { share: 0.10, spend: 1500 },
  haut: { share: 0.15, spend: 3000 },
};
const SOM_CLIENTS = { bas: 50, central: 200, haut: 600 };
const PRICE_Y = 2400; // ~200 $/mois, équivalent approx. du tarif pilote 190 €/mois (FX à vérifier)

const fmtK = (x) => Math.round(x / 1000).toLocaleString("fr-FR").replace(/ | /g, " ") + " k";
const fmtN = (x) => Math.round(x).toLocaleString("fr-FR").replace(/ | /g, " ");
const fmtM = (x) => (x >= 1e9 ? (x / 1e9).toFixed(2).replace(".", ",") + " Md$" : (x / 1e6).toFixed(0) + " M$");
const tam = (s, n = SL_TOTAL) => n * SCEN[s].share * SCEN[s].spend;
const sam = (s) => (NA + EMEA) * SCEN[s].share * SCEN[s].spend;
const som = (s) => SOM_CLIENTS[s] * PRICE_Y;

// ---------- Deck scaffolding ----------
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625
pres.title = "Solen — Marché & go-to-market";
pres.author = "Solen";

let pageNo = 0;
const TRACK = ["Marché", "Cible", "Approche", "Risques"];
function base(section, title) {
  const s = pres.addSlide();
  pageNo++;
  s.background = { color: WHITE };
  if (section) {
    s.addText(section.toUpperCase(), {
      x: 0.5, y: 0.22, w: 5, h: 0.22, fontFace: FONT, fontSize: 8, bold: true,
      color: TEAL_D, charSpacing: 2, margin: 0, isTextBox: true,
    });
    // Page tracker: current section in accent, others muted
    const cur = TRACK.find((t) => section.startsWith(t)) || (section.startsWith("Hypothèses") ? "Risques" : null);
    if (cur) {
      s.addText(TRACK.map((t, i) => ({
        text: t + (i < TRACK.length - 1 ? "   ·   " : ""),
        options: { color: t === cur ? TEAL_D : "A7B3BC", bold: t === cur },
      })), { x: 5.5, y: 0.22, w: 4, h: 0.22, fontFace: FONT, fontSize: 8, align: "right", margin: 0, isTextBox: true });
    }
  }
  s.addText(title, {
    x: 0.5, y: 0.44, w: 9, h: 0.7, fontFace: FONT, fontSize: 17, bold: true,
    color: INK, valign: "top", margin: 0, isTextBox: true,
  });
  s.addText(String(pageNo), {
    x: 9.1, y: 5.3, w: 0.4, h: 0.2, fontFace: FONT, fontSize: 8, color: SLATE,
    align: "right", margin: 0, isTextBox: true,
  });
  return s;
}
function source(s, txt) {
  s.addText(txt, {
    x: 0.5, y: 5.08, w: 8.5, h: 0.42, fontFace: FONT, fontSize: 7, color: SLATE,
    valign: "bottom", margin: 0, isTextBox: true,
  });
}
function flag(s, x, y, w, txt) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h: 0.26, fill: { color: "FBF1DF" }, line: { color: AMBER, width: 0.75 }, rectRadius: 0.05,
  });
  s.addText(txt, {
    x: x + 0.08, y, w: w - 0.16, h: 0.26, fontFace: FONT, fontSize: 8, color: "7A5410",
    valign: "middle", margin: 0, isTextBox: true,
  });
}
function card(s, x, y, w, h, fill = MIST) {
  s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: fill }, line: { color: fill } });
}
function bullets(s, items, opts) {
  s.addText(
    items.map((t, i) => {
      const o = { bullet: { indent: 12 }, breakLine: i < items.length - 1, paraSpaceAfter: 4 };
      if (typeof t === "string") return { text: t, options: o };
      return { text: t.text, options: { ...o, bold: !!t.bold, color: t.color } };
    }),
    { fontFace: FONT, fontSize: 10.5, color: INK, valign: "top", margin: 0, isTextBox: true, ...opts }
  );
}
function txt(s, text, opts) {
  s.addText(text, { fontFace: FONT, fontSize: 10.5, color: INK, valign: "top", margin: 0, isTextBox: true, ...opts });
}
function table(s, rows, opts) {
  const header = rows[0].map((c) => ({
    text: c, options: { bold: true, color: WHITE, fill: { color: INK }, fontSize: 9 },
  }));
  const body = rows.slice(1).map((r, ri) =>
    r.map((c) => {
      const cell = typeof c === "object" ? c : { text: String(c) };
      return { text: cell.text, options: { fontSize: 9, color: INK, fill: { color: ri % 2 ? WHITE : MIST }, ...(cell.options || {}) } };
    })
  );
  s.addTable([header, ...body], {
    fontFace: FONT, border: { type: "solid", pt: 0.5, color: LINE }, valign: "middle", margin: 0.05, ...opts,
  });
}
function darkSlide(kicker, title, sub) {
  const s = pres.addSlide();
  pageNo++;
  s.background = { color: INK };
  s.addShape(pres.shapes.OVAL, { x: 7.6, y: -1.2, w: 4, h: 4, fill: { color: TEAL, transparency: 85 }, line: { color: TEAL, transparency: 85 } });
  s.addText(kicker.toUpperCase(), { x: 0.6, y: 1.6, w: 8, h: 0.3, fontFace: FONT, fontSize: 10, bold: true, color: TEAL, charSpacing: 3, margin: 0, isTextBox: true });
  s.addText(title, { x: 0.6, y: 1.95, w: 8.4, h: 1.3, fontFace: FONT, fontSize: 28, bold: true, color: WHITE, valign: "top", margin: 0, isTextBox: true });
  if (sub) s.addText(sub, { x: 0.6, y: 3.35, w: 8.2, h: 0.9, fontFace: FONT, fontSize: 12, color: "B8C7D1", valign: "top", margin: 0, isTextBox: true });
  return s;
}

// ================= 1. Title =================
{
  const s = darkSlide(
    "Solen · document de travail · septembre 2026",
    "Marché et go-to-market : où Solen doit jouer, et comment y entrer seul",
    "Dimensionnement intercontinental, ICP par région, approche inspirée de Tally.\nTous les choix sont des hypothèses : aucune n'est encore validée sur le terrain."
  );
  s.addNotes("Deck construit à partir de docs/SOLEN_CONTEXT.md et docs/GTM_STRATEGY.md. Niveau de preuve global : P0–P1 (desk research, aucune donnée client).");
}

// ================= 2. SCQA opening =================
{
  const s = base("Contexte", "Les marchands ont les données, pas le temps d'en tirer des tests : c'est l'espace de Solen");
  const rows = [
    ["S", "Situation", `${fmtN(SL_TOTAL)} boutiques Shopify actives (Store Leads, 2026). Les données de comportement existent déjà : GA4, Shopify Analytics, Hotjar.`, false],
    ["C", "Complication", "Transformer ces données en modifications testées demande du temps et une expertise que les petites équipes n'ont pas. C'est l'hypothèse centrale de Solen, pas encore validée.", false],
    ["Q", "Question", "Le marché est-il assez grand, qui attaquer d'abord, et comment l'atteindre seul, sans budget ?", false],
    ["R", "Réponse", "Oui en ordre de grandeur. L'Europe francophone d'abord. Build in public, audit gratuit et concierge plutôt qu'un modèle freemium viral.", true],
  ];
  rows.forEach(([l, h, b, hi], i) => {
    const y = 1.35 + i * 0.9;
    s.addShape(pres.shapes.OVAL, { x: 0.5, y: y + 0.12, w: 0.55, h: 0.55, fill: { color: hi ? TEAL : INK }, line: { color: hi ? TEAL : INK } });
    txt(s, l, { x: 0.5, y: y + 0.12, w: 0.55, h: 0.55, align: "center", valign: "middle", bold: true, fontSize: 14, color: hi ? INK : WHITE });
    txt(s, h, { x: 1.25, y: y + 0.1, w: 1.6, h: 0.6, bold: true, fontSize: 11, valign: "middle", color: hi ? TEAL_D : INK });
    card(s, 2.95, y, 6.55, 0.78, hi ? "E3F5F1" : MIST);
    txt(s, b, { x: 3.1, y, w: 6.3, h: 0.78, fontSize: 10, valign: "middle" });
  });
  source(s, "Sources : Store Leads (juillet 2026) ; SOLEN_CONTEXT.md §4 (problème), §47 (questions ouvertes).");
}

// ================= 3. Executive summary =================
{
  const s = base("Synthèse", "Commencer par l'Europe francophone, en concierge, sur un marché central estimé à ~430 M$");
  const reasons = [
    ["Marché", "Le marché justifie l'effort, pas encore une levée de fonds.", `TAM central ${fmtM(tam("central"))} (${fmtM(tam("bas"))} à ${fmtM(tam("haut"))}) ; objectif à 3 ans ~0,5 M$ d'ARR. Deux hypothèses restent à vérifier.`],
    ["Cible", "L'Europe francophone est la seule région où un fondateur seul peut apprendre vite.", "L'Amérique du Nord pèse ~42 % des boutiques, mais l'accès y est faible sans réseau ni budget."],
    ["Approche", "De Tally, garder le build in public et le contenu ; remplacer le badge viral par un audit gratuit plafonné et un concierge.", "À 2 % de conversion, 200 clients exigeraient 10 000 boutiques gratuites."],
  ];
  reasons.forEach(([k, claim, proof], i) => {
    const y = 1.35 + i * 0.95;
    txt(s, k.toUpperCase(), { x: 0.5, y: y + 0.05, w: 1.3, h: 0.3, bold: true, fontSize: 9, color: TEAL_D, charSpacing: 1 });
    txt(s, claim, { x: 1.85, y, w: 7.65, h: 0.4, bold: true, fontSize: 11.5 });
    txt(s, proof, { x: 1.85, y: y + 0.4, w: 7.65, h: 0.4, fontSize: 9.5, color: SLATE });
    if (i < 2) s.addShape(pres.shapes.LINE, { x: 0.5, y: y + 0.88, w: 9, h: 0, line: { color: LINE, width: 0.75 } });
  });
  card(s, 0.5, 4.25, 9, 0.75, INK);
  txt(s, "DÉCISION DEMANDÉE", { x: 0.65, y: 4.25, w: 1.6, h: 0.75, bold: true, fontSize: 9, color: TEAL, valign: "middle" });
  txt(s, "90 jours sur la France, la Belgique et la Suisse romande, en concierge, à 0 € de budget. Mesurer H1 et H3 dès la semaine 1. Amérique du Nord seulement après au moins 2 clients payants.", { x: 2.3, y: 4.25, w: 7.05, h: 0.75, fontSize: 10, color: WHITE, valign: "middle" });
  source(s, "Sources : Store Leads (juillet 2026) ; rapports A/B testing (2025) ; blog Tally. Détail, source et niveau de preuve sur chaque slide.");
}

// ================= 4. Issue tree =================
{
  const s = base("Structure du problème", "Trois questions décident de la suite : taille du marché, cible de départ, mode d'accès");
  const root = { x: 0.5, y: 2.45, w: 1.9, h: 1.1 };
  card(s, root.x, root.y, root.w, root.h, INK);
  txt(s, "Solen peut-il construire une activité rentable en optimisant des boutiques Shopify existantes ?", { x: root.x + 0.1, y: root.y + 0.05, w: root.w - 0.2, h: root.h - 0.1, color: WHITE, fontSize: 9, bold: true, valign: "middle" });
  const branches = [
    { t: "1. Le marché est-il assez grand ?", subs: ["Combien de boutiques ont assez de trafic ?", "Combien dépensent-elles déjà en CRO, analytics et tests ?", "Le top-down confirme-t-il l'ordre de grandeur ?"] },
    { t: "2. Qui attaquer d'abord ?", subs: ["Quel ICP ressent le plus le problème ?", "Quelle région combine taille, accès et coût du problème ?", "Dans quel ordre étendre ?"] },
    { t: "3. Comment l'atteindre seul et sans budget ?", subs: ["Quels leviers de Tally se transposent ?", "Lesquels ne se transposent pas, et quoi à la place ?", "Quels risques et hypothèses tester d'abord ?"] },
  ];
  branches.forEach((b, i) => {
    const y = 1.35 + i * 1.22;
    s.addShape(pres.shapes.LINE, { x: root.x + root.w, y: root.y + root.h / 2, w: 0.35, h: 0, line: { color: LINE, width: 1 } });
    s.addShape(pres.shapes.LINE, { x: 2.75, y: Math.min(y + 0.45, root.y + root.h / 2), w: 0, h: Math.abs(y + 0.45 - (root.y + root.h / 2)), line: { color: LINE, width: 1 } });
    s.addShape(pres.shapes.LINE, { x: 2.75, y: y + 0.45, w: 0.2, h: 0, line: { color: LINE, width: 1 } });
    card(s, 2.95, y + 0.1, 2.4, 0.7, INK);
    txt(s, b.t, { x: 3.05, y: y + 0.1, w: 2.2, h: 0.7, color: WHITE, bold: true, fontSize: 10, valign: "middle" });
    s.addShape(pres.shapes.LINE, { x: 5.35, y: y + 0.45, w: 0.25, h: 0, line: { color: LINE, width: 1 } });
    card(s, 5.6, y + 0.02, 3.9, 0.86);
    bullets(s, b.subs, { x: 5.7, y: y + 0.08, w: 3.75, h: 0.78, fontSize: 9 });
    txt(s, ["Partie 1", "Partie 2", "Partie 3"][i], { x: 5.6, y: y + 0.9, w: 3.9, h: 0.2, fontSize: 7.5, color: SLATE, align: "right" });
  });
  source(s, "Arbre MECE construit à partir des questions ouvertes de SOLEN_CONTEXT.md §47 (marché, ICP, GTM). Les trois branches structurent les trois parties du document.");
}

// ================= 5. Section divider =================
darkSlide("Partie 1 · Marché", "Un marché réel mais modeste, dont la taille dépend de deux hypothèses non vérifiées", "Bottom-up par région, contrôle top-down, trois scénarios.\nChaque chiffre porte sa source ; chaque hypothèse est affichée comme telle.");

// ================= 6. Stores by region (chart) =================
{
  const s = base("Marché · boutiques", "L'Amérique du Nord concentre ~42 % des boutiques Shopify actives, l'Europe environ un tiers");
  s.addChart(pres.charts.BAR, [{ name: "Boutiques actives", labels: REG.map((r) => r.k), values: REG.map((r) => Math.round(r.n / 1000)) }], {
    x: 0.5, y: 1.35, w: 5.4, h: 3.6, barDir: "bar", chartColors: [TEAL, "A7B3BC", "A7B3BC", "A7B3BC"],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 10, dataLabelColor: INK, dataLabelFormatCode: "#,##0\" k\"",
    catAxisLabelColor: INK, catAxisLabelFontSize: 10, valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: false, showTitle: true, title: "Boutiques Shopify actives par région (milliers)", titleFontSize: 10, titleColor: SLATE,
    catAxisOrientation: "maxMin",
  });
  card(s, 6.2, 1.35, 3.3, 3.6);
  txt(s, "Comptages pays sourcés (Store Leads, T2 2026)", { x: 6.35, y: 1.45, w: 3.0, h: 0.3, bold: true, fontSize: 9.5 });
  table(s, [
    ["Pays", "Boutiques"],
    ["États-Unis", fmtN(SL_US)],
    ["Royaume-Uni", fmtN(SL_UK)],
    ["Canada", fmtN(SL_CA)],
    ["Australie", fmtN(SL_AU)],
    ["Inde", fmtN(SL_IN)],
    ["France, Allemagne, Brésil…", { text: "à vérifier", options: { color: "7A5410", bold: true } }],
  ], { x: 6.35, y: 1.8, w: 3.0, colW: [1.8, 1.2] });
  txt(s, "Hors Amérique du Nord, la répartition applique le split 31 / 16 / 5 (EMEA / APAC / LatAm) au reliquat. « Europe » inclut donc le Moyen-Orient et l'Afrique.", { x: 6.35, y: 4.0, w: 3.0, h: 0.9, fontSize: 8.5, color: SLATE });
  source(s, "Sources : Store Leads, 03/07/2026 (via storeinspect.com / ecomm.design) pour le total et les pays ; répartition régionale 44/31/16/5/5 attribuée au 10-K Shopify FY2025 par 3plinsider.com : source secondaire, à vérifier (possible confusion avec le chiffre d'affaires par zone).");
}

// ================= 7. Hypotheses & scenarios table =================
{
  const s = base("Marché · hypothèses", "Deux hypothèses non vérifiées font varier le TAM d'un facteur 15 : les mesurer d'abord");
  txt(s, [
    { text: "TAM = boutiques × part > 10k visiteurs × dépense annuelle  →  ", options: { color: SLATE } },
    { text: `${fmtM(tam("bas"))}  ·  ${fmtM(tam("central"))}  ·  ${fmtM(tam("haut"))}`, options: { bold: true, color: TEAL_D } },
    { text: "  (bas · central · haut)", options: { color: SLATE } },
  ], { x: 0.5, y: 1.3, w: 9, h: 0.3, fontSize: 9.5 });
  table(s, [
    ["Paramètre", "Bas", "Central", "Haut", "Statut", "Comment la vérifier"],
    ["Boutiques Shopify actives", fmtN(SL_TOTAL), fmtN(SL_TOTAL), fmtN(SL_TOTAL), { text: "Sourcé (2026)", options: { color: TEAL_D, bold: true } }, "Store Leads, mise à jour trimestrielle"],
    ["Part > 10k visiteurs/mois", "5 %", "10 %", "15 %", { text: "À vérifier", options: { color: "7A5410", bold: true } }, "Aucune source publique : échantillon de 500 boutiques (Store Leads / Similarweb)"],
    ["Dépense annuelle CRO + analytics + tests / boutique", "600 $", "1 500 $", "3 000 $", { text: "À vérifier", options: { color: "7A5410", bold: true } }, "Aucun chiffre de marché : interviews (§23), grilles Hotjar / VWO / AB Tasty"],
    ["Régions servies (SAM)", "NA + Europe", "NA + Europe", "NA + Europe", { text: "Choix", options: { color: SLATE, bold: true } }, "Langues maîtrisées, fuseaux, Shopify dominant"],
    ["Clients payants à 3 ans (SOM)", "50", "200", "600", { text: "Hypothèse", options: { color: "7A5410", bold: true } }, "Entonnoir des 90 jours (GTM_STRATEGY §5)"],
    ["Prix annuel", "2 400 $", "2 400 $", "2 400 $", { text: "Hypothèse", options: { color: "7A5410", bold: true } }, "≈ tarif pilote 190 €/mois ; taux de change à vérifier"],
  ], { x: 0.5, y: 1.72, w: 9, colW: [2.1, 0.95, 0.95, 0.95, 1.15, 2.9], rowH: 0.38 });
  flag(s, 0.5, 4.62, 9, "Même dépense par boutique dans toutes les régions : simplification. Les dépenses sont probablement plus élevées en Amérique du Nord (non démontré).");
  source(s, "Sources : Store Leads, 03/07/2026 (2 865 709 boutiques live ; les comptages de 6–9 M incluent essais et boutiques parquées) ; SOLEN_CONTEXT.md §12 (seuil de 10k = seuil de travail, non statistique), §23 ; GTM_STRATEGY.md §4.4.");
}

// ================= 8. TAM / SAM / SOM =================
{
  const s = base("Marché · TAM / SAM / SOM", `TAM central ~${fmtM(tam("central"))}, SOM à 3 ans ~0,5 M$ d'ARR : un marché rentable, pas encore « VC »`);
  // Nested bars (central) left
  const vals = [["TAM", tam("central"), "Boutiques > 10k visiteurs, monde, dépense actuelle"], ["SAM", sam("central"), "Amérique du Nord + Europe"], ["SOM (3 ans)", som("central"), "200 clients × 2 400 $/an"]];
  vals.forEach(([k, v, d], i) => {
    const y = 1.45 + i * 1.1;
    const w = Math.max(0.35, 4.6 * Math.sqrt(v / tam("central")));
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y, w, h: 0.8, fill: { color: [INK, TEAL_D, TEAL][i] }, line: { color: WHITE } });
    txt(s, k, { x: 0.6, y: y + 0.05, w: 1.4, h: 0.3, color: WHITE, bold: true, fontSize: 10 });
    txt(s, v >= 1e6 ? fmtM(v) : (v / 1e3).toFixed(0) + " k$", { x: 0.5 + w + 0.15, y: y + 0.08, w: 1.4, h: 0.4, bold: true, fontSize: 16, color: INK });
    txt(s, d, { x: 0.5 + w + 0.15, y: y + 0.45, w: 3.2, h: 0.3, fontSize: 8.5, color: SLATE });
  });
  // Scenario table right
  table(s, [
    ["", "Bas", "Central", "Haut"],
    ["TAM", fmtM(tam("bas")), fmtM(tam("central")), fmtM(tam("haut"))],
    ["SAM", fmtM(sam("bas")), fmtM(sam("central")), fmtM(sam("haut"))],
    ["SOM (ARR à 3 ans)", (som("bas") / 1e3).toFixed(0) + " k$", (som("central") / 1e3).toFixed(0) + " k$", (som("haut") / 1e6).toFixed(2).replace(".", ",") + " M$"],
    ["SOM / boutiques SAM", (SOM_CLIENTS.bas / ((NA + EMEA) * SCEN.bas.share) * 100).toFixed(2).replace(".", ",") + " %", (SOM_CLIENTS.central / ((NA + EMEA) * SCEN.central.share) * 100).toFixed(2).replace(".", ",") + " %", (SOM_CLIENTS.haut / ((NA + EMEA) * SCEN.haut.share) * 100).toFixed(2).replace(".", ",") + " %"],
  ], { x: 5.9, y: 1.45, w: 3.6, colW: [1.2, 0.8, 0.8, 0.8], rowH: 0.36 });
  txt(s, "Lecture : même en haut de fourchette, le SOM reste inférieur à 0,2 % des boutiques adressables. Le plafond ne vient pas du marché mais de la capacité de vente d'un fondateur seul.", { x: 5.9, y: 3.45, w: 3.6, h: 1.0, fontSize: 9, color: INK });
  flag(s, 5.9, 4.5, 3.6, "Part > 10k, dépense, clients et prix : hypothèses à vérifier");
  source(s, "Calcul : boutiques (Store Leads, 2026) × part > 10k visiteurs × dépense annuelle (hypothèses, slide 7). SAM = Amérique du Nord + Europe (EMEA). Surfaces de gauche proportionnelles à la valeur (échelle racine carrée pour la lisibilité).");
}

// ================= 9. TAM by region chart =================
{
  const s = base("Marché · régions", "L'Amérique du Nord et l'Europe pèsent ~77 % du TAM ; l'APAC et la LatAm attendront");
  const f = (sc) => REG.map((r) => +(tam(sc, r.n) / 1e6).toFixed(0));
  s.addChart(pres.charts.BAR, [
    { name: "Bas", labels: REG.map((r) => r.k), values: f("bas") },
    { name: "Central", labels: REG.map((r) => r.k), values: f("central") },
    { name: "Haut", labels: REG.map((r) => r.k), values: f("haut") },
  ], {
    x: 0.5, y: 1.35, w: 6.2, h: 3.65, barDir: "col", barGrouping: "clustered", chartColors: ["D5DDE2", TEAL, SLATE],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 8, dataLabelColor: INK,
    catAxisLabelColor: INK, catAxisLabelFontSize: 9, valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: true, legendPos: "t", legendFontSize: 9, showTitle: true, title: "TAM par région et par scénario (M$)", titleFontSize: 10, titleColor: SLATE,
  });
  card(s, 7.0, 1.35, 2.5, 3.65);
  const shareNAEU = (NA + EMEA) / SL_TOTAL;
  txt(s, Math.round(shareNAEU * 100) + " %", { x: 7.15, y: 1.5, w: 2.2, h: 0.7, fontSize: 36, bold: true, color: TEAL_D });
  txt(s, "du TAM en Amérique du Nord + Europe (mêmes hypothèses dans toutes les régions)", { x: 7.15, y: 2.25, w: 2.2, h: 0.7, fontSize: 9 });
  txt(s, "Si la dépense par boutique est plus forte en Amérique du Nord (probable, non démontré), cette part augmente. En LatAm, Shopify est concurrencé par des plateformes locales (Tiendanube / Nuvemshop, VTEX) : part de marché à vérifier.", { x: 7.15, y: 3.05, w: 2.2, h: 1.9, fontSize: 8.5, color: SLATE });
  source(s, "Calcul : boutiques par région (slide 6) × hypothèses de part > 10k et de dépense (slide 7). Répartition hors Amérique du Nord : source secondaire, à vérifier.");
}

// ================= 10. Top-down control =================
{
  const s = base("Marché · contrôle top-down", "Le top-down confirme l'ordre de grandeur, mais les estimations varient de 1 à 10");
  const tops = [
    ["Bottom-up Solen (central)", +(tam("central") / 1e9).toFixed(2)],
    ["Business Research Insights (2025)", 0.85],
    ["Research and Markets (2025)", 1.30],
    ["Spherical Insights (2025)", 1.48],
    ["Credence Research (2024)", 8.18],
  ];
  s.addChart(pres.charts.BAR, [{ name: "Md$", labels: tops.map((t) => t[0]), values: tops.map((t) => t[1]) }], {
    x: 0.5, y: 1.35, w: 5.6, h: 3.1, barDir: "bar", chartColors: [TEAL, "A7B3BC", "A7B3BC", "A7B3BC", "D5DDE2"],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 10, dataLabelColor: INK, dataLabelFormatCode: "0.00\" Md$\"",
    catAxisLabelColor: INK, catAxisLabelFontSize: 9, valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: false, showTitle: true, title: "Marché mondial des logiciels d'A/B testing (Md$) vs bottom-up Solen", titleFontSize: 10, titleColor: SLATE, catAxisOrientation: "maxMin",
  });
  txt(s, `Bottom-up : fourchette ${fmtM(tam("bas"))} à ${fmtM(tam("haut"))}, Shopify seul. Credence (8,18 Md$) : outlier, périmètre à vérifier.`, { x: 0.5, y: 4.5, w: 5.6, h: 0.4, fontSize: 9, color: SLATE });
  card(s, 6.4, 1.35, 3.1, 3.55);
  txt(s, "Pourquoi les deux approches ne se comparent pas terme à terme", { x: 6.55, y: 1.45, w: 2.8, h: 0.5, bold: true, fontSize: 10 });
  bullets(s, [
    "Le top-down couvre toutes les plateformes et tous les segments, surtout les grands comptes ; le bottom-up ne couvre que Shopify.",
    "Le bottom-up inclut l'analytics comportemental (type Hotjar), exclu du top-down A/B testing.",
    "L'estimation Credence (8,18 Md$) est un outlier : périmètre probablement plus large, à vérifier.",
    "Aucun rapport « CRO software » consolidé n'a pu être sourcé : à vérifier.",
  ], { x: 6.55, y: 2.0, w: 2.85, h: 2.85, fontSize: 8.5 });
  source(s, "Sources : Business Research Insights (0,85 Md$, 2025) ; Research and Markets (1,30 Md$, 2025 ; 2,73 Md$ en 2032, TCAC 11,2 %) ; Spherical Insights (1,48 Md$, 2025 ; 4,26 Md$ en 2035) ; Credence Research (8,18 Md$, 2024). Chiffres relevés via les pages de présentation des rapports, non achetés.");
}

// ================= 11. Section 2 =================
darkSlide("Partie 2 · Cible", "Un même ICP partout ; l'Europe francophone d'abord, pour apprendre vite", "Le profil de boutique qui souffre du problème est comparable d'une région à l'autre.\nCe qui change, c'est la capacité d'un fondateur seul à l'atteindre et à apprendre vite.");

// ================= 12. ICP by region table =================
{
  const s = base("Cible · ICP par région", "Même ICP partout ; l'Europe francophone est la seule région accessible dès maintenant");
  table(s, [
    ["", "Amérique du Nord", "Europe (FR d'abord)", "APAC (Australie)", "LatAm"],
    ["ICP", "Marque DTC Shopify, 20k–150k visiteurs, paie Meta / Google Ads, pas de CRO interne", "Idem ; décideur = fondateur ou 1er responsable e-commerce", "Idem, marques anglophones (AU / NZ)", "Idem, Brésil / Mexique"],
    ["Taille (TAM central)", fmtM(tam("central", NA)), fmtM(tam("central", EMEA)) + " (EMEA)", fmtM(tam("central", APAC)) + " (APAC total)", fmtM(tam("central", LATAM))],
    ["Accessibilité pour le fondateur", "Moyenne : anglais, fuseau décalé, marché saturé de sollicitations", "Forte : langue, réseau SKEMA, communautés FR, même fuseau", "Faible : fuseau opposé, pas de réseau", "Faible : langue (PT / ES), pas de réseau"],
    ["Coût actuel du problème", "Élevé : coût du trafic, agences chères (à vérifier)", "Moyen : budgets plus bas, agences moins chères (à vérifier)", "Moyen–élevé (à vérifier)", "Bas–moyen (à vérifier)"],
    ["Concurrence perçue", "Très forte (apps Shopify CRO, Hotjar, VWO, Amboras)", "Forte mais peu d'offres en français (à vérifier)", "Forte", "Plateformes locales dominantes"],
    ["Frein spécifique", "Cycle de confiance, références exigées", "RGPD / consentement", "Support en décalé", "Shopify minoritaire (à vérifier)"],
  ], { x: 0.5, y: 1.3, w: 9, colW: [1.5, 1.95, 1.95, 1.8, 1.8], rowH: 0.42, fontSize: 8 });
  source(s, "Sources : TAM central (slides 6–9) ; accessibilité et coût : hypothèses fondateur (P0), à confronter aux interviews. « Europe » = EMEA dans le calcul de taille.");
}

// ================= 13. Region scoring =================
{
  const s = base("Cible · priorisation", "L'Europe francophone l'emporte sur l'accès et la vitesse d'apprentissage, pas sur la taille");
  const HI = { color: INK, fill: { color: "D2F0EA" }, bold: true };
  const rowsSc = [
    ["Amérique du Nord", 5, 2, 5, 2],
    ["Europe francophone", 3, 5, 3, 5],
    ["APAC (Australie)", 2, 1, 3, 1],
    ["LatAm", 1, 1, 2, 1],
  ];
  table(s, [
    ["Région", "Taille", "Accès", "Coût du problème", "Vitesse d'apprentissage", "Total / 20"],
    ...rowsSc.map((r) => {
      const hi = r[0] === "Europe francophone";
      const tot = r.slice(1).reduce((x, y) => x + y, 0);
      return [r[0], ...r.slice(1).map(String), String(tot)].map((c, j) => ({ text: c, options: { align: j ? "center" : "left", ...(hi ? HI : {}), ...(j === 5 ? { bold: true } : {}) } }));
    }),
  ], { x: 0.5, y: 1.45, w: 5.8, colW: [1.6, 0.7, 0.7, 0.9, 1.1, 0.8], rowH: 0.5, fontSize: 9.5 });
  txt(s, "L'Amérique du Nord gagne sur la taille et le coût du problème (10 points contre 6), mais perd sur l'accès et la vitesse d'apprentissage : ce sont les deux critères qui comptent pour un fondateur seul pendant 90 jours.", { x: 0.5, y: 4.1, w: 5.8, h: 0.8, fontSize: 9.5 });
  card(s, 6.6, 1.35, 2.9, 3.6);
  txt(s, "Séquence proposée", { x: 6.75, y: 1.45, w: 2.6, h: 0.3, bold: true, fontSize: 10.5 });
  const seq = [
    ["J0–90", "France, Belgique, Suisse romande. Concierge, 5–8 pilotes."],
    ["M4–9", "Royaume-Uni + marques FR qui vendent aux US : premier test en anglais."],
    ["M9+", "Amérique du Nord si ≥ 2 clients payants et message validé ; APAC (AU) ensuite."],
  ];
  seq.forEach(([k, v], i) => {
    const y = 1.85 + i * 0.95;
    s.addShape(pres.shapes.OVAL, { x: 6.75, y, w: 0.55, h: 0.55, fill: { color: TEAL }, line: { color: TEAL } });
    txt(s, String(i + 1), { x: 6.75, y, w: 0.55, h: 0.55, align: "center", valign: "middle", bold: true, color: INK, fontSize: 12 });
    txt(s, k, { x: 7.4, y: y - 0.02, w: 2.0, h: 0.25, bold: true, fontSize: 9 });
    txt(s, v, { x: 7.4, y: y + 0.22, w: 2.0, h: 0.65, fontSize: 8.5, color: SLATE });
  });
  source(s, "Notes : jugement du fondateur, sans données terrain (P0). Taille : TAM central (slide 9). À re-noter après les 15 interviews de la phase 1 (GTM_STRATEGY §5).");
}

// ================= 14. Section 3 =================
darkSlide("Partie 3 · Approche", "Emprunter à Tally le build in public et le contenu, pas le modèle viral", "Tally : outil de formulaires, bootstrappé, porté par une offre gratuite généreuse et une boucle virale.\nSolen : outil B2B à valeur différée, avec un coût marginal par client.");

// ================= 15. Tally facts =================
{
  const s = base("Approche · le cas Tally", "Tally a atteint plusieurs M$ d'ARR sans lever de fonds, porté par un badge viral");
  const stats = [["~6 M$", "ARR revendiqué, sept. 2026"], ["2,5 M", "utilisateurs revendiqués"], ["~2 %", "des utilisateurs passent à Pro"], ["8", "personnes (4 à temps plein)"]];
  stats.forEach(([v, l], i) => {
    const x = 0.5 + i * 2.28;
    card(s, x, 1.4, 2.1, 1.2);
    txt(s, v, { x: x + 0.12, y: 1.45, w: 1.9, h: 0.6, fontSize: 26, bold: true, color: TEAL_D });
    txt(s, l, { x: x + 0.12, y: 2.08, w: 1.9, h: 0.45, fontSize: 9, color: SLATE });
  });
  const lev = [
    ["Offre gratuite généreuse", "Formulaires et réponses illimités gratuits ; la monétisation vient des fonctions avancées."],
    ["Boucle virale", "Badge « Made with Tally » vu par chaque répondant : décrit comme la principale boucle de croissance."],
    ["Build in public", "Chiffres et coulisses partagés sur X, Reddit et Indie Hackers dès le début."],
    ["Recherche de marque et IA", "Le bouche-à-oreille nourrit les recherches « Tally forms » ; ChatGPT cité comme 1re source de référence en 2026."],
  ];
  lev.forEach(([h, b], i) => {
    const x = 0.5 + (i % 2) * 4.55, y = 2.8 + Math.floor(i / 2) * 1.05;
    s.addShape(pres.shapes.OVAL, { x, y: y + 0.05, w: 0.4, h: 0.4, fill: { color: INK }, line: { color: INK } });
    txt(s, String(i + 1), { x, y: y + 0.05, w: 0.4, h: 0.4, align: "center", valign: "middle", color: WHITE, bold: true, fontSize: 11 });
    txt(s, h, { x: x + 0.55, y, w: 3.85, h: 0.3, bold: true, fontSize: 10.5 });
    txt(s, b, { x: x + 0.55, y: y + 0.3, w: 3.85, h: 0.65, fontSize: 9, color: SLATE });
  });
  source(s, "Sources : blog.tally.so (« From 2 to $3M ARR », « How we grew Tally to $4M ARR, fully bootstrapped ») ; okara.ai (6 M$ ARR, 2,5 M utilisateurs, sept. 2026) ; profitablefounder.xyz (5 M$ ARR 2025, ~2 % de conversion). Chiffres autodéclarés, repris en partie de sources secondaires : à vérifier dans les billets primaires.");
}

// ================= 16. Lever transposition =================
{
  const s = base("Approche · transposition", "Sur six leviers Tally, deux se transposent, deux s'adaptent, et le cœur viral ne passe pas");
  const OK = { text: "Se transpose", options: { color: WHITE, fill: { color: TEAL_D }, bold: true, align: "center" } };
  const AD = { text: "À adapter", options: { color: INK, fill: { color: "F6D9A3" }, bold: true, align: "center" } };
  const NO = { text: "Ne se transpose pas", options: { color: WHITE, fill: { color: RED }, bold: true, align: "center" } };
  table(s, [
    ["Levier Tally", "Verdict", "Pourquoi", "Version Solen"],
    ["Build in public sur X", OK, "Fondateur seul, récit authentique, coût nul", "Chiffres des pilotes, erreurs, décisions : X en anglais, LinkedIn en français"],
    ["Contenu qui capte la recherche", OK, "Les marchands cherchent « pourquoi ma boutique ne convertit pas »", "Autopsies publiques de boutiques, guides par friction, lisibles par Google et les IA"],
    ["Offre gratuite généreuse", AD, "Coût marginal non nul (tracking, LLM, relecture concierge)", "Audit de friction gratuit plafonné (1 boutique, 1 rapport), puis pilote"],
    ["Recherche sur le nom de marque", AD, "Conséquence du bouche-à-oreille, pas un levier de départ", "Indicateur à suivre (volume de recherche « Solen ») ; homonymes à vérifier"],
    ["Badge viral visible des utilisateurs finaux", NO, "L'optimisation est invisible pour l'acheteur ; pas de badge possible", "Rapport partageable (associé, agence) : boucle faible, à tester"],
    ["Self-serve instantané, 2 % de conversion", NO, "Valeur après plusieurs semaines ; base potentielle ~100× plus petite", "Concierge d'abord ; Shopify App Store après preuve de valeur"],
  ], { x: 0.5, y: 1.3, w: 9, colW: [1.8, 1.3, 2.75, 3.15], rowH: 0.48, fontSize: 8.5 });
  source(s, "Analyse : adaptation des leviers Tally (slide 15) aux contraintes de Solen (SOLEN_CONTEXT §6, §10, §42 ; GTM_STRATEGY §3–4). Verdicts = hypothèses P0.");
}

// ================= 17. Freemium math =================
{
  const s = base("Approche · économie du gratuit", "Au taux Tally (~2 %), 200 clients exigent 10 000 boutiques gratuites, ~5 % du SAM");
  const rates = [0.01, 0.02, 0.05, 0.10, 0.25];
  const need = rates.map((r) => SOM_CLIENTS.central / r);
  s.addChart(pres.charts.BAR, [{ name: "Boutiques gratuites nécessaires", labels: rates.map((r) => (r * 100).toString().replace(".", ",") + " %"), values: need }], {
    x: 0.5, y: 1.35, w: 5.6, h: 3.55, barDir: "col", chartColors: ["D5DDE2", TEAL, "D5DDE2", "D5DDE2", SLATE],
    showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 10, dataLabelColor: INK, dataLabelFormatCode: "#,##0",
    catAxisLabelColor: INK, catAxisLabelFontSize: 10, valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: false, showTitle: true, title: "Boutiques gratuites nécessaires pour 200 clients, par taux de conversion gratuit → payant", titleFontSize: 9, titleColor: SLATE,
  });
  card(s, 6.4, 1.35, 3.1, 3.55);
  txt(s, "Implication", { x: 6.55, y: 1.45, w: 2.8, h: 0.3, bold: true, fontSize: 10.5 });
  bullets(s, [
    `SAM central : ~${fmtK((NA + EMEA) * SCEN.central.share)} boutiques. Tally vise des millions d'utilisateurs ; Solen, des dizaines de milliers.`,
    "Chaque boutique gratuite a un coût (LLM, stockage, relecture) : la gratuité doit sélectionner, pas maximiser le volume.",
    "Le modèle viable ressemble à un entonnoir de vente assistée avec une conversion de 20–30 % des pilotes (hypothèse, barre gris foncé).",
  ], { x: 6.55, y: 1.85, w: 2.85, h: 3.0, fontSize: 9 });
  source(s, "Calcul : 200 clients (SOM central, slide 8) ÷ taux de conversion. ~2 % : taux Tally revendiqué (profitablefounder.xyz, à vérifier). 25 % : hypothèse de conversion pilote → payant (GTM_STRATEGY §4).");
}

// ================= 18. Solen motion =================
{
  const s = base("Approche · modèle retenu", "Le contenu public attire, un audit gratuit qualifie, le concierge convertit");
  const steps = [
    ["Build in public", "X (EN) + LinkedIn (FR) : 3 posts / semaine, chiffres et erreurs réels"],
    ["Autopsies publiques", "1 boutique / semaine analysée publiquement, avec son accord ou sur des éléments visibles"],
    ["Audit gratuit plafonné", "1 rapport de 3 frictions, sans installation, puis avec script"],
    ["Pilote 4 semaines", "Concierge : 0 € puis 149 € ; rapport hebdo + appel"],
    ["Abonnement", "~190 €/mois (hypothèse) ; cas anonymisé → nouveau contenu"],
  ];
  steps.forEach(([h, b], i) => {
    const x = 0.5 + i * 1.83;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.5, w: 1.65, h: 2.2, fill: { color: i === 4 ? INK : MIST }, line: { color: i === 4 ? INK : MIST }, rectRadius: 0.08 });
    s.addShape(pres.shapes.OVAL, { x: x + 0.12, y: 1.62, w: 0.42, h: 0.42, fill: { color: TEAL }, line: { color: TEAL } });
    txt(s, String(i + 1), { x: x + 0.12, y: 1.62, w: 0.42, h: 0.42, align: "center", valign: "middle", bold: true, fontSize: 11 });
    txt(s, h, { x: x + 0.12, y: 2.12, w: 1.42, h: 0.5, bold: true, fontSize: 10, color: i === 4 ? WHITE : INK });
    txt(s, b, { x: x + 0.12, y: 2.62, w: 1.42, h: 1.05, fontSize: 8.5, color: i === 4 ? "B8C7D1" : SLATE });
    if (i < 4) s.addText("›", { x: x + 1.63, y: 2.35, w: 0.22, h: 0.4, fontFace: FONT, fontSize: 20, color: TEAL_D, align: "center", valign: "middle", margin: 0, isTextBox: true });
  });
  card(s, 0.5, 3.95, 9, 0.95);
  txt(s, "Boucle de retour", { x: 0.65, y: 4.02, w: 2, h: 0.3, bold: true, fontSize: 10, color: TEAL_D });
  txt(s, "Chaque pilote produit une autopsie publiable (anonymisée) et des données réelles pour le build in public. C'est la version Solen de la boucle Tally : plus lente, non virale, mais cumulative. Hypothèse à tester : une autopsie publiée génère ≥ 1 demande d'audit entrante.", { x: 0.65, y: 4.3, w: 8.7, h: 0.55, fontSize: 9 });
  source(s, "Sources : GTM_STRATEGY.md §3–4 (canaux, offre de pilote, prix) ; adaptation des leviers Tally (slide 16). Prix et taux : hypothèses.");
}

// ================= 19. 90-day milestones =================
{
  const s = base("Approche · 90 jours", "Les 90 premiers jours visent trois preuves : douleur, installation, premier paiement");
  const ph = [
    ["Sem. 1–4", "Problème & cible", "15 interviews, 3 messages testés, ≥ 3 pilotes acceptés", "< 30 % d'histoires concrètes → changer de segment"],
    ["Sem. 5–8", "Valeur réelle", "Pilotes installés < 1 semaine ; ≥ 1 reco / 3 jugée nouvelle ; 1er pilote payant", "0 reco appliquée → la valeur est dans l'exécution (V2), creuser sans construire"],
    ["Sem. 9–13", "Paiement", "≥ 2 clients payants ; ≤ 2 h / client / semaine", "0 client payant → retour en SEEK, pas de V2"],
  ];
  ph.forEach(([w, t, ok, ko], i) => {
    const x = 0.5 + i * 3.05;
    card(s, x, 1.4, 2.85, 3.5);
    txt(s, w, { x: x + 0.15, y: 1.5, w: 2.55, h: 0.3, fontSize: 9, bold: true, color: TEAL_D });
    txt(s, t, { x: x + 0.15, y: 1.8, w: 2.55, h: 0.4, fontSize: 14, bold: true });
    txt(s, "Succès", { x: x + 0.15, y: 2.35, w: 2.55, h: 0.25, fontSize: 8.5, bold: true, color: SLATE });
    txt(s, ok, { x: x + 0.15, y: 2.6, w: 2.55, h: 0.9, fontSize: 9.5 });
    txt(s, "Seuil de changement de cap", { x: x + 0.15, y: 3.55, w: 2.55, h: 0.25, fontSize: 8.5, bold: true, color: RED });
    txt(s, ko, { x: x + 0.15, y: 3.8, w: 2.55, h: 1.0, fontSize: 9.5 });
  });
  source(s, "Source : GTM_STRATEGY.md §5 (plan semaine par semaine). Attention : Black Friday (27/11/2026) tombe en semaine 9 ; lancer tous les pilotes avant mi-novembre.");
}

// ================= 20. Risks =================
{
  const s = base("Risques", "Le risque n°1 est l'absence de preuve : deux des cinq risques touchent la taille du marché");
  table(s, [
    ["#", "Risque", "Impact", "Signal précoce", "Mitigation"],
    ["1", "Moins de 5 % des boutiques dépassent 10k visiteurs/mois", "TAM divisé par 2 ou plus", "Échantillon Store Leads / Similarweb de 500 boutiques", "Mesurer en semaine 1, avant tout investissement"],
    ["2", "Dépense outils réelle < 600 $/an (Hotjar gratuit, GA4)", "Pas de budget à capter ; Solen crée une nouvelle ligne de dépense", "Interviews : « combien dépensez-vous aujourd'hui ? »", "Ancrer la valeur sur le coût du trafic et de l'agence, pas des outils"],
    ["3", "Recommandations V1 génériques", "Aucune différenciation face à Hotjar ou un blog", "> 50 % de chaque rapport réécrit ; « je le savais déjà »", "Journal des corrections du concierge = spécification produit"],
    ["4", "Build in public sans audience marchande", "Temps perdu ; audience d'indie hackers, pas de clients", "0 demande entrante après 6 semaines de posts", "Plafonner à 3 h / semaine ; privilégier LinkedIn FR"],
    ["5", "Concurrence mieux financée (apps CRO Shopify, Amboras)", "Prix tirés vers le bas, message noyé", "Prospects qui citent une app concurrente", "Rester sur « l'existant d'abord » et la preuve par le test"],
  ], { x: 0.5, y: 1.35, w: 9, colW: [0.3, 2.1, 1.9, 2.3, 2.4], rowH: 0.55, fontSize: 8.5 });
  source(s, "Sources : SOLEN_CONTEXT.md §40 ; GTM_STRATEGY.md §6 ; hypothèses des slides 7 et 16.");
}

// ================= 21. Hypotheses to validate =================
{
  const s = base("Hypothèses à valider", "Huit hypothèses conditionnent la stratégie ; H1 et H3 se testent dès la semaine 1");
  table(s, [
    ["Hypothèse", "Preuve actuelle", "Test", "Seuil d'invalidation", "Quand"],
    ["H1. ≥ 10 % des boutiques dépassent 10k visiteurs/mois", "Aucune (P0)", "Échantillon de 500 boutiques", "< 5 %", "Sem. 1"],
    ["H2. L'ICP dépense ≥ 1 500 $/an en outils CRO", "Aucune (P0)", "15 interviews", "Médiane < 600 $", "Sem. 1–4"],
    ["H3. La répartition 31 / 16 / 5 est correcte", "Source secondaire (P1)", "Lire le 10-K Shopify FY2025", "Écart > 5 pts", "Sem. 1"],
    ["H4. L'Europe FR apprend plus vite que l'Amérique du Nord", "Raisonnement (P0)", "Taux de réponse FR vs EN (60 + 60)", "EN ≥ FR", "Sem. 2–3"],
    ["H5. L'audit gratuit plafonné qualifie les prospects", "Aucune (P0)", "Conversion audit → pilote", "< 20 %", "Sem. 4–8"],
    ["H6. Le build in public génère des demandes entrantes", "Cas Tally (autre marché)", "Demandes entrantes attribuées", "0 après 6 semaines", "Sem. 4–10"],
    ["H7. Les marchands paient ~190 €/mois", "Aucune (P0)", "Conversion post-pilote", "0 / 3 pilotes", "Sem. 9–12"],
    ["H8. Les agences sont un levier, pas une menace", "Aucune (P0)", "3 agences approchées", "0 / 3 avec « menace »", "Sem. 6–8"],
  ], { x: 0.5, y: 1.3, w: 9, colW: [3.3, 1.3, 2.0, 1.4, 1.0], rowH: 0.36, fontSize: 8 });
  source(s, "Niveaux de preuve : P0 intuition · P1 desk · P2 déclaratif · P3 comportemental · P4 monétaire (GTM_STRATEGY §0).");
}

// ================= 22. Sources =================
{
  const s = base("Annexe", "Toutes les sources sont publiques, plusieurs secondaires : à vérifier avant usage externe");
  bullets(s, [
    { text: "Boutiques Shopify", bold: true },
    "Store Leads, « Shopify stores by country », données au 03/07/2026 (2 865 709 boutiques live ; US 1 088 283 ; UK 197 736 ; CA 121 955 ; AU 119 745 ; IN 114 995), relayé par storeinspect.com et ecomm.design (2026).",
    "BuiltWith, Shopify usage statistics, février 2026 (6,9 M de sites avec du code Shopify, y compris inactifs) : non retenu pour le calcul.",
    "Répartition 44 / 31 / 16 / 5 / 5 (US / EMEA / APAC / CA / LatAm) attribuée au 10-K Shopify FY2025 par 3plinsider.com : à vérifier dans le 10-K.",
    { text: "Marché top-down", bold: true },
    "Research and Markets, A/B Testing Software Market (2025 : 1,30 Md$ ; 2032 : 2,73 Md$). Spherical Insights (2025 : 1,48 Md$ ; 2035 : 4,26 Md$). Business Research Insights (2025 : 0,85 Md$). Credence Research (2024 : 8,18 Md$).",
    { text: "Tally", bold: true },
    "blog.tally.so : « From 2 to $3M ARR: How We Bootstrapped Tally With a Tiny Team » ; « How we grew Tally to $4M ARR, fully bootstrapped ». okara.ai (6 M$ ARR, 2,5 M utilisateurs, sept. 2026). profitablefounder.xyz (5 M$ ARR en 2025, ~2 % de conversion, badge comme boucle principale).",
    { text: "Documents internes", bold: true },
    "docs/SOLEN_CONTEXT.md ; docs/GTM_STRATEGY.md (29/09/2026).",
  ], { x: 0.5, y: 1.35, w: 9, h: 3.7, fontSize: 8.5 });
  source(s, "Recherche documentaire réalisée le 29/09/2026 ; les rapports de marché n'ont pas été achetés (chiffres tirés des pages de présentation).");
}

pres.writeFile({ fileName: OUT }).then((f) => console.log("wrote", f));
