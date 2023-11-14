from src.utility import calculate_deck_value
from src.logger_setup import global_logger as logger


def dealer_turn(cards, value, deck):
    """
    Handles the dealer's logic in his turn.
    Tries to at least tie the received value until busted
    :param cards: The dealer's list of cards
    :param value: The value for the dealer to beat
    :param deck: The current deck
    :return: The value of the dealer's card at the end of his turn.
    No need to return his cards
    """
    dealer_value = calculate_deck_value(cards)
    while dealer_value < value:
        cards.append(deck.pop())
        dealer_value = calculate_deck_value(cards)
    logger.info(f"Dealer turn is over. His cards are: {cards} with a value of {dealer_value}")
    return dealer_value
