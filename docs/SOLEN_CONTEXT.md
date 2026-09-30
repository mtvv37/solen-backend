# SOLEN — MASTER BUSINESS PROMPT

> Document de référence du projet Solen. Toute IA ou personne qui travaille sur ce repo doit le considérer comme le contexte business de référence.
> Règle d'or : ne jamais présenter une hypothèse comme un fait validé.

## 0. Instruction générale

Solen est un projet SaaS B2B dans l'e-commerce, au stade **prototype / pré-validation marché**. Porté seul par son fondateur (profil stratégie, produit, marketing digital, data, acquisition), qui cherche à terme un **cofondateur technique / Software & AI Engineer** pour transformer le prototype en SaaS scalable.

L'objectif actuel n'est PAS de construire beaucoup de fonctionnalités, mais de **valider le problème, la cible, la proposition de valeur, le comportement des utilisateurs, le willingness-to-pay et le positionnement avant d'investir lourdement dans le produit**.

Toujours distinguer :

- ce qui est déjà construit ;
- ce qui est observé ;
- ce qui est une hypothèse ;
- ce qui doit encore être validé ;
- ce qui relève de la vision long terme.

---

## 1. Nom et positionnement

- **Nom :** Solen
- **EN :** The Self-Optimizing Commerce Layer
- **FR :** La couche d'optimisation autonome de l'e-commerce

Description courte :

> Solen permet aux boutiques e-commerce de s'améliorer automatiquement grâce au comportement de leurs visiteurs.

Alternative :

> Solen transforme le comportement des visiteurs en actions d'optimisation concrètes pour les boutiques e-commerce.

Passer de **Data → Dashboard → Humain → Décision → Développeur → Modification** à **Observer → Comprendre → Proposer → Tester → Apprendre → Améliorer**.

## 2. Vision

Rendre les boutiques e-commerce **auto-améliorantes**. Les boutiques reçoivent en continu des signaux (clics, scroll, abandon, rage clicks, temps passé, navigation, recherches, interactions, parcours, segments, conversions/non-conversions, différences device/audience…), mais ces données restent dans GA4, Shopify Analytics, Hotjar, Contentsquare, CRM/CDP, outils de testing, dashboards, Excel, rapports d'agences.

Le problème est moins le manque de données que **le temps et la complexité pour transformer ces données en décisions puis en changements réellement testés**.

> Vision ultime : une boutique qui observe son propre comportement, identifie ses opportunités, formule des hypothèses, génère des modifications, teste leur impact, apprend des résultats et améliore progressivement sa performance.

## 3. Philosophie produit

> **AI proposes. Reality decides.**

L'IA génère des hypothèses et propose des changements, mais une prédiction ou une analyse observationnelle n'est pas une preuve causale. Distinguer :

- **Observation** — « Les visiteurs mobiles abandonnent davantage sur cette étape. »
- **Hypothèse** — « La longueur / complexité de cette section pourrait contribuer à cette friction. »
- **Expérimentation** — « Testons une version simplifiée contre le contrôle. »
- **Résultat** — « La variante a généré +X% sur le KPI principal, avec tels effets secondaires. »

## 4. Le problème

Problème formulé pour la validation :

> « Comment les e-commerçants peuvent-ils identifier efficacement les frictions sur leur site et automatiser l'amélioration de leur conversion sans équipe dédiée ? »

- **4.1 Données dispersées** — Shopify, GA4, Hotjar, Contentsquare, Algolia, CRM, CDP, A/B testing, dashboards, agences ; aucun outil ne fait nécessairement toute la boucle.
- **4.2 Analyse manuelle** — regarder → anomalie → comprendre → hypothèse → décider → créer → designer/dev → test → attendre → analyser → décider. Chaîne longue.
- **4.3 Petites équipes sans ressources** — trafic, catalogue, budget marketing, mais pas de CRO specialist, data analyst, dev, UX, spécialiste A/B. Savent vouloir « améliorer la conversion » sans savoir quoi modifier ni comment tester.
- **4.4 Plus d'opportunités que de capacité d'exécution** — limites : temps, devs, validations internes, design, priorités, nombre d'expériences.
- **4.5 Agences limitées par la capacité humaine** — l'automatisation peut être un levier… ou une menace si le modèle dépend du temps facturé (à valider).

