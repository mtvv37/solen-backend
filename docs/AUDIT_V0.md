# Audit V0 : audit de conversion gratuit

Outil d'acquisition de l'étape 0. Le marchand colle l'adresse de sa boutique Shopify et obtient un score sur 100 et ses 5 principales fuites de conversion. Le rapport complet est débloqué contre un email, avec consentement explicite.

## Parcours

1. `/audit/` : le marchand colle une adresse (accueil ou fiche produit). Il peut indiquer son trafic mensuel et son panier moyen.
2. `POST /api/audits` : le serveur lit `robots.txt`, la page d'accueil et une fiche produit (2 pages maximum), calcule le score, chiffre les fuites, puis Claude les rédige.
3. `/r/<id>` : rapport public, à l'adresse non devinable (128 bits). On y voit le score, le détail par catégorie et 2 fuites. Les 3 autres sont floutées.
4. `POST /api/audits/<id>/unlock` : email + case de consentement. Le serveur renvoie le rapport complet et un jeton, gardé dans le navigateur pour les visites suivantes.
5. `/api/audits/<id>/og.png` : image de partage 1200 × 630 (X, LinkedIn, WhatsApp).

## Ce qui est calculé, et par qui

| Élément | Par qui | Fichier |
|---|---|---|
| Extraction (avis, photos, description, prix, réassurance, poids, mobile, panier) | Code, lecture du HTML sans exécuter le JavaScript | `src/audit/extract.js` |
| Score sur 100 (6 catégories pondérées) | Code, règles fixes | `src/audit/score.js` |
| Fuites et montants en €/mois | Code, à partir d'hypothèses affichées | `src/audit/leaks.js` |
| Texte des fuites en français | Claude (`claude-opus-5-5`), sans aucun chiffre | `src/audit/writer.js` |

- **Hypothèses affichées dans chaque rapport** : trafic de 10 000 visiteurs par mois si le marchand ne le donne pas, taux de conversion de 1,5 %, panier moyen égal au prix du produit audité, et gains relatifs par fuite issus d'ordres de grandeur internes, non d'une étude. Tous ces chiffres sont marqués [hypothèse]. Les fuites ne s'additionnent pas.
- **Claude ne fixe aucun chiffre.** Si un texte qu'il renvoie contient un « € » ou un « % », il est remplacé par un texte fixe. Il l'est aussi en cas de refus, d'erreur ou d'absence de clé API : l'audit fonctionne donc sans Claude.
- **Position du bouton d'achat sur mobile** : c'est une estimation tirée de l'ordre du code, sans affichage de la page. Le rapport le précise.

## Sécurité

- **SSRF** (`src/audit/safeFetch.js`) : seuls http et https sur les ports 80 et 443 sont acceptés. Sont refusés les identifiants dans l'URL, les noms internes (`localhost`, `.local`…) et les IP privées, de bouclage, link-local ou de métadonnées cloud, en IPv4 comme en IPv6, y compris sous forme décimale, hexadécimale ou mappée. L'IP vérifiée est celle sur laquelle le socket se connecte, ce qui ferme la porte au DNS rebinding. Chaque redirection est revalidée (4 au maximum).
- **Limites** : délai de 7 s par page, 3 Mo par page, 256 Ko pour `robots.txt`.
- **robots.txt** : l'analyse est refusée si une page est interdite ou si `robots.txt` répond en erreur 5xx.
- **Limite de débit** : 6 tentatives d'audit et 10 déblocages par heure et par IP. Les tentatives qui échouent comptent aussi. L'IP n'est jamais stockée en clair, seulement son HMAC salé.
- **Données** : les tables ont le RLS activé et aucune politique d'accès. Seul le serveur, avec la clé service-role, peut lire et écrire. Le texte exact du consentement et sa version sont stockés avec chaque email.
- **Pages** : CSP stricte (pas de script inline, `frame-ancestors 'none'`), `nosniff`, rapports en `noindex`.

## Interface sur ton propre site

L'interface intégrée (`/audit/`) peut être remplacée par un site sur ton domaine : voir [`AUDIT_API.md`](AUDIT_API.md). Renseigne `ALLOWED_ORIGINS` et `REPORT_URL_TEMPLATE` côté backend.

## Déploiement

1. **Supabase** : SQL Editor → coller `supabase/migrations/20261022000000_audit_v0.sql` → Run. Le script crée `audits`, `audit_leads` et `audit_attempts`.
2. **Vercel** → Settings → Environment Variables : renseigner les clés de `.env.example`, dont `SUPABASE_SERVICE_ROLE_KEY`, `AUDIT_TOKEN_SECRET`, `AUDIT_IP_SALT` (à générer chacun avec `openssl rand -base64 32`), `ANTHROPIC_API_KEY` et `PUBLIC_BASE_URL`. En production, l'app refuse de démarrer l'audit si les secrets ou Supabase manquent.
3. **Déployer** : fusionner sur `main`. `vercel.json` route désormais toute l'app Express vers `api/index.js`, avec une durée maximale de 60 s. Les anciens endpoints (`/events`, `/heatmap`, `/analyze`) gardent les mêmes adresses.
4. **Vérifier** : ouvrir `/audit/`, auditer ta propre boutique, débloquer le rapport, puis coller le lien du rapport dans X ou LinkedIn pour voir l'image de partage.

## En local

```bash
npm install
npm test        # 21 tests : SSRF, robots.txt, extraction, score, fuites, rédaction, parcours complet
npm run dev     # http://localhost:3000/audit/ (stockage en mémoire si Supabase n'est pas configuré)
```

## Limites connues

- **Le JavaScript des pages n'est pas exécuté.** Les widgets d'avis chargés uniquement en JavaScript peuvent passer inaperçus : la détection se fait sur les traces dans le code (judge.me, Yotpo, Loox, Okendo…).
- **Certaines boutiques bloquent les robots** (protection anti-bots) : l'audit renvoie alors une erreur claire.
- **Les seuils du score et les gains par fuite sont des heuristiques internes.** Ils sont à recalibrer avec les données réelles des boutiques installées (étape 1).
