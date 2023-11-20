from src.utils import calculate_deck_value
from src.logs import logger


def hit(player_cards, deck):
    """
    Picks a card, and asks the player continuously if he wants to hit again
    :param player_cards: Current user's list of cards
    :param deck: Current deck
    :return: The new value of the deck. Not the cards as they're no longer relevant
    """
    cards_value = 0  # Initializing just to solve annoying warning
    player_choice = "h"
    while player_choice == "h":
        player_cards += [deck.pop()]
        cards_value = calculate_deck_value(player_cards)
        logger.info(f"Your hand is {player_cards} with a value of {cards_value}")
        if cards_value > 21:
            return cards_value
        player_choice = input("Press h to hit again, anything else to stand \n")
    return cards_value


def double_down(player_cards, deck):
    """
    Handles double logic.
    Gives the player 1 more card only from deck and finishes turn
    :param player_cards: The player's list of cards
    :param deck: The current deck
    :return: The current player's list value
    """
    player_cards += [deck.pop()]
    cards_value = calculate_deck_value(player_cards)
    logger.info(f"Your hand is {player_cards} with a value of {cards_value}")
    return cards_value
