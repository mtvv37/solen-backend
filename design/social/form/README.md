# Visuels du formulaire (Tally)

| Fichier | Où le mettre dans Tally | Taille |
|---|---|---|
| `cover.png` | Couverture du formulaire (« Add cover ») | 1800 × 480. Tally recadre selon l'écran : le texte reste dans la bande centrale. |
| `share.png` | Image d'aperçu du lien, si ton plan Tally permet de la changer (Settings, partage) | 1200 × 630 |
| `../avatar-01-blanc-sur-sapin.png` | Logo du formulaire (« Add logo ») | 1024 × 1024, déjà existant |

Couleurs à reprendre dans Customize, si ton plan le permet : fond `#040A06`, texte `#EEF5F0`, boutons `#2BD07A` avec texte `#04140A`, champs `#07130C` avec bordure `#183323`.

Même DA que les visuels X (`../x-friction/`) : fond sapin, tuiles blanches penchées, deux courbes au plus. Pas de tiret long, pas d'emoji (`../RULES.md`).

Régénérer depuis `_src/` : `node ../../x-friction/_src/render.js 1800 480 cover.html` et `node ../../x-friction/_src/render.js 1200 630 share.html`
(le contrôle « titre trop large » de ce script vise le format 1200 × 675 et peut être ignoré ici).
