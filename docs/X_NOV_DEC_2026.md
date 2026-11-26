# Solen : 3 posts X par jour, du 24 novembre au 31 décembre 2026

> Version 2.0, 26/11/2026 : tout passe en français (tutoiement). Les frictions sont réécrites pour ne pas être évidentes (pièges Shopify réels, effets de bord, le bon indicateur), en format long X Premium ; « Worth stealing » devient « Idée à piquer », citations recopiées depuis les captures. Appels : 20 min en visio d'abord, le formulaire en option. Les versions anglaises sont dans l'historique git.
> Version 1.5, 24/11/2026 : Worth stealing complet (38 posts). Version 1.4, 23/11/2026 : départ décalé au mardi 24 novembre. Frictions #28 à #65 jusqu'au 31 décembre, #66 à #70 en réserve pour janvier. 22 visuels de friction, visuel d'appel ; sans tiret long ni emoji, selon `design/social/RULES.md`. Compteur X : les emoji et « € » comptent double.
> Suite de [`X_BUILD_IN_PUBLIC.md`](X_BUILD_IN_PUBLIC.md). Objectif : obtenir des appels 1:1 et des réponses au formulaire, pas des abonnés.

## Mode d'emploi

- **A · 9h : Friction Shopify à tester**, #28 à #70. Une friction qu'on ne voit pas en testant sa propre boutique, l'hypothèse, le test, l'indicateur. Finit par « Abonne-toi pour la suite. » Entre 280 et 500 caractères (X Premium) : le titre et le début de l'hypothèse restent visibles avant « Afficher plus ». 22 posts sur 43 ont un visuel (`design/social/x-friction/`).
- **B · 13h : Idée à piquer**, format long (X Premium). Une capture d'une fonctionnalité d'un site, ce qui marche, le mécanisme pas évident, ce qu'on testerait. 900 caractères maximum, puces en tiret, finit par « Abonne-toi pour la suite. »
- **C · 18h : question, demande d'échange, opinion ou journal.** Le dimanche : le bilan chiffré de la semaine, écrit avec tes vrais chiffres.
- **D · 21h, 13 jours sur 38 : un 4e post, uniquement un appel.** Surtout les lundis, mercredis et vendredis où le post C n'en est pas déjà un. Avec les 7 appels en C : 20 appels, plus la réponse type sous chaque post A et B.
- **« Réponds "appel" »** : envoie le lien Cal.com en message privé à chaque personne qui répond.
- **Sous chaque post A et B**, ta première réponse : ce texte, avec le visuel `design/social/x-friction/cta-form.png`. Remplace `[lien Cal.com]` et `[lien Tally]`.
  ```
  Boutique Shopify, e-commerce ou dev d'apps Shopify ?

  Je construis Solen, une app IA qui trouve quoi tester sur une boutique, segment par segment. J'ai besoin de ton avis, rien à acheter :

  20 min en visio : [lien Cal.com]
  4 min de formulaire : [lien Tally]
  ```
- **« Lien en réponse »** dans un post C ou D : les liens vont en première réponse (la réponse type), jamais dans le post.

## Idée à piquer : le format long

Une capture, un nom de marque, ce qui marche, une chose qu'on testerait. Au-delà de 280 caractères, X demande un compte Premium ;
le fil coupe après quelques lignes avec « Afficher plus », donc la marque et la fonctionnalité tiennent dans les deux premières lignes.

Le gabarit :

```
Idée à piquer #1 : [le détail] de [Marque].

[Ce qu'on voit, en une ou deux phrases, avec le texte exact du site entre « »].

Pourquoi ça marche :
- [ce que le client voit]
- [la question à laquelle ça répond avant qu'il la pose]
- [la friction que ça enlève]
- [comment ça soutient l'offre ou la marque]

Le vrai tour : [une idée pas évidente, en une ou deux phrases : le mécanisme, pas la description].

Ce que je testerais : [une idée précise, formulée comme un test].
Ou plus simple : [une version plus petite de la même idée].

Je regarderais [l'indicateur, et le segment si ça compte].

Abonne-toi pour la suite.
```

