from src.logs import logger

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
