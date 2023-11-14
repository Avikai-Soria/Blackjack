from src.utility import is_blackjack


def handle_insurance(dealer_cards, bet, bank):
    """
    Checks if the player want to bet insurance, and calculate the change if he did
    :param dealer_cards: The dealer's cards
    :param bet: The amount of original bet
    :param bank: The current player's money
    :return: False if player didn't bet. The amount received if player did
    """
    if dealer_cards[1] == 'A' and bet * 1.5 <= bank:
        choice = input("Do you want insurance? Press y for yes, anything else for no\n")
        if choice == 'y':
            if dealer_cards[0] == 10:
                print(f"Dealer had a blackjack! You won {bet}")
                return bet * 2  # This is 2 * half of the bet
            else:
                print(f"Dealer doesn't have blackjack, you lose {0.5 * bet}")
                return -0.5 * bet
    return False


def handle_blackjack(player_value, dealer_value, bet, bank):
    """
    Checks if player got a blackjack, and if he did, whether he won or not
    :param player_value: The value of player's card
    :param dealer_value: The value of dealer's card
    :param bet: The amount of money that was bet
    :param bank: The current amount of money
    :return:
    """
    if is_blackjack(player_value):
        if is_blackjack(dealer_value):
            print("Even match with blackjack!")
            return "Push", bank
        print("Nice blackjack!")
        print(f"You won {bet}")
        return "Win", bank + bet * 1.5
    return False
