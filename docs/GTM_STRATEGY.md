# Solen — Stratégie go-to-market (90 jours, fondateur seul)

> Version 0.1 — 29/09/2026. Document de travail, **pas une stratégie validée**.
> Contexte de référence : [`SOLEN_CONTEXT.md`](SOLEN_CONTEXT.md). Règle : *AI proposes. Reality decides.* S'applique aussi à ce plan.

## 0. Comment lire ce document

Chaque choix est une **hypothèse**, accompagnée d'un **niveau de preuve** :

| Niveau | Signification |
|---|---|
| **P0 — Aucune** | Intuition ou raisonnement du fondateur, pas de donnée. |
| **P1 — Desk** | Raisonnement appuyé sur des sources publiques (prix affichés, structure du marché), pas de terrain. |
| **P2 — Déclaratif** | Des prospects l'ont *dit* en interview. |
| **P3 — Comportemental** | Des prospects l'ont *fait* : installé le script, donné du temps, ouvert les rapports, appliqué une reco. |
| **P4 — Monétaire** | Des prospects ont *payé* ou signé un engagement de paiement. |

**État actuel : tout ce plan est au niveau P0–P1.** Aucune interview n'est encore consolidée dans le repo, aucun marchand n'utilise le prototype, aucun euro n'a été encaissé. L'objectif des 90 jours est de faire monter les hypothèses critiques à P3 minimum, et au moins une à P4.

**Ce que le prototype fait aujourd'hui** (constaté dans `index.js`) : ingestion d'événements (`POST /events`), heatmap clics / scroll par device (`GET /heatmap`), analyse LLM des 500 derniers événements en recommandations (`GET /analyze`). **Ce qu'il ne fait pas encore** et qui compte pour le GTM : pas de séparation par boutique (`/analyze` agrège tous les événements, sans `site_id`), pas d'authentification, pas de gestion du consentement RGPD, pas de lien avec les données de vente Shopify. Ces écarts sont traités dans le plan comme des prérequis minimaux, pas comme une roadmap produit.

---

## 1. Les trois personas comparés et l'ICP de départ

### 1.1 Comparaison

Notes de 1 (défavorable) à 5 (favorable) **pour un fondateur seul, sans budget, avec un V1**. Toutes les notes sont P0–P1.

| Critère | P1 — Founder Shopify | P2 — E-commerce / Growth Manager | P3 — Agence CRO / e-commerce |
|---|---|---|---|
| **Douleur** | Forte mais diffuse : « la conversion est mauvaise, je ne sais pas pourquoi ». Souvent en concurrence avec l'acquisition, le stock, le SAV. **3/5** | Forte et quantifiée : objectifs de conversion, backlog d'hypothèses, dépendance aux devs, ROI à prouver. **4/5** | Forte sur la productivité (audits répétitifs, reporting), mais ambiguë : l'automatisation peut cannibaliser le temps facturé. **3/5** |
| **Budget** | Faible, dépense d'apps Shopify en dizaines d'€/mois ; les petites boutiques n'ont souvent ni Hotjar payant ni agence. **2/5** | Existant et alloué (outils analytics, testing, agence). Hotjar / VWO / AB Tasty / Contentsquare déjà en place selon la taille. **4/5** | Budget outils existant et refacturable au client ; sensible à la marge. **3/5** |
| **Accessibilité** | Très accessible : LinkedIn, communautés Shopify FR, Slack/Discord e-commerce, décideur unique. **5/5** | Accessible sur LinkedIn mais sollicité ; installation d'un script sur la prod = validation dev / IT / juridique. **3/5** | Peu d'agences, faciles à identifier, mais méfiantes vis-à-vis d'un outil non éprouvé qui touche à leur cœur de métier. **3/5** |
| **Cycle de vente** | Court (jours à 2–3 semaines), décision seule. **5/5** | Moyen à long (1–3 mois), plusieurs parties prenantes, parfois achat formel. **2/5** | Moyen (3–8 semaines) pour un test sur 1 client ; long pour un déploiement sur le portefeuille. **3/5** |
| **Trafic suffisant pour produire du signal** | Très variable : beaucoup de boutiques sous le seuil. **2/5** | Oui en général. **5/5** | Oui, sur plusieurs boutiques. **4/5** |
| **Concurrence perçue** | Faible outillage : GA4 + Shopify Analytics, parfois Hotjar gratuit. Solen est comparé à « ne rien faire ». | Forte : Contentsquare / Hotjar / VWO / AB Tasty déjà en place, équipe interne. Solen doit prouver un gain sur l'existant. | L'agence *est* l'alternative. Solen doit être un outil pour elle, pas contre elle. |
| **Valeur d'un client pour l'apprentissage** | 1 boutique = 1 contexte. | 1 boutique, données riches. | 1 agence = N boutiques, N contextes (précieux pour l'hypothèse de mémoire d'expérimentation). |
| **Total indicatif** | **22** | **21** | **19** |

