from src.game_logic import dealer_turn
from src.game_actions import hit
from src.utils import calculate_deck_value, is_busted
from src.logs import logger


def split(deck, initial_card, dealer_cards, bet, bank):
    """
    Handles split's game logic, as they're very quite different from normal matches
    a) No double allowed
    b) No blackjack allowed
    c) The player allowed to hit on any of his hands.
    d) The dealer tries to at least tie one hand.
    :param deck: Current deck of cards
    :param initial_card: The first card given to each of the player's hands
    :param dealer_cards: A list of all dealer's cards
    :param bet: The sum of bet for each hand.
    :param bank: The current bank of the player.
    :return: The final result, "Win", "Push" or "Lose", and the updated bank
    """
    first_hand = [initial_card, deck.pop()]
    second_hand = [initial_card, deck.pop()]
    logger.info(f"Your first hand is {first_hand}")
    logger.info(f"Your second hand is {second_hand}")

    # Player's turn
    choice = input("Do you want to hit on your first hand? h for yes, anything else for no \n")
    if choice == "h":
        first_value = hit(first_hand, deck)
    else:
        first_value = calculate_deck_value(first_hand)
    if is_busted(first_value):
        logger.info("First hand busted :/")
        first_value = 0  # Easier solution than rewriting logic later

    choice = input("Do you want to hit on your second hand? h for yes, anything else for no \n")
    if choice == "h":
        second_value = hit(second_hand, deck)
    else:
        second_value = calculate_deck_value(second_hand)
    if is_busted(second_value):
        logger.info("Second hand busted :/")
        second_value = 0  # Easier solution than rewriting logic later
    logger.info("Your turn is over. Dealer's turn now")

    # Dealer's turn. Will try to tie at least lower hand
    low_player_value = min(first_value, second_value)
    high_player_value = max(first_value, second_value)
    dealer_value = dealer_turn(dealer_cards, low_player_value, deck)

    if is_busted(dealer_value):
        logger.info("Dealer busted!")
        return "Win", bank + bet * 2

    if dealer_value == high_player_value:
        logger.info("Dealer won lower hand, tied higher hand")
        return "Lose", bank - bet
    elif low_player_value < dealer_value < high_player_value:
        logger.info("Dealer won low hand and lost to high hand")
        return "Push", bank  # No change
    # There's no scenario of dealer ending up lower than low hand
    logger.info("Dealer tied lower hand and lost to high hand")
    return "Win", bank + bet
