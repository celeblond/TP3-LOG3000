# Résultats initiaux des tests backend

Les tests ont été exécutés sur le code original, avant toute correction.

## Première exécution : opérations

Commande :

```bash
python -m pytest tests/test_operators.py -v
```

Résultat : **12 tests, 5 réussis, 7 échoués**.

## Résultats initiaux du backend

- Système : Windows
- Python : 3.12.10
- pytest : 9.1.1
- Branche : `tests/backend-initial`

Commande :

```bash
python -m pytest tests/test_operators.py tests/test_calculate.py -v
```

**Résultat : 26 tests exécutés, 16 réussis, 10 échoués.**

| Module | Tests | Réussites | Échecs |
| --- | ---: | ---: | ---: |
| `test_operators.py` | 12 | 5 | 7 |
| `test_calculate.py` | 14 | 11 | 3 |
| **Total** | **26** | **16** | **10** |

## Bogues confirmés

| Issue | Problème | Cas en échec | Exemple |
| --- | --- | ---: | --- |
| #13 | Soustraction inversée | 3 | `subtract(9, 4)` donne -5 au lieu de 5 |
| #14 | Puissance au lieu de multiplication | 4 | `multiply(3, 4)` donne 81 au lieu de 12 |
| #15 | Division entière au lieu de division usuelle | 3 | `divide(7, 2)` donne 3 au lieu de 3.5 |

Les tests de `calculate()` échouent pour ces mêmes trois opérations, car cette fonction appelle les opérations de `operators.py`. Il ne s'agit pas de trois nouveaux bogues.

Les cas d'addition, les expressions invalides et la division par zéro testés ont réussi.