Les totaux sont proches : **l'écart n'est pas significatif** et ne remplace pas les interviews. Il sert à choisir *où commencer*, pas à trancher.

### 1.2 ICP de départ recommandé (hypothèse H-ICP)

> **Marque Shopify DTC, biens physiques, 20 000 à 150 000 visiteurs/mois, 2 à 15 personnes, sans spécialiste CRO ni data en interne. Le décideur est le fondateur ou le premier responsable e-commerce. Elle dépense déjà de l'argent pour faire venir du trafic (Meta / Google Ads) et le sait.**

C'est la **partie haute du persona 1, qui chevauche la partie basse du persona 2**. Justification :

1. **Accessibilité et cycle court** : un fondateur seul peut contacter, convaincre et installer en quelques jours. C'est le seul segment compatible avec 90 jours et 0 € de budget.
2. **Plancher de trafic** : 20k visiteurs/mois (au-dessus du seuil de travail de 10k) pour que le V1 ait assez d'événements à analyser. Le seuil reste une **hypothèse** (question §12 du contexte) : le plan le mesure.
3. **Plafond de taille** : au-delà de ~150k visiteurs et ~15 personnes, on retombe sur des équipes outillées (Contentsquare, VWO) avec un cycle d'achat long.
4. **Douleur monétisée** : une marque qui paie son trafic ressent chaque point de conversion perdu. L'argument est « rentabiliser le trafic que vous payez déjà ».
5. **Adéquation au V1** : ce segment a besoin de *savoir quoi changer*, pas d'une plateforme d'expérimentation. C'est exactement ce que fait V1 (analyse + recommandations, humain dans la boucle).

**Pari secondaire, volontairement limité** : 2 à 3 **agences** approchées comme *partenaires de pilote* (et non comme clientes), pour tester H-AGENCE : « une agence voit Solen comme un levier de productivité, pas comme une menace ». Si c'est vrai, c'est le canal le plus efficace à moyen terme (1 agence → N boutiques). Mais **on ne construit pas le GTM dessus tant que ce n'est pas démontré**.

**Écarté pour 90 jours** : les growth managers de marques > 150k visiteurs. Cycle trop long, stack concurrente déjà en place, exigences sécurité / RGPD que le prototype ne remplit pas. On en interviewe quelques-uns pour comparer, on ne les prospecte pas.

**Niveau de preuve de H-ICP : P0–P1.** Signaux qui la renverseraient : voir §5 (semaines 3–4).

---

## 2. Proposition de valeur et message pour l'ICP

### 2.1 Positionnement (format de l'outil gtm-plan)

| Champ | Contenu | Preuve |
|---|---|---|
| Catégorie | Optimisation de conversion pour boutiques Shopify existantes (pas analytics, pas A/B testing seul) | P0 |
| Pour | Marques Shopify de 20k à 150k visiteurs/mois sans spécialiste CRO | P0 |
| Qui ont besoin de | savoir *quoi* changer sur leur site, et dans quel ordre, sans y passer des heures ni payer une agence | P0 |
| Solen est | une couche qui observe le comportement des visiteurs et le transforme en frictions priorisées et en tests à lancer | Construit (V1 partiel) |
| Contrairement à | GA4 / Shopify Analytics (des chiffres sans diagnostic), Hotjar (des enregistrements à regarder soi-même), une agence CRO (cher, lent) | P1 |
| Solen | livre des recommandations expliquées (ce qu'on observe, l'hypothèse, le test à faire), sans migrer la boutique | P0 |

