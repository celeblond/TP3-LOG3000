# Tests de la calculatrice

Ce répertoire contient les tests des opérations, de l'analyse des expressions, des routes Flask et de l'interface HTML.

## Fichiers

- `test_operators.py` : addition, soustraction, multiplication, division et cas limites.
- `test_calculate.py` : calcul des expressions et traitement des entrées invalides.
- `test_frontend.py` : routes Flask, formulaires et textes des boutons.
- `resultats_initiaux_backend.md` : résultats des tests avant les corrections.

Les tests backend utilisent `pytest`. Les tests frontend utilisent `unittest` et le client de test Flask. Les vérifications des boutons analysent le HTML, sans exécuter JavaScript dans un navigateur.

## Prérequis

Depuis la racine du dépôt :

```bash
python -m pip install Flask pytest
```

## Exécution

Toute la suite :

```bash
python -m pytest -v
```

Tests backend seulement :

```bash
python -m pytest tests/test_operators.py tests/test_calculate.py -v
```

Tests frontend seulement :

```bash
python -m unittest discover -s tests -p "test_frontend.py" -v
```

Sur certains systèmes, utiliser `python3` plutôt que `python`.

## Suivi des bogues

1. Exécuter les tests avant de corriger le code et conserver les échecs.
2. Créer une Issue pour chaque bogue distinct et l'assigner à un membre.
3. Corriger le problème sur une branche dédiée.
4. Relancer le test concerné et noter le résultat dans la Pull Request.
5. Faire revoir la Pull Request avant la fusion.
6. Après toutes les fusions, relancer la suite complète sur `main`.

## Résultats initiaux

- Backend : 26 tests exécutés sur le poste de Charles-Émile, 16 réussis et 10 échoués. Voir `resultats_initiaux_backend.md`.
- Frontend : la PR #3 rapporte 9 tests exécutés, 5 réussis et 4 échoués. Le journal d'exécution initial reste à conserver pour le rapport.

Ces échecs correspondent aux problèmes suivis dans les Issues GitHub. La réussite de tous les tests ne pourra être confirmée qu'après les corrections et leur intégration.
