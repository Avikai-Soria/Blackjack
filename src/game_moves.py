from src.utility import calculate_deck_value


def hit(cards, deck):
    """
    Allows to player to pick cards from the deck and add them to his cards
    :param cards: Current user's list of cards
    :param deck: Current deck
    :return: The new value of the deck. Not the cards as they're no longer relevant
    """
    value = 0  # Initializing just to solve annoying warning
    choice = "h"
    while choice == "h":
        cards += [deck.pop()]
        value = calculate_deck_value(cards)
        print(f"Your hand is {cards} with a value of {value}")
        if value > 21:
            return value
        choice = input("Press h to hit again, anything else to stand \n")
    return value


def double_down(cards, deck):
    """
    Handles double logic.
    Gives the player 1 more card only from deck and finishes turn
    :param cards: The player's list of cards
    :param deck: The current deck
    :return: The current player's list value
    """
    cards += [deck.pop()]
    value = calculate_deck_value(cards)
    print(f"Your hand is {cards} with a value of {value}")
    return value