### 2.2 Messages

**Phrase principale (à tester)** :
> **« Vous payez déjà votre trafic. Solen vous dit où il se perd sur votre boutique, et quoi tester en premier. »**

**Variantes à tester en A/B dans l'outreach** (une seule variable change) :
- **A — Coût du trafic** : « Vous payez déjà votre trafic. Solen vous dit où il se perd et quoi tester en premier. »
- **B — Temps** : « Les 3 frictions qui coûtent le plus sur votre boutique, chaque semaine, sans passer vos soirées dans GA4 et Hotjar. »
- **C — Alternative à l'agence** : « Un audit de conversion continu, pour une fraction du prix d'une agence CRO. »

**Pitch 30 secondes** :
> « Sur la plupart des boutiques Shopify, les données sont là (GA4, Shopify, parfois Hotjar), mais personne n'a le temps de les transformer en décisions. Solen installe un petit script, observe comment vos visiteurs se comportent, sur mobile comme sur desktop, et vous envoie chaque semaine les frictions les plus coûteuses : ce qu'on voit, pourquoi ça bloque probablement, et quoi tester. Vous restez maître de ce qui change sur votre site. On ne promet pas un chiffre de conversion : on vous aide à tester les bonnes choses plus vite. »

**Trois propositions de valeur** :
1. **Savoir quoi changer** : des frictions précises (page, device, élément), pas un tableau de bord de plus.
2. **Comprendre pourquoi** : chaque recommandation distingue ce qui est observé de ce qui est supposé.
3. **Garder le contrôle** : rien n'est modifié sur la boutique sans votre validation.

**Preuves disponibles aujourd'hui** : aucune preuve client. On peut seulement montrer un rapport réel sur une boutique réelle (d'où l'offre de pilote gratuite au démarrage). **Ne pas inventer de chiffres ni de témoignages.**

**Mots à éviter** : « AI agent », « révolutionner l'e-commerce », « IA qui augmente vos ventes », « autopilot », « l'OS de l'e-commerce ». Parler de **frictions, visiteurs, tests, recommandations**. Mentionner l'IA seulement si on demande comment ça marche.

### 2.3 Objections anticipées (hypothèses, à enrichir après les interviews)

| Objection | Réponse |
|---|---|
| « J'ai déjà GA4 et Hotjar. » | « Parfait, Solen ne les remplace pas. Combien d'heures par mois passez-vous à les regarder, et quelle est la dernière modification que vous avez faite grâce à eux ? » (C'est une question de découverte, pas un argument.) |
| « Encore un script qui ralentit mon site. » | Mesurer l'impact réel (Lighthouse avant / après) pendant le pilote et le montrer. Ne rien affirmer avant de l'avoir mesuré. |
| « Les recommandations IA sont génériques. » | Montrer un rapport sur *leur* boutique pendant le pilote. Si elles sont génériques, c'est un signal produit à noter, pas à défendre. |
| « Mes données / RGPD ? » | Pas de données personnelles collectées (à vérifier et à documenter avant le premier pilote), script chargé après consentement, suppression des données à la fin du pilote sur demande. |
| « Pourquoi pas une agence ? » | « Une agence reste pertinente pour exécuter. Solen vous aide à savoir quoi lui demander. » |

---

## 3. Canaux d'acquisition classés

Classement par **coût** (temps du fondateur ; le budget est de 0 €) et **vitesse d'apprentissage** (délai avant d'obtenir un signal exploitable).

