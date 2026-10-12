"""Tests unitaires des opérations arithmétiques."""

import pytest

from operators import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 3, 5), (-2, 3, 1), (1.5, 2.5, 4)],
    ids=["entiers", "negatif", "decimaux"],
)
def test_add(a, b, expected):
    """Vérifie l'addition de deux nombres.

    Paramètres:
        a: Premier opérande.
        b: Deuxième opérande.
        expected: Résultat attendu.

    Retour:
        Aucun. Le test échoue si la somme est incorrecte.
    """
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(9, 4, 5), (4, 9, -5)],
    ids=["positif", "negatif"],
)
def test_subtract(a, b, expected):
    """Vérifie que la soustraction respecte l'ordre des opérandes.

    Paramètres:
        a: Premier opérande.
        b: Deuxième opérande.
        expected: Résultat attendu pour a moins b.

    Retour:
        Aucun. Le test échoue si la différence est incorrecte.
    """
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(3, 4, 12), (2, 0, 0), (1.5, 2, 3)],
    ids=["entiers", "facteur_nul", "decimaux"],
)
def test_multiply(a, b, expected):
    """Vérifie que la multiplication produit le bon résultat.

    Paramètres:
        a: Premier facteur.
        b: Deuxième facteur.
        expected: Produit attendu.

    Retour:
        Aucun. Le test échoue si le produit est incorrect.
    """
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(7, 2, 3.5), (8, 4, 2), (3, 2, 1.5)],
    ids=["quotient_fractionnaire", "quotient_entier", "autre_fraction"],
)
def test_divide(a, b, expected):
    """Vérifie la division usuelle sans troncature du quotient.

    Paramètres:
        a: Dividende.
        b: Diviseur non nul.
        expected: Quotient attendu.

    Retour:
        Aucun. Le test échoue si le quotient est incorrect.
    """
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    """Vérifie le signalement d'une division par zéro.

    Paramètres:
        Aucun.

    Retour:
        Aucun. Le test échoue si ZeroDivisionError n'est pas levée.
    """
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
