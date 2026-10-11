# Calculatrice web Flask - TP3 LOG3000

**Équipe :** 15  
**Cours :** LOG3000, Processus du génie logiciel

## Présentation

Ce projet contient une calculatrice web simple développée avec Python et Flask. L'utilisateur entre une expression arithmétique dans une interface HTML et obtient le résultat du calcul.

Le TP3 consiste à organiser le dépôt GitHub, documenter la base de code existante, ajouter des tests, suivre les bogues avec des Issues et effectuer les corrections par branches et Pull Requests.

## Structure du projet

- `app.py` : application Flask, analyse des expressions et affichage du résultat.
- `operators.py` : fonctions arithmétiques appelées par l'application.
- `templates/index.html` : interface de la calculatrice et fonctions JavaScript des boutons.
- `static/style.css` : mise en forme de l'interface.
- `tests/` : répertoire prévu pour les tests automatisés, à ajouter pendant la phase de tests.

Les répertoires du projet disposeront également d'un README précisant le rôle de leurs fichiers et leurs dépendances.

## Prérequis

- Python 3 et `pip`.
- Git pour récupérer le dépôt.
- Un navigateur web moderne.
- Flask, installé à l'étape suivante.

## Installation

1. Cloner le dépôt GitHub :

   ```bash
   git clone https://github.com/celeblond/TP3-LOG3000.git
   ```

2. Ouvrir le répertoire du projet :

   ```bash
   cd TP3-LOG3000
   ```

3. Installer Flask :

   ```bash
   python -m pip install Flask
   ```

Sur certains systèmes, la commande Python est `python3` plutôt que `python`. Comme le dépôt est privé pendant le développement, le clonage nécessite un compte autorisé à y accéder.

## Lancement

Depuis la racine du dépôt, exécuter :

```bash
python app.py
```

Ouvrir ensuite `http://127.0.0.1:5000/` dans le navigateur. Pour arrêter le serveur, utiliser `Ctrl+C` dans le terminal.

Le serveur lancé de cette manière est destiné au développement local.

## Utilisation

1. Cliquer sur les boutons numériques pour construire une expression.
2. Choisir un opérateur parmi `+`, `-`, `*` et `/`.
3. Saisir le deuxième nombre.
4. Cliquer sur `=` pour envoyer l'expression au serveur et afficher la réponse.
5. Utiliser `C` pour vider le champ d'affichage.

L'analyseur de `app.py` est conçu pour traiter une expression composée de deux opérandes et d'un seul opérateur. En cas d'entrée invalide ou d'erreur de calcul, l'application affiche un message d'erreur. Le comportement de la version initiale doit être vérifié par les tests avant toute correction.

## Tests

Les tests seront ajoutés pendant la phase de tests du TP3. Le répertoire `tests/` et son README préciseront les cas couverts. Aucun résultat de test n'est présumé à cette étape.

La commande prévue pour exécuter la suite, une fois les tests ajoutés et `pytest` installé, est :

```bash
python -m pip install pytest
python -m pytest
```

Les résultats initiaux, les corrections et les résultats finaux seront documentés dans les Issues et Pull Requests pertinentes.

## Contributions

Les modifications de l'équipe suivent ce processus :

1. Décrire tout bogue confirmé dans une Issue et l'assigner à un membre.
2. Créer une branche distincte associée à cette Issue.
3. Corriger uniquement le problème ciblé, puis relancer le test concerné.
4. Créer un commit avec un message décrivant clairement le changement.
5. Ouvrir une Pull Request qui renvoie à l'Issue et indique les résultats des tests.
6. Faire examiner la Pull Request par l'autre membre avant de la fusionner dans `main`.
7. Après les fusions, exécuter à nouveau toute la suite de tests.

Les modifications de documentation sont également préparées sur des branches séparées et soumises à une revue avant leur fusion.