| Rang | Canal | Coût (temps) | Vitesse d'apprentissage | Commentaire |
|---|---|---|---|---|
| 1 | **Outbound LinkedIn + email ciblé** vers fondateurs Shopify | Moyen | **Très rapide** (réponses en 48 h) | Contrôle total de la cible et du message. Canal principal. |
| 2 | **Communautés e-commerce / Shopify FR** | Faible | Rapide | Permet de publier une offre d'audit, de recruter des interviewés et de tester le message à froid. |
| 3 | **Réseau personnel + SKEMA / Vianeo** | Très faible | Rapide mais biaisé | Premières interviews et introductions chaudes. Biais de politesse à surveiller. |
| 4 | Agences CRO / e-commerce (partenariat de pilote) | Moyen | Moyenne (3–6 semaines) | Levier fort si H-AGENCE se vérifie. Pari secondaire. |
| 5 | Contenu LinkedIn (« autopsies de conversion » de boutiques publiques) | Moyen | Lente (semaines à mois) | Construit la crédibilité ; à démarrer en fond à partir du mois 2. |
| 6 | Shopify App Store | Élevé (dev, review) | Lente | Pas avant d'avoir un produit multi-boutique et une preuve de valeur. |
| 7 | Publicité payante, Product Hunt, salons | Budget / temps élevés | Variable | Hors périmètre (0 € et pas de produit self-serve). |

### 3.1 Canal 1 — Outbound LinkedIn + email

