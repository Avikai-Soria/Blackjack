from src.dealer_logic import dealer_turn
from src.game_moves import hit, double_down
from src.logger_setup import global_logger as logger
from src.player_choice_handler import get_valid_bet, handle_split
from src.side_bets_handler import handle_blackjack, handle_insurance
from src.split_handler import split
from src.utility import initialize_deck, deal_initial_cards, calculate_deck_value, is_busted


def new_match(bank):
    """
    This function represents a single match according to these stages:
    a) The player picks a valid bet
    b) The dealer and player gets cards
    c) The player's turn, can choose any option that's available to him
    d) If player busted, dealer wins the match
    e) The dealer's turn, tries to at least tie the player's value
    f) Checks results
    :param bank: The current amount of money that the player has
    :return: The status of the match, Win, Push (Tie) or Lose, and the updated bank
    """
    bet = get_valid_bet(bank)

    # The deal
    deck = initialize_deck()
    player_cards, dealer_cards = deal_initial_cards(deck)

    player_value = calculate_deck_value(player_cards)
    dealer_value = calculate_deck_value(dealer_cards)
    logger.info(f"Your hand is {player_cards} with a value of {player_value}")
    logger.info(f"Dealer's face-up card is {dealer_cards[1]}")

    # Checking blackjack scenario
    blackjack_result = handle_blackjack(player_value, dealer_value, bet, bank)
    if blackjack_result:  # Blackjack happened
        return blackjack_result

    # Checking insurance scenario. This bet is independent, so results go directly to bank
    insurance_result = handle_insurance(dealer_cards, bet, bank)
    if insurance_result:  # Insurance was chosen
        bank += insurance_result

    # Checking split scenario
    if handle_split(player_cards, bet, bank):  # If player can and want to split
        return split(deck, player_cards[0], dealer_cards, bet, bank)

    # Player's turn
    logger.info("Press h to hit")
    if bet * 2 <= bank:
        logger.info("Press d to double")
    logger.info("Press anything else to stand ")
    choice = input()
    match choice:
        case "h":
            player_value = hit(player_cards, deck)

        case "d":
            if bet * 2 <= bank:
                bet *= 2
                player_value = double_down(player_cards, deck)

    if is_busted(player_value):
        logger.info("You busted :/")
        return "Lose", bank - bet
    logger.info("Your turn is over. Dealer's turn now.")
    dealer_value = dealer_turn(dealer_cards, player_value, deck)
    if is_busted(dealer_value):
        logger.info("Dealer busted!")
        return "Win", bank + bet
    if dealer_value == player_value:
        logger.info("It's a tie!")
        return "Push", bank  # No changes
    logger.info("Too bad")  # If dealer not busted and didn't tie, he definitely won
    return "Lose", bank - bet
