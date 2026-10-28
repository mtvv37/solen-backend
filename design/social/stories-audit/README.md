# Stories Instagram 1080×1920 — « On a analysé… »

Visuels de la story d'offre (audit de page produit). Les versions `-sans-prix` n'affichent pas le prix.

- `solen-story-offre-v1..v4` : variantes de texte (v3 et v4 citent des marques par leur nom).
- `solen-story-banner-en/fr` : la bannière X reprise en story, avec icônes.
- `_src/` : générateur (`gen_story.py`, rendu via Playwright avec `shot3.js`) et logos recadrés.

À vérifier avant toute publication :
- Chaque marque citée ou affichée doit avoir été mesurée par le robot (`tools/benchmark`). Au dernier contrôle, Horace et Jacquemus ne l'étaient pas.
- Les chiffres « 300+ boutiques » et « 1 500+ pages » viennent de `stats.md` (branche `benchmark-data`) : à relire le jour de la publication.
- « Sur cette base » n'est vrai que si l'audit livré cite des chiffres du benchmark.
- Logos : marques de leurs propriétaires, aucune affiliation (mention incluse dans l'image).
