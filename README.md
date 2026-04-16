# Projet de jeu de bataille de cartes

Ce projet implemente une version simple du jeu de bataille en Python. L'objectif est de distribuer des cartes a deux joueurs, de comparer les cartes tour par tour et de gerer une pile centrale lorsqu'il y a egalite.

## Principe du jeu

Chaque joueur recoit une main de cartes sous forme de file. A chaque tour, chacun pioche la premiere carte de sa main. Les deux cartes sont comparees selon leur valeur.

Si une carte est plus forte que l'autre, le joueur gagnant ramasse les cartes presentes sur la table. En cas d'egalite, les cartes sont empilees dans une pile commune pour etre redistribuees plus tard.

## Structure du projet

- [card.py](card.py) gere la creation et la comparaison des cartes.
- [apqueue.py](apqueue.py) fournit une structure de file pour representer la main d'un joueur.
- [apstack.py](apstack.py) fournit une structure de pile pour la table de jeu.
- [war.py](war.py) contient la logique principale de distribution et de deroulement d'une partie.

## Fonctionnalites

Le projet repose sur les elements suivants:

- creation d'une carte avec une valeur et une couleur;
- comparaison de deux cartes;
- generation aleatoire d'un paquet de cartes;
- distribution des cartes entre deux joueurs;
- gestion d'une pile de cartes sur la table;
- simulation d'une partie sur un nombre limite de tours.

## Execution

Le fichier [war.py](war.py) contient un bloc `__main__` qui lance les tests doctest du module.

Pour verifier le comportement des modules, tu peux executer:

```bash
python war.py
python card.py
python apqueue.py
python apstack.py
```

## Etat actuel

Certaines fonctions sont encore a completer dans le code source, notamment la logique de distribution, de collecte de la pile et de deroulement complet de la partie. La documentation ci-dessus refleche donc la structure prevue du jeu ainsi que l'organisation actuelle du projet.

## Ameliorations possibles

- ajouter une interface en ligne de commande pour lancer une partie complete;
- afficher le score ou le gagnant final;
- ajouter plus d'exemples dans les doctests;
- traiter le cas des egalites longues de facon plus detaillee.
