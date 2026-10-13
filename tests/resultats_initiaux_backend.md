# Résultats initiaux des tests backend

Exécution du 13 octobre 2026 sur le code original, sans correction.

## Commande

```bash
python -m pytest tests/test_operators.py -v
```

Environnement : Python 3.13.5, pytest 9.0.2.

Les versions de `operators.py` et `tests/test_operators.py` utilisées pour cette exécution correspondent exactement aux fichiers des branches `main` et `tests/backend-initial`, respectivement (empreintes Git vérifiées).

## Résultat

**12 tests exécutés, 5 réussis, 7 échoués.**

| Fonction | Réussites | Échecs | Constat |
| --- | ---: | ---: | --- |
| `add` | 3 | 0 | Résultats attendus |
| `subtract` | 0 | 2 | Ordre des opérandes inversé |
| `multiply` | 0 | 3 | Puissance au lieu du produit |
| `divide` | 2 | 2 | Quotient entier pour les divisions non exactes |

Pour `divide`, le test de division par zéro et celui du quotient entier ont réussi.

## Exemples d'échecs

- `subtract(9, 4)` : obtenu -5, attendu 5.
- `multiply(3, 4)` : obtenu 81, attendu 12.
- `divide(7, 2)` : obtenu 3, attendu 3.5.

Les tests de `calculate()` n'ont pas été exécutés dans cet environnement parce que Flask n'y est pas installé. Ils restent à vérifier avec Flask avant toute correction.
