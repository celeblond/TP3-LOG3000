# Résultats finaux des tests

## Contexte

Exécution de la suite complète sur la branche `main`, après la fusion des corrections des Issues #4, #5, #6, #7, #13, #14 et #15.

- Date : 17 octobre 2026
- Environnement : Windows, Python 3.12.10, pytest 9.1.1
- Commande : `python -m pytest -v`
- Durée rapportée par pytest : 2,15 s

## Résultat

**35 tests exécutés, 35 réussis, 0 échec.**

| Fichier | Tests réussis | Tests échoués |
| --- | ---: | ---: |
| `tests/test_operators.py` | 12 | 0 |
| `tests/test_calculate.py` | 14 | 0 |
| `tests/test_frontend.py` | 9 | 0 |
| **Total** | **35** | **0** |

## Corrections vérifiées

| Issue | Correction | Pull Request |
| --- | --- | --- |
| #4 | Affichage du bouton 2 | #8 |
| #5 | Affichage du bouton 8 | #9 |
| #6 | Affichage du bouton de multiplication | #10 |
| #7 | Affichage du bouton de division | #11 |
| #13 | Ordre des opérandes de la soustraction | #16 |
| #14 | Utilisation du produit pour la multiplication | #17 |
| #15 | Division sans troncature du quotient | #18 |

Les tests initiaux du backend sont consignés dans `resultats_initiaux_backend.md`. Les tests initiaux du frontend et les vérifications ciblées après correction sont documentés dans les Issues et les Pull Requests correspondantes.
