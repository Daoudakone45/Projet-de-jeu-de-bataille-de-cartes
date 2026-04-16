#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`war` game

:author: `FIL - Faculté des Sciences et Technologies -
         Univ. Lille <http://portail.fil.univ-lille1.fr>`

:date: 2021, april.


"""

import card
import apqueue
import apstack


def distribute(n_card):
    """
    distribute `n_card` cartes différentes aux deux joueurs
    :param n_card: (int) le nombre de cartes à distribuer à chaque joueur
    :return: (tuple) un couple (m1, m2) constitué de deux files,
             contenant pour chacune `n_card` cartes
    :CU: n_card > 0
    :Exemples:

    >>> m1, m2 = distribute( 4 )
    >>> len(m1) == 4
    True
    >>> len(m2) == 4
    True
    >>> type(m1) == apqueue.ApQueue
    True
    >>> type(m2) == apqueue.ApQueue
    True
    >>> carte = m1.dequeue()
    >>> card.is_card( carte )
    True
    """
    pass

def gather_stack(main, pile):
    """
    ajoute les carte de la pile dans la main

    :param main: (ApQueue) une main
    :param pile: (ApStack) une pile de carte
    :return: None
    :Exemples:

    >>> cartes = card.deck(4)
    >>> main = apqueue.ApQueue()
    >>> pile = apstack.ApStack()
    >>> for c in cartes:
    ...   pile.push(c)
    >>> gather_stack( main, pile )
    >>> len( main ) == 4
    True
    >>> all( main.dequeue() == cartes[ 3 - i ] for i in range(3))
    True
    """
    pass


def play_one_round(m1, m2, pile):
    """
    Simule une étape du jeu :
    `j1`` et ``j2`` prennent la première carte de leur
    main. On compare les deux cartes :

    * Si la carte de ``j1`` est supérieure à celle de ``j2``, alors
    ``j1`` remporte toutes les cartes de la pile ;
    * Si la carte de ``j1`` est inférieure à celle de ``j2``, alors
    ``j2`` remporte toutes les cartes de la pile ;
    * Si les cartes sont égales, alors elles sont *empilées* sur la
      pile.

    :param m1: (ApQueue) la main du premier joueur
    :param m2: (ApQueue) la main du second joueur
    :param pile: (ApStack) la pile des cartes sur la table
    :return: None
    :CU: m1 et m2 ne sont pas vides
    """
    pass


def play(n_card, n_round):
    """
    simule une partie de bataille

    :param n_card: (int) le nombre de cartes à distribuer à chaque joueur.
    :param n_round: (int) le nombre maximal de tours
    :return: None
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
