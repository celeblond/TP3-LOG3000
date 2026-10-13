# Tests frontend

## Objectif
Vérifier les routes Flask et les éléments de l'interface HTML.

## Fichiers
- test_frontend.py : tests des routes, formulaires et boutons.

## Exécution
Depuis la racine du projet :

    python -m unittest discover -s tests -p "test_frontend.py" -v

## Couverture
- Chargement de la page principale.
- Traitement des expressions valides et invalides.
- Affichage des boutons numériques et des opérateurs.
- Présence des boutons C et =.

## Dépendances
- Python, Flask et unittest.
- Les tests utilisent le client Flask et analysent le HTML.
- Ils n'exécutent pas les interactions JavaScript dans un navigateur.
