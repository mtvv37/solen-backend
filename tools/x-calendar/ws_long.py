"""Format long de la série Idée à piquer : 900 caractères maximum (au-delà de 280, X Premium), puces en tiret simple."""

TEMPLATE = """Idée à piquer #1 : [le détail] de [Marque].

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

Abonne-toi pour la suite."""

EXAMPLE = """Idée à piquer #1 : le choix de taille de [Marque].

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

Abonne-toi pour la suite."""

if __name__ == '__main__':
    for name, t in (('TEMPLATE', TEMPLATE), ('EXAMPLE', EXAMPLE)):
        assert '–' not in t and '—' not in t, name
        print(name, len(t), 'caractères ; les 2 premières lignes :', repr(t.split('\n\n')[0]))