## 5. Problème structurel

Aujourd'hui : Comportement → Analytics → Analyse humaine → Hypothèse → Designer/dev → Modification → A/B test → Analyse → Rapport → Nouvelle hypothèse.

Solen vise : Comportement → Compréhension → Hypothèse → Modification → Expérimentation → Résultat → Mémoire → Nouvelle hypothèse.

Ne PAS positionner comme « un dashboard avec de l'IA » ni « un AI agent pour Shopify », mais :

> Une couche d'optimisation qui transforme continuellement les comportements observés en expérimentations et en améliorations.

## 6. Ce que Solen n'est pas

- Un concurrent de Shopify.
- Une nouvelle plateforme e-commerce (pas d'hébergement, checkout, paiement, catalogue, infra complète).
- Un simple outil analytics (GA4, Shopify Analytics, Hotjar, Contentsquare y répondent déjà en partie).
- Un simple dashboard.
- Une agence CRO.
- Un simple outil d'A/B testing (le test n'est qu'une étape de la boucle).
- Un chatbot (le conversationnel peut exister mais n'est pas la valeur centrale).
- Un « AI agent » générique.

## 7. Vision fonctionnelle

1. **Observer** — clics, scroll, abandon, navigation, interactions, recherche, conversions, parcours, device, landing pages, segments.
2. **Comprendre** — frictions, anomalies, opportunités, pages sous-performantes, comportements inhabituels, segments problématiques.
3. **Proposer** — hypothèses (ex. « Les mobiles arrivent sur cette section mais interagissent peu avec le CTA ; hypothèse : CTA insuffisamment visible »).
4. **Modifier** — copy, CTA, variantes, sections, ordre de blocs, éléments de PDP, contenus, expériences UX.
5. **Tester** — baseline, contrôle, variantes, répartition du trafic, KPI principal, guardrails, arrêt, rollback.
6. **Apprendre** — résultat structuré : Contexte → Comportement → Problème supposé → Hypothèse → Modification → Résultat ; alimente les futures recommandations.

## 8. Roadmap d'autonomie

- **V1 — Intelligence** : analyse, identification des problèmes, recommandations. Human-in-the-loop.
- **V2 — Copilot** : génère modifications, contenus, variantes, prépare les expériences. Le marchand valide avant publication.
- **V3 — Experimentation** : crée les expériences, répartit le trafic, mesure, compare. Le marchand valide le déploiement.
- **V4 — Autopilot** : automatise Observe → Understand → Hypothesize → Modify → Test → Learn → Repeat, avec garde-fous.

## 9. Gouvernance et sécurité

L'autonomie ne signifie jamais « laisser une IA modifier aveuglément la production ». Le système intègre : contrôle, baseline, expérimentation, limites de déploiement, kill switch, rollback, guardrails, KPI principal/secondaires, seuils de sécurité, validation humaine pour certaines catégories.

- **Potentiellement automatisable :** CTA, copy, ordre de sections, contenu, blocs PDP, éléments UX.
- **Validation humaine :** prix, promotions, checkout, éléments juridiques, branding critique, modifications à fort impact business.

Autonomie **graduelle et contrôlée**.

## 10. Prototype actuel

Un prototype V1 existe (analyse comportementale, identification d'opportunités, génération de recommandations). C'est une première preuve de faisabilité technique, mais **PAS** : un SaaS commercial, un produit validé, une preuve de WTP, de PMF, de moat ou de performance commerciale.

## 11. Premier marché cible

E-commerce B2C → biens physiques → **Shopify** → petits e-commerçants et équipes e-commerce → trafic suffisant pour analyser et expérimenter. Plus tard éventuellement : WooCommerce, Magento, autres stacks.

## 12. Trafic

Seuil de travail pour sélectionner des interviewés : **~10 000 visiteurs/mois**. Ce n'est PAS une règle statistique. Question à valider :

> À partir de quel niveau de trafic et de volume de conversion Solen produit-il suffisamment de signal pour générer des recommandations et expériences utiles ?

## 13–15. Personas à tester (non validés)

### Persona 1 — Petit e-commerçant Shopify / Founder
- **Job :** améliorer la performance commerciale à partir du trafic existant sans devenir expert CRO.
- **Tâches :** surveiller ventes/conversion, analyser les pages, identifier problèmes, modifier le site, tester, gérer l'acquisition, arbitrer.
- **Pains :** temps, expertise, savoir quoi changer, coût des agences, peur de casser, mesure d'impact, trop d'outils.
- **Gains :** opportunités détectées automatiquement, recommandations actionnables, gain de temps, moins de dépendance aux experts, amélioration continue.

### Persona 2 — E-commerce / Growth Manager
- **Job :** identifier régulièrement des opportunités et démontrer leur impact commercial.
- **Tâches :** KPI, opportunités, priorisation, hypothèses, coordination UX/design/dev, tests, analyse, reporting.
- **Pains :** trop de données, temps, dépendance aux devs, validations longues, backlog, trop peu d'expériences, ROI difficile à démontrer.
- **Gains :** plus d'expériences, cycles plus courts, analyses automatisées, moins de travail répétitif, meilleure exploitation du trafic.

### Persona 3 — Agence e-commerce / CRO
- **Job :** optimiser plusieurs boutiques clients avec une capacité d'exécution limitée.
- **Tâches :** audits, analytics, recommandations, variantes, tests, reporting, suivi client.
- **Pains :** travail répétitif, analyse manuelle, coûts humains, capacité limitée, reporting, nombreux comptes.
- **Gains :** productivité, plus de clients, focus stratégique, valeur délivrée.
- **Risque :** si facturation au temps, Solen = menace. À tester : menace ou levier ? Un modèle lié à la performance pourrait rendre l'automatisation attractive.

## 16. Job-to-be-done central

> « Améliorer la performance commerciale d'une boutique à partir du trafic existant. »

Différences entre segments : qui fait le travail, ressources, fréquence, expertise, budget, degré d'autonomie souhaité.

## 17. Méthode de validation

Logique **SEEK → COMMIT**. Valider : problème, marché, personas, concurrence, alternatives, proposition de valeur, positionnement, business model, GTM, WTP, MVP.

## 18. Interviews terrain

**15 interviews qualitatives** : 5 petits e-commerçants Shopify, 5 responsables e-commerce/Growth, 5 agences CRO/e-commerce. Aucune prétention statistique ; objectif : problèmes réels, comportements réels, solutions actuelles, frustrations, budgets, différences entre segments.

## 19. Question d'interview centrale

Ne pas pitcher Solen. Demander :

> « Racontez-moi la dernière fois où vous avez essayé d'améliorer la conversion de votre site, étape par étape. »

Reconstruire : Observation → Analyse → Identification → Solution → Modification → Test → Mesure → Décision. Comprendre ce qui s'est réellement passé.

## 20. À capturer par interview

- **Problème :** difficulté, intensité, fréquence.
- **Processus :** ce qui est réellement fait, dans quel ordre.
- **Outils :** Shopify, GA4, Hotjar, Contentsquare, Optimizely, VWO, AB Tasty, Excel, scripts, agence.
- **Temps :** combien, combien de personnes.
- **Coût :** outils, agence, consultants, ressources internes, devs.
- **Frustration :** ce qui ne marche pas, est lent, est abandonné.
- **Solutions abandonnées :** « Quel outil avez-vous arrêté de payer récemment et pourquoi ? »
- **Solutions maison :** scripts, automatisations, Make, n8n, workflows, dashboards, Excel, outils internes.

## 21. Questions critiques à valider

1. Le problème est-il réellement douloureux ?
2. Est-il fréquent ?
3. Combien coûte aujourd'hui sa résolution ?
4. Qui souffre le plus ?
5. Quelle solution actuelle ?
6. Pourquoi insuffisante ?
7. A-t-il cherché une alternative ?
8. A-t-il déjà payé pour le résoudre ?
9. Est-il prêt à changer son workflow ?
10. Quel niveau d'autonomie accepte-t-il ?

## 22. Niveaux d'autonomie à tester

Ne pas demander « Utiliseriez-vous Solen ? ». Tester :

1. Solen détecte un problème et recommande une action.
2. Solen génère la modification, l'humain valide.
3. Solen lance automatiquement un test contrôlé.
4. Solen déploie automatiquement les améliorations sous certaines règles.

Objectif : trouver **la zone de confiance réelle**.

## 23. Willingness-to-pay

Ne pas demander « Combien paieriez-vous ? ». Préférer : dépenses outils actuelles, coût agence, heures consacrées, outil arrêté et pourquoi, coût actuel de l'optimisation, qui fait le travail, budget déjà alloué.

**Coût actuel → valeur potentielle → capacité à payer → prix acceptable.**

## 24. Grille d'évaluation des personas

| Critère               | Question                                            |
| --------------------- | --------------------------------------------------- |
| Intensité             | Le problème est-il douloureux ?                     |
| Fréquence             | Combien de fois apparaît-il ?                       |
| Coût                  | Combien coûte sa résolution ?                       |
| Solutions actuelles   | Comment est-il résolu aujourd'hui ?                 |
| Insatisfaction        | Les solutions actuelles sont-elles insuffisantes ?  |
| Solutions abandonnées | Ont-ils déjà essayé autre chose ?                   |
| Willingness to change | Sont-ils prêts à changer ?                          |
| Budget                | Ont-ils déjà un budget ?                            |
| Autonomie             | Quel niveau d'automatisation acceptent-ils ?        |
| Intégration           | Préfèrent-ils une couche externe ou un all-in-one ? |
| Valeur                | Quelle valeur économique est créée ?                |

## 25. Concurrence

- **Analytics :** GA4, Shopify Analytics.
- **Behavioral analytics :** Hotjar, Contentsquare.
- **CRO / A/B testing :** Optimizely, VWO, AB Tasty.
- **Agences :** CRO, consultants, agences e-commerce.
- **Équipes internes :** Growth, Product, UX, Data, Engineering.
- **Solutions maison :** scripts, dashboards, automatisations, Make/n8n, outils internes.
- **Nouveaux acteurs AI-native :** notamment **Amboras** (US, YC S26).

## 26. Amboras

Positionnement : **AI-native e-commerce platform / AI Native Shopify** — reconstruire l'infrastructure e-commerce autour de l'IA.

- **Amboras :** Infrastructure → Commerce → AI
- **Solen :** Existing Commerce → Optimization Layer → AI

Solen ne demande pas de migrer la boutique. Cette distinction est une **hypothèse de différenciation à valider**, pas un avantage démontré.

## 27. Différenciation hypothétique

> Solen n'essaie pas de remplacer l'e-commerce. Il cherche à rendre l'e-commerce existant auto-optimisant.

Existing stack + Behavioral data + AI reasoning + Experimentation + Learning = Continuous optimization.

## 28. Hypothèse de moat : Experimentation Memory

Structure : **Context → Behavior → Friction → Hypothesis → Modification → Result**.

> « Dans ce contexte, ce type de comportement a déjà été observé. Cette hypothèse a été testée. Voici le résultat. »

Pourrait améliorer recommandations, priorisation, génération d'hypothèses, compréhension du contexte, expérimentations futures.

**Ce n'est qu'une hypothèse de moat.** Il faut démontrer : (1) qu'elle améliore effectivement les performances, (2) qu'elle produit de meilleurs résultats dans le temps, (3) qu'elle est difficile à reproduire, (4) qu'elle crée une learning loop propriétaire. Ne jamais dire que Solen possède déjà un moat.

## 29. Learning loop

> Every experiment makes the next experiment smarter.

La valeur croît avec le nombre d'expériences, la qualité des données, la diversité des contextes, la qualité des résultats, la structuration des connaissances. Distinguer :

- **Learning propre au marchand** (ce qui marche sur la boutique A) ;
- **Learning généralisable** (transférable à d'autres boutiques).

Distinction importante pour l'architecture et la confidentialité.

## 30. Architecture produit — vision

E-commerce stack → Solen → Optimization. Intégrations possibles : Shopify, GA4, tracking comportemental, analytics, outils marketing, éventuellement CDP. Références utiles : BigQuery, CDP, analytics, outils d'expérimentation. **Architecture finale non figée.**

## 31. Modèle business — hypothèse

SaaS B2B récurrent (hypothèse).

- **Subscription :** selon trafic, volume d'événements, nombre de boutiques, fonctionnalités, niveau d'autonomie.
- **Performance-based :** abonnement faible + composante liée à la valeur créée — pose des questions de causalité, attribution, baseline, saisonnalité, biais, contrôle, confiance. Non décidé.

## 32. Go-to-market

Non validé. Priorité : **trouver qui ressent le problème le plus fortement et pourquoi**. Canaux possibles ensuite : prospection directe, réseau Shopify, communautés e-commerce, agences, partenaires, contenu, LinkedIn, démos, outbound ciblé, partenariats agences. Le fondateur a de l'expérience en acquisition, landing pages, marketing digital, tracking, CRO, data, stratégie.

## 33. Validation avant construction

> **Do not build your way out of uncertainty.**

Interviewer → comprendre → identifier les patterns → sélectionner une cible → formuler une proposition de valeur → tester le besoin → tester le WTP → définir un MVP → construire → faire tester → vendre. Le prototype existe, mais ne doit pas pousser à construire inutilement.

## 34. Stratégie SKEMA / Vianeo

Accompagnement **SKEMA Entrepreneurs / Vianeo Néo**.

- **SEEK :** problème, marché, cible, concurrence, proposition de valeur, business model, GTM, WTP.
- **COMMIT :** MVP, pilotes, premiers clients, prospection, démos, ventes, structuration de l'entreprise.

Et non : construire pendant des mois → chercher ensuite si quelqu'un en veut.

## 35. Ressources humaines

Fondateur seul. Compétences : stratégie, produit, business, marketing digital, acquisition (Google/Meta/TikTok Ads), data, tracking, CRO, sites & landing pages, Looker Studio, BigQuery, Make, n8n, SQL ; expérience en stratégie, M&A, analyse de marché, AI & Data Strategy. Rôle naturel : **Founder / Product / Strategy / GTM**.

## 36. Besoin de cofondateur

**Software Engineer / AI Engineer / Technical Cofounder** : SaaS, backend, frontend, APIs, data, AI/LLM, tracking, intégrations Shopify, infrastructure, expérimentation, scalabilité. Objectif : **prototype local → SaaS scalable** (interface, backend, collecte de données, intégrations, gestion utilisateurs, expérimentation, sécurité, architecture scalable).

## 37. Réseau SKEMA

Rencontrer entrepreneurs, profils techniques / cofondateurs potentiels, mentors, experts ; obtenir des retours ; challenger le pitch ; workshops. Priorité : **rencontrer des profils techniques et obtenir des feedbacks**.

## 38. Ressources physiques / intellectuelles

Prototype local, logique produit, connaissances CRO/acquisition/web/marketing/data, expérience AI/data strategy, réseau SKEMA et entrepreneurial. Pas de brevet. PI potentielle : code, architecture, workflows, logique d'optimisation, données, mémoire d'expérimentation, connaissances accumulées, produit.

## 39. Ressources financières

Autofinancé, coûts volontairement faibles, pas de financement externe nécessaire pour la validation. Coûts futurs : hosting, base de données, APIs, LLM, tracking, infra, Shopify, monitoring, expérimentation, outils commerciaux, acquisition.

> **Validate first → spend later.** Utiliser startup credits, crédits cloud, programmes partenaires, outils gratuits / open source.

## 40. Risques principaux

1. Le problème n'est pas assez douloureux.
2. Les outils existants suffisent (GA4, Hotjar, Shopify, agence, équipe interne).
3. Manque de confiance dans l'automatisation.
4. Manque de trafic.
5. Intégration complexe.
6. Causalité (corrélation ≠ causalité).
7. Attribution.
8. Résistance des agences.
9. Coût d'infrastructure (tracking + AI au volume).
10. Faible différenciation (fonctionnalités copiables) — d'où l'importance potentielle de la mémoire d'expérimentation.

## 41. Principes produit

1. **Existing stack first.**
2. **Experimentation over prediction.**
3. **Human-in-the-loop initially.**
4. **Progressive autonomy.**
5. **Evidence over hype** — ne jamais affirmer qu'une IA « sait » qu'une modification augmentera la conversion.
6. **Continuous improvement.**
7. **Merchant control.**

## 42. Positionnement à éviter

« AI-powered e-commerce platform », « AI agent for e-commerce », « révolutionner le e-commerce avec l'IA », « l'OS de l'e-commerce », « IA qui augmente automatiquement vos ventes ».

Préférer : **The Self-Optimizing Commerce Layer** ou « Solen transforme le comportement des visiteurs en optimisations e-commerce testées. »

## 43. Positionnement simple

- **Court :** Solen aide les boutiques e-commerce à s'améliorer automatiquement à partir du comportement de leurs visiteurs.
- **Précis :** Solen analyse le comportement des visiteurs, identifie les frictions, génère des hypothèses d'optimisation et permet de tester les changements pour améliorer continuellement la conversion.
- **Vision :** Make every e-commerce store self-improving.

## 44. Core loop

**Observe → Understand → Propose → Test → Learn → Improve**

Forme technique : **Behavior → Hypothesis → Modification → Experiment → Result → Learning**

## 45. Exemple concret

Boutique Shopify, 50 000 visiteurs/mois. Solen observe : beaucoup d'arrivées sur une PDP, scroll important, faible interaction CTA, abandon avant ajout panier.

Hypothèse : CTA insuffisamment visible ou trop tard dans le parcours. Propose : variante A (CTA plus visible), variante B (CTA déplacé), contrôle. Répartition du trafic ; après suffisamment de données : contrôle X, A Y, B Z. Solen identifie la gagnante selon le KPI et les guardrails ; résultat enregistré dans la mémoire d'expérimentation pour les recommandations suivantes.

## 46. Vision long terme

Infrastructure d'optimisation continue. La boutique devient un système qui apprend de son trafic :

Traffic → Behavior → Insight → Hypothesis → Experiment → Result → Learning → Better experience → More learning.

> **Every store learns from every visitor.**

## 47. Questions stratégiques ouvertes (non résolues)

- **Marché :** quel segment souffre le plus ? Petit e-commerce ou entreprise structurée ? Shopify uniquement ? Quelle taille de trafic ?
- **Produit :** quelle fonctionnalité crée immédiatement de la valeur (analyse, recommandation, génération de modification, A/B testing, autonomie) ?
- **Confiance :** jusqu'où les marchands acceptent-ils l'automatisation ?
- **Business model :** SaaS, pricing par trafic / boutique / usage, performance-based, hybride ?
- **Moat :** la mémoire d'expérimentation produit-elle réellement un avantage propriétaire ?
- **GTM :** direct sales, écosystème Shopify, agences, partenariats, contenu, outbound ?
- **ICP :** Founder, Growth Manager, agence CRO ?

## 48. À faire maintenant

La priorité n'est pas V4. Priorités :

1. Faire les interviews.
2. Comprendre comment les utilisateurs optimisent aujourd'hui.
3. Identifier les problèmes réellement douloureux.
4. Mesurer le coût actuel.
5. Comprendre les outils utilisés.
6. Identifier les solutions abandonnées.
7. Comprendre la volonté de changer.
8. Comprendre le niveau d'autonomie acceptable.
9. Comparer les trois personas.
10. Choisir éventuellement un ICP initial.
11. Formuler une proposition de valeur plus précise.
12. Définir le MVP correspondant au problème réellement validé.

## 49. Règle de décision

Pas « Est-ce que les gens aiment Solen ? », mais :

> **Qui ressent le problème le plus fortement, le plus fréquemment, avec le plus de coût, et dispose déjà d'un budget ou d'une volonté claire de changer sa manière de travailler ?**

La cible initiale doit émerger des preuves terrain.

## 50. Philosophie finale

Pas « J'ai une idée d'IA, trouvons à quoi elle peut servir », mais :

> « Il existe un problème coûteux dans l'optimisation e-commerce. L'IA et l'automatisation permettent peut-être de construire une meilleure manière de le résoudre. Vérifions-le sur le terrain. »

| | |
|---|---|
| **Vision** | Make every e-commerce store self-improving. |
| **Produit** | The Self-Optimizing Commerce Layer. |
| **Mécanisme** | Observe → Understand → Propose → Test → Learn → Improve. |
| **Philosophie** | AI proposes. Reality decides. |
| **Priorité actuelle** | Terrain → données → synthèse → décision → produit. |
| **Priorité technique** | Prototype local → SaaS scalable. |
| **Besoin humain** | Founder Product/Strategy/GTM + Technical Cofounder Software/AI. |
| **Hypothèse de différenciation** | Optimiser l'existant plutôt que remplacer l'infrastructure e-commerce. |
| **Hypothèse de moat** | Une mémoire structurée des expérimentations permettant à Solen de devenir progressivement meilleur. |
| **État actuel** | Prototype fonctionnel, mais marché, ICP, pricing, GTM et PMF encore à valider. |

## 51. Instructions pour une IA qui travaille sur Solen

1. Challenger les hypothèses plutôt que les accepter automatiquement.
2. Distinguer faits, observations, hypothèses et vision.
3. Ne pas sur-vendre le produit.
4. Privilégier les preuves terrain.
5. Éviter le jargon startup inutile.
6. Chercher le problème avant la fonctionnalité.
7. Toujours réfléchir à la valeur économique créée.
8. Considérer les solutions existantes comme de vrais concurrents.
9. Ne pas supposer que l'IA est automatiquement une différenciation.
10. Ne pas considérer la mémoire d'expérimentation comme un moat prouvé.
11. Privilégier les expériences rapides et peu coûteuses.
12. Ne pas recommander de construire une fonctionnalité importante sans raison utilisateur claire.
13. Toujours demander : **« Quelle hypothèse cela permet-il de valider ? »**
14. Toujours demander : **« Quelle preuve avons-nous ? »**
15. Distinguer ce qui est souhaitable de ce qui est réellement faisable.
16. Garder une logique **SEEK → COMMIT**.
17. Ne pas perdre de vue l'objectif : un SaaS capable de générer une valeur mesurable pour les e-commerçants.
18. Garder la vision ambitieuse, mais traiter chaque étape avec pragmatisme.

### Phrase de synthèse

> **Solen veut transformer les boutiques e-commerce en systèmes capables d'apprendre et de s'améliorer continuellement à partir du comportement réel de leurs visiteurs, en utilisant l'IA pour générer et exécuter des hypothèses d'optimisation et l'expérimentation pour déterminer ce qui fonctionne réellement.**
