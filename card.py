#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`card` module

:author: `FIL - Faculté des Sciences et Technologies -
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2021, april.


"""

import random

COLORS = ('spade', 'heart', 'diamond', 'club')
VALUES = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
          'Jack', 'Knight', 'Queen', 'King')


def create(value, color):
    """
    create a new card

    :param value: (str) card's value
    :param color: (str) card's color
    :return: (dict) a dictionnary representing a card
    :CU: color in COLORS and value in VALUES
    :Exemples:

    >>> col = random.choice(COLORS)
    >>> val = random.choice(VALUES)
    >>> carte = create(val, col)
    >>> type(carte) == dict and len(carte) == 2
    True
    """
    assert color in COLORS, 'couleur incorrecte'
    assert value in VALUES, 'valeur incorrecte'
    cart= dict()
    cart['value']= value
    cart['color']= color
    return cart


def get_color(card):
    """
    :param card: (dict) a card
    :return: (str) card's color
    :CU: card must be a valid card
    :Exemples:

    >>> col = random.choice(COLORS)
    >>> val = random.choice(VALUES)
    >>> carte = create(val, col)
    >>> get_color(carte) == col
    True
    """
    return card['color']


def get_value(card):
    """
    :param card: (dict) a card
    :return: (str) card's color
    :CU: card must be a valid card
    :Exemples:

    >>> col = random.choice(COLORS)
    >>> val = random.choice(VALUES)
    >>> carte = create(val, col)
    >>> get_value(carte) == val
    True
    """
    return card['value']


def compare(card1, card2):
    """
    :param card1: (dict) a card
    :param card2: (dict) a card
    :return: (int) * -1 if card1 is less than card2 ,
                   * +1 if card1 is greater than card2 ,
                   * 0 if card1 and card2 are equals
    :CU: card1 and card2 must be valid cards
    :Exemples:

    >>> carte1 = create('Ace', 'spade')
    >>> carte2 = create('2', 'spade')
    >>> carte3 = create('2', 'spade')
    >>> compare( carte1, carte2 )
    -1
    >>> compare(carte3, carte1)
    1
    >>> compare(carte2, carte3)
    0
    """
    if VALUES.index(card1['value']) > VALUES.index(card2['value']):
        return -1
    elif VALUES.index(card1['value']) < VALUES.index(card2['value']):
        return 1
    else:
        return 0

def is_card(dico):
    """
    :param dico: (dict) a dictionnary
    :return (bool) True if dico is a card, False otherwise
    :CU: None
    :Exemples:

    >>> is_card( { 'Nom': 'Oléon', 'Prénom' : 'Tim' })
    False
    >>> is_card( create('Ace', 'spade') )
    True
    """
    if len(dico)== 2:
        for c in dico.keys():
            if c in VALUES and c in COLORS:
                return True
    return False



def to_str(card):
    """
    :param card: (dict) a card
    :return: (str) a string representation of the card
    :CU: is_card(card)
    :Exemples:

    >>> to_str( create('Ace', 'spade'))
    'Ace of spade'
    >>> to_str( create('8', 'heart'))
    '8 of heart'
    """
    pass



def deck(n_card):
    """
    :param n_card: (int) number of cards
    :return: (list) a list of `n_card` randomly chosen cards
    :CU: n_card > 0 and n_card <= 4*13
    :Exemples:

    >>> cartes = deck( 10 )
    >>> len(cartes) == 10
    True
    >>> all( is_card(c) for c in cartes)
    True
    """
    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
