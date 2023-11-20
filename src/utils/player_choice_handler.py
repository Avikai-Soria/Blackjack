from src.utils.utils import valid_bet
from src.logs import logger


def get_valid_bet(bank):
    """
    Gets a bet, checks if it's valid and returns it in int
    :param bank: The current amount of money the player has
    :return: The valid bet in int
    """
    while True:
        bet = input("Please place your bet: ")
        if valid_bet(bet, bank):
            return int(bet)
        logger.info("Please place a valid bet.")


def handle_split(player_cards, bet, bank):
    """
    Checks if player can and wants to split and returns it
    :param player_cards: The player's cards
    :param bet: The amount of original bet
    :param bank: The current sum in player's bank
    :return: True if player can and want to split. False otherwise
    """
    if player_cards[0] == player_cards[1] and bet * 2 <= bank:
        logger.info("Do you want to split? Press y for yes, anything else for no ")
        choice = input()
        if choice == "y":
            return True
    return False
