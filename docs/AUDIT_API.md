# API de l'audit : contrat pour le site Solen

Le site public (ton domaine, fait avec ton outil de création de site) affiche l'interface. Le backend (ce repo, sur Vercel) fait tout le calcul. **Le site ne calcule ni score ni montant : il affiche ce que l'API renvoie.**

- **Adresse de l'API** : `https://<backend>` (ex. `https://api.solen.fr` ou l'URL Vercel du backend). Appelée **depuis le navigateur**, pas depuis un serveur intermédiaire, sinon la limite par visiteur ne marche plus.
- **CORS** : le domaine du site doit figurer dans `ALLOWED_ORIGINS` côté backend.
- **Pages à créer sur le site** : `/audit` (formulaire) et `/audit/rapport/[id]` (rapport). Côté backend, `REPORT_URL_TEMPLATE=https://<ton-domaine>/audit/rapport/{id}`.

## 1. Lancer un audit

`POST /api/audits` · `Content-Type: application/json`

```json
{ "url": "maboutique.fr", "monthlyVisitors": 20000, "averageOrderValue": 65 }
```
`monthlyVisitors` et `averageOrderValue` sont optionnels (nombres > 0).

- **201** → `{ "id": "BqLlqFKil2WBiCH9brw6Ng", "reportUrl": "https://<site>/audit/rapport/<id>", "shareUrl": "https://<backend>/r/<id>" }` → rediriger vers `reportUrl`.
- **400 / 422** → `{ "error": "message en français à afficher tel quel", "code": "..." }` (adresse invalide, robots.txt, pas de fiche produit, site injoignable…).
- **429** → trop d'audits depuis ce visiteur (6 par heure) : afficher `error`.
- **500** → afficher `error`.

Durée : 5 à 40 secondes. Afficher un état de chargement avec des étapes (robots.txt → accueil → fiche produit → score → rédaction) et désactiver le bouton.

## 2. Lire un rapport

`GET /api/audits/:id` (ajouter `?t=<token>` si un jeton est stocké, voir 3).

```json
{
  "id": "…", "createdAt": "2026-10-22T16:00:00Z",
  "shopDomain": "maboutique.fr", "productUrl": "https://…/products/…", "productName": "Robe lin",
  "isShopify": true,
  "score": 62,
  "categories": [ { "id": "socialProof", "label": "Preuve sociale", "score": 14, "max": 20 }, … 6 au total ],
  "summary": "2 phrases en français.",
  "leakCount": 5,
  "leaks": [
    { "id": "review_widget", "category": "socialProof", "title": "…", "explanation": "…", "test": "…",
      "monthlyLossEur": { "low": 230, "high": 600 }, "estimate": true },
    { "locked": true, "category": "trust", "categoryLabel": "Réassurance" }
  ],
  "assumptions": { "notes": [ "Trafic mensuel supposé : 10 000 visiteurs [hypothèse].", "…" ] },
  "unlocked": false
}
```

- **404** → rapport introuvable.
- Les fuites sont **déjà classées par impact** : afficher dans l'ordre, numérotées 1 à 5.
- Une fuite `locked: true` n'a pas de contenu : afficher une carte floutée avec seulement `categoryLabel`.
- Le montant s'affiche ainsi : `Manque à gagner estimé : 230 € à 600 € par mois [hypothèse]`, toujours avec la mention [hypothèse].
- Toujours afficher `assumptions.notes` dans une section « Comment lire les montants ».
- `isShopify: false` → afficher un avertissement : « Ce site ne semble pas tourner sur Shopify. »

## 3. Débloquer le rapport complet

`POST /api/audits/:id/unlock`

```json
{ "email": "vous@maboutique.fr", "consent": true }
```

- La case de consentement est **obligatoire, non cochée par défaut**, avec exactement ce texte : « J’accepte que Solen utilise mon email pour m’envoyer ce rapport et des conseils pour améliorer ma boutique. Désinscription possible à tout moment. »
- **200** → `{ "token": "…", "report": { …rapport complet, unlocked: true } }` → afficher `report` et stocker `token` dans `localStorage` sous la clé `solen-audit-<id>` (pour les visites suivantes : `GET /api/audits/:id?t=<token>`).
- **400** (email invalide, case non cochée), **429**, **404** → afficher `error`.

## 4. Partage

- Lien à partager : `shareUrl` (`https://<backend>/r/<id>`). Il porte l'aperçu (titre, image avec le score) pour X, LinkedIn et WhatsApp, puis renvoie le visiteur vers la page du rapport sur le site.
- Image seule : `GET /api/audits/:id/og.png` (1200 × 630).
- Boutons : copier le lien, partager sur X (`https://twitter.com/intent/tweet?text=…&url=<shareUrl>`), partager sur LinkedIn (`https://www.linkedin.com/sharing/share-offsite/?url=<shareUrl>`).

## Règles d'affichage

- Ne jamais inventer, arrondir autrement ou additionner les montants : les fuites ne s'additionnent pas.
- Afficher tous les textes de l'API comme du texte, jamais comme du HTML.
- Le score se colore selon sa valeur : ≥ 75 vert, 50–74 ambre, < 50 rouge.
