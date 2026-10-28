# Solen : brief complet pour une IA collaboratrice

Document de passation, rédigé le 28 octobre 2026. Il sert à ce qu'une IA (Claude, Grok Bot ou autre) comprenne le projet sans rien d'autre : la vision, ce qui tourne aujourd'hui, ce que le produit doit faire et la feuille de route. Il complète `docs/SOLEN_CONTEXT.md` (le prompt business) et `docs/SOLEN-ETAT-DU-PROJET.md` côté Base44.

Règle de lecture : chaque affirmation est marquée **Fait** (vérifié), **Hypothèse** (à valider) ou **Ambition** (but, pas un constat). Ne jamais présenter une hypothèse ou une ambition comme un fait.

---

## 0. Comment travailler avec le fondateur

1. Challenger les hypothèses plutôt que les accepter.
2. Distinguer faits, observations, hypothèses et vision. Ne pas sur-vendre.
3. Se demander à chaque fonctionnalité : **quelle hypothèse cela valide-t-il, et quelle preuve avons-nous ?**
4. Préférer les expériences rapides et peu coûteuses. Ne pas construire pour sortir de l'incertitude.
5. Considérer les outils existants (agence, GA4, Hotjar, VWO, tableurs) comme de vrais concurrents.
6. Ne pas supposer que l'IA est une différenciation en soi. La mémoire d'expérimentation n'est pas un avantage prouvé.
7. Répondre en français, de façon courte et directe. Une question à la fois. Ne jamais inventer un chiffre.
8. Le fondateur décide. Toute action qui sort de la session (publier, payer, écrire dans l'app, envoyer un message) demande son accord explicite.

---

## 1. Solen en un paragraphe

**Signature (toujours écrite ainsi, en anglais)** : *The Self-Optimizing E-commerce Layer*. En français : « La couche d'optimisation autonome de l'e-commerce ».

**Ambition** : Solen est une couche d'optimisation autonome pour les boutiques e-commerce, d'abord Shopify. Elle observe le comportement réel des visiteurs, repère où les ventes se perdent, propose des changements précis, les teste sur de petits segments de visiteurs, puis déploie ce qui gagne sur tout le site. À terme, elle génère aussi les pages produit de A à Z : le marchand dépose son produit, Solen construit la page à partir de ce que font les meilleures pages de la catégorie et de ce que disent ses propres visiteurs. L'objectif est un SaaS très rentable qui devienne la référence de l'optimisation de conversion sur Shopify.

**Ce qui est vrai aujourd'hui** : un prototype avec un audit gratuit de fiche produit qui fonctionne, un suivi de boutique par pixel (phase 1), des recommandations générées par IA, un robot qui compare les pages à un échantillon de boutiques, et **aucun client payant**. La boucle de test (tester, mesurer, garder le gagnant) n'existe pas encore.

Phrase de synthèse (fondateur) : *« Every store learns from every visitor. »*

---

## 2. La vision en deux briques

1. **Adapter le site en continu** à partir de ce que font les visiteurs : Observer, Comprendre, Proposer, Tester, Apprendre, Améliorer.
2. **Générer des pages produit par IA** : le marchand donne son produit et ses faits, Solen construit la page.

### La boucle

`Comportement -> Hypothèse -> Modification -> Expérience -> Résultat -> Apprentissage`

Quatre choses à ne jamais mélanger :
- **Observation** : les visiteurs mobiles abandonnent plus à cette étape.
- **Hypothèse** : la longueur de cette section y contribue peut-être.
- **Expérience** : une version simplifiée contre le contrôle, sur une petite part du trafic.
- **Résultat** : la variante a donné tel écart sur la mesure principale, avec tels effets secondaires.

### Les niveaux d'autonomie

| Niveau | Contenu | Rôle de l'humain |
|---|---|---|
| V1 Intelligence | Analyse, détection des fuites, recommandations | Décide tout |
| V2 Copilote | Génère les modifications, les contenus, les pages ; prépare les tests | Valide avant publication |
| V3 Expérimentation | Crée les tests, répartit le trafic, mesure, compare | Valide le déploiement |
| V4 Pilote automatique | Boucle complète avec garde-fous | Valide seulement les catégories sensibles |

### Le test par segments, puis le déploiement

Une variante est d'abord servie à une **petite part du trafic** (par exemple un segment d'appareil ou 10 à 20 % des visiteurs), face à un groupe témoin. Si la mesure principale s'améliore sans dégrader les mesures de sécurité, et si les données sont suffisantes, la variante est proposée au déploiement sur tout le site. Sinon elle est retirée.

