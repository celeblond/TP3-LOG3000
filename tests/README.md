# Tests de la calculatrice

Ce répertoire contient les tests automatisés de la logique Python de la calculatrice.

## Fichiers

- `test_operators.py` : tests unitaires des quatre opérations arithmétiques, dont les valeurs négatives, décimales et la division par zéro.
- `test_calculate.py` : tests de l'analyse des expressions, des résultats arithmétiques et des erreurs pour les entrées mal formées.

Les tests vérifient le comportement attendu d'une calculatrice, et non uniquement celui du code initial. Certains tests peuvent donc échouer avant la correction des bogues.

## Prérequis

Depuis la racine du dépôt, installer Flask et pytest :

```bash
python -m pip install Flask pytest
```

## Exécution

Depuis la racine du dépôt :

```bash
python -m pytest
```

Pour exécuter un seul module :

```bash
python -m pytest tests/test_operators.py
python -m pytest tests/test_calculate.py
```

Pour afficher le détail de chaque cas :

```bash
python -m pytest -v
```

Sur certains systèmes, utiliser `python3` à la place de `python`.

## Suivi des résultats

1. Exécuter les tests sur la version initiale avant toute correction.
2. Conserver la sortie du terminal, les noms des cas échoués et les messages d'erreur.
3. Ouvrir et assigner une Issue GitHub pour chaque bogue distinct confirmé.
4. Réexécuter les tests concernés sur la branche de correction correspondante.
5. Consigner les résultats dans la Pull Request avant la revue.
6. Après les fusions, exécuter l'ensemble des tests sur `main` et documenter le résultat.

Les tests du formulaire Flask et les vérifications de l'interface seront ajoutés séparément. Aucune exécution ni réussite des tests présentés ici n'est encore attestée.
