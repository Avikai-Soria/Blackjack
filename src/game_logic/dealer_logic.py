from src.utils import calculate_deck_value
from src.logs import logger


def dealer_turn(dealer_cards, value_to_beat, deck):
    """
    Handles the dealer's logic in his turn.
    Tries to at least tie the received value until busted
    :param dealer_cards: The dealer's list of cards
    :param value_to_beat: The value for the dealer to beat
    :param deck: The current deck
    :return: The value of the dealer's card at the end of his turn.
    No need to return his cards
    """
    dealer_value = calculate_deck_value(dealer_cards)
    while dealer_value < value_to_beat:
        dealer_cards.append(deck.pop())
        dealer_value = calculate_deck_value(dealer_cards)
    logger.info(f"Dealer turn is over. His cards are: {dealer_cards} with a value of {dealer_value}")
    return dealer_value