- **Où trouver les prospects** :
  - Liste de boutiques : BuiltWith / Store Leads (versions gratuites ou essais) filtrés sur Shopify + France / Belgique / Suisse ; à défaut, recherche Google `site:myshopify.com` et marques DTC suivies sur Instagram.
  - Filtrage du trafic : Similarweb gratuit, fourchette 20k–150k visites/mois (estimation imprécise : la confirmer pendant l'appel).
  - Décideur : LinkedIn, recherche « fondateur » / « co-founder » / « head of e-commerce » + nom de la marque.
  - Signal d'achat prioritaire : la marque fait tourner des pubs Meta (Meta Ad Library), donc elle paie son trafic.
- **Message (premier contact, sans pitch, orienté interview)** :
  > « Bonjour [Prénom], je travaille sur l'optimisation de conversion des boutiques Shopify et j'étudie comment les marques comme [Marque] décident de ce qu'elles changent sur leur site. Est-ce que 20 minutes pour me raconter la dernière fois que vous avez essayé d'améliorer votre conversion vous paraîtraient envisageables ? Je ne vends rien pendant cet appel. En échange, je vous envoie une analyse gratuite de 3 frictions visibles sur votre fiche produit mobile. »
- **Relance J+4** : une ligne avec une observation concrète et vraie sur leur site (ex. « sur mobile, le bouton d'ajout au panier de votre fiche X arrive après 2 écrans de scroll »).
- **Volume** : **20 contacts qualifiés par jour ouvré, 3 jours par semaine = 60 / semaine**, soit ~400 sur les semaines 1–8. Cibles : taux de réponse ≥ 10 %, ≥ 30 % des réponses → appel.

### 3.2 Canal 2 — Communautés e-commerce

- **Où** : groupes Facebook et LinkedIn de marchands Shopify francophones, Slack / Discord e-commerce, subreddits r/shopify et r/ecommerce (anglophones : utiles pour les interviews, hors cible commerciale FR). Vérifier les règles de chaque groupe (autopromotion souvent interdite).
- **Message** (post à valeur, pas publicitaire) :
  > « J'étudie comment les petites équipes e-commerce décident quoi changer sur leur site pour améliorer la conversion. Je cherche 10 marques Shopify (20k+ visiteurs/mois) pour un appel de 20 min. En échange : une analyse gratuite de votre parcours mobile. »
- **Volume** : **2 posts / semaine** dans des groupes différents, **5 commentaires utiles / semaine** (répondre à des questions de conversion, sans lien). Cible : ≥ 5 réponses qualifiées par post.

### 3.3 Canal 3 — Réseau personnel + SKEMA / Vianeo

- **Où** : contacts directs du fondateur, alumni SKEMA fondateurs de marques e-commerce, mentors Vianeo, anciens collègues en agence ou marketing.
- **Message** :
  > « Je cherche à parler à des fondateurs ou responsables e-commerce de marques Shopify (20k+ visiteurs/mois). Connais-tu 1 ou 2 personnes à qui je pourrais demander 20 minutes ? Voici un message prêt à transférer : [2 lignes]. »
- **Volume** : **30 demandes d'introduction** sur les semaines 1–2. Cible : ≥ 10 introductions → ≥ 6 interviews.
- **Attention** : les interviews obtenues via le réseau surestiment l'intérêt. Les marquer comme telles dans le suivi et ne pas les compter comme des signaux d'achat.

---

## 4. Offre de pilote

### 4.1 Hypothèse testée

**H-PILOTE** : « Une marque de l'ICP installe un script tiers et consacre 30 min/semaine à un rapport pendant 4 semaines, en échange de recommandations sur sa boutique. » **H-WTP** : « Après avoir vu la valeur, au moins 1 sur 3 accepte de payer. »

### 4.2 Ce que le marchand obtient (4 semaines)

1. **Installation faite par le fondateur** (script via Shopify Custom Pixel / thème, 30 min en visio), avec mesure de l'impact sur la vitesse du site.
2. **Rapport hebdomadaire** (4 rapports) : les 3 frictions prioritaires, avec pour chacune *observation → hypothèse → modification proposée → comment la mesurer*, et la heatmap mobile / desktop des pages clés.
3. **Un appel de 20 min par semaine** pour passer le rapport en revue.
4. **Un accompagnement sur 1 à 2 modifications** choisies par le marchand, avec comparaison avant / après (et non un A/B test, que le V1 ne fait pas ; l'annoncer clairement, car un avant / après n'est **pas une preuve causale**).

**Mode « concierge » assumé** : le fondateur relit et corrige chaque rapport généré par `/analyze` avant envoi. Cela permet de mesurer l'écart entre la sortie brute de l'IA et ce qui a de la valeur, et donc ce qui doit être construit.

### 4.3 Ce que je demande en échange

- Accès en lecture à Shopify Analytics (ou export hebdomadaire de la conversion) pour comparer.
- 30 min/semaine d'attention (appel + lecture du rapport).
- Un **entretien de fin de pilote** enregistré (avec accord).
- L'autorisation d'utiliser les apprentissages de façon **anonymisée**, et un témoignage public seulement si le marchand le souhaite.
- **Un engagement de principe** : « si le pilote vous a été utile, vous passez à l'offre payante au tarif pilote ».

### 4.4 Hypothèse de prix à tester

**Pas de données de WTP aujourd'hui (P0).** Repères de prix : ordres de grandeur publics, **à vérifier** avant de s'y référer devant un prospect. Hotjar a un palier gratuit et des paliers payants à quelques dizaines à centaines d'€/mois ; VWO / AB Tasty / Contentsquare sont dans les centaines à milliers d'€/mois, souvent sur devis ; un audit CRO en agence coûte typiquement quelques milliers d'€.

| Vague | Offre | Prix testé | Ce qu'on apprend |
|---|---|---|---|
| Pilotes 1–3 | Pilote 4 semaines | **0 €** | Installation, usage, valeur perçue (H-PILOTE) |
| Pilotes 4–8 | Pilote 4 semaines | **149 € (remboursé si aucune recommandation jugée utile)** | Le paiement initial filtre-t-il les curieux ? |
| Conversion post-pilote | Abonnement mensuel, rapport hebdo + appel mensuel | **Ancrage à 290 €/mois, tarif pilote à 190 €/mois** | Taux d'acceptation, objections de prix |

Méthode : présenter le prix **après** avoir recueilli ce que le marchand dépense déjà (outils, agence, heures), selon §23 du contexte. Noter chaque réaction de prix mot pour mot. Si > 80 % acceptent sans discuter, le prix est probablement trop bas ; si 0 % acceptent, chercher d'abord si c'est un problème de valeur ou de prix.

**Hors périmètre** : le prix à la performance (§31). Il suppose une attribution causale que le V1 ne permet pas.

### 4.5 Prérequis minimaux avant le premier pilote (une semaine, pas plus)

Seulement ce qui bloque un pilote réel :
1. `site_id` sur les événements et filtre par boutique dans `/heatmap` et `/analyze` (sinon les données des pilotes se mélangent).
2. Protection minimale des endpoints de lecture (token par boutique).
3. Vérifier qu'aucune donnée personnelle n'est collectée ; script conditionné au consentement ; une page « données & confidentialité » d'une page.
4. Un modèle de rapport (Google Doc ou Notion), rempli à la main à partir de `/analyze` et `/heatmap`.

Tout le reste (dashboard, génération de variantes, A/B testing) est **explicitement hors périmètre** des 90 jours.

---

## 5. Plan de 90 jours, semaine par semaine

Rythme type d'une semaine : **3 demi-journées outbound, 2 à 3 demi-journées interviews / pilotes, 1 demi-journée produit, 1 demi-journée synthèse**. Le fondateur est seul : si une semaine déborde, c'est le produit qui est coupé, pas le terrain.

### Phase 1 — Problème et cible (semaines 1–4)

| Sem. | Actions | Hypothèse testée | Indicateur de succès | Seuil qui fait changer de cap |
|---|---|---|---|---|
| **1** | Tableau de suivi (CRM simple : Notion / Sheets). Guide d'interview (§19–23). Liste de 150 boutiques ICP. 30 demandes d'introduction réseau. Premiers 60 contacts outbound (variante A). | H-ACCÈS : l'ICP est joignable par un fondateur seul. | ≥ 6 interviews planifiées. | < 3 interviews planifiées → revoir le message (plus court, offre d'audit en premier) et élargir à la Belgique / Suisse / Québec. |
| **2** | 5–6 interviews. 60 contacts outbound (variante B). 2 posts en communauté. Prérequis produit §4.5 (1 demi-journée). | H-DOULEUR : l'ICP a essayé d'améliorer sa conversion dans les 3 derniers mois et en garde une frustration concrète. | ≥ 60 % des interviewés racontent une tentative récente avec un coût (temps ou argent). | < 30 % → le problème n'est pas prioritaire pour ce segment : tester le haut de fourchette (P2) en semaine 3. |
| **3** | 5–6 interviews, dont **2 growth managers et 2 agences** pour comparer. 60 contacts (variante C). Prérequis produit terminés. | H-ICP : le segment 20k–150k souffre plus / décide plus vite que P2 et P3. | Grille §24 remplie pour chaque interview ; l'ICP a le meilleur score douleur × accessibilité. | Si P2 ou P3 a un score nettement supérieur sur au moins 4 interviews → pivoter l'ICP pour la phase 2. |
| **4** | Synthèse des ~15 interviews (patterns, citations, coût actuel, outils abandonnés, niveau d'autonomie accepté). Choix du message gagnant (A / B / C). **Décision go / pivot sur l'ICP.** Proposition de pilote à 5 interviewés. | H-MESSAGE : un message génère ≥ 2 fois plus de réponses que les autres. H-PILOTE (début). | ≥ 3 pilotes acceptés. Taux de réponse outbound ≥ 10 % sur le meilleur message. | < 2 pilotes acceptés sur 5 propositions → la valeur perçue d'un « rapport » est faible : tester une offre plus concrète (audit ponctuel en direct) avant de poursuivre. |

### Phase 2 — Valeur en conditions réelles (semaines 5–8)

| Sem. | Actions | Hypothèse testée | Indicateur de succès | Seuil qui fait changer de cap |
|---|---|---|---|---|
| **5** | Installation des 3 premiers pilotes (gratuits). Mesure vitesse avant / après. Outbound continu (60 / sem., meilleur message, CTA = pilote). | H-INSTALL : l'installation prend < 1 h et ne bloque pas. | 3/3 installés en < 1 semaine ; impact vitesse négligeable. | ≥ 2 installations bloquées (dev, RGPD, peur) → l'intégration est un frein majeur : documenter les raisons et prioriser une installation « 1 clic » avant tout autre travail. |
| **6** | Premier rapport hebdo (concierge). Chronométrer le temps de relecture / correction de chaque rapport. Contact de 3 agences pour un pilote partenaire. | H-SIGNAL : le volume de trafic de l'ICP suffit à produire des recommandations non génériques. | Le marchand juge ≥ 1 reco sur 3 « nouvelle et actionnable ». Relecture < 1 h / rapport. | Si les recos sont jugées génériques sur les boutiques < 30k visiteurs mais pas au-dessus → relever le plancher de l'ICP. Si génériques partout → le problème est le produit : revoir l'analyse avant de recruter d'autres pilotes. |
| **7** | Rapport n° 2. Accompagner 1 modification par pilote. Pilotes 4–5 proposés à **149 €**. | H-USAGE : le marchand agit sur les recos. H-PAY-1 : un pilote payant est acceptable. | ≥ 2 marchands sur 3 appliquent ≥ 1 modification. ≥ 1 pilote payant signé. | 0 modification appliquée → la valeur n'est pas dans le diagnostic mais dans l'exécution (piste V2) : à creuser en interview, sans construire. 0 pilote payant sur 5 propositions → garder 0 € mais exiger un engagement plus fort (témoignage, accès aux données). |
| **8** | Rapport n° 3. Entretien à mi-parcours. Réponse des agences. **Revue de mi-parcours** : écrire ce qui est P3, ce qui est encore P0. | H-AGENCE : une agence voit Solen comme un levier. | ≥ 1 agence accepte un pilote sur 1 de ses clients. | 0 / 3 agences, avec « menace » comme raison → abandonner le canal agence pour ce cycle. |

### Phase 3 — Disposition à payer et décision (semaines 9–13)

| Sem. | Actions | Hypothèse testée | Indicateur de succès | Seuil qui fait changer de cap |
|---|---|---|---|---|
| **9** | Rapport n° 4 et entretien de fin pour les pilotes 1–3. Proposition de conversion (190 €/mois tarif pilote). Démarrage des pilotes payants 4–5. | H-WTP : la valeur perçue justifie un abonnement. | ≥ 1 sur 3 accepte de payer. | 0 / 3 → identifier si c'est la valeur (« utile mais pas indispensable ») ou le prix ; si c'est la valeur, arrêter le recrutement et retravailler la proposition. |
| **10** | Premier contenu LinkedIn : 1 « autopsie de conversion » anonymisée par semaine, tirée des pilotes. Outbound continu. | H-CONTENU : le contenu issu de cas réels génère des conversations entrantes. | ≥ 3 conversations entrantes qualifiées d'ici la semaine 13. | 0 conversation → le contenu reste secondaire, rester sur l'outbound. |
| **11** | Pilotes payants en cours. Mesurer le temps fondateur par client (rapport + appel). | H-UNIT : un client prend < 2 h/semaine au fondateur. | ≤ 2 h / client / semaine. | > 4 h → le modèle concierge ne passe pas à l'échelle : identifier les 1–2 étapes à automatiser en priorité (c'est le vrai backlog produit). |
| **12** | Deuxième vague de conversion (pilotes 4–5). Consolider les chiffres : entonnoir contacts → réponses → appels → pilotes → payants. | H-WTP (confirmation). | ≥ 2 clients payants au total. | 0 client payant sur l'ensemble des 90 jours → ne pas construire V2 ; revenir en SEEK avec un autre segment ou un autre problème. |
| **13** | **Revue des 90 jours** : mise à jour de `SOLEN_CONTEXT.md` (ce qui passe de l'hypothèse au fait observé), décision ICP / prix / canal, brief pour un cofondateur technique fondé sur les preuves. | — | Document de décision écrit, chiffres à l'appui. | — |

### Cibles cumulées à 90 jours (hypothèses de travail, pas des prévisions)

| Étape | Cible |
|---|---|
| Contacts outbound qualifiés | ~500 |
| Interviews réalisées | ≥ 15 (dont ≥ 4 hors ICP pour comparer) |
| Pilotes démarrés | 5–8 |
| Pilotes ayant appliqué ≥ 1 reco | ≥ 3 |
| Clients payants | ≥ 2 (P4) |
| Agences en pilote partenaire | ≥ 1 |

---

## 6. Les 5 plus gros risques du plan et comment les détecter tôt

| # | Risque | Pourquoi c'est grave | Signal d'alerte précoce | Quand on le voit | Réponse prévue |
|---|---|---|---|---|---|
| 1 | **Le problème n'est pas prioritaire** : l'ICP reconnaît la friction mais ne l'a jamais traitée et ne compte pas le faire. | Tout le reste s'effondre ; les gens sont polis en interview. | Les interviewés parlent du problème en termes généraux, sans exemple récent, sans montant, sans outil essayé. « Intéressant » sans demande de suite. | Semaines 2–4 | Appliquer strictement la question §19 (dernière fois, étape par étape). Si < 30 % ont une histoire concrète, changer de segment avant de lancer des pilotes. |
| 2 | **Les recommandations du V1 sont génériques** (« rendez le CTA plus visible ») et n'apportent rien de plus qu'un article de blog ou Hotjar. | La valeur perçue est nulle ; aucune différence avec l'existant. | Le fondateur réécrit > 50 % de chaque rapport ; le marchand dit « je le savais déjà » ; le taux « nouvelle et actionnable » est < 1 reco sur 3. | Semaine 6 | Tenir un journal des corrections du concierge : c'est la spécification de ce qu'il faut améliorer. Tester si la qualité dépend du trafic (seuil §12). |
| 3 | **Le fondateur finit par construire au lieu de vendre.** Seul, avec un prototype, la tentation est forte. | Le terrain ralentit, les hypothèses restent P0 à J90. | < 40 contacts envoyés par semaine ; > 1 jour par semaine passé sur le code ; interviews reportées. | Chaque vendredi | Tableau de bord hebdo de 4 chiffres : contacts, appels, pilotes actifs, heures de code. Plafond : 1 demi-journée de code / semaine hors semaine 2. |
| 4 | **Blocage à l'installation** : dev indisponible, crainte RGPD, peur de ralentir le site, refus d'un script inconnu. | Les pilotes n'ont jamais lieu, ou trop tard pour mesurer quoi que ce soit. | Délai entre « oui au pilote » et script actif > 7 jours ; questions répétées sur les données. | Semaines 4–5 | Préparer une page données & confidentialité et une installation guidée de 15 min. Si ça reste bloquant, tester un mode sans script (analyse à partir de GA4 / Shopify) pour isoler la valeur du diagnostic. |
| 5 | **On confond corrélation et effet** : un avant / après positif est présenté comme une preuve de valeur, ou un avant / après négatif fait abandonner une bonne piste. | Mauvaise décision sur la valeur de Solen ; perte de crédibilité si on sur-vend. | Tentation d'écrire « +X % de conversion grâce à Solen » avec < 4 semaines de données, sans contrôle et avec de la saisonnalité (Q4 : Black Friday, Noël). | Semaines 7–12 | Ne jamais communiquer de gain de conversion comme un résultat Solen. Mesurer la valeur par ce qui est observable : recos appliquées, temps gagné, disposition à payer. **Attention particulière : le plan tombe en octobre–décembre, les données de conversion seront faussées par la saisonnalité, et les marchands seront moins disponibles fin novembre.** |

**Risque de calendrier à noter à part** : les semaines 8–10 tombent autour du Black Friday / Cyber Monday. Les marchands de l'ICP seront peu disponibles et peu enclins à installer quoi que ce soit. Mitigation : démarrer tous les pilotes avant mi-novembre, et utiliser la période pour les entretiens avec les agences et la rédaction de contenu.

---

## 7. Ce qui n'est volontairement pas dans ce plan

- Construire V2 (génération de variantes), V3 (A/B testing) ou V4.
- Shopify App Store, publicité payante, Product Hunt.
- Pricing à la performance.
- Communication sur l'hypothèse de moat (mémoire d'expérimentation) ou sur la différenciation face à Amboras : elles ne sont pas pertinentes pour ce segment à ce stade et ne sont pas démontrées.

## 8. Note de méthode

Plan construit avec la trame de la skill `plugin-gtm:gtm-plan` (positionnement, messages, ICP, canaux, prix, calendrier). Le serveur MCP `plugin-gtm` n'était pas joignable lors de la rédaction : le plan n'a donc pas été enregistré dans l'outil gtm (ni checklist de lancement générée) ; ce fichier est la seule source.