---

## 3. Positionnement et marché

- **Cible** (hypothèse) : e-commerçants Shopify ayant déjà du trafic et des ventes, francophones d'abord. Seuil de trafic minimal évoqué : environ 10 000 visiteurs par mois (**non validé**).
- **Ce que Solen n'est pas** : un concurrent de Shopify, une nouvelle plateforme e-commerce, un simple outil d'analytics, un simple outil d'A/B test, une agence, un chatbot.
- **Amboras** (YC S26, États-Unis) : plateforme e-commerce « native IA », qui reconstruit l'infrastructure. Solen se place **à côté** : *Existing Commerce -> Optimization Layer -> AI*, sans migration. Cette différence est une **hypothèse**, pas un avantage démontré. Le fondateur formule l'ambition comme : devenir le leader de l'optimisation sur Shopify, y compris par la génération de pages produit par IA. Attention à la formulation : Solen vise le marché des marchands Shopify, il ne remplace pas Shopify.
- **Concurrents réels** : GA4 et Shopify Analytics, Hotjar et Contentsquare, VWO, Optimizely, AB Tasty, agences CRO, équipes internes, solutions maison.
- **Outils de veille** (par exemple TrendTrack : boutiques en croissance, bibliothèques de pubs, e-mails, analyse de boutique, MCP) : plutôt complémentaires. Ils répondent à « que vendre et qui copier », Solen à « ma page mérite-t-elle le trafic ? ». À vérifier, la fiche exacte de leur offre n'a pas été lue.
- **Moat envisagé** (**hypothèse**) : la mémoire d'expérimentation, c'est-à-dire des résultats structurés (contexte, comportement, hypothèse, modification, résultat) qui améliorent les recommandations suivantes. À démontrer : qu'elle améliore les résultats, qu'elle s'améliore dans le temps, qu'elle est difficile à copier.

---

## 4. Ce qui tourne aujourd'hui (état au 28 octobre 2026)

### 4.1 L'application Solen sur Base44 (source de vérité du produit)

