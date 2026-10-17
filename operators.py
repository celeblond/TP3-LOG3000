"""Fonctions utilisees pour les operations arithmetiques de la calculatrice."""

def add(a,b):
    """Additionne deux nombres.

    Parametres:
        a (int ou float): Premier operande.
        b (int ou float): Deuxieme operande.

    Retour:
        int ou float: Somme de a et b.
    """
    return a + b

def subtract(a,b):
    """Traite la soustraction entre deux nombres.

    Parametres:
        a (int ou float): Premier operande.
        b (int ou float): Deuxieme operande.

    Retour:
        int ou float: Resultat de la fonction de soustraction.
    """
    return a - b

def multiply(a,b):
    """Traite la multiplication entre deux nombres.

    Parametres:
        a (int ou float): Premier operande.
        b (int ou float): Deuxieme operande.

    Retour:
        int ou float: Resultat de la fonction de multiplication.
    """
    return a * b

def divide(a,b):
    """Traite la division entre deux nombres.

    Parametres:
        a (int ou float): Premier operande.
        b (int ou float): Deuxieme operande.

    Retour:
        int ou float: Resultat de la fonction de division.

    Exceptions:
        ZeroDivisionError: Second operande egal a zero.
    """
    return a // b
