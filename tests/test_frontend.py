"""Tests des routes Flask et de l'interface HTML de la calculatrice."""

import unittest
from html.parser import HTMLParser
from app import app


class ButtonParser(HTMLParser):
    """Extrait les boutons HTML, leurs attributs et leurs textes."""

    def __init__(self):
        """Initialise la liste des boutons et le bouton courant."""
        super().__init__()
        self.buttons = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        """Enregistre les attributs lorsqu'un bouton commence."""
        if tag == "button":
            self.current = {"attrs": dict(attrs), "text": ""}

    def handle_data(self, data):
        """Accumule le texte du bouton courant."""
        if self.current is not None:
            self.current["text"] += data

    def handle_endtag(self, tag):
        """Enregistre le bouton terminé dans la liste."""
        if tag == "button" and self.current is not None:
            self.buttons.append(self.current)
            self.current = None


class TestFrontend(unittest.TestCase):
    """Vérifie les routes Flask et les éléments de l'interface."""

    def setUp(self):
        """Prépare un client Flask et récupère les boutons de la page."""
        app.config["TESTING"] = True
        self.client = app.test_client()
        response = self.client.get("/")
        parser = ButtonParser()
        parser.feed(response.get_data(as_text=True))
        self.buttons = parser.buttons

    def button(self, action):
        """Retourne le bouton associé à une action JavaScript."""
        return next(
            b for b in self.buttons
            if b["attrs"].get("onclick") == action
        )

    def test_get_home(self):
        """Vérifie que la page principale est accessible."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask Calculator", response.data)

    def test_post_addition(self):
        """Vérifie l'affichage d'une addition valide."""
        response = self.client.post("/", data={"display": "2+3"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('value="5.0"', response.get_data(as_text=True))

    def test_post_invalid_expression(self):
        """Vérifie l'affichage d'une erreur pour une expression invalide."""
        response = self.client.post("/", data={"display": "abc"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Error:", response.get_data(as_text=True))

    def test_button_2(self):
        """Vérifie que le bouton 2 affiche le bon chiffre."""
        self.assertEqual(
            self.button("appendToDisplay('2')")["text"].strip(), "2"
        )

    def test_button_8(self):
        """Vérifie que le bouton 8 affiche le bon chiffre."""
        self.assertEqual(
            self.button("appendToDisplay('8')")["text"].strip(), "8"
        )

    def test_button_multiply(self):
        """Vérifie que le bouton multiplication affiche son symbole."""
        self.assertEqual(
            self.button("appendToDisplay('*')")["text"].strip(), "*"
        )

    def test_button_divide(self):
        """Vérifie que le bouton division affiche son symbole."""
        self.assertEqual(
            self.button("appendToDisplay('/')")["text"].strip(), "/"
        )

    def test_button_clear(self):
        """Vérifie la présence du bouton d'effacement."""
        self.assertEqual(
            self.button("clearDisplay()")["text"].strip(), "C"
        )

    def test_button_equals(self):
        """Vérifie que le bouton égal soumet le formulaire."""
        self.assertTrue(any(
            b["attrs"].get("type") == "submit"
            and b["text"].strip() == "="
            for b in self.buttons
        ))


if __name__ == "__main__":
    unittest.main()
