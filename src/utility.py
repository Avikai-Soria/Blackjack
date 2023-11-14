import random

from src.logger_setup import global_logger as logger

BLACKJACK_VALUE = 21


def is_busted(value):
    """
    Checks if the received value is bigger than blackjack
    :param value:
    :return: True if bigger than blackjack value, false otherwise
    """
    return value > BLACKJACK_VALUE


def valid_bet(bet, bank):
    """
    Confirms whether bet is int, bigger than 0 and lower than bank
    :param bet: The amount to bet
    :param bank: The current amount of money
    :return: True if the bet is valid, false otherwise
    """
    try:
        bet = int(bet)
    except ValueError:
        logger.error("Bet must be an integer.")
        return False
    if not 0 < bet <= bank:
        logger.error("Bet must be positive lower than current bank")
        return False
    return True


def is_blackjack(value):
    """
    Checks if value is equal to blackjack value
    :param value:
    :return: True if blackjacked, false otherwise
    """
    return value == BLACKJACK_VALUE


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


def calculate_deck_value(cards):
    """
    Gets a list of cards and calculates their value, with consideration to aces
    :param cards: A list that contains numbers or 'A' for ace
    :return: The value of the card's list
    """
    value = 0
    for card in cards:
        if isinstance(card, int):
            value += card
        else:  # This is an ace
            value += 1 if value + 11 > 21 else 11
    return value
