# Visuels X : « Friction Shopify à tester » et appel (visio ou formulaire)

Format du premier lot (`brand/posts/`) : **1200 × 675 (16:9)**, téléphone annoté à gauche, texte à droite.
DA de la bannière X verte (`design/social/banniere-x-1500x500.png`) : fond sapin, fils verts lumineux, tuiles blanches à icônes,
Inter Tight / Archivo Expanded / JetBrains Mono. Règles : `design/social/RULES.md` (pas de tiret long, pas d'emoji, aucun chiffre inventé).

| Fichier | Usage |
|---|---|
| `friction-NN.png` | 22 visuels de la série, #28 à #65 (la moitié des posts du calendrier `docs/X_NOV_DEC_2026.md`) |
| `cta-form.png` | Visuel d'appel au formulaire, en réponse sous chaque post avec le texte du calendrier |
| `planche.png` | Les 22 visuels sur une seule image, pour relire |

En français depuis le 26/11/2026 : un visuel par angle de friction (voir `tools/x-calendar/posts.py`). Les prix des maquettes sont des exemples (« Maquette, pas une vraie boutique. »), jamais des données de marchand.

**Régénérer** (depuis `_src/`) :
```
python3 gen_frictions.py                        # écrit friction-NN.html depuis SPECS et friction.tpl.html
node render.js 1200 675 friction-*.html cta-form.html   # écrit les PNG dans ce dossier, signale tout débordement
```
