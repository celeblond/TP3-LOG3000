# Module templates

## Rôle
Contient les modèles HTML utilisés par Flask pour afficher l'interface de la calculatrice.

## Fichiers
- `index.html` : définit l'interface, les boutons, le formulaire et les fonctions JavaScript de saisie.

## Dépendances et hypothèses
- Flask utilise Jinja2 pour générer la page HTML.
- Le formulaire transmet les expressions au serveur par POST.
- JavaScript est nécessaire pour saisir et effacer les expressions.
- Les styles sont chargés depuis `static/style.css`.
