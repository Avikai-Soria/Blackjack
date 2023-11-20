from src.utils.utils import is_blackjack
from src.logs import logger


def handle_insurance(dealer_cards, bet, bank):
    """
    Checks if the player wants to bet insurance and calculates the change if they did
    :param dealer_cards: The dealer's cards
    :param bet: The amount of the original bet
    :param bank: The current player's money
    :return: False if the player didn't bet. The amount received if the player did
    """
    if dealer_cards[1] == 'A' and bet * 1.5 <= bank:
        user_choice = input("Do you want insurance? Press y for yes, anything else for no\n")
        if user_choice == 'y':
            if dealer_cards[0] == 10:
                logger.info(f"Dealer had a blackjack! You won {bet}")
                return bet * 2  # This is 2 * half of the bet
            else:
                logger.info(f"Dealer doesn't have blackjack, you lose {0.5 * bet}")
                return -0.5 * bet
    return False


def handle_blackjack(player_value, dealer_value, bet, bank):
    """
    Checks if the player got a blackjack, and if they did, whether they won or not
    :param player_value: The value of the player's card
    :param dealer_value: The value of the dealer's card
    :param bet: The amount of money that was bet
    :param bank: The current amount of money
    :return:
    """
    if is_blackjack(player_value):
        if is_blackjack(dealer_value):
            logger.info("Even match with blackjack!")
            return "Push", bank
        logger.info("Nice blackjack!")
        logger.info(f"You won {bet}")
        return "Win", bank + bet * 1.5
    return False
