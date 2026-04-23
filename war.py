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
    assert n_card > 0, 'n_card doit etre strictement positif'
    cards = card.deck(2 * n_card)
    m1 = apqueue.ApQueue()
    m2 = apqueue.ApQueue()
    for i in range(n_card):
        m1.enqueue(cards[i])
        m2.enqueue(cards[n_card + i])
    return m1, m2

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
    while not pile.is_empty():
        main.enqueue(pile.pop())


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
    c1 = m1.dequeue()
    c2 = m2.dequeue()
    pile.push(c1)
    pile.push(c2)

    cmp_cards = card.compare(c1, c2)
    if cmp_cards > 0:
        gather_stack(m1, pile)
    elif cmp_cards < 0:
        gather_stack(m2, pile)


def play(n_card, n_round):
    """
    simule une partie de bataille

    :param n_card: (int) le nombre de cartes à distribuer à chaque joueur.
    :param n_round: (int) le nombre maximal de tours
    :return: None
    """
    assert n_card > 0 and n_round >= 0, 'parametres invalides'
    m1, m2 = distribute(n_card)
    pile = apstack.ApStack()

    round_count = 0
    while round_count < n_round and not m1.is_empty() and not m2.is_empty():
        play_one_round(m1, m2, pile)
        round_count += 1

    if not pile.is_empty():
        if len(m1) >= len(m2):
            gather_stack(m1, pile)
        else:
            gather_stack(m2, pile)


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
