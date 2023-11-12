import random

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
        print("bet must be an integer.")
        return False
    if not 0 < bet <= bank:
        print("Bet must be positive lower than current bank")
        return False
    return True


def blackjack(value):
    """
    Checks if value is equal to blackjack value
    :param value:
    :return: True if blackjack, false otherwise
    """
    return value == BLACKJACK_VALUE


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
    bet = input("Please place your bet: ")
    while not valid_bet(bet, bank):
        bet = input("Please place a valid bet: ")
    bet = int(bet)

    # The deal
    deck = initialize_deck()
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]
    player_value = calculate_deck_value(player_cards)
    dealer_value = calculate_deck_value(dealer_cards)
    print(f"Your hand is {player_cards} with a value of {player_value}")
    print(f"Dealer's face-up card is {dealer_cards[1]}")

    # Checking blackjack scenario
    if blackjack(player_value):
        if blackjack(dealer_value):
            print("Even match")
            return "Push", bank
        print("Nice blackjack!")
        return "Win", bank + bet * 1.5

    # Checking insurance scenario. This bet is independent, so results go directly to bank
    if dealer_cards[1] == 'A':
        if bet * 1.5 <= bank:  # Checking if there's enough money for extra bet
            print("Do you want insurance? Press y for yes, anything else for no ")
            choice = input()
            if choice == 'y':
                if dealer_cards[0] == 10:
                    print(f"Dealer had an blackjack! You won {bet}")
                    bank += bet  # This is 2 * half of the bet
                else:
                    print(f"Dealer doesn't have blackjack, you lose {0.5 * bet}")
                    bank -= 0.5 * bet

    # Checking split scenario
    if player_cards[0] == player_cards[1]:
        if bet * 2 < bank:  # Checking if there's enough money for splitting
            print("Do you want to split? Press y for yes, anything else for no ")
            choice = input()
            if choice == "y":
                #  Split's game logic within split function
                return split(deck, player_cards[0], dealer_cards, bet, bank)

    # Player's turn
    print("Press h to hit")
    if bet * 2 <= bank:
        print("Press d to double")
    print("Press anything else to stand ")
    choice = input()
    match choice:
        case "h":
            player_value = hit(player_cards, deck)

        case "d":
            if bet * 2 <= bank:
                bet *= 2
                player_value = double_down(player_cards, deck)

    if is_busted(player_value):
        print("You busted :/")
        return "Lose", bank - bet
    print("Your turn is over. Dealer's turn now.")
    dealer_value = dealer_turn(dealer_cards, player_value, deck)
    if is_busted(dealer_value):
        print("Dealer busted!")
        return "Win", bank + bet
    if dealer_value == player_value:
        print("It's a tie!")
        return "Push", bank  # No changes

    print("Too bad")  # If dealer not busted and didn't tie, he definitely won
    return "Lose", bank - bet


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


def hit(cards, deck):
    """
    Allows to player to pick cards from the deck and add them to his cards
    :param cards: Current user's list of cards
    :param deck: Current deck
    :return: The new value of the deck. Not the cards as they're no longer relevant
    """
    value = 0  # Initializing just to solve annoying warning
    choice = "h"
    while choice == "h":
        cards += [deck.pop()]
        value = calculate_deck_value(cards)
        print(f"Your hand is {cards} with a value of {value}")
        if value > 21:
            return value
        choice = input("Press h to hit again, anything else to stand \n")
    return value


def dealer_turn(cards, value, deck):
    """
    Handles the dealer's logic in his turn.
    Tries to at least tie the received value until busted
    :param cards: The dealer's list of cards
    :param value: The value for the dealer to beat
    :param deck: The current deck
    :return: The value of dealer's card at the end of his turn.
    No need to return his cards
    """
    dealer_value = calculate_deck_value(cards)
    while dealer_value < value:
        cards.append(deck.pop())
        dealer_value = calculate_deck_value(cards)
    print(f"Dealer turn is over. His cards are: {cards} with a value of {dealer_value}")
    return dealer_value


def double_down(cards, deck):
    """
    Handles double logic.
    Gives the player 1 more card only from deck and finishes turn
    :param cards: The player's list of cards
    :param deck: The current deck
    :return: The current player's list value
    """
    cards += [deck.pop()]
    value = calculate_deck_value(cards)
    print(f"Your hand is {cards} with a value of {value}")
    return value


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
    print(f"Your first hand is {first_hand}")
    print(f"Your second hand is {second_hand}")

    # Player's turn
    choice = input("Do you want to hit on your first hand? h for yes, anything else for no \n")
    if choice == "h":
        first_value = hit(first_hand, deck)
    else:
        first_value = calculate_deck_value(first_hand)
    if is_busted(first_value):
        print("First hand busted :/")
        first_value = 0  # Easier solution than rewriting logic later

    choice = input("Do you want to hit on your second hand? h for yes, anything else for no \n")
    if choice == "h":
        second_value = hit(second_hand, deck)
    else:
        second_value = calculate_deck_value(second_hand)
    if is_busted(second_value):
        print("Second hand busted :/")
        second_value = 0  # Easier solution than rewriting logic later
    print("Your turn is over. Dealer's turn now")

    # Dealer's turn. Will try to tie at least lower hand
    low_player_value = min(first_value, second_value)
    high_player_value = max(first_value, second_value)
    dealer_value = dealer_turn(dealer_cards, low_player_value, deck)

    if is_busted(dealer_value):
        print("Dealer busted!")
        return "Win", bank + bet * 2
    if dealer_value == high_player_value:
        print("Dealer won lower hand, tied higher hand")
        return "Lose", bank - bet
    elif low_player_value < dealer_value < high_player_value:
        print("Dealer won low hand and lost to high hand")
        return "Push", bank  # No change
    else:  # There's no scenario of dealer ending up lower than low hand
        print("Dealer tied lower hand and lost to high hand")
        return "Win", bank + bet


def main():
    bank = 1000
    choice = 1
    print("Welcome! Let's play blackjack! Your initial bank is 1000")
    while choice != '0':
        result, updated_bank = new_match(bank)
        bank = updated_bank
        print(f"Match result is {result}")
        print(f"Your current bank is {bank}")
        if bank == 0:
            print("Sorry, no more money left. Better luck next time!")
            break
        choice = input("Type 0 to exit, anything else to play again! \n")
    print(f"Final score is {bank}, gg")

if __name__ == "__main__":
    main()
