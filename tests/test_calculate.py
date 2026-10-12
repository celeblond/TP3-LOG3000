"""Tests de l'analyse des expressions par le module Flask."""

import pytest

from app import calculate


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("2+3", 5),
        ("9-4", 5),
        ("3*4", 12),
        ("7/2", 3.5),
        (" 2 + 3 ", 5),
        ("1.5+2.5", 4),
    ],
    ids=[
        "addition",
        "soustraction",
        "multiplication",
        "division",
        "espaces",
        "decimaux",
    ],
)
def test_calculate_valid_expression(expression, expected):
    """Vérifie l'évaluation d'une expression arithmétique valide.

    Paramètres:
        expression: Expression de deux opérandes à analyser.
        expected: Résultat arithmétique attendu.

    Retour:
        Aucun. Le test échoue si le résultat est incorrect.
    """
    assert calculate(expression) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("expression", "message"),
    [
        ("", "empty expression"),
        ("2", "invalid expression format"),
        ("2+", "invalid expression format"),
        ("+2", "invalid expression format"),
        ("2+3*4", "only one operator is allowed"),
        ("abc+3", "operands must be numbers"),
        ("2+xyz", "operands must be numbers"),
    ],
)
def test_calculate_invalid_expression(expression, message):
    """Vérifie le rejet d'une expression mal formée.

    Paramètres:
        expression: Entrée invalide.
        message: Message d'erreur attendu.

    Retour:
        Aucun. Le test échoue si ValueError n'est pas levée
        avec le message attendu.
    """
    with pytest.raises(ValueError, match=message):
        calculate(expression)


def test_calculate_division_by_zero():
    """Vérifie le traitement d'une division par zéro.

    Paramètres:
        Aucun.

    Retour:
        Aucun. Le test échoue si ZeroDivisionError n'est pas levée.
    """
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")