Un exemple rempli (889 caractères ; la marque reste entre crochets, le vrai post ne décrit que ce qu'on voit sur la capture) :

```
Idée à piquer #1 : le choix de taille de [Marque].

Toutes les tailles visibles d'un coup, les épuisées barrées, et une ligne sous les tailles : « Taille petit, prends au-dessus si tu hésites. »

Pourquoi ça marche :
- pas de menu déroulant à ouvrir
- les tailles épuisées restent à l'écran, donc tu sais qu'elles existent
- le conseil de taille arrive pile au moment du choix, pas dans un guide à part
- le bouton reste inactif tant qu'aucune taille n'est choisie

Le vrai tour : le conseil vient des avis. L'info existait déjà, ils l'ont juste déplacée là où le client décide.

Ce que je testerais : un lien « Entre deux tailles ? » qui ouvre le guide dans un tiroir, sans quitter la page.
Ou plus simple : la taille du mannequin et la taille qu'il porte, à côté des tailles.

Je regarderais le taux d'ajout au panier sur mobile, et les retours pour la taille.

Abonne-toi pour la suite.
```

**Règles**
- On parle de ce qu'on voit sur la capture, jamais des résultats de la marque : pas de « +20 % de conversion », on ne les connaît pas.
- On cite le texte du site tel qu'il est écrit, même en anglais. Si on n'a pas la capture sous les yeux, on paraphrase sans guillemets.
- « Ce que je testerais », jamais « ils devraient ». Ce n'est pas une critique.
- Pas évident : on explique le mécanisme (pourquoi ça marche), pas seulement ce qu'on voit.
- On ne refait pas une fonctionnalité déjà décortiquée par un autre compte (par exemple le sticky add-to-cart de Comfrt).
- On n'écrit « sur Shopify » que si on l'a vérifié.

## Marques à décortiquer

Des marques e-commerce dans l'esprit de Gymshark, Boku, Arntreal, Fincut et Holy. Pour chacune, où regarder en premier ; si rien ne ressort, prends une autre fonctionnalité ou une autre marque.

| Marque | Catégorie | Où regarder |
|---|---|---|
| Gymshark | sport | fiche produit mobile, tailles, panier |
| Boku | salle de bain (helloboku.com) | la fiche produit de référence du robot |
| Arntreal | marque de référence du robot (arntreal.com) | fiche produit |
| Fincut | envoie-moi le lien | fiche produit |
| Holy | envoie-moi le lien | fiche produit, packs |
| Represent | streetwear | fiche produit, drops |
| Oner Active | sport | tailles, avis |
| AYBL | sport | fiche produit, panier |
| Alphalete | sport | tailles, infos de coupe |
| YoungLA | sport | fiche produit, collections |
| Corteiz | streetwear | drops, ruptures |
| Broken Planet | streetwear | drops, fiche produit |
| Castore | sport | fiche produit, livraison |
| Skims | mode | tailles, infos de coupe |
| Alo Yoga | sport | fiche produit, panier |
| Vuori | sport | guide des tailles, avis |
| Horace | soin homme | routines, packs |
| Le Slip Français | mode | packs, cadeaux |
| Polène | maroquinerie | galerie photo, mise à l'échelle |
| Sézane | mode | fiche produit, livraison |
| Asphalte | mode | précommande |
| Jacquemus | mode | fiche produit, galerie |
| Respire | beauté | routines, abonnement |
| Typology | beauté | diagnostic, recommandations |
| Glossier | beauté | teintes, avis |
| Rhode | beauté | fiche produit, ruptures |
| Huel | nutrition | abonnement, packs |
| AG1 | nutrition | abonnement |
| Grenade | nutrition | packs, prix par unité |
| Ruggable | maison | tailles, variantes |
| HexClad | cuisine | packs, garanties |
| Ridge | accessoires | comparaison de modèles |
| Manscaped | soin homme | packs, abonnement |

## Calendrier

## Semaine du 24 novembre

### Mardi 24 novembre

**A · 9h · Friction #28** (357 caractères, X Premium)
```
Friction Shopify à tester #28 :

Un prix barré pour une remise de 5 %.

Hypothèse : une petite remise affichée rappelle surtout que l'affaire est petite. Le client se dit qu'il y aura mieux, et attend.
Test : le prix barré seulement au-dessus de 15 %, le prix seul en dessous.
À mesurer : ajout au panier des articles peu remisés.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-28.png`

**B · 13h · Idée à piquer #1 · Gymshark** (740 caractères, X Premium)
```
Idée à piquer #1 : le badge promo de Gymshark.

Une petite étiquette au-dessus du nom du produit : « -30% | 12 € D'ÉCONOMIE ».

Ce que j'aime :
- tu lis l'affaire avant le produit
- la même remise, dite deux fois : en pourcentage et en euros
- l'ancien prix (40 €) juste à côté du nouveau (28 €), zéro calcul

Et l'ordre n'est pas un hasard. Sur un article à 40 €, « -30 % » sonne plus fort que « 12 € ». C'est la règle des 100 : sous 100 €, commence par le pourcentage. Au-dessus, commence par les euros.

Ce que je testerais : l'inverser sur tout ce qui dépasse 100 €. « 45 € D'ÉCONOMIE | -30% » au lieu de « -30% | 45 € D'ÉCONOMIE ».

Je regarderais l'ajout au panier des articles remisés, par tranche de prix.

Abonne-toi pour la suite.
```
Image : ta capture Gymshark.

**C · 18h · Appel** (280/280)
```
Nouveau plan, et je passe en français.

J'arrête les audits gratuits (8 semaines, zéro preneur) et je fais ce que j'aurais dû faire dès le début : parler aux e-commerçants.

Comment tu décides quoi changer sur ta boutique ? 20 min en visio ou 4 min de formulaire. Lien en réponse.
```

### Mercredi 25 novembre

**A · 9h · Friction #29** (471 caractères, X Premium)
```
Friction Shopify à tester #29 :

Ton Black Friday passe par un code, et le panier affiche les prix pleins avec « réductions calculées au paiement ».

Hypothèse : le client qui n'a pas vu le code croit qu'il lui en faut un, part le chercher sur Google, et revient via un site de codes promo. Ou pas du tout.
Test : une remise automatique, visible dans le panier.
À mesurer : passage du panier au paiement, ventes attribuées à des sites de codes.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-29.png`

**B · 13h · Idée à piquer #2 · Arntreal** (881 caractères, X Premium)
```
Idée à piquer #2 : le tirage au sort Black Friday d'Arntreal.

Sur la fiche produit : « Chaque commande = 1 participation pour gagner une montre de luxe ». Une Rolex, une Omega Speedmaster ou une Cartier Santos. Le règlement juste en dessous.

Pourquoi c'est malin :
- la marque vend « tout d'un sac de luxe, sauf le prix ». Le lot, c'est le vrai logo de luxe. Même histoire.
- une remise mange de la marge sur chaque commande. Trois montres, c'est un coût fixe.
- le prix de 149,90 € ne bouge pas, donc il reste crédible en janvier

Ce que je testerais : « chaque commande » récompense le fait de couper son panier. Deux commandes d'un sac = 2 participations, une commande de deux sacs = 1. Fincut fait un tirage proche, mais donne un ticket par article. J'essaierais 1 participation par sac.

Je regarderais les articles par commande pendant le tirage.

Abonne-toi pour la suite.
```
Image : ta capture Arntreal.

**C · 18h · Question** (137/280)
```
Quel est LE truc qui casse sur ta boutique à chaque Black Friday ?

Codes promo, stock, vitesse du site, boîte mail du SAV, autre chose ?
```

**D · 21h · Appel** (213/280)
```
Tu connais quelqu'un qui a une boutique Shopify ?

Envoie-lui ce post : 20 minutes d'échange sur comment on décide quoi changer sur une boutique, et la synthèse de toutes les réponses en janvier.

Lien en réponse.
```

### Jeudi 26 novembre · Thanksgiving (US)

**A · 9h · Friction #30** (421 caractères, X Premium)
```
Friction Shopify à tester #30 :

Les boutons Apple Pay et Shop Pay sur la fiche produit.

Hypothèse : ils sautent le panier, donc ta barre de livraison offerte et tes suggestions. Plus de commandes, mais peut-être plus petites.
Test : le paiement express seulement dans le panier, pour les produits sous ton seuil de livraison offerte.
À mesurer : conversion et panier moyen, regardés ensemble.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-30.png`

**B · 13h · Idée à piquer #3 · Based** (851 caractères, X Premium)
```
Idée à piquer #3 : le bouton Black Friday de Based.

Le bouton principal ne dit pas « Ajouter au panier ». Il dit « BUY ONE GET ONE €21,95 », en doré.

- l'offre est là où tout le monde regarde juste avant de décider
- même prix qu'un seul, donc « un offert » ne demande aucun calcul
- la bannière en dessous le répète, et une garantie de 60 jours ferme la page

Ils n'ont pas ajouté un bloc promo à côté du produit. Ils ont changé l'action elle-même.

Ce que je testerais, pour les clients européens :
- les prix sont en euros, mais les seuils de livraison offerte en dollars (50 $+, 100 $+). Une seule devise, s'il te plaît.
- « 2.5 g » à côté de 21,95 € paraît minuscule. « Dure environ X semaines » répondrait à ça, s'ils ont le chiffre.

Je regarderais la conversion du trafic européen et les avis qui disent « petit ».

Abonne-toi pour la suite.
```
Image : ta capture Based.

**C · 18h · Opinion** (249/280)
```
Chaque promo des fêtes ajoute une ligne sur la fiche produit. Remise, seuil de livraison offerte, emballage cadeau, date limite de livraison.

À un moment, « Ajouter au panier » devient la 6e chose qu'on lit. Ça vaut un coup d'œil avant le week-end.
```

### Vendredi 27 novembre · Black Friday

**A · 9h · Friction #31** (412 caractères, X Premium)
```
Friction Shopify à tester #31 :

Un compte à rebours qui repart à zéro à chaque visite.

Hypothèse : ceux qui reviennent, tes acheteurs les plus probables, sont justement ceux qui le voient repartir. Le truc coûte la confiance du segment le plus chaud.
Test : une vraie date de fin, ou pas de compte à rebours.
À mesurer : conversion des visiteurs qui reviennent, séparée des nouveaux.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-31.png`

**B · 13h · Idée à piquer #4 · Arntreal** (815 caractères, X Premium)
```
Idée à piquer #4 : la case vide d'Arntreal.

Offre Black Friday : « 1 acheté = 1 offert », couleur au choix. À côté du sac choisi, un sac grisé avec un « + » : « CHOISIS TON SAC OFFERT ».

Based met son offre dans le bouton (#3). Arntreal la dessine.

Cette case vide, c'est une tâche à moitié faite. Tu en as choisi un, une place t'attend. On pousse plus fort vers un objectif qu'on croit déjà entamé. Nunes et Drèze ont un nom pour ça : l'endowed progress effect.

Un détail me gêne : l'offre affiche 149.90 € barré à côté de 149.90 €. Aucune économie visible.

Ce que je testerais : 299,80 € barré, ou « 2 sacs pour 149,90 €, soit 74,95 € le sac ». Et une fois la couleur offerte choisie, « 149,90 € économisés » en vert.

Je regarderais combien de commandes prennent l'offre à 2 sacs.

Abonne-toi pour la suite.
```
Image : ta capture Arntreal.

**C · 18h · Opinion** (190/280)
```
Ma règle du Black Friday, pour n'importe quelle boutique : ne rien changer aujourd'hui.

Note juste chaque moment « hmm, ça cloche ». Cette liste, c'est en gros ton plan de tests de janvier.
```

**D · 21h · Appel** (222/280)
```
Grosse journée pour les e-commerçants, donc je fais court.

Quand ça se calme : 20 minutes pour me dire comment tu décides quoi corriger sur ta boutique m'aideraient plus que tout ce que je pourrais coder. Lien en réponse.
```

### Samedi 28 novembre

**A · 9h · Friction #32** (456 caractères, X Premium)
```
Friction Shopify à tester #32 :

Un badge « Promo » sur la carte produit, alors que seule la taille XS est remisée.

Hypothèse : le client clique pour une affaire, choisit sa taille, voit le prix plein. Il ne se sent pas déçu, il se sent piégé.
Test : le badge seulement si toutes les tailles sont remisées, sinon « Promo sur certaines tailles ».
À mesurer : retours en arrière depuis la fiche, ajout au panier depuis les soldes.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-32.png`

**B · 13h · Idée à piquer #5 · Based** (869 caractères, X Premium)
```
Idée à piquer #5 : le panier de Based.

Pendant l'offre « 1 acheté, 1 offert », le panier devient un jeu. « Your haul. 1 pick, 0 free. » Une barre de progression, une case en pointillés marquée FREE à côté de ton article, et « BOGO savings €0.00 » en doré. Un zéro qu'on a envie de corriger.

« Haul » et « picks », c'est le vocabulaire des vidéos d'unboxing. Le panier parle comme ceux qui achètent.

Il y a aussi un plafond par commande. Une limite rend l'affaire précieuse.

Mais le plus gros chiffre du panier, c'est « €255.76 left ». Un budget que personne n'avait prévu. La barre mesure la distance jusqu'au plafond, pas jusqu'à la prochaine récompense.

Ce que je testerais : faire de la prochaine étape le titre. « Choisis-en 1 de plus, il est offert. » Le plafond en petit.

Je regarderais la part de paniers avec 2 articles ou plus.

Abonne-toi pour la suite.
```
Image : ta capture Based.

**C · 18h · Question** (86/280)
```
Qu'est-ce qui t'a le plus surpris sur ta boutique ce Black Friday ? En bien ou en mal.
```

**D · 21h · Appel** (229/280)
```
Si ta boutique fait moins de 10k visiteurs par mois, ta réponse m'intéresse encore plus.

Honnêtement, je ne sais pas encore si Solen peut aider les boutiques de ta taille. 20 min en visio ou 4 min de formulaire, lien en réponse.
```

### Dimanche 29 novembre

**A · 9h · Friction #33** (373 caractères, X Premium)
```
Friction Shopify à tester #33 :

Un code promo refusé au paiement, avec juste « code non valide ».

Hypothèse : le code est bon, il ne se cumule pas avec ta remise en cours. Mais le client comprend « on m'a menti » et s'en va.
Test : dire pourquoi : « Ne se cumule pas avec -20 %, déjà appliqué. »
À mesurer : abandons juste après un code refusé.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-33.png`

**B · 13h · Idée à piquer #6 · DJI** (895 caractères, X Premium)
```
Idée à piquer #6 : le Black Friday de DJI, sans remise.

Un bundle drone à 1 599 €, et le prix ne bouge pas. À la place : un sac à dos DJI Pro marqué « Cadeau », et « 5 fois plus de crédit DJI sur votre achat ».

Pourquoi c'est malin :
- pas de baisse de prix = pas de nouveau prix de référence. 1 599 € reste crédible après novembre.
- le crédit ne marche que chez DJI, donc il te ramène pour les batteries, les filtres, le prochain drone
- le cadeau est un objet qu'on visualise, listé avant les caractéristiques

Ce que je testerais : le crédit en euros. La base affichée, c'est « Récompense 1 % en crédit DJI ». 5 fois plus, ça fait environ 80 € sur ce bundle. « 80 € offerts » parle plus que « 5 fois plus ». Au-dessus de 100, les euros battent le ratio (règle des 100, voir #1).

Je regarderais la conversion pendant la promo, et le crédit utilisé sous 90 jours.

Abonne-toi pour la suite.
```
Image : ta capture DJI.

**C · 18h · Bilan de la semaine** : envoie-moi tes chiffres (réponses au formulaire, appels, abonnés), je l'écris.


## Semaine du 30 novembre

### Lundi 30 novembre · Cyber Monday

**A · 9h · Friction #34** (382 caractères, X Premium)
```
Friction Shopify à tester #34 :

« 2 achetés, -10 % » écrit sur la fiche produit, et plus un mot dans le panier.

Hypothèse : c'est dans le panier qu'on décide d'ajouter un 2e article. Pile là, l'offre a disparu.
Test : dans le panier : « Ajoute 1 article, -10 % sur les deux », avec l'économie en euros.
À mesurer : part des paniers à 2 articles ou plus.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-34.png`

**B · 13h · Idée à piquer #7 · HOLY** (887 caractères, X Premium)
```
Idée à piquer #7 : le panier de HOLY, à un centime près.

Une barre de récompenses de 49 € à 200 €. En dessous : la casquette et le shaker sont débloqués, et il ne manque que 0,01 € pour le Thermo Shaker bleu.

Le bundle coûte 99,99 €. Le cadeau suivant se débloque à 100 €.

Ce qu'ils font bien :
- les cadeaux débloqués sont de vraies lignes du panier, gratuites, valeur barrée
- le suivant est juste en dessous, avec un cadenas
- la livraison est déjà offerte, la barre ne parle que de cadeaux

À un centime du but, l'attraction est maximale : on accélère quand l'objectif se rapproche.

Ce que je changerais :
- le total des économies ne compte que les cadeaux (33,97 €). Avec la remise du bundle, c'est 53,95 €. Ils sous-vendent leur offre.
- 1 centime peut ressembler à un piège. Je testerais le shaker débloqué à 99,99 €, avec « on a arrondi pour toi ».

Abonne-toi pour la suite.
```
Image : ta capture HOLY.

**C · 18h · Appel** (204/280)
```
C'est juste après le Black Friday qu'on se souvient le mieux de ce qui a cassé.

Si tu as une boutique : 20 min pour me raconter comment tu décides quoi corriger, ou 4 min de formulaire.

Lien en réponse.
```

### Mardi 1 décembre

**A · 9h · Friction #35** (414 caractères, X Premium)
```
Friction Shopify à tester #35 :

Une protection de livraison payante, cochée d'office dans le panier.

Hypothèse : le client qui la repère doute de tout le reste de la commande. Et dans l'UE, un supplément payant pré-coché ne vaut pas consentement (directive 2011/83, art. 22).
Test : décochée, avec une ligne sur ce qu'elle couvre.
À mesurer : taux d'adhésion réel, paiements finalisés.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-35.png`

**B · 13h · Idée à piquer #8 · Fincut** (897 caractères, X Premium)
```
Idée à piquer #8 : les tickets dans le panier de Fincut.

Grand jeu Black Friday pour gagner 3 voitures, 1 ticket par article acheté. Dans le panier, les tickets sont une vraie ligne : ticket Grand Jeu, offert, x3.

Tu retires un t-shirt, tu perds un ticket. On déteste lâcher ce qu'on « a » déjà.

Aussi :
- le t-shirt offert du pack 3+1 ne donne pas de ticket. 4 t-shirts, 3 tickets. La règle tient.
- la barre de livraison offerte est déjà pleine
- première suggestion : une boîte cadeau à 9 €. Très de saison.

Ce qui me gêne : un bandeau donne le code BLACK20 (-20 %), à taper dans le champ code promo. Ce champ est replié tout en bas, et le total de 84 € ne l'inclut pas. Pourquoi me faire taper un code que le panier connaît déjà ?

Ce que je testerais : l'appliquer automatiquement, ou un bouton « Appliquer » sur le bandeau. Et dire s'il se cumule avec le pack.

Abonne-toi pour la suite.
```
Image : ta capture Fincut.

**C · 18h · Opinion** (232/280)
```
Honnêtement, le meilleur move de décembre pour la plupart des boutiques, c'est de ne rien refaire.

Ceux qui achètent des cadeaux ne sont pas tes visiteurs habituels. Note ce qui les bloque, corrige en janvier pour ceux qui restent.
```

### Mercredi 2 décembre

**A · 9h · Friction #36** (439 caractères, X Premium)
```
Friction Shopify à tester #36 :

La bulle de chat qui apparaît quelques secondes après le chargement, pile sur le bouton « Ajouter au panier » mobile.

Hypothèse : le pouce visait le bouton et ouvre le chat. Invisible sur ordi, invisible dans tes stats de chat.
Test : masquer la bulle sur les fiches produit mobiles, ou la remonter.
À mesurer : chats ouverts sans aucun message envoyé : la trace des taps ratés.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-36.png`

**B · 13h · Idée à piquer #9 · Represent** (864 caractères, X Premium)
```
Idée à piquer #9 : les deux lignes sous les boutons de Represent.

Boutique française, marque anglaise. Sous les boutons : « Express France Shipping » avec un drapeau, et « EU Import Duties Included ».

Depuis le Brexit, la peur n'est pas le prix, c'est la facture de douane à la porte. Ils la tuent avant même que tu poses la question.

- la livraison nomme ton pays, pas « livraison internationale »
- Klarna en 3 paiements de 18,66 €, chacun sous 20 €
- « Style With » montre 4 pièces, toutes avec un prix barré

Ils ont localisé les risques. Reste à localiser les mots. La page dit « RRP » et « 30% OFF - SAUVEGARDER €24 ». Sauvegarder, c'est pour un fichier. « Économisez 24 € » et « Prix conseillé » feraient boutique française.

Ce que je testerais : corriger cette seule ligne, et comparer la conversion française avant et après.

Abonne-toi pour la suite.
```
Image : ta capture Represent.

**C · 18h · Question** (111/280)
```
Qui fait vraiment les changements sur ton site ?

Toi, quelqu'un de l'équipe, une agence, ou en vrai personne ?
```

**D · 21h · Appel** (171/280)
```
Si tu as déjà dit « faudrait tester ça » sans jamais le faire, je veux ta réponse.

Ce qui t'en a empêché, c'est exactement ce que j'essaie de comprendre. Lien en réponse.
```

### Jeudi 3 décembre

**A · 9h · Friction #37** (413 caractères, X Premium)
```
Friction Shopify à tester #37 :

L'« Ajout rapide » des collections qui ajoute la première variante : souvent le XS.

Hypothèse : le client ne vérifie pas, la mauvaise taille part, et le retour coûte plus que la vente gagnée.
Test : l'ajout rapide ouvre d'abord le choix de taille.
À mesurer : taux de retour des commandes en ajout rapide, comparé aux commandes passées depuis la fiche.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-37.png`

**B · 13h · Idée à piquer #10 · Alphalete** (892 caractères, X Premium)
```
Idée à piquer #10 : l'info de coupe d'Alphalete.

« Ilon is 6'1"/185cm, wearing a size L with a 43"/109cm chest. »

La taille du mannequin seule ne dit presque rien pour un sweat. Son tour de poitrine, si. Ils donnent les deux, en pouces et en cm, pour que personne ne convertisse de tête.

- « Oversized » est un badge en haut et la première ligne de l'info de coupe. Dit deux fois, pour que personne ne prenne une taille en dessous.
- « Final sale » est aussi visible que le -70 %. Pas de surprise après la livraison.

Final sale, ça veut dire pas de retour. Et c'est justement là que l'info de coupe devient plus précise. J'adore.

Ce que je testerais : les mesures du vêtement à côté de celles du mannequin (largeur et longueur du L). Ou une ligne sur quoi faire entre deux tailles.

Je regarderais les questions de taille au SAV sur les articles en final sale.

Abonne-toi pour la suite.
```
Image : ta capture Alphalete.

**C · 18h · Journal** (246/280)
```
Solen aujourd'hui, honnêtement :

- site en ligne
- offres payantes à partir de 19 €/mois
- 0 client payant

La prochaine étape n'est pas une feature. C'est 15 conversations avec des e-commerçants. Le seul chiffre qui compte pour moi ce mois-ci.
```

> Vérifie le jour même : toujours 0 client payant ? Prix toujours à 19 € ?

### Vendredi 4 décembre

**A · 9h · Friction #38** (453 caractères, X Premium)
```
Friction Shopify à tester #38 :

Une pub Google Shopping qui envoie sur une taille épuisée.

Hypothèse : le lien pointe vers une variante précise. Si elle est épuisée, la page s'ouvre sur « Épuisé », même s'il reste d'autres tailles. Tu paies le clic, le client part.
Test : rediriger vers la première taille dispo quand celle du lien est épuisée, ou la retirer du flux.
À mesurer : rebond des visites payantes sur ces fiches.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #11 · HOLY** (877 caractères, X Premium)
```
Idée à piquer #11 : le prix par portion de HOLY.

Bundle à 99,99 €. Juste en dessous : « 150 PORTIONS / Seulement €0,80 PAR PORTION ».

Même somme, plus petite unité. Un prix à trois chiffres devient un prix de tous les jours.

- « Valeur totale : €119,97 » est juste au-dessus, donc 99,99 € se lit déjà comme une économie
- le bouton est à la première personne : « J'AJOUTE AU PANIER ». C'est le client qui parle, pas la marque.
- « Mix & match : économise jusqu'à 20 % » pour ceux qui ne veulent pas tous les goûts

0,80 €, c'est un chiffre que tu compares tout de suite à ce que tu achètes déjà. La comparaison se fait dans ta tête, gratuitement.

Ce que je testerais : la rendre explicite, si c'est vrai pour leurs clients. « 0,80 € la portion, moins qu'une canette d'energy drink. » Et à côté de « Expédition sous 6 à 10 jours », une vraie date.

Abonne-toi pour la suite.
```
Image : ta capture HOLY.

**C · 18h · Appel** (214/280)
```
Si tu as une boutique en ligne, j'aimerais 20 minutes avec toi. Pas de pitch. Je veux comprendre comment tu décides quoi changer sur ta boutique.

Pas le temps pour un appel ? 4 min de formulaire.

Lien en réponse.
```

### Samedi 5 décembre

**A · 9h · Friction #39** (432 caractères, X Premium)
```
Friction Shopify à tester #39 :

Tu fermes la pop-up « -10 % », le code disparaît pour de bon.

Hypothèse : fermer, ce n'est pas dire non à -10 %, c'est dire « pas maintenant ». Le client revient au moment de payer, et le code n'existe plus nulle part.
Test : un petit onglet « -10 % » qui reste après la fermeture.
À mesurer : inscriptions depuis l'onglet, conversion de ceux qui avaient fermé la pop-up.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-39.png`

**B · 13h · Idée à piquer #12 · Boku** (897 caractères, X Premium)
```
Idée à piquer #12 : le bouton compatibilité de Boku.

Un bidet qu'on installe sur ses propres toilettes amène une question évidente. Boku en fait un bouton : « Ce bidet est-il compatible avec vos WC ? »

- il nomme le doute avec les mots du client, avant qu'il aille le googler
- « Installation en 10 minutes sans travaux, sans électricité », avec une vidéo, règle la peur suivante
- la première suggestion est un robinet 3 voies pour les arrivées d'eau rigides. La solution au blocage le plus probable, vendue juste là.

Ça ressemble moins à une vente additionnelle qu'à de l'aide.

Ce que je testerais : transformer le bouton en test de 3 questions (forme des WC, abattant, arrivée d'eau) qui finit sur « Compatible » et ajoute la bonne pièce. Ou au moins garder la réponse jusqu'au panier.

Je regarderais la conversion après le test, et les retours « incompatible ».

Abonne-toi pour la suite.
```
Image : ta capture Boku.

**C · 18h · Question** (150/280)
```
Quelle est la dernière app que tu as désinstallée de ta boutique, et pourquoi ?

J'apprends plus de ce que les gens arrêtent que de ce qu'ils gardent.
```

### Dimanche 6 décembre

**A · 9h · Friction #40** (394 caractères, X Premium)
```
Friction Shopify à tester #40 :

« Expédié sous 3 à 5 jours ouvrés », en décembre.

Hypothèse : le client refait le calcul avec les week-ends, prend le pire cas, et conclut que ce ne sera pas là pour Noël. Même quand ça le serait.
Test : une date : « Commande avant le 18/12, reçu avant Noël. »
À mesurer : conversion en décembre, questions « ça arrivera à temps ? ».

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-40.png`

**B · 13h · Idée à piquer #13 · Gymshark** (878 caractères, X Premium)
```
Idée à piquer #13 : le panier latéral de Gymshark.

Tu ouvres le panier, et la première chose que tu vois, c'est la distance jusqu'à la livraison offerte : « Il manque 31 € », une barre de 0 € à 59 €.

- l'objectif passe avant les articles, donc il cadre tout ce qui suit
- chaque ligne répète couleur, taille et coupe (« Black Wash, M, Boxy Fit »)
- l'économie par article, en euros, même ici
- « Vos articles ne sont pas réservés », une urgence qui se trouve être vraie

La barre change la livraison : ce n'est plus un coût, c'est un objectif déjà à moitié atteint.

Mais regarde les suggestions. Le lot de 6 paires de chaussettes à 19,60 € ne comble pas 31 €. Ajoute la paire suivante à 11,20 €, et il manque encore 0,20 €.

Ce que je testerais : suggérer des produits juste au-dessus de l'écart. Ou en marquer un « Débloque la livraison offerte ».

Abonne-toi pour la suite.
```
Image : ta capture Gymshark.

**C · 18h · Bilan de la semaine** : envoie-moi tes chiffres (réponses au formulaire, appels, abonnés), je l'écris.


## Semaine du 7 décembre

### Lundi 7 décembre

**A · 9h · Friction #41** (425 caractères, X Premium)
```
Friction Shopify à tester #41 :

Aucune option pour que le prix ne soit pas dans le colis.

Hypothèse : celui qui offre se soucie moins de l'emballage que de la facture avec le prix dans la boîte, surtout quand le colis part direct chez la personne.
Test : une case « C'est un cadeau » : facture sans prix + petit message.
À mesurer : conversion en décembre, part des commandes avec la case cochée.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-41.png`

**B · 13h · Idée à piquer #14 · Fincut** (898 caractères, X Premium)
```
Idée à piquer #14 : le choix de pack de Fincut.

Trois options. Seul le t-shirt à l'unité affiche un coût en plus : « + Livraison 7,90 € ».

La livraison apparaît au moment du choix, sur l'option qu'ils préfèrent que tu évites. C'est le prix de ne pas prendre le pack.

- le t-shirt offert du 3+1 a sa propre ligne, couleur et taille. Tu l'as choisi, il est déjà un peu à toi.
- « Meilleure vente » sur le pack du milieu, « Meilleure offre (bientôt terminée) » sur le gros. Deux raisons différentes de monter d'un cran.
- « Prenez votre taille habituelle. » Une ligne, plus de doute.

1 t-shirt revient à 35,90 € livré. 4 t-shirts, 84 €, livraison offerte. L'option à l'unité existe surtout pour rendre le pack évident.

Ce que je testerais : le prix par t-shirt sur chaque option. 21 € pièce pour le 3+1, moins de 20 € pour le 5+2. Ou « 21 € le t-shirt » dans le bouton.

Abonne-toi pour la suite.
```
Image : ta capture Fincut.

**C · 18h · Opinion** (203/280)
```
Le taux de conversion seul cache qui tu as perdu.

Découpe-le par appareil, et entre nouveaux et anciens visiteurs, avant de décider quoi que ce soit. Un taux « stable » peut cacher une chute sur mobile.
```

**D · 21h · Appel** (213/280)
```
Tu as une marque en France, en Belgique, en Suisse ou au Québec ?

Je préfère parler que t'envoyer un formulaire : 20 minutes, pas de pitch. Juste comment tu décides quoi changer sur ta boutique.

Lien en réponse.
```

### Mardi 8 décembre

**A · 9h · Friction #42** (476 caractères, X Premium)
```
Friction Shopify à tester #42 :

Le panier dit « Livraison offerte » à 52 €. Au paiement, le code -10 % fait repasser sous 50 €, et les frais reviennent.

Hypothèse : la barre du panier compte avant le code, le seuil de livraison après. Le client voit revenir des frais qu'on lui avait annoncés offerts.
Test : une barre qui compte après remise, ou un seuil calculé avant remise.
À mesurer : abandons à l'étape livraison quand un code est utilisé.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-42.png`

**B · 13h · Idée à piquer #15 · AYBL** (839 caractères, X Premium)
```
Idée à piquer #15 : le bouton d'AYBL.

Tant que tu n'as pas choisi de taille, le bouton ne dit pas « Ajouter au panier ». Il dit « SÉLECTIONNEZ LA TAILLE ».

Pas d'erreur rouge après le tap, pas de bouton qui tremble. Juste l'étape suivante, là où tu regardes déjà.

- la taille du mannequin est écrite sur la première photo : 1,67 m, porte du XS
- « Taille normalement » ferme le bloc des caractéristiques clés
- la newsletter est un petit onglet sur le côté (« Ne manque plus aucun drop »), pas une pop-up. Facile à ignorer, facile à retrouver.

Ils évitent l'erreur au lieu de la corriger.

Ce que je testerais : une fois la taille choisie, la répéter dans le bouton. « Ajouter le XS au panier. » Petit, mais ça confirme le choix juste avant le tap.

Je regarderais les échanges et les retours pour la taille.

Abonne-toi pour la suite.
```
Image : ta capture AYBL.

**C · 18h · Question** (132/280)
```
Combien d'heures par mois tu passes à essayer d'améliorer ta boutique ?

Une estimation suffit. J'essaie de comprendre le vrai coût.
```

### Mercredi 9 décembre

**A · 9h · Friction #43** (461 caractères, X Premium)
```
Friction Shopify à tester #43 :

Tu choisis « Vert sapin », le panier affiche la photo du noir.

Hypothèse : sans image par variante, le panier montre la photo principale. Le client doute de sa couleur, retourne vérifier sur la fiche, et une partie ne revient pas.
Test : une image pour chaque variante, reprise dans le panier et l'email de confirmation.
À mesurer : allers-retours entre panier et fiche, retours « mauvaise couleur ».

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #16 · Arntreal** (840 caractères, X Premium)
```
Idée à piquer #16 : les trois lignes d'Arntreal.

Juste sous le nom du produit :
« Un sac basique, c'est de la mauvaise qualité.
Un sac de luxe, c'est 3 000 €, et tu paies le logo.
Celui-là a tout du luxe, à 149.90 €. »

Deux mauvaises options, et le produit se place au milieu. L'effet de compromis, fait en texte au lieu d'un tableau de prix. Et 3 000 € ancre le prix avant même que 149,90 € apparaisse.

Ça parle comme un pote, pas comme un catalogue.

Le vrai tour : tu arrêtes de te demander « 149,90 €, c'est cher ? » et tu te demandes « je veux payer un logo trop cher ? ». Réponse beaucoup plus facile.

Ce que je testerais : les 3 boutons en dessous (Look luxe, Tous les jours, Format cabine) ne font encore rien. Tape « Format cabine », vois le sac dans un coffre à bagages d'avion, avec ses dimensions.

Abonne-toi pour la suite.
```
Image : ta capture Arntreal.

**C · 18h · Opinion** (219/280)
```
La recherche en conversion la moins chère que je connaisse : une question sur ta page de confirmation de commande.

« Qu'est-ce qui a failli t'empêcher d'acheter aujourd'hui ? »

Lis 50 réponses avant ton prochain test.
```

**D · 21h · Appel** (188/280)
```
Tu as essayé l'A/B testing sur ta boutique et tu as arrêté ? Je veux savoir pourquoi.

Pas assez de trafic, les outils, le temps, des résultats pas fiables ? Lien en réponse, pas de pitch.
```

### Jeudi 10 décembre

**A · 9h · Friction #44** (391 caractères, X Premium)
```
Friction Shopify à tester #44 :

Tes avis répètent « taille petit », ta fiche produit n'en dit rien.

Hypothèse : personne ne lit 30 avis avant de choisir sa taille. L'info existe, mais pas là où le client décide.
Test : une ligne sous les tailles, tirée des avis : « Taille petit selon les avis, prends au-dessus. »
À mesurer : échanges et retours pour la taille.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-44.png`

**B · 13h · Idée à piquer #17 · Oner Active** (886 caractères, X Premium)
```
Idée à piquer #17 : les noms de couleur d'Oner Active.

La couleur choisie ne s'appelle pas « Brown ». Elle s'appelle « 70% Cocoa ».

Tu connais la teinte avant de zoomer. Chocolat noir, pas beige, pas noir. Et ça reste en tête : « la veste 70% Cocoa », c'est bien plus facile à raconter que « la marron ».

Il y a même de la recherche là-dessus : des noms de couleur inhabituels tendent à faire plus aimer le produit (Miller et Kahn, 2005).

Autres détails :
- les points affichés : 6 660 pour une veste à 66,60 €. Les gros chiffres font généreux.
- « In Stock » en vert, juste à côté du prix

Ce que je testerais : le nom de chaque pastille au tap, pas seulement celle choisie. Les gens parcourraient des noms, pas des points. Et garder le nom dans le panier et l'email de confirmation.

Je regarderais les taps sur les pastilles et les couleurs commandées.

Abonne-toi pour la suite.
```
Image : ta capture Oner Active.

**C · 18h · Appel** (201/280)
```
Agences et freelances CRO, ton avis m'intéresse aussi.

Comment tu choisis quoi tester en premier pour un client ? 20 min en visio ou 4 min de formulaire, lien en réponse. Les réponses restent privées.
```

### Vendredi 11 décembre

**A · 9h · Friction #45** (388 caractères, X Premium)
```
Friction Shopify à tester #45 :

Une liste d'envies qu'on ne peut pas partager, en décembre.

Hypothèse : en décembre, la liste d'envies devient la liste au Père Noël. Si on ne peut pas l'envoyer à sa famille, elle ne sert à rien.
Test : un bouton « Partager ma liste » : un lien, sans compte.
À mesurer : visites venues de listes partagées, et leurs commandes.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #18 · Cabaia** (889 caractères, X Premium)
```
Idée à piquer #18 : les tailles en litres de Cabaia.

Fiche d'un sac à dos : Medium, 18 L. Large, 23 L. Avec un lien pour comparer les tailles juste au-dessus.

Le litre, c'est la bonne unité pour un sac. « Medium » ne veut rien dire tant que tu ne sais pas ce qui rentre.

- chaque pastille est une photo du sac avec sa pochette assortie, pas un rond de couleur
- le prix est dans le bouton d'ajout, 53,40 €
- sous 100 €, ils commencent par le pourcentage (-40 %). La règle des 100 du #1, bien appliquée.

Ce que je testerais : transformer les litres en objets. Presque personne ne visualise 18 litres. « 18 L : un ordi 14 pouces, un pull, une gourde. 23 L : en plus, une paire de baskets. » Si c'est vraiment ce qui rentre.

Ou plus simple : la comparaison des tailles sous les boutons, pas derrière un lien.

Je regarderais les échanges entre Medium et Large.

Abonne-toi pour la suite.
```
Image : ta capture Cabaia.

**C · 18h · Question** (132/280)
```
Tu demandes à tes clients pourquoi ils ont failli ne pas acheter ?

Si oui : quelle réponse a changé quelque chose sur ta boutique ?
```

**D · 21h · Appel** (155/280)
```
Tu as bossé avec une agence ou un freelance CRO et tu as arrêté ? J'aimerais savoir ce qui n'a pas marché.

Les réponses restent anonymes. Lien en réponse.
```

### Samedi 12 décembre

**A · 9h · Friction #46** (374 caractères, X Premium)
```
Friction Shopify à tester #46 :

Des prix convertis automatiquement : 49,37 € au lieu de 49 €.

Hypothèse : un prix pas rond trahit la conversion. Le client comprend que la boutique n'est pas faite pour son pays, et imagine des frais de douane.
Test : des règles d'arrondi par marché (Shopify Markets le permet).
À mesurer : conversion par pays.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-46.png`

**B · 13h · Idée à piquer #19 · Boku** (900 caractères, X Premium)
```
Idée à piquer #19 : les trois pourcentages de Boku.

Une image produit, pas un bloc d'avis. « Testé sous contrôle dermatologique », puis :
- 95 % des utilisateurs trouvent qu'il améliore l'hygiène
- 97 % des utilisatrices trouvent qu'il améliore l'hygiène lors des menstruations
- 98 % le trouvent agréable à utiliser

Chaque chiffre répond à un doute différent. Est-ce que ça marche, est-ce que ça marche pour moi, est-ce bizarre à utiliser.

Celui du milieu nomme un usage que la plupart des marques laissent dans le flou. Les concernées s'y reconnaissent tout de suite.

Et le flacon repose sur une main ouverte : nomade, avant même de lire un mot.

Ce que je testerais : rendre les chiffres vérifiables. Sans base, 95 % peut vouloir dire 19 personnes sur 20. « 95 % de [n] utilisateurs après [x] semaines », avec les vrais chiffres, transforme une promesse en résultat.

Abonne-toi pour la suite.
```
Image : ta capture Boku.

**C · 18h · Journal** (184/280)
```
Ce que je fais des réponses au formulaire et des appels :

- tout lire, une par une
- classer les problèmes
- publier une synthèse en janvier

Aucun nom, aucun nom de boutique, jamais.
```

### Dimanche 13 décembre

**A · 9h · Friction #47** (420 caractères, X Premium)
```
Friction Shopify à tester #47 :

Des droits de douane payés à la livraison, le cas de beaucoup de marques UK depuis le Brexit.

Hypothèse : le client paie la douane et les frais du transporteur à sa porte, sans prévenir. Il ne recommande pas, et certains refusent le colis, que tu paies deux fois.
Test : droits inclus au paiement.
À mesurer : colis refusés, taux de recommande des clients UE.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-47.png`

**B · 13h · Idée à piquer #20 · Broken Planet** (897 caractères, X Premium)
```
Idée à piquer #20 : les deux mannequins de Broken Planet.

« Dawn is 6'2, wearing size XL sweatpants. Supriya is 5'3, wearing size M sweatpants. »

Même jogging, deux morphologies très différentes. Un mannequin te donne un repère. Deux te donnent une fourchette où te placer. Ça dit unisexe sans l'écrire.

- « 540 GSM organic cotton fabric » arrive en premier. Pour le streetwear épais, le grammage est la preuve de qualité.
- les tailles épuisées restent visibles, barrées. Tu vois ce qui existe et ce qui est parti.

Ces cases barrées sont la donnée la plus précieuse de la page, et personne ne la compte. Chaque tap dessus est une demande perdue.

Ce que je testerais : les rendre tapables. « XS épuisé. Préviens-moi au retour. » Puis utiliser le nombre d'inscrits par taille pour décider combien en refaire.

Je regarderais les ventes des emails de retour en stock.

Abonne-toi pour la suite.
```
Image : ta capture Broken Planet.

**C · 18h · Bilan de la semaine** : envoie-moi tes chiffres (réponses au formulaire, appels, abonnés), je l'écris.


## Semaine du 14 décembre

### Lundi 14 décembre

**A · 9h · Friction #48** (382 caractères, X Premium)
```
Friction Shopify à tester #48 :

Un téléphone obligatoire au paiement, sans dire pourquoi.

Hypothèse : le client imagine du démarchage. Or le vrai motif, le SMS du livreur, est justement celui qui lui donnerait envie de le donner.
Test : sous le champ : « Pour le SMS du livreur, rien d'autre. »
À mesurer : abandons à l'étape contact, livraisons ratées.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-48.png`

**B · 13h · Idée à piquer #21 · Gymshark** (884 caractères, X Premium)
```
Idée à piquer #21 : les « 224 XP » de Gymshark.

Sous le bouton d'achat : « L'achat de ce produit rapporte 224 XP ».

XP, pas « points ». C'est le langage du jeu vidéo, et les gens qui vont à la salle suivent déjà leur progression. Pour une marque de sport, monter de niveau, c'est toute l'identité.

- c'est propre à ce produit, pas un « rejoins notre programme » générique
- le même bloc répond aux dernières questions : livraison gratuite dès 59 €, express disponible
- le paiement en 4 fois affiché en 4 x 7,00 €. Plus petit chiffre, même total.

Problème : 224 XP de quoi ? Des points sans taux de change, c'est juste un nombre.

Ce que je testerais : lui donner un sens. « 224 XP, à une commande de ton prochain niveau », ou ce qu'ils valent sur la prochaine commande.

Je regarderais les créations de compte depuis les fiches produit, et les rachats.

Abonne-toi pour la suite.
```
Image : ta capture Gymshark.

**C · 18h · Question** (165/280)
```
Si un logiciel te signalait un problème sur ta boutique chaque semaine, où devrait-il regarder en premier ?

Fiches produit, panier, paiement, ou sources de trafic ?
```

**D · 21h · Appel** (193/280)
```
Tu gères la growth ou l'e-commerce d'une plus grosse marque ? Ta réponse compte aussi.

Tu as sûrement plus de données que de temps. Comment tu choisis quoi tester en premier ? Lien en réponse.
```

### Mardi 15 décembre

**A · 9h · Friction #49** (495 caractères, X Premium)
```
Friction Shopify à tester #49 :

Sur iPhone, ta fiche produit perd une bonne partie de l'écran : barre Safari, header fixe, bandeau promo, bannière cookies.

Hypothèse : tu ne le vois jamais : tu as accepté les cookies et tu testes sur ordi. Un nouveau visiteur, lui, voit tout en même temps.
Test : ouvre ta fiche en navigation privée sur un téléphone, puis teste un header qui se cache au scroll.
À mesurer : scroll et ajout au panier des nouveaux visiteurs mobiles.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #22 · Alphalete** (880 caractères, X Premium)
```
Idée à piquer #22 : le guide des tailles d'Alphalete.

La plupart des guides te donnent des chiffres. Celui-là t'apprend d'abord à trouver les tiens.

- des repères sur le corps, sans jargon : environ un pouce sous l'aisselle, au niveau du nombril
- un geste pour la taille : penche-toi sur le côté, trouve le pli. Faisable seul dans ta chambre.
- un bouton IN / CM
- des fourchettes, pas un chiffre unique : poitrine de 39 à 42 pouces pour un M. Les vrais corps sont entre deux tailles.

Un guide des tailles ne vaut que la mesure qu'on y apporte. Ils ont corrigé l'entrée, pas seulement le tableau.

Ce que je testerais : une option « pas de mètre ruban ? ». Pose à plat un sweat que tu as déjà, mesure d'aisselle à aisselle, compare.

Petite correction aussi : la fiche produit vend du XXL et du XXXL, le guide dit 2XL et 3XL. Les mêmes noms partout.

Abonne-toi pour la suite.
```
Image : ta capture Alphalete.

**C · 18h · Opinion** (191/280)
```
Un test « perdant » n'est du gâchis que si tu n'as jamais noté pourquoi tu l'as lancé.

L'hypothèse d'abord, le résultat ensuite. C'est comme ça qu'une boutique devient vraiment plus maligne.
```

### Mercredi 16 décembre

**A · 9h · Friction #50** (351 caractères, X Premium)
```
Friction Shopify à tester #50 :

Sur mobile, la photo portée arrive en 4e position dans la galerie.

Hypothèse : beaucoup ne swipent pas jusque-là. Ils jugent un vêtement posé à plat, sans jamais voir comment il tombe.
Test : la photo portée en 1re ou 2e position.
À mesurer : swipes dans la galerie, ajout au panier mobile.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #23 · Kosbiotic** (895 caractères, X Premium)
```
Idée à piquer #23 : l'abonnement de Kosbiotic.

L'abonnement est sélectionné par défaut. Ce qui le rend acceptable, c'est ce qui est écrit dedans :
- « Économisez 10% », « Sans engagement »
- « Livraison automatique tous les 28 jours »
- « Annulation en 1 clic »

Un abonnement présélectionné sans ces lignes ressemblerait à un piège. Avec elles, il ressemble au choix évident.

28 jours, c'est la durée d'une cure, donc la boîte suivante arrive quand la précédente se termine. Et tous les 28 jours, ça fait 13 livraisons par an, pas 12. La cure et le chiffre d'affaires s'alignent.

Ce que je testerais : prouver l'annulation en 1 clic, avec un petit lien qui montre l'écran où on le fait. Ou ajouter « Décale ou mets en pause quand tu veux » pour ceux qui ont peur de crouler sous les boîtes.

Je regarderais la part d'abonnements et les annulations du premier mois.

Abonne-toi pour la suite.
```
Image : ta capture Kosbiotic.

**C · 18h · Appel** (172/280)
```
Mi-décembre.

Si tu as une boutique Shopify et 20 minutes entre deux commandes : comment tu décides quoi changer ? Lien en réponse.

Merci à tous ceux qui ont déjà répondu.
```

### Jeudi 17 décembre

**A · 9h · Friction #51** (409 caractères, X Premium)
```
Friction Shopify à tester #51 :

Sur mobile, tes noms de produits sont coupés pile avant ce qui les distingue.

Hypothèse : six cartes « Sweat oversize bro... » : il faut tout ouvrir pour savoir lequel est lequel. Le client en ouvre deux et s'arrête.
Test : mettre la différence au début : « Vert sapin, sweat oversize ».
À mesurer : clics vers les fiches, produits vus par session.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #24 · Cabaia** (884 caractères, X Premium)
```
Idée à piquer #24 : le panier de Cabaia, prêt pour décembre.

Un sac à dos dans le panier, et les trois dernières questions réglées.

Quand ça arrive ? Une vraie date, calculée avec ton code postal, et un lien pour comparer les options. Pas « 3 à 5 jours ouvrés ».

C'est un cadeau ? Une case directement sur la ligne : emballage cadeau, 2,80 €.

Qu'est-ce qui va avec ? Une poche latérale Pau, à 7 €. Le sac s'appelle Pau aussi. Des noms de villes : l'association se fait sans étiquette « va avec ».

En décembre, la date de livraison, c'est quasiment la décision. L'avoir dans le panier enlève le dernier « est-ce que ça arrivera à temps ? ».

Ce que je testerais : une fois l'emballage coché, proposer un message et une facture sans prix. L'emballage, c'est la moitié du cadeau. L'autre moitié, c'est que le prix ne soit pas dans la boîte (friction #41).

Abonne-toi pour la suite.
```
Image : ta capture Cabaia.

**C · 18h · Question** (80/280)
```
Quelle page de ta boutique tu regardes le moins, alors que tu devrais sûrement ?
```

### Vendredi 18 décembre

**A · 9h · Friction #52** (397 caractères, X Premium)
```
Friction Shopify à tester #52 :

Chaque couleur créée comme un produit à part.

Hypothèse : tes avis sont éparpillés : six fiches à 12 avis au lieu d'une à 72. Même produit, moins de preuves sur chaque page.
Test : regrouper les avis des couleurs (beaucoup d'apps d'avis le permettent), ou passer en variantes.
À mesurer : ajout au panier des couleurs les moins vendues.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #25 · Alo** (889 caractères, X Premium)
```
Idée à piquer #25 : la photo annotée d'Alo.

Deuxième photo, des petites étiquettes qui pointent le t-shirt : « Soft Performance Fabric », « Fitted Sleeves », « Relaxed Fit ».

On regarde les photos avant de lire. Donc le texte va là où l'attention est déjà, sur le corps, au lieu d'un accordéon que personne n'ouvre. La recherche appelle ça la contiguïté spatiale : un mot placé à côté de ce qu'il décrit se comprend plus vite.

- l'info de coupe (taille normalement, coupe ample) juste au-dessus du guide des tailles
- un prix membre, 47 € au lieu de 68 € si tu crées un compte. La remise devient un compte.

Ce que je testerais : rendre les étiquettes tapables. « Soft Performance Fabric » ouvre un gros plan du tissu. Ou une 4e étiquette sur ce que leurs 1 943 avis demandent le plus.

Je regarderais le taux d'ajout au panier et les ouvertures d'accordéons.

Abonne-toi pour la suite.
```
Image : ta capture Alo.

**C · 18h · Opinion** (134/280)
```
La plupart des captures « on a doublé la conversion » comparent décembre à novembre.

C'est juste la saison. Demande le groupe témoin.
```

**D · 21h · Appel** (201/280)
```
Chaque réponse est lue, classée et comptée. Rien n'est utilisé pour te vendre quoi que ce soit.

Si tu as une boutique et 20 minutes avant les fêtes : comment tu décides quoi changer ? Lien en réponse.
```

### Samedi 19 décembre

**A · 9h · Friction #53** (426 caractères, X Premium)
```
Friction Shopify à tester #53 :

Tu ouvres le 40e produit d'une collection, tu reviens en arrière : retour tout en haut.

Hypothèse : personne ne refait 40 produits de scroll. Le client s'arrête au premier ouvert, et ta collection est jugée sur une seule fiche.
Test : garder la position au retour, ou un bouton « Voir plus » à la place du scroll infini.
À mesurer : produits vus par session mobile.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #26 · Horace** (877 caractères, X Premium)
```
Idée à piquer #26 : les deux questions d'Horace.

La description, c'est juste deux questions en gras : « Que fait-il ? » et « Comment l'utiliser ? »

Pour un premier achat, « comment l'utiliser ? » est une vraie question. Réponse : le matin et/ou le soir, à faire mousser sur visage et cou humides. Fini.

- ce sont les questions qu'on poserait à un pote au comptoir, pas des titres marketing
- « Parfum : Sans parfum » a sa propre ligne. Pour beaucoup d'hommes, c'est le critère éliminatoire.
- le prix est dans le bouton : « AJOUTER AU PANIER - 13 € »

Ils vendent la routine, pas juste le flacon. Savoir comment l'utiliser enlève la peur d'acheter un truc qui finira au fond du placard.

Ce que je testerais : une troisième question, « Avec quoi ? », qui montre l'étape suivante de la routine et la distance jusqu'à la livraison offerte, dès 40 €.

Abonne-toi pour la suite.
```
Image : ta capture Horace.

**C · 18h · Question** (83/280)
```
Qu'est-ce que tu aimerais que tes analytics te disent, et qu'ils ne te disent pas ?
```

### Dimanche 20 décembre

**A · 9h · Friction #54** (440 caractères, X Premium)
```
Friction Shopify à tester #54 :

Le 22 décembre, la carte cadeau est le seul produit qui arrive encore à temps. Et elle est dans le footer.

Hypothèse : les retardataires ne la cherchent pas, ils partent ailleurs.
Test : dès la date limite de livraison passée, un bandeau : « Trop tard pour la livraison ? Carte cadeau envoyée par email, tout de suite. »
À mesurer : ventes de cartes cadeaux après la date limite.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-54.png`

**B · 13h · Idée à piquer #27 · Le Slip Français** (897 caractères, X Premium)
```
Idée à piquer #27 : le « Fréquemment achetés ensemble » du Slip Français.

Sous un lot de 5 boxers à 99 €, les suggestions ne sont ni des chaussettes ni des ceintures. Ce sont des lots plus gros : 7 boxers à 160 €, 10 à 185 €.

De la montée en gamme déguisée en vente croisée.

- la photo du lot de 7 est un cadeau : fond rouge, sachet doré « Un petit cadeau, un joli paquet »
- les motifs ont des noms de fête (Guirlande, Tout Schuss). En décembre, les noms de produits font le marketing de saison.

Maintenant, le calcul. Le lot de 10 revient à 18,50 € le boxer, moins cher que le lot de 5 (19,80 €). Le lot de 7 : 22,86 €, plus cher. Il vend l'emballage, pas le prix unitaire.

Ce que je testerais : le prix par boxer seulement là où il aide, « 18,50 € pièce » sur le lot de 10. Et vendre le lot cadeau sur le moment : « emballé, livré avant Noël », si c'est tenable.

Abonne-toi pour la suite.
```
Image : ta capture Le Slip Français.

**C · 18h · Bilan de la semaine** : envoie-moi tes chiffres (réponses au formulaire, appels, abonnés), je l'écris.


## Semaine du 21 décembre

### Lundi 21 décembre

**A · 9h · Friction #55** (413 caractères, X Premium)
```
Friction Shopify à tester #55 :

Un cadeau livré le 5 décembre, ouvert le 25 : ton délai de retour de 14 jours est déjà fini.

Hypothèse : celui qui offre y pense, surtout pour une taille. Il hésite, ou choisit une boutique qui en parle.
Test : « Retours des commandes de décembre jusqu'au 31 janvier », écrit sur la fiche, si ta politique le permet.
À mesurer : conversion en décembre.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #28 · Based** (876 caractères, X Premium)
```
Idée à piquer #28 : les tuiles ingrédients de Based.

Une image produit : « The Key Ingredients. Endless Benefits. » Quatre tuiles, chacune avec un ingrédient, une bande de la vraie texture de la poudre, et une ligne sur ce qu'il fait.

- tu vois la silice, l'arrow-root, la poudre de riz et le mica. Tu ne fais pas que lire leurs noms.
- chaque nom chimique devient un résultat : volume, moins de gras, douceur, fini mat
- 4 ingrédients, 4 rôles. Rien n'est là sans raison.

Cette image répond en silence à la question que pose un produit à 21,95 € qui pèse 2,5 g : je paie quoi ? Quatre actifs nommés font paraître un petit format dense plutôt que minuscule.

Ce que je testerais : partir du problème, pas de l'ingrédient. « Cheveux plats ? Silica silylate. Racines grasses à midi ? Arrow-root. » Les gens connaissent leur problème, pas la chimie.

Abonne-toi pour la suite.
```
Image : ta capture Based.

**C · 18h · Journal** (255/280)
```
Ce que j'ai remarqué sur les 27 premières frictions Shopify :

les plus lues parlaient toutes de surprises sur le chemin du paiement. Moyens de paiement cachés, frais de port qui arrivent tard, pop-ups trop tôt.

Personne n'aime les surprises à la caisse.
```

**D · 21h · Appel** (189/280)
```
Réponds « appel » et je t'envoie le lien.

20 minutes avant la pause des fêtes, sur comment tu décides quoi changer sur ta boutique. La synthèse part en janvier à tous ceux qui ont répondu.
```

### Mardi 22 décembre

**A · 9h · Friction #56** (375 caractères, X Premium)
```
Friction Shopify à tester #56 :

Une taille sélectionnée qui se voit à peine : juste un contour un peu plus épais.

Hypothèse : dehors, au soleil, le client ne sait plus s'il a pris M ou L. Il retape, doute, et va vérifier dans le panier.
Test : la taille choisie en plein (fond noir, texte blanc).
À mesurer : changements de taille dans le panier.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #29 · Polène** (882 caractères, X Premium)
```
Idée à piquer #29 : l'écran coupé en deux de Polène.

Moitié gauche : le sac porté, dans un immense paysage. Moitié droite : le même sac seul sur fond blanc, nom, prix, un bouton.

L'émotion et les faits côte à côte. Tu ne scrolles jamais de l'un à l'autre. Et tu lis le côté gauche en premier, donc l'envie passe avant les détails.

- énormément de blanc autour du packshot. À 380 €, l'espace signale la valeur.
- la « Vue 3D » te laisse tourner le sac toi-même au lieu de faire défiler six angles

Moitié magazine, moitié vitrine. La page ne te force jamais à choisir entre en avoir envie et vérifier.

Ce que je testerais : la question que pose chaque petit sac. Qu'est-ce qui rentre dedans ? Une photo ouvert avec un téléphone, des cartes et des clés. Ou une ligne sous le prix.

Je regarderais le taux d'ajout au panier et les retours « trop petit ».

Abonne-toi pour la suite.
```
Image : ta capture Polène.

**C · 18h · Appel** (202/280)
```
Avant de fermer pour les fêtes : 20 min en visio, ou 4 min de formulaire, sur comment tu décides quoi changer sur ta boutique.

Tous ceux qui répondent reçoivent la synthèse en janvier. Lien en réponse.
```

### Mercredi 23 décembre

**A · 9h · Friction #57** (418 caractères, X Premium)
```
Friction Shopify à tester #57 :

Des couleurs nommées « Coloris 2 » ou « Dark ».

Hypothèse : le nom suit le produit partout : panier, email, formulaire de retour, souvent sans photo. Là, « Coloris 2 » ne veut plus rien dire, et le client doute de sa commande.
Test : un nom qu'on voit dans sa tête : « Vert sapin ».
À mesurer : questions au SAV sur la couleur, retours « mauvaise couleur ».

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #30 · Typology** (898 caractères, X Premium)
```
Idée à piquer #30 : les codes labo de Typology.

Le sérum s'appelle « A63 ». Au-dessus du nom, une référence comme sur un échantillon de labo : « LAB1035-30ML-SG ». La description est en police machine à écrire.

- le nom, c'est l'actif et sa concentration (« Complexe PDRN-EGF 3% »), pas un mot d'ambiance comme « Glow »
- les chiffres précis font honnête : « 150 000 micro-spicules véganes par gramme », « 95% d'ingrédients d'origine naturelle »
- un 15 ml à côté du 30 ml, pour essayer moins cher
- « Ce produit est-il compatible avec votre type de peau? » juste sous le bouton

La promesse, c'est la science, donc la page ressemble à une fiche de labo.

Ce que je testerais : appeler le 15 ml par ce qu'il est, « Format découverte », et afficher son prix sur le bouton avant le clic.

Je regarderais la conversion des premières commandes et le passage du 15 au 30 ml.

Abonne-toi pour la suite.
```
Image : ta capture Typology.

**C · 18h · Opinion** (185/280)
```
Mon plan de janvier pour n'importe quelle boutique :

- choisir 3 changements, pas 30
- un indicateur pour chacun
- écrire l'hypothèse avant de mettre en ligne
- vérifier avant de fêter
```

**D · 21h · Appel** (188/280)
```
Boutiques de mode et de beauté : les questions de taille, de teinte et de coupe ont l'air de créer beaucoup d'hésitation. C'est vrai chez toi ?

Raconte-moi en 20 minutes. Lien en réponse.
```

### Jeudi 24 décembre · Réveillon

**A · 9h · Friction #58** (374 caractères, X Premium)
```
Friction Shopify à tester #58 :

Le lot de 3 paires affiché à 29 €, sans dire que ça fait 9,67 € la paire contre 12 €.

Hypothèse : le client compare 29 € à 12 €, pas 9,67 € à 12 €. Le gros chiffre fait peur, l'économie reste invisible.
Test : « 9,67 € la paire au lieu de 12 € » sous le lot.
À mesurer : part des lots dans les commandes.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-58.png`

**B · 13h · Idée à piquer #31 · Stüssy** (838 caractères, X Premium)
```
Idée à piquer #31 : la fiche produit de Stüssy, pour ce qu'elle n'a pas.

Un cendrier en verre à 70 €. Pas d'avis, pas de « plus que 3 », pas de compte à rebours, pas de carrousel de suggestions.

- les détails du produit sont ouverts par défaut, en simple liste
- chaque dimension en pouces et en cm. Pour un objet, la taille est la première inconnue.
- un guide des livraisons des fêtes en haut, avec un lien « Hide »
- une liste, une photo, un bouton noir. La page ressemble à la marque.

Pour une marque culte, les techniques de persuasion feraient cheap. La retenue est le signal.

Ce que je testerais : l'échelle. Sur fond blanc, 20 cm ne se voit pas. Une photo à côté d'une main ou d'un briquet. Ou une vue de profil qui montre les 2,5 cm de hauteur.

Je regarderais les retours « plus petit que prévu ».

Abonne-toi pour la suite.
```
Image : ta capture Stüssy.

**C · 18h · Question** (106/280)
```
Quand ça se calme après ce soir, quelle est la première chose que tu corriges sur ta boutique en janvier ?
```

### Vendredi 25 décembre · Noël

**A · 9h · Friction #59** (417 caractères, X Premium)
```
Friction Shopify à tester #59 :

L'abonnement coché par défaut sur la fiche produit.

Hypothèse : il fait monter la part d'abonnements, mais une partie annule dès le 1er prélèvement, ou conteste le paiement. Le chiffre qui monte n'est pas le bon.
Test : l'achat unique par défaut, l'économie de l'abonnement juste à côté.
À mesurer : abonnés encore là au 3e mois, pas la part d'abonnements.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-59.png`

**B · 13h · Idée à piquer #32 · Charles Tyrwhitt** (893 caractères, X Premium)
```
Idée à piquer #32 : la chemise à composer de Charles Tyrwhitt.

Chemise à 29,95 € (au lieu de 84,95 €), et un bandeau rouge : « ÉCONOMISEZ 55 € AUJOURD'HUI - SANS CODE PROMOTION ».

« Sans code promotion » évite le détour par Google pour en chercher un. La fuite de la friction #27, fermée en trois mots.

- la coupe se choisit sur des dessins de la chemise, pas avec des mots comme « slim » qui veulent dire autre chose pour chacun
- les tailles de col en cm, regroupées sous S, M, L, XL. Les experts lisent les cm, les autres lisent la lettre.
- « Vos Sélections » récapitule chaque choix avec une coche

Un détail cloche : le badge « LES PLUS POPULAIRES » est sur Ajustée, qui est barrée. Indisponible. Le badge pousse vers ce qu'on ne peut pas acheter.

Ce que je testerais : quand une option est épuisée, déplacer le badge, ou le remplacer par « Préviens-moi ».

Abonne-toi pour la suite.
```
Image : ta capture Charles Tyrwhitt.

**C · 18h · Question** (108/280)
```
Pas de conseil aujourd'hui. Une question : quelle a été ta meilleure décision pour ta boutique cette année ?
```

### Samedi 26 décembre · Boxing Day

**A · 9h · Friction #60** (371 caractères, X Premium)
```
Friction Shopify à tester #60 :

« Paiement 100 % sécurisé » avec un cadenas, collé au bouton « Ajouter au panier ».

Hypothèse : à cette étape, personne ne paie encore. Parler de sécurité trop tôt peut faire penser au risque plutôt qu'au produit.
Test : le garder au paiement, l'enlever de la fiche produit.
À mesurer : taux d'ajout au panier.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #33 · Le Slip Français** (863 caractères, X Premium)
```
Idée à piquer #33 : l'échelle de remises du Slip Français.

Trois petites pastilles sous le prix : « -5% supp. dès 3 », « -10% supp. dès 4 », « -20% supp. dès 5 ».

- tu vois la récompense d'acheter plus avant de choisir la quantité, pas au paiement
- trois marches au lieu d'un seul seuil. Chacune est un petit oui.
- « supp. » veut dire que ça se cumule sur un prix déjà réduit (99 € au lieu de 125 €)
- un point vert sur chaque taille, donc le stock est réglé sans un clic

L'échelle transforme « combien ? » en « à quelle marche je m'arrête ? ». On s'ancre sur la marche suivante, pas sur 1.

Ce que je testerais : la prolonger dans le panier. « Ajoute 1 article pour débloquer -10 %. » Ou mettre en avant la marche que le panier a atteinte.

Je regarderais les articles par commande, et combien de commandes s'arrêtent à 3, 4 et 5.

Abonne-toi pour la suite.
```
Image : ta capture Le Slip Français.

**C · 18h · Question** (122/280)
```
Une boutique où tu achètes en partie parce que le site est agréable à utiliser ?

Je cherche les prochaines à décortiquer.
```

### Dimanche 27 décembre

**A · 9h · Friction #61** (444 caractères, X Premium)
```
Friction Shopify à tester #61 :

Tu passes des heures sur la bannière de ta page d'accueil.

Hypothèse : les visiteurs venus des pubs et de Google Shopping arrivent souvent direct sur une fiche produit. Ta vraie page d'accueil, c'est peut-être ta fiche la plus visitée.
Test : regarder les pages d'entrée dans Shopify Analytics avant de toucher à l'accueil.
À mesurer : part des sessions qui commencent sur l'accueil.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #34 · Arntreal** (875 caractères, X Premium)
```
Idée à piquer #34 : la preuve avant la promesse, chez Arntreal.

Au-dessus du nom du produit, avant tout le reste : cinq étoiles, « Plus de 100 000 sacs vendus » avec un drapeau français, et cinq mini photos de clients.

La plupart des pages font produit, promesse, puis les avis tout en bas. Arntreal inverse : preuve, promesse, produit.

- la phrase forte qui suit (« Tout d'un sac de luxe. Sauf le prix. ») tombe sur une foule qui a déjà acheté
- les visages transforment 100 000 en personnes. Un chiffre, c'est abstrait. Cinq visages, c'est quelqu'un comme toi.

Mais les étoiles n'ont ni note ni nombre d'avis. 100 000 sacs vendus, c'est un chiffre de ventes, pas d'avis : seules, cinq étoiles font déco.

Ce que je testerais : la vraie moyenne et le nombre d'avis, avec les étoiles qui y mènent. Ou chaque visage tapable, vers son avis photo.

Abonne-toi pour la suite.
```
Image : ta capture Arntreal.

**C · 18h · Bilan de la semaine** : envoie-moi tes chiffres (réponses au formulaire, appels, abonnés), je l'écris.


## Semaine du 28 décembre

### Lundi 28 décembre

**A · 9h · Friction #62** (415 caractères, X Premium)
```
Friction Shopify à tester #62 :

Des accordéons fermés nommés « Description », « Détails », « Infos ».

Hypothèse : personne n'ouvre « Détails » en espérant y trouver sa réponse. Les titres ne disent pas ce qu'il y a dedans.
Test : les titrer avec les vraies questions du SAV : « Ça taille comment ? », « Livré quand ? ».
À mesurer : ouvertures d'accordéons, questions au SAV avant achat.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #35 · Apple** (883 caractères, X Premium)
```
Idée à piquer #35 : le configurateur étape par étape d'Apple.

Chaque étape s'ouvre sur une phrase en deux couleurs : « Modèle. » en noir, « Choisissez la taille. » en gris. Puis deux grandes cartes, 13 pouces et 15 pouces.

- une décision par étape. Le noir nomme l'étape, le gris dit quoi faire.
- des points sur le côté montrent combien d'étapes il reste
- la taille d'abord, la question à laquelle tout le monde sait répondre
- chaque carte affiche le total et la mensualité

Maintenant, regarde l'écart. En total, le 15 pouces coûte 300 € de plus. Par mois, 8,96 € de plus. Même différence, et l'une des deux sonne comme un café par semaine.

Ce que je testerais : une fois le 13 pouces choisi, afficher la montée en gamme comme une différence, « +8,96 €/mois », sur la carte 15 pouces.

Je regarderais la part de 15 pouces et le prix moyen configuré.

Abonne-toi pour la suite.
```
Image : ta capture Apple.

**C · 18h · Question** (84/280)
```
Qu'est-ce qu'il y a sur la liste de janvier de ta boutique ? Une seule chose suffit.
```

**D · 21h · Appel** (190/280)
```
Semaine calme entre les fêtes. Un bon moment pour 20 minutes sur comment tu vas décider quoi changer sur ta boutique en janvier.

Lien en réponse. Synthèse envoyée à tous ceux qui répondent.
```

### Mardi 29 décembre

**A · 9h · Friction #63** (417 caractères, X Premium)
```
Friction Shopify à tester #63 :

Un suivi de colis qui ne bouge pas pendant 2 jours après « Expédié ».

Hypothèse : le colis est étiqueté mais pas encore scanné. Le client voit « Expédié » sans aucun mouvement, et écrit au SAV.
Test : dans l'email d'expédition : « Le suivi peut mettre 24 à 48 h à s'activer. »
À mesurer : tickets « Où est ma commande ? » dans les 3 jours après expédition.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #36 · Decathlon** (898 caractères, X Premium)
```
Idée à piquer #36 : le bloc prix de Decathlon.

Table de ping-pong d'extérieur à 459,99 €. Sous le prix : « 85 € de réduction » en rouge, puis « Promotion du 03/11/2026 au 26/01/2027 ».

- l'économie en euros, pas en pourcentage. Sur un produit à 544,99 €, 85 € sonne plus fort que 16 %. La règle des 100, bien appliquée.
- la promo a de vraies dates. De l'urgence sans faux compte à rebours, et tu y crois parce que c'est précis.
- la description vend l'usage : entre amis, en famille, dehors, grandes roues, rangement des raquettes

Une promo datée, c'est la version honnête d'un timer.

Deux petits conflits quand même. Le badge du haut dit « Livraison offerte », le bloc prix dit « Des frais de livraison peuvent être ajoutés ». Un seul message, en haut, avec sa condition. Et « Taille : Sans taille » peut disparaître. Une ligne vide coûte quand même de l'attention.

Abonne-toi pour la suite.
```
Image : ta capture Decathlon.

**C · 18h · Opinion** (196/280)
```
Les boutiques que je décortique dans « Idée à piquer » ont toutes un point commun.

Rien sur la fiche produit n'est là par hasard. Chaque bloc répond à une question que quelqu'un se pose vraiment.
```

### Mercredi 30 décembre

**A · 9h · Friction #64** (400 caractères, X Premium)
```
Friction Shopify à tester #64 :

Panier rempli sur mobile le midi, retour sur ordi le soir : panier vide.

Hypothèse : sans compte, le panier ne suit pas d'un appareil à l'autre. Le client croit à un bug, ou n'a pas le courage de tout retrouver.
Test : dans le panier mobile, « Envoie-toi ton panier par email ».
À mesurer : paniers récupérés par email, et leurs commandes.

Abonne-toi pour la suite.
```
Sans visuel.

**B · 13h · Idée à piquer #37 · Garmin** (895 caractères, X Premium)
```
Idée à piquer #37 : le choix de version de Garmin.

Sur la fiche de la fēnix E, les autres versions sont des boutons juste sous la taille du boîtier : fēnix 8 AMOLED, Solar, Pro AMOLED, Pro MicroLED.

- toute la gamme est à un tap, sans quitter la page
- la taille du boîtier est une rangée de boutons en mm, avec une icône info si tu ne connais pas ton poignet
- la remise affichée en euros (150 €), et Klarna la coupe en 3 paiements de 149,99 €, juste sous 150 €

Mais « Solar », « AMOLED », « MicroLED » sont des caractéristiques, pas des raisons. Personne ne monte en gamme pour un mot qu'il ne comprend pas.

Ce que je testerais : sous chaque version, l'écart de prix et un bénéfice en mots simples (« se recharge au soleil »). Ou une icône info sur chaque version, comme sur la taille du boîtier.

Je regarderais la part des commandes au-dessus de cette version.

Abonne-toi pour la suite.
```
Image : ta capture Garmin.

**C · 18h · Journal** (180/280)
```
Le 1er janvier, je poste les vrais chiffres : réponses au formulaire, appels, clients, abonnés.

Quels qu'ils soient. Même règle que le premier jour : les zéros aussi sont publics.
```

**D · 21h · Appel** (179/280)
```
Dernier appel de 2026 : je commence à écrire la synthèse des réponses en janvier.

Si tu as une boutique Shopify : 20 minutes sur comment tu décides quoi changer. Lien en réponse.
```

### Jeudi 31 décembre · Dernier jour de l'année

**A · 9h · Friction #65** (387 caractères, X Premium)
```
Friction Shopify à tester #65 :

Le filtre « Taille M » de ta page soldes montre aussi les produits où le M est épuisé.

Hypothèse : le client clique, tombe trois fois sur « Épuisé », et conclut qu'il n'y a plus rien pour lui.
Test : un filtre qui ne garde que le stock dispo dans la taille choisie.
À mesurer : conversion de la page soldes filtrée par taille.

Abonne-toi pour la suite.
```
Visuel : `design/social/x-friction/friction-65.png`

**B · 13h · Idée à piquer #38 · Based** (899 caractères, X Premium)
```
Idée à piquer #38 : l'annonce de packaging de Based.

Sur la fiche produit, deux tubes côte à côte : « New Packaging, Same Texture Powder. » Puis une ligne : tu peux recevoir l'ancien ou le nouveau packaging, le produit dedans est le même.

Pendant un changement de marque, le risque n'est pas le design. C'est quelqu'un qui ouvre un colis qui ne ressemble pas à la photo, et qui croit à une contrefaçon.

- ils montrent les deux versions, donc ce qui arrive était prévu
- ça répond à un ticket SAV avant que quelqu'un l'écrive
- un problème de logistique devient une petite actu de marque

La satisfaction, c'est en gros l'écart entre ce que tu attendais et ce que tu reçois. Ils ont déplacé l'attente au lieu d'espérer écouler l'ancien stock d'abord.

Ce que je testerais : la même image dans l'email d'expédition. Le doute arrive au déballage, pas sur la fiche produit.

Abonne-toi pour la suite.
```
Image : ta capture Based.

**C · 18h · Appel** (197/280)
```
Dernier post de l'année. Merci de m'avoir lu.

Si tu as une boutique, le plus utile que tu puisses donner à Solen, c'est 20 minutes : comment tu décides quoi changer. Lien en réponse.

Bonne année.
```


## En réserve pour janvier

Ces frictions ne tiennent plus avant le 31 décembre.

**Friction #66** (397 caractères)
```
Friction Shopify à tester #66 :

Dans le panier latéral mobile, les suggestions repoussent le bouton « Paiement » sous l'écran.

Hypothèse : le client prêt à payer doit scroller pour trouver le bouton. Certains pensent qu'il n'y en a pas.
Test : le bouton de paiement fixé en bas du panier, les suggestions réduites.
À mesurer : passage du panier au paiement sur mobile.

Abonne-toi pour la suite.
```

**Friction #67** (373 caractères)
```
Friction Shopify à tester #67 :

Une collection triée « manuellement » depuis le lancement.

Hypothèse : l'ordre ne bouge plus, mais tes ventes, si. Tes meilleurs produits d'aujourd'hui sont peut-être en bas de page.
Test : comparer l'ordre actuel au tri « Meilleures ventes » des 30 derniers jours.
À mesurer : clics sur les 8 premiers produits.

Abonne-toi pour la suite.
```

**Friction #68** (407 caractères)
```
Friction Shopify à tester #68 :

Un sweat dans le panier, et les suggestions proposent d'autres sweats.

Hypothèse : un produit similaire ne s'ajoute pas, il remplace. Il rouvre la décision au moment de payer.
Test : des produits complémentaires plutôt que similaires (l'app Search & Discovery de Shopify le permet).
À mesurer : ajouts depuis les suggestions, passage au paiement.

Abonne-toi pour la suite.
```

**Friction #69** (430 caractères)
```
Friction Shopify à tester #69 :

Des produits supprimés qui renvoient une 404, alors que Google et des influenceurs pointent encore dessus.

Hypothèse : ces visiteurs arrivent avec une intention d'achat et tombent sur une impasse.
Test : une redirection vers le produit le plus proche ou sa collection (redirections d'URL de Shopify).
À mesurer : visites sur la 404, conversions depuis les redirections.

Abonne-toi pour la suite.
```

**Friction #70** (432 caractères)
```
Friction Shopify à tester #70 :

Le Black Friday est fini, mais le prix barré est resté sur une partie du catalogue.

Hypothèse : un prix barré permanent ne fait plus effet. Et dans l'UE, le prix de référence d'une réduction doit être le plus bas des 30 derniers jours.
Test : une date de fin sur chaque prix barré, vérifiée le lendemain de chaque promo.
À mesurer : produits encore barrés après la promo.

Abonne-toi pour la suite.
```

