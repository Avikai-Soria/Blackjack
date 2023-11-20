import random


def initialize_deck():
    """
    Initializes all 52 cards and randomizes their order.
    :return: A list of all 52 cards randomized
    """
    deck = []
    for i in range(2, 10):
        deck += [i] * 4
    deck += [10] * 4 * 4
    deck += ["A"] * 4
    random.shuffle(deck)
    return deck


def deal_initial_cards(deck):
    """
    Returns 2 lists of cards, one for player and one for dealer
    :param deck: The list of cards to deal from
    :return:
    """
    return [deck.pop(), deck.pop()], [deck.pop(), deck.pop()]