- Identifiant de l'app : `6ada3ee9eafc0a1dbc24bee6`. Adresse : `solen-bc24bee6.base44.app`, domaine connecté `withsolen.com`.
- **Statut honnête** : publiée techniquement, mais **pas lancée** : pas d'utilisateur externe connu, paiement Stripe en cours d'activation. Les chiffres du 26 octobre : 3 demandes d'audit, 1 candidature pilote, 1 achat, 1 boutique, probablement tous des tests internes.
- **Site public** bilingue FR / EN, onze sections. Attention : ses textes présentent la boucle complète (« lance l'A/B test, garde les gagnants ») comme si elle existait. **À corriger** : le texte doit décrire ce qui marche aujourd'hui.
- **Audit gratuit d'une fiche produit** (`/audit`), **fonctionne** : le marchand colle l'adresse, son e-mail et son chiffre d'affaires ; un compte est créé par code envoyé par e-mail ; la page est récupérée (adresses publiques seulement, protection contre les requêtes vers l'interne) puis analysée par IA ; le résultat est un score sur 100, un verdict et trois correctifs. Le score vient d'un modèle de langage (non calculé par du code). Un audit d'exemple existe (`/audit/exemple`).
- **Suivi de boutique, phase 1**, **fonctionne** : le marchand déclare son domaine, reçoit une clé et colle deux blocs (pixel personnalisé et injection dans `theme.liquid`). Le consentement Shopify est respecté. La collecte est anonyme : identifiant de session aléatoire, appareil, source, pays, étape du tunnel, profondeur de scroll, clics, clics de frustration, temps par page. Aucune donnée personnelle. Tableau de bord : entonnoir, segments, frustration, recommandations classées (à faire, en test, fait). Consolidation chaque nuit à 3 h (Paris), purge des sessions brutes après 90 jours.
- **Espace client**, candidatures pilotes (avec e-mail de notification), pages légales (mentions, CGU, confidentialité : plusieurs trous à combler).
- **Page de vente des guides vidéo** (`/ai-videos`) : fonctionnelle, cachée (`noindex`), mise de côté par le fondateur pour l'instant.
- **Données** (7 tables) : Store, Session, DailyAggregate, Recommendation (constat, hypothèse, test, segment, statut), AuditRequest, PilotApplication, Purchase.
- **Fonctions serveur** : analyzeAudit, findLeaks, getStoreInsights, ingestEvents, rollupSessions, notifyPilotApplication, stripeWebhook, getDownloads.
- **MCP** (accès depuis Claude, ChatGPT ou Cursor, derrière OAuth) : configuré, **inactif** (il faut republier l'app).
- **Sécurité** : le dernier scan est périmé ; quatre points ouverts (dépendance `zod`, deux correctifs à confirmer, huit fonctions à contrôler une à une).
- **Mesure d'audience** : GA4, Clarity, deux événements métier.

### 4.2 Le dépôt GitHub `mtvv37/solen-backend` (public)

- **Prototype historique** Express (audit V0, `/events`, `/heatmap`, `/analyze`), conçu pour Vercel mais **son déploiement échoue** : ce n'est pas le produit en cours. Voir `CLAUDE.md` et `docs/AUDIT_V0.md`.
- **Documents** : `docs/SOLEN_CONTEXT.md` (prompt business), ce brief.
- **Design** : logo (cadre tournant penché), kit visuel, carrousels Instagram et TikTok, images, vidéos, bannières, guides PDF « You met me at... » (mis de côté).
- **Robot de référence** (`tools/benchmark/` et `.github/workflows/benchmark.yml`), **fonctionne** et tourne **chaque nuit sur GitHub Actions** : il lit des pages produit publiques (robots.txt respecté, une requête par domaine toutes les 1,5 s, sites bloquants laissés tranquilles), n'enregistre que des **critères** (jamais les textes ni les images) et publie des statistiques sur la branche `benchmark-data`. Sources d'adresses : articles de listes de boutiques, classement Tranco, liste de référence faite à la main (arntreal.com, helloboku.com). Notification de fin de run sur ntfy.
  - Au 27 octobre : environ 566 sites échantillonnés, 2 692 pages. **Limites connues** : la détection de plateforme comptait à tort des milliers de pages en « Magento » (corrigée dans la demande de fusion n° 6, à confirmer comme fusionnée) ; seuls les chiffres de la colonne **Shopify** (172 boutiques) étaient fiables ; les statistiques se reconstruisent sur une à deux nuits ; l'échantillon est surtout composé de marques connues, pas de ventes mesurées.
  - Résultat exploitable aujourd'hui (Shopify seulement, échantillon de marques connues) : retours mentionnés juste après le bouton d'achat sur environ 38 % des boutiques où le bouton est lu ; livraison sur environ 54 %.
- **Autres dépôts du compte** : `mtvv37/solen` (vide, aucun commit), `verzo-sale-agent`, `verzo-site`, `photo` (projets sans lien avec Solen).

### 4.3 Marketing en place

Identité visuelle (fond vert très sombre, logo cadre tournant, polices Inter Tight, Archivo Expanded, JetBrains Mono), carrousels sur la conversion, une série de vidéos avec un personnage original (Kane), guides PDF. Règles de contenu : pas de tiret long, pas d'émoji, pas de chiffre inventé, deux mots-dièse seulement (`#shopify #ecommerce`).

---

## 5. Ce que le produit doit faire (cible)

### 5.1 Modules

| Module | Fonction | État |
|---|---|---|
| Observer | Pixel et script thème : événements anonymes, consentement respecté | Phase 1 en place |
| Comprendre | Détection des fuites, segments, frustration | En place (qualité à valider) |
| Comparer | Comparatif des pratiques de la page à celles de la catégorie (robot de référence) | Prototype |
| Proposer | Fiche de test : un seul changement, mesure principale, mesures de sécurité, part du trafic, durée | À construire (phase A) |
| Générer | Page produit complète à partir des faits du marchand et des structures de la catégorie | À construire |
| Servir | Attribution des visiteurs (témoin / variante) et application du changement | À construire |
| Mesurer | Comptage, résultat, règles d'arrêt, arrêt d'urgence | À construire |
| Apprendre | Mémoire d'expérimentation (opt-in) qui améliore les propositions | À construire |

### 5.2 Modèle de données à ajouter (proposition)

`ExperimentPlan` (lié à Recommendation et Store : observation, hypothèse, un seul changement, type de changement, périmètre, mesure principale, mesures de sécurité, part du trafic, visiteurs minimum par groupe, durée prévue, statut, drapeau « catégorie sensible »), `Variant`, `Exposure` (visiteur, test, groupe), `ExperimentResult` (valeurs par groupe, verdict : gagné / perdu / pas assez de données), `Learning` (contexte, comportement, hypothèse, modification, résultat).

### 5.3 Garde-fous (non négociables)

- **Un seul changement par test**, un groupe témoin toujours conservé, petite part du trafic au départ.
- **Durée et nombre de visiteurs fixés avant le lancement**, pas d'arrêt dès que ça a l'air bon.
- **Un petit échantillon est bruité** : en dessous du volume nécessaire, le résultat est « pas assez de données », jamais « gagnant ».
- **Bouton d'arrêt et retour arrière automatique** si une mesure de sécurité se dégrade.
- **Validation humaine obligatoire** pour les prix, promotions, paiement, mentions légales, identité de marque et tout changement à fort impact.
- **Jamais de fausse preuve** dans une page générée : pas d'avis, de certification, de garantie ou de chiffre que le marchand n'a pas fourni.
- **Pas de copie** : apprendre la structure des pages des autres, jamais leurs textes ni leurs images.
- **Données** : collecte anonyme, consentement, durée de conservation, hébergeur déclaré, usage des données pour améliorer le produit en **opt-in** explicite.

---

## 6. Feuille de route

Chaque phase doit pouvoir se vendre seule et prouver une hypothèse. Les prix sont des **hypothèses non validées**.

### Phase 0 : devenir vendable et honnête (cette semaine et la suivante)

- Aligner le texte du site sur ce qui existe vraiment.
- Activer Stripe, compléter la confidentialité, les CGU et la FAQ sécurité.
- Corriger les statistiques du robot (plateformes, filtre de boutiques), ajouter un segment français, vérifier à la main 20 à 30 boutiques pour connaître le taux d'erreur.
- **Test de demande** : proposer à 10 personnes réelles un service livré à la main, pour savoir si on paie. Offre d'entrée : fiche produit réécrite en 48 h (environ 29 €). Critère : au moins 2 acheteurs sur 10.

### Phase 1 : intelligence récurrente (V1)

- **Solen Watch** : surveillance hebdomadaire de 3 pages produit, sans pixel, comparée à l'échantillon, avec rapport par e-mail (environ 19 à 29 € par mois). Critère : au moins 3 abonnés.
- **Fiches de test** (ExperimentPlan) générées par IA, validées par l'humain.
- Champ de résultat saisi à la main (gagné, perdu) pour démarrer la mémoire.

### Phase 2 : copilote et génération de pages (V2)

- Générateur : « tu déposes le produit, je construis la page » à partir des faits du marchand et des structures de la catégorie. Livraison d'abord en document (structure et textes), puis page hébergée, puis intégration Shopify.
- Génération de variantes de textes et de blocs. Le marchand valide avant publication.

### Phase 3 : expérimentation (V3)

- Script du thème : attribution déterministe des visiteurs, application des changements côté navigateur, enregistrement des expositions.
- Moteur de mesure : comptage par groupe, contrôle de la répartition, règles d'arrêt, arrêt d'urgence, résultat écrit dans la mémoire.
- Application Shopify officielle (installation en un clic).
- Tests sur segments puis déploiement du gagnant après validation.

### Phase 4 : pilote automatique prudent (V4)

- Boucle continue avec garde-fous ; validation humaine pour les catégories sensibles.
- Mémoire d'expérimentation entre boutiques (opt-in), pour améliorer les propositions.

### Pourquoi cet ordre

Observer et proposer sont peu risqués et se vendent tout de suite. Servir et mesurer sont la partie où l'on se trompe le plus facilement (statistiques, trafic, effets de bord) : elle doit venir quand il y a des clients qui veulent ce résultat.

---

## 7. Modèles économiques à tester (hypothèses)

| Offre | Prix évoqué | Nature |
|---|---|---|
| Audit gratuit | 0 | Produit d'appel |
| Fiche produit réécrite, livrée à la main | ~29 € | Revenu immédiat, validation |
| Solen Watch | ~19 à 29 €/mois | Premier récurrent |
| Conseil (tableau de bord et lecture hebdomadaire livrée) | 99 €/mois, tarif fondateur | Plus cher, plus de valeur |
| Audit approfondi, test implémenté | 150 à 290 € ; 500 à 1 500 € | Services, à ne pas privilégier |
| Paiement au pourcentage des ventes | Non retenu | Invérifiable sans infrastructure de test solide |

Repère : se comparer à l'agence CRO, pas aux cartes de chaleur.

---

## 8. Backlog ouvert (côté app)

1. Texte du site : retirer ce qui n'existe pas encore.
2. Confidentialité (suivi anonyme, durée, hébergeur, usage des données), CGU, tarif (espaces réservés visibles), FAQ sécurité.
3. Stripe : finaliser l'activation du compte.
4. Résultat des tests : champ gagné / perdu.
5. Mettre à jour `zod`, refaire un scan, vérifier le contrôle d'accès de chaque fonction.
6. Supprimer la fonction de sonde, republier pour activer le MCP.
7. Page `/bot` qui explique le robot de référence et comment demander son exclusion.
8. Enrichir `/audit/exemple` de deux exemples sectoriels réels.

---

## 9. Risques principaux

Le problème n'est peut-être pas assez douloureux ; les outils existants et les agences suffisent peut-être ; manque de confiance dans l'automatisation ; trafic insuffisant chez les petits marchands ; corrélation confondue avec causalité ; résistance des agences (leur modèle de facturation décide : à l'heure, elles voient une menace ; au forfait, une marge) ; coût de l'IA au volume ; fonctionnalités faciles à copier ; risques juridiques (copie de contenus, fausses preuves, RGPD).

## 10. Questions encore ouvertes

Qui ressent le plus la douleur (fondateur, responsable croissance, agence) ? Quel niveau d'autonomie les marchands acceptent-ils réellement ? Combien de trafic faut-il pour qu'un test conclue ? L'abonnement doit-il dépendre du trafic, des boutiques ou de l'autonomie ? Les agences sont-elles des clients ou des revendeurs ?

---

## 11. Travailler dans Base44

- Deux façons de modifier l'app : **demander au constructeur IA** de Base44 (consomme des crédits, résultat à relire) ou **éditer le code directement** (fichiers dans `base44/` et `src/`), puis créer un point de sauvegarde.
- Ne jamais éditer directement pendant qu'un tour du constructeur est en cours.
- Toute écriture dans l'app, tout paiement, tout envoi à un client demande l'accord explicite du fondateur.
- Le MCP Base44 permet de lire le code, les schémas et les données ; ne jamais copier de données personnelles dans un document.

*Fin du brief.*
