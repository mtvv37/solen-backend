"""Posts « Idée à piquer » (ex-« Worth stealing ») écrits à partir des captures de Thomas (format long, X Premium).

Une capture = un post, dans l'ordre de publication à 13h, à partir du 24 novembre.
`shot` = nom du fichier de la capture, publié à côté de la page (les captures restent hors du repo) ;
`new:...` = capture reçue sans fichier : le texte est prêt, Thomas a l'image. Sur ces captures-là, on paraphrase
au lieu de citer entre guillemets, faute de pouvoir relire le texte exact du site.
Règles : français, tutoiement, 900 caractères maximum, puces en tiret simple « - », ton humain, pas de tiret long ni d'emoji,
on ne décrit que ce qui est visible, citations recopiées telles quelles depuis les captures (y compris quand le site
est en anglais), aucun résultat de marque inventé. Finit par « Abonne-toi pour la suite. »
Les versions anglaises sont dans l'historique git (avant le 26/11/2026).
"""

WS = [
 dict(brand="Gymshark", shot="9.webp", text="""Idée à piquer #1 : le badge promo de Gymshark.

Une petite étiquette au-dessus du nom du produit : « -30% | 12 € D'ÉCONOMIE ».

Ce que j'aime :
- tu lis l'affaire avant le produit
- la même remise, dite deux fois : en pourcentage et en euros
- l'ancien prix (40 €) juste à côté du nouveau (28 €), zéro calcul

Et l'ordre n'est pas un hasard. Sur un article à 40 €, « -30 % » sonne plus fort que « 12 € ». C'est la règle des 100 : sous 100 €, commence par le pourcentage. Au-dessus, commence par les euros.

Ce que je testerais : l'inverser sur tout ce qui dépasse 100 €. « 45 € D'ÉCONOMIE | -30% » au lieu de « -30% | 45 € D'ÉCONOMIE ».

Je regarderais l'ajout au panier des articles remisés, par tranche de prix.

Abonne-toi pour la suite."""),

 dict(brand="Arntreal", shot="39.png", text="""Idée à piquer #2 : le tirage au sort Black Friday d'Arntreal.

Sur la fiche produit : « Chaque commande = 1 participation pour gagner une montre de luxe ». Une Rolex, une Omega Speedmaster ou une Cartier Santos. Le règlement juste en dessous.

Pourquoi c'est malin :
- la marque vend « tout d'un sac de luxe, sauf le prix ». Le lot, c'est le vrai logo de luxe. Même histoire.
- une remise mange de la marge sur chaque commande. Trois montres, c'est un coût fixe.
- le prix de 149,90 € ne bouge pas, donc il reste crédible en janvier

Ce que je testerais : « chaque commande » récompense le fait de couper son panier. Deux commandes d'un sac = 2 participations, une commande de deux sacs = 1. Fincut fait un tirage proche, mais donne un ticket par article. J'essaierais 1 participation par sac.

Je regarderais les articles par commande pendant le tirage.

Abonne-toi pour la suite."""),

 dict(brand="Based", shot="30.png", text="""Idée à piquer #3 : le bouton Black Friday de Based.

Le bouton principal ne dit pas « Ajouter au panier ». Il dit « BUY ONE GET ONE €21,95 », en doré.

- l'offre est là où tout le monde regarde juste avant de décider
- même prix qu'un seul, donc « un offert » ne demande aucun calcul
- la bannière en dessous le répète, et une garantie de 60 jours ferme la page

Ils n'ont pas ajouté un bloc promo à côté du produit. Ils ont changé l'action elle-même.

Ce que je testerais, pour les clients européens :
- les prix sont en euros, mais les seuils de livraison offerte en dollars (50 $+, 100 $+). Une seule devise, s'il te plaît.
- « 2.5 g » à côté de 21,95 € paraît minuscule. « Dure environ X semaines » répondrait à ça, s'ils ont le chiffre.

Je regarderais la conversion du trafic européen et les avis qui disent « petit ».

Abonne-toi pour la suite."""),

 dict(brand="Arntreal", shot="41.png", text="""Idée à piquer #4 : la case vide d'Arntreal.

Offre Black Friday : « 1 acheté = 1 offert », couleur au choix. À côté du sac choisi, un sac grisé avec un « + » : « CHOISIS TON SAC OFFERT ».

Based met son offre dans le bouton (#3). Arntreal la dessine.

Cette case vide, c'est une tâche à moitié faite. Tu en as choisi un, une place t'attend. On pousse plus fort vers un objectif qu'on croit déjà entamé. Nunes et Drèze ont un nom pour ça : l'endowed progress effect.

Un détail me gêne : l'offre affiche 149.90 € barré à côté de 149.90 €. Aucune économie visible.

Ce que je testerais : 299,80 € barré, ou « 2 sacs pour 149,90 €, soit 74,95 € le sac ». Et une fois la couleur offerte choisie, « 149,90 € économisés » en vert.

Je regarderais combien de commandes prennent l'offre à 2 sacs.

Abonne-toi pour la suite."""),

 dict(brand="Based", shot="new:based-cart", text="""Idée à piquer #5 : le panier de Based.

Pendant l'offre « 1 acheté, 1 offert », le panier devient un jeu. « Your haul. 1 pick, 0 free. » Une barre de progression, une case en pointillés marquée FREE à côté de ton article, et « BOGO savings €0.00 » en doré. Un zéro qu'on a envie de corriger.

« Haul » et « picks », c'est le vocabulaire des vidéos d'unboxing. Le panier parle comme ceux qui achètent.

Il y a aussi un plafond par commande. Une limite rend l'affaire précieuse.

Mais le plus gros chiffre du panier, c'est « €255.76 left ». Un budget que personne n'avait prévu. La barre mesure la distance jusqu'au plafond, pas jusqu'à la prochaine récompense.

Ce que je testerais : faire de la prochaine étape le titre. « Choisis-en 1 de plus, il est offert. » Le plafond en petit.

Je regarderais la part de paniers avec 2 articles ou plus.

Abonne-toi pour la suite."""),

 dict(brand="DJI", shot="33.png", text="""Idée à piquer #6 : le Black Friday de DJI, sans remise.

Un bundle drone à 1 599 €, et le prix ne bouge pas. À la place : un sac à dos DJI Pro marqué « Cadeau », et « 5 fois plus de crédit DJI sur votre achat ».

Pourquoi c'est malin :
- pas de baisse de prix = pas de nouveau prix de référence. 1 599 € reste crédible après novembre.
- le crédit ne marche que chez DJI, donc il te ramène pour les batteries, les filtres, le prochain drone
- le cadeau est un objet qu'on visualise, listé avant les caractéristiques

Ce que je testerais : le crédit en euros. La base affichée, c'est « Récompense 1 % en crédit DJI ». 5 fois plus, ça fait environ 80 € sur ce bundle. « 80 € offerts » parle plus que « 5 fois plus ». Au-dessus de 100, les euros battent le ratio (règle des 100, voir #1).

Je regarderais la conversion pendant la promo, et le crédit utilisé sous 90 jours.

Abonne-toi pour la suite."""),

 dict(brand="HOLY", shot="new:holy-cart", text="""Idée à piquer #7 : le panier de HOLY, à un centime près.

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

Abonne-toi pour la suite."""),

 dict(brand="Fincut", shot="new:fincut-cart", text="""Idée à piquer #8 : les tickets dans le panier de Fincut.

Grand jeu Black Friday pour gagner 3 voitures, 1 ticket par article acheté. Dans le panier, les tickets sont une vraie ligne : ticket Grand Jeu, offert, x3.

Tu retires un t-shirt, tu perds un ticket. On déteste lâcher ce qu'on « a » déjà.

Aussi :
- le t-shirt offert du pack 3+1 ne donne pas de ticket. 4 t-shirts, 3 tickets. La règle tient.
- la barre de livraison offerte est déjà pleine
- première suggestion : une boîte cadeau à 9 €. Très de saison.

Ce qui me gêne : un bandeau donne le code BLACK20 (-20 %), à taper dans le champ code promo. Ce champ est replié tout en bas, et le total de 84 € ne l'inclut pas. Pourquoi me faire taper un code que le panier connaît déjà ?

Ce que je testerais : l'appliquer automatiquement, ou un bouton « Appliquer » sur le bandeau. Et dire s'il se cumule avec le pack.

Abonne-toi pour la suite."""),

 dict(brand="Represent", shot="16.png", text="""Idée à piquer #9 : les deux lignes sous les boutons de Represent.

Boutique française, marque anglaise. Sous les boutons : « Express France Shipping » avec un drapeau, et « EU Import Duties Included ».

Depuis le Brexit, la peur n'est pas le prix, c'est la facture de douane à la porte. Ils la tuent avant même que tu poses la question.

- la livraison nomme ton pays, pas « livraison internationale »
- Klarna en 3 paiements de 18,66 €, chacun sous 20 €
- « Style With » montre 4 pièces, toutes avec un prix barré

Ils ont localisé les risques. Reste à localiser les mots. La page dit « RRP » et « 30% OFF - SAUVEGARDER €24 ». Sauvegarder, c'est pour un fichier. « Économisez 24 € » et « Prix conseillé » feraient boutique française.

Ce que je testerais : corriger cette seule ligne, et comparer la conversion française avant et après.

Abonne-toi pour la suite."""),

 dict(brand="Alphalete", shot="19.webp", text="""Idée à piquer #10 : l'info de coupe d'Alphalete.

« Ilon is 6'1"/185cm, wearing a size L with a 43"/109cm chest. »

La taille du mannequin seule ne dit presque rien pour un sweat. Son tour de poitrine, si. Ils donnent les deux, en pouces et en cm, pour que personne ne convertisse de tête.

- « Oversized » est un badge en haut et la première ligne de l'info de coupe. Dit deux fois, pour que personne ne prenne une taille en dessous.
- « Final sale » est aussi visible que le -70 %. Pas de surprise après la livraison.

Final sale, ça veut dire pas de retour. Et c'est justement là que l'info de coupe devient plus précise. J'adore.

Ce que je testerais : les mesures du vêtement à côté de celles du mannequin (largeur et longueur du L). Ou une ligne sur quoi faire entre deux tailles.

Je regarderais les questions de taille au SAV sur les articles en final sale.

Abonne-toi pour la suite."""),

 dict(brand="HOLY", shot="15.png", text="""Idée à piquer #11 : le prix par portion de HOLY.

Bundle à 99,99 €. Juste en dessous : « 150 PORTIONS / Seulement €0,80 PAR PORTION ».

Même somme, plus petite unité. Un prix à trois chiffres devient un prix de tous les jours.

- « Valeur totale : €119,97 » est juste au-dessus, donc 99,99 € se lit déjà comme une économie
- le bouton est à la première personne : « J'AJOUTE AU PANIER ». C'est le client qui parle, pas la marque.
- « Mix & match : économise jusqu'à 20 % » pour ceux qui ne veulent pas tous les goûts

0,80 €, c'est un chiffre que tu compares tout de suite à ce que tu achètes déjà. La comparaison se fait dans ta tête, gratuitement.

Ce que je testerais : la rendre explicite, si c'est vrai pour leurs clients. « 0,80 € la portion, moins qu'une canette d'energy drink. » Et à côté de « Expédition sous 6 à 10 jours », une vraie date.

Abonne-toi pour la suite."""),

 dict(brand="Boku", shot="12.webp", text="""Idée à piquer #12 : le bouton compatibilité de Boku.

Un bidet qu'on installe sur ses propres toilettes amène une question évidente. Boku en fait un bouton : « Ce bidet est-il compatible avec vos WC ? »

- il nomme le doute avec les mots du client, avant qu'il aille le googler
- « Installation en 10 minutes sans travaux, sans électricité », avec une vidéo, règle la peur suivante
- la première suggestion est un robinet 3 voies pour les arrivées d'eau rigides. La solution au blocage le plus probable, vendue juste là.

Ça ressemble moins à une vente additionnelle qu'à de l'aide.

Ce que je testerais : transformer le bouton en test de 3 questions (forme des WC, abattant, arrivée d'eau) qui finit sur « Compatible » et ajoute la bonne pièce. Ou au moins garder la réponse jusqu'au panier.

Je regarderais la conversion après le test, et les retours « incompatible ».

Abonne-toi pour la suite."""),

 dict(brand="Gymshark", shot="10.png", text="""Idée à piquer #13 : le panier latéral de Gymshark.

Tu ouvres le panier, et la première chose que tu vois, c'est la distance jusqu'à la livraison offerte : « Il manque 31 € », une barre de 0 € à 59 €.

- l'objectif passe avant les articles, donc il cadre tout ce qui suit
- chaque ligne répète couleur, taille et coupe (« Black Wash, M, Boxy Fit »)
- l'économie par article, en euros, même ici
- « Vos articles ne sont pas réservés », une urgence qui se trouve être vraie

La barre change la livraison : ce n'est plus un coût, c'est un objectif déjà à moitié atteint.

Mais regarde les suggestions. Le lot de 6 paires de chaussettes à 19,60 € ne comble pas 31 €. Ajoute la paire suivante à 11,20 €, et il manque encore 0,20 €.

Ce que je testerais : suggérer des produits juste au-dessus de l'écart. Ou en marquer un « Débloque la livraison offerte ».

Abonne-toi pour la suite."""),

 dict(brand="Fincut", shot="14.png", text="""Idée à piquer #14 : le choix de pack de Fincut.

Trois options. Seul le t-shirt à l'unité affiche un coût en plus : « + Livraison 7,90 € ».

La livraison apparaît au moment du choix, sur l'option qu'ils préfèrent que tu évites. C'est le prix de ne pas prendre le pack.

- le t-shirt offert du 3+1 a sa propre ligne, couleur et taille. Tu l'as choisi, il est déjà un peu à toi.
- « Meilleure vente » sur le pack du milieu, « Meilleure offre (bientôt terminée) » sur le gros. Deux raisons différentes de monter d'un cran.
- « Prenez votre taille habituelle. » Une ligne, plus de doute.

1 t-shirt revient à 35,90 € livré. 4 t-shirts, 84 €, livraison offerte. L'option à l'unité existe surtout pour rendre le pack évident.

Ce que je testerais : le prix par t-shirt sur chaque option. 21 € pièce pour le 3+1, moins de 20 € pour le 5+2. Ou « 21 € le t-shirt » dans le bouton.

Abonne-toi pour la suite."""),

 dict(brand="AYBL", shot="18.png", text="""Idée à piquer #15 : le bouton d'AYBL.

Tant que tu n'as pas choisi de taille, le bouton ne dit pas « Ajouter au panier ». Il dit « SÉLECTIONNEZ LA TAILLE ».

Pas d'erreur rouge après le tap, pas de bouton qui tremble. Juste l'étape suivante, là où tu regardes déjà.

- la taille du mannequin est écrite sur la première photo : 1,67 m, porte du XS
- « Taille normalement » ferme le bloc des caractéristiques clés
- la newsletter est un petit onglet sur le côté (« Ne manque plus aucun drop »), pas une pop-up. Facile à ignorer, facile à retrouver.

Ils évitent l'erreur au lieu de la corriger.

Ce que je testerais : une fois la taille choisie, la répéter dans le bouton. « Ajouter le XS au panier. » Petit, mais ça confirme le choix juste avant le tap.

Je regarderais les échanges et les retours pour la taille.

Abonne-toi pour la suite."""),

 dict(brand="Arntreal", shot="13.webp", text="""Idée à piquer #16 : les trois lignes d'Arntreal.

Juste sous le nom du produit :
« Un sac basique, c'est de la mauvaise qualité.
Un sac de luxe, c'est 3 000 €, et tu paies le logo.
Celui-là a tout du luxe, à 149.90 €. »

Deux mauvaises options, et le produit se place au milieu. L'effet de compromis, fait en texte au lieu d'un tableau de prix. Et 3 000 € ancre le prix avant même que 149,90 € apparaisse.

Ça parle comme un pote, pas comme un catalogue.

Le vrai tour : tu arrêtes de te demander « 149,90 €, c'est cher ? » et tu te demandes « je veux payer un logo trop cher ? ». Réponse beaucoup plus facile.

Ce que je testerais : les 3 boutons en dessous (Look luxe, Tous les jours, Format cabine) ne font encore rien. Tape « Format cabine », vois le sac dans un coffre à bagages d'avion, avec ses dimensions.

Abonne-toi pour la suite."""),

 dict(brand="Oner Active", shot="17.webp", text="""Idée à piquer #17 : les noms de couleur d'Oner Active.

La couleur choisie ne s'appelle pas « Brown ». Elle s'appelle « 70% Cocoa ».

Tu connais la teinte avant de zoomer. Chocolat noir, pas beige, pas noir. Et ça reste en tête : « la veste 70% Cocoa », c'est bien plus facile à raconter que « la marron ».

Il y a même de la recherche là-dessus : des noms de couleur inhabituels tendent à faire plus aimer le produit (Miller et Kahn, 2005).

Autres détails :
- les points affichés : 6 660 pour une veste à 66,60 €. Les gros chiffres font généreux.
- « In Stock » en vert, juste à côté du prix

Ce que je testerais : le nom de chaque pastille au tap, pas seulement celle choisie. Les gens parcourraient des noms, pas des points. Et garder le nom dans le panier et l'email de confirmation.

Je regarderais les taps sur les pastilles et les couleurs commandées.

Abonne-toi pour la suite."""),

 dict(brand="Cabaia", shot="new:cabaia-product", text="""Idée à piquer #18 : les tailles en litres de Cabaia.

Fiche d'un sac à dos : Medium, 18 L. Large, 23 L. Avec un lien pour comparer les tailles juste au-dessus.

Le litre, c'est la bonne unité pour un sac. « Medium » ne veut rien dire tant que tu ne sais pas ce qui rentre.

- chaque pastille est une photo du sac avec sa pochette assortie, pas un rond de couleur
- le prix est dans le bouton d'ajout, 53,40 €
- sous 100 €, ils commencent par le pourcentage (-40 %). La règle des 100 du #1, bien appliquée.

Ce que je testerais : transformer les litres en objets. Presque personne ne visualise 18 litres. « 18 L : un ordi 14 pouces, un pull, une gourde. 23 L : en plus, une paire de baskets. » Si c'est vraiment ce qui rentre.

Ou plus simple : la comparaison des tailles sous les boutons, pas derrière un lien.

Je regarderais les échanges entre Medium et Large.

Abonne-toi pour la suite."""),

 dict(brand="Boku", shot="38.webp", text="""Idée à piquer #19 : les trois pourcentages de Boku.

Une image produit, pas un bloc d'avis. « Testé sous contrôle dermatologique », puis :
- 95 % des utilisateurs trouvent qu'il améliore l'hygiène
- 97 % des utilisatrices trouvent qu'il améliore l'hygiène lors des menstruations
- 98 % le trouvent agréable à utiliser

Chaque chiffre répond à un doute différent. Est-ce que ça marche, est-ce que ça marche pour moi, est-ce bizarre à utiliser.

Celui du milieu nomme un usage que la plupart des marques laissent dans le flou. Les concernées s'y reconnaissent tout de suite.

Et le flacon repose sur une main ouverte : nomade, avant même de lire un mot.

Ce que je testerais : rendre les chiffres vérifiables. Sans base, 95 % peut vouloir dire 19 personnes sur 20. « 95 % de [n] utilisateurs après [x] semaines », avec les vrais chiffres, transforme une promesse en résultat.

Abonne-toi pour la suite."""),

 dict(brand="Broken Planet", shot="22.png", text="""Idée à piquer #20 : les deux mannequins de Broken Planet.

« Dawn is 6'2, wearing size XL sweatpants. Supriya is 5'3, wearing size M sweatpants. »

Même jogging, deux morphologies très différentes. Un mannequin te donne un repère. Deux te donnent une fourchette où te placer. Ça dit unisexe sans l'écrire.

- « 540 GSM organic cotton fabric » arrive en premier. Pour le streetwear épais, le grammage est la preuve de qualité.
- les tailles épuisées restent visibles, barrées. Tu vois ce qui existe et ce qui est parti.

Ces cases barrées sont la donnée la plus précieuse de la page, et personne ne la compte. Chaque tap dessus est une demande perdue.

Ce que je testerais : les rendre tapables. « XS épuisé. Préviens-moi au retour. » Puis utiliser le nombre d'inscrits par taille pour décider combien en refaire.

Je regarderais les ventes des emails de retour en stock.

Abonne-toi pour la suite."""),

 dict(brand="Gymshark", shot="11.png", text="""Idée à piquer #21 : les « 224 XP » de Gymshark.

Sous le bouton d'achat : « L'achat de ce produit rapporte 224 XP ».

XP, pas « points ». C'est le langage du jeu vidéo, et les gens qui vont à la salle suivent déjà leur progression. Pour une marque de sport, monter de niveau, c'est toute l'identité.

- c'est propre à ce produit, pas un « rejoins notre programme » générique
- le même bloc répond aux dernières questions : livraison gratuite dès 59 €, express disponible
- le paiement en 4 fois affiché en 4 x 7,00 €. Plus petit chiffre, même total.

Problème : 224 XP de quoi ? Des points sans taux de change, c'est juste un nombre.

Ce que je testerais : lui donner un sens. « 224 XP, à une commande de ton prochain niveau », ou ce qu'ils valent sur la prochaine commande.

Je regarderais les créations de compte depuis les fiches produit, et les rachats.

Abonne-toi pour la suite."""),

 dict(brand="Alphalete", shot="20.png", text="""Idée à piquer #22 : le guide des tailles d'Alphalete.

La plupart des guides te donnent des chiffres. Celui-là t'apprend d'abord à trouver les tiens.

- des repères sur le corps, sans jargon : environ un pouce sous l'aisselle, au niveau du nombril
- un geste pour la taille : penche-toi sur le côté, trouve le pli. Faisable seul dans ta chambre.
- un bouton IN / CM
- des fourchettes, pas un chiffre unique : poitrine de 39 à 42 pouces pour un M. Les vrais corps sont entre deux tailles.

Un guide des tailles ne vaut que la mesure qu'on y apporte. Ils ont corrigé l'entrée, pas seulement le tableau.

Ce que je testerais : une option « pas de mètre ruban ? ». Pose à plat un sweat que tu as déjà, mesure d'aisselle à aisselle, compare.

Petite correction aussi : la fiche produit vend du XXL et du XXXL, le guide dit 2XL et 3XL. Les mêmes noms partout.

Abonne-toi pour la suite."""),

 dict(brand="Kosbiotic", shot="23.webp", text="""Idée à piquer #23 : l'abonnement de Kosbiotic.

L'abonnement est sélectionné par défaut. Ce qui le rend acceptable, c'est ce qui est écrit dedans :
- « Économisez 10% », « Sans engagement »
- « Livraison automatique tous les 28 jours »
- « Annulation en 1 clic »

Un abonnement présélectionné sans ces lignes ressemblerait à un piège. Avec elles, il ressemble au choix évident.

28 jours, c'est la durée d'une cure, donc la boîte suivante arrive quand la précédente se termine. Et tous les 28 jours, ça fait 13 livraisons par an, pas 12. La cure et le chiffre d'affaires s'alignent.

Ce que je testerais : prouver l'annulation en 1 clic, avec un petit lien qui montre l'écran où on le fait. Ou ajouter « Décale ou mets en pause quand tu veux » pour ceux qui ont peur de crouler sous les boîtes.

Je regarderais la part d'abonnements et les annulations du premier mois.

Abonne-toi pour la suite."""),

 dict(brand="Cabaia", shot="new:cabaia-cart", text="""Idée à piquer #24 : le panier de Cabaia, prêt pour décembre.

Un sac à dos dans le panier, et les trois dernières questions réglées.

Quand ça arrive ? Une vraie date, calculée avec ton code postal, et un lien pour comparer les options. Pas « 3 à 5 jours ouvrés ».

C'est un cadeau ? Une case directement sur la ligne : emballage cadeau, 2,80 €.

Qu'est-ce qui va avec ? Une poche latérale Pau, à 7 €. Le sac s'appelle Pau aussi. Des noms de villes : l'association se fait sans étiquette « va avec ».

En décembre, la date de livraison, c'est quasiment la décision. L'avoir dans le panier enlève le dernier « est-ce que ça arrivera à temps ? ».

Ce que je testerais : une fois l'emballage coché, proposer un message et une facture sans prix. L'emballage, c'est la moitié du cadeau. L'autre moitié, c'est que le prix ne soit pas dans la boîte (friction #41).

Abonne-toi pour la suite."""),

 dict(brand="Alo", shot="24.webp", text="""Idée à piquer #25 : la photo annotée d'Alo.

Deuxième photo, des petites étiquettes qui pointent le t-shirt : « Soft Performance Fabric », « Fitted Sleeves », « Relaxed Fit ».

On regarde les photos avant de lire. Donc le texte va là où l'attention est déjà, sur le corps, au lieu d'un accordéon que personne n'ouvre. La recherche appelle ça la contiguïté spatiale : un mot placé à côté de ce qu'il décrit se comprend plus vite.

- l'info de coupe (taille normalement, coupe ample) juste au-dessus du guide des tailles
- un prix membre, 47 € au lieu de 68 € si tu crées un compte. La remise devient un compte.

Ce que je testerais : rendre les étiquettes tapables. « Soft Performance Fabric » ouvre un gros plan du tissu. Ou une 4e étiquette sur ce que leurs 1 943 avis demandent le plus.

Je regarderais le taux d'ajout au panier et les ouvertures d'accordéons.

Abonne-toi pour la suite."""),

 dict(brand="Horace", shot="25.png", text="""Idée à piquer #26 : les deux questions d'Horace.

La description, c'est juste deux questions en gras : « Que fait-il ? » et « Comment l'utiliser ? »

Pour un premier achat, « comment l'utiliser ? » est une vraie question. Réponse : le matin et/ou le soir, à faire mousser sur visage et cou humides. Fini.

- ce sont les questions qu'on poserait à un pote au comptoir, pas des titres marketing
- « Parfum : Sans parfum » a sa propre ligne. Pour beaucoup d'hommes, c'est le critère éliminatoire.
- le prix est dans le bouton : « AJOUTER AU PANIER - 13 € »

Ils vendent la routine, pas juste le flacon. Savoir comment l'utiliser enlève la peur d'acheter un truc qui finira au fond du placard.

Ce que je testerais : une troisième question, « Avec quoi ? », qui montre l'étape suivante de la routine et la distance jusqu'à la livraison offerte, dès 40 €.

Abonne-toi pour la suite."""),

 dict(brand="Le Slip Français", shot="27.png", text="""Idée à piquer #27 : le « Fréquemment achetés ensemble » du Slip Français.

Sous un lot de 5 boxers à 99 €, les suggestions ne sont ni des chaussettes ni des ceintures. Ce sont des lots plus gros : 7 boxers à 160 €, 10 à 185 €.

De la montée en gamme déguisée en vente croisée.

- la photo du lot de 7 est un cadeau : fond rouge, sachet doré « Un petit cadeau, un joli paquet »
- les motifs ont des noms de fête (Guirlande, Tout Schuss). En décembre, les noms de produits font le marketing de saison.

Maintenant, le calcul. Le lot de 10 revient à 18,50 € le boxer, moins cher que le lot de 5 (19,80 €). Le lot de 7 : 22,86 €, plus cher. Il vend l'emballage, pas le prix unitaire.

Ce que je testerais : le prix par boxer seulement là où il aide, « 18,50 € pièce » sur le lot de 10. Et vendre le lot cadeau sur le moment : « emballé, livré avant Noël », si c'est tenable.

Abonne-toi pour la suite."""),

 dict(brand="Based", shot="42.png", text="""Idée à piquer #28 : les tuiles ingrédients de Based.

Une image produit : « The Key Ingredients. Endless Benefits. » Quatre tuiles, chacune avec un ingrédient, une bande de la vraie texture de la poudre, et une ligne sur ce qu'il fait.

- tu vois la silice, l'arrow-root, la poudre de riz et le mica. Tu ne fais pas que lire leurs noms.
- chaque nom chimique devient un résultat : volume, moins de gras, douceur, fini mat
- 4 ingrédients, 4 rôles. Rien n'est là sans raison.

Cette image répond en silence à la question que pose un produit à 21,95 € qui pèse 2,5 g : je paie quoi ? Quatre actifs nommés font paraître un petit format dense plutôt que minuscule.

Ce que je testerais : partir du problème, pas de l'ingrédient. « Cheveux plats ? Silica silylate. Racines grasses à midi ? Arrow-root. » Les gens connaissent leur problème, pas la chimie.

Abonne-toi pour la suite."""),

 dict(brand="Polène", shot="28.webp", text="""Idée à piquer #29 : l'écran coupé en deux de Polène.

Moitié gauche : le sac porté, dans un immense paysage. Moitié droite : le même sac seul sur fond blanc, nom, prix, un bouton.

L'émotion et les faits côte à côte. Tu ne scrolles jamais de l'un à l'autre. Et tu lis le côté gauche en premier, donc l'envie passe avant les détails.

- énormément de blanc autour du packshot. À 380 €, l'espace signale la valeur.
- la « Vue 3D » te laisse tourner le sac toi-même au lieu de faire défiler six angles

Moitié magazine, moitié vitrine. La page ne te force jamais à choisir entre en avoir envie et vérifier.

Ce que je testerais : la question que pose chaque petit sac. Qu'est-ce qui rentre dedans ? Une photo ouvert avec un téléphone, des cartes et des clés. Ou une ligne sous le prix.

Je regarderais le taux d'ajout au panier et les retours « trop petit ».

Abonne-toi pour la suite."""),

 dict(brand="Typology", shot="29.png", text="""Idée à piquer #30 : les codes labo de Typology.

Le sérum s'appelle « A63 ». Au-dessus du nom, une référence comme sur un échantillon de labo : « LAB1035-30ML-SG ». La description est en police machine à écrire.

- le nom, c'est l'actif et sa concentration (« Complexe PDRN-EGF 3% »), pas un mot d'ambiance comme « Glow »
- les chiffres précis font honnête : « 150 000 micro-spicules véganes par gramme », « 95% d'ingrédients d'origine naturelle »
- un 15 ml à côté du 30 ml, pour essayer moins cher
- « Ce produit est-il compatible avec votre type de peau? » juste sous le bouton

La promesse, c'est la science, donc la page ressemble à une fiche de labo.

Ce que je testerais : appeler le 15 ml par ce qu'il est, « Format découverte », et afficher son prix sur le bouton avant le clic.

Je regarderais la conversion des premières commandes et le passage du 15 au 30 ml.

Abonne-toi pour la suite."""),

 dict(brand="Stüssy", shot="32.png", text="""Idée à piquer #31 : la fiche produit de Stüssy, pour ce qu'elle n'a pas.

Un cendrier en verre à 70 €. Pas d'avis, pas de « plus que 3 », pas de compte à rebours, pas de carrousel de suggestions.

- les détails du produit sont ouverts par défaut, en simple liste
- chaque dimension en pouces et en cm. Pour un objet, la taille est la première inconnue.
- un guide des livraisons des fêtes en haut, avec un lien « Hide »
- une liste, une photo, un bouton noir. La page ressemble à la marque.

Pour une marque culte, les techniques de persuasion feraient cheap. La retenue est le signal.

Ce que je testerais : l'échelle. Sur fond blanc, 20 cm ne se voit pas. Une photo à côté d'une main ou d'un briquet. Ou une vue de profil qui montre les 2,5 cm de hauteur.

Je regarderais les retours « plus petit que prévu ».

Abonne-toi pour la suite."""),

 dict(brand="Charles Tyrwhitt", shot="37.png", text="""Idée à piquer #32 : la chemise à composer de Charles Tyrwhitt.

Chemise à 29,95 € (au lieu de 84,95 €), et un bandeau rouge : « ÉCONOMISEZ 55 € AUJOURD'HUI - SANS CODE PROMOTION ».

« Sans code promotion » évite le détour par Google pour en chercher un. La fuite de la friction #27, fermée en trois mots.

- la coupe se choisit sur des dessins de la chemise, pas avec des mots comme « slim » qui veulent dire autre chose pour chacun
- les tailles de col en cm, regroupées sous S, M, L, XL. Les experts lisent les cm, les autres lisent la lettre.
- « Vos Sélections » récapitule chaque choix avec une coche

Un détail cloche : le badge « LES PLUS POPULAIRES » est sur Ajustée, qui est barrée. Indisponible. Le badge pousse vers ce qu'on ne peut pas acheter.

Ce que je testerais : quand une option est épuisée, déplacer le badge, ou le remplacer par « Préviens-moi ».

Abonne-toi pour la suite."""),

 dict(brand="Le Slip Français", shot="26.png", text="""Idée à piquer #33 : l'échelle de remises du Slip Français.

Trois petites pastilles sous le prix : « -5% supp. dès 3 », « -10% supp. dès 4 », « -20% supp. dès 5 ».

- tu vois la récompense d'acheter plus avant de choisir la quantité, pas au paiement
- trois marches au lieu d'un seul seuil. Chacune est un petit oui.
- « supp. » veut dire que ça se cumule sur un prix déjà réduit (99 € au lieu de 125 €)
- un point vert sur chaque taille, donc le stock est réglé sans un clic

L'échelle transforme « combien ? » en « à quelle marche je m'arrête ? ». On s'ancre sur la marche suivante, pas sur 1.

Ce que je testerais : la prolonger dans le panier. « Ajoute 1 article pour débloquer -10 %. » Ou mettre en avant la marche que le panier a atteinte.

Je regarderais les articles par commande, et combien de commandes s'arrêtent à 3, 4 et 5.

Abonne-toi pour la suite."""),

 dict(brand="Arntreal", shot="40.png", text="""Idée à piquer #34 : la preuve avant la promesse, chez Arntreal.

Au-dessus du nom du produit, avant tout le reste : cinq étoiles, « Plus de 100 000 sacs vendus » avec un drapeau français, et cinq mini photos de clients.

La plupart des pages font produit, promesse, puis les avis tout en bas. Arntreal inverse : preuve, promesse, produit.

- la phrase forte qui suit (« Tout d'un sac de luxe. Sauf le prix. ») tombe sur une foule qui a déjà acheté
- les visages transforment 100 000 en personnes. Un chiffre, c'est abstrait. Cinq visages, c'est quelqu'un comme toi.

Mais les étoiles n'ont ni note ni nombre d'avis. 100 000 sacs vendus, c'est un chiffre de ventes, pas d'avis : seules, cinq étoiles font déco.

Ce que je testerais : la vraie moyenne et le nombre d'avis, avec les étoiles qui y mènent. Ou chaque visage tapable, vers son avis photo.

Abonne-toi pour la suite."""),

 dict(brand="Apple", shot="34.png", text="""Idée à piquer #35 : le configurateur étape par étape d'Apple.

Chaque étape s'ouvre sur une phrase en deux couleurs : « Modèle. » en noir, « Choisissez la taille. » en gris. Puis deux grandes cartes, 13 pouces et 15 pouces.

- une décision par étape. Le noir nomme l'étape, le gris dit quoi faire.
- des points sur le côté montrent combien d'étapes il reste
- la taille d'abord, la question à laquelle tout le monde sait répondre
- chaque carte affiche le total et la mensualité

Maintenant, regarde l'écart. En total, le 15 pouces coûte 300 € de plus. Par mois, 8,96 € de plus. Même différence, et l'une des deux sonne comme un café par semaine.

Ce que je testerais : une fois le 13 pouces choisi, afficher la montée en gamme comme une différence, « +8,96 €/mois », sur la carte 15 pouces.

Je regarderais la part de 15 pouces et le prix moyen configuré.

Abonne-toi pour la suite."""),

 dict(brand="Decathlon", shot="35.png", text="""Idée à piquer #36 : le bloc prix de Decathlon.

Table de ping-pong d'extérieur à 459,99 €. Sous le prix : « 85 € de réduction » en rouge, puis « Promotion du 03/11/2026 au 26/01/2027 ».

- l'économie en euros, pas en pourcentage. Sur un produit à 544,99 €, 85 € sonne plus fort que 16 %. La règle des 100, bien appliquée.
- la promo a de vraies dates. De l'urgence sans faux compte à rebours, et tu y crois parce que c'est précis.
- la description vend l'usage : entre amis, en famille, dehors, grandes roues, rangement des raquettes

Une promo datée, c'est la version honnête d'un timer.

Deux petits conflits quand même. Le badge du haut dit « Livraison offerte », le bloc prix dit « Des frais de livraison peuvent être ajoutés ». Un seul message, en haut, avec sa condition. Et « Taille : Sans taille » peut disparaître. Une ligne vide coûte quand même de l'attention.

Abonne-toi pour la suite."""),

 dict(brand="Garmin", shot="36.png", text="""Idée à piquer #37 : le choix de version de Garmin.

Sur la fiche de la fēnix E, les autres versions sont des boutons juste sous la taille du boîtier : fēnix 8 AMOLED, Solar, Pro AMOLED, Pro MicroLED.

- toute la gamme est à un tap, sans quitter la page
- la taille du boîtier est une rangée de boutons en mm, avec une icône info si tu ne connais pas ton poignet
- la remise affichée en euros (150 €), et Klarna la coupe en 3 paiements de 149,99 €, juste sous 150 €

Mais « Solar », « AMOLED », « MicroLED » sont des caractéristiques, pas des raisons. Personne ne monte en gamme pour un mot qu'il ne comprend pas.

Ce que je testerais : sous chaque version, l'écart de prix et un bénéfice en mots simples (« se recharge au soleil »). Ou une icône info sur chaque version, comme sur la taille du boîtier.

Je regarderais la part des commandes au-dessus de cette version.

Abonne-toi pour la suite."""),

 dict(brand="Based", shot="31.png", text="""Idée à piquer #38 : l'annonce de packaging de Based.

Sur la fiche produit, deux tubes côte à côte : « New Packaging, Same Texture Powder. » Puis une ligne : tu peux recevoir l'ancien ou le nouveau packaging, le produit dedans est le même.

Pendant un changement de marque, le risque n'est pas le design. C'est quelqu'un qui ouvre un colis qui ne ressemble pas à la photo, et qui croit à une contrefaçon.

- ils montrent les deux versions, donc ce qui arrive était prévu
- ça répond à un ticket SAV avant que quelqu'un l'écrive
- un problème de logistique devient une petite actu de marque

La satisfaction, c'est en gros l'écart entre ce que tu attendais et ce que tu reçois. Ils ont déplacé l'attente au lieu d'espérer écouler l'ancien stock d'abord.

Ce que je testerais : la même image dans l'email d'expédition. Le doute arrive au déballage, pas sur la fiche produit.

Abonne-toi pour la suite."""),
]

MAX_CHARS = 900

if __name__ == '__main__':
    import re
    for i, p in enumerate(WS, 1):
        t = p['text']
        assert t.startswith(f'Idée à piquer #{i} : '), (i, t[:30])
        assert len(t) <= MAX_CHARS, (i, p['brand'], len(t))
        assert '·' not in t and '–' not in t and '—' not in t, i
        assert not re.search('[\U0001F000-\U0001FFFF☀-➿]', t), i
        assert t.endswith('Abonne-toi pour la suite.'), i
    print(len(WS), 'posts ; max', max(len(p['text']) for p in WS), '; longueurs :', [len(p['text']) for p in WS])
