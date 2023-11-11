import random

def isBusted(value):
    return value > 21

def new_match():
    # bet = int(input("Please place your bet: ")) # Need to make sure it's lower tha bank and valid number
    deck = initialDeck()
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]
    player_value = calculateDeckValue(player_cards)
    print(f"Your hand is {player_cards}")
    print(f"Your current value is {player_value}")
    print(f"Dealer's face-up card is {dealer_cards[1]}")
    print("Press h to hit")
    print("Press d to double")
    if player_cards[0] == player_cards[1]:
        print("Press s to split")
    print("Press anything else to stand")
    choice = input()
    match choice:
        case "h":
            player_cards, player_value = hit(player_cards, player_value, deck)
            if isBusted(player_value):
                return "Lose"
            

        case "s":
            if player_cards[0] == player_cards[1]:
                split()
            else:
                pass
        case "d":
            # bet *= 2
            player_cards, player_value = double_down()
            if isBusted(player_value):
                return "Lose"

    print("Your turn is over. Dealer's turn now.")
    dealer_value = stand(dealer_cards, player_value, deck)
    if isBusted(dealer_value):
        return "Win"
    elif dealer_value == player_value:
        return "Push"
    else:
        return "Lose"

def initialDeck():
    deck = []
    for i in range(2, 10):
        deck += [i] * 4
    deck += [10] * 4 * 4
    deck += ["A"] * 4
    random.shuffle(deck)
    return deck


def calculateDeckValue(cards):
    value = 0
    for card in cards:
        if isinstance(card, int):
            value += card
        else:  # This is an ace
            value += 1 if value + 11 > 21 else 11
    return value

def hit(cards, value, deck):
    while choice == "h":
        cards += [deck.pop()]
        value = calculateDeckValue(cards)
        print(f"Your hand is {cards}")
        print(f"Your current value is {value}")
        choice = input("Press h to hit again, anything else to stand")
    return cards, value


def stand(cards, value, deck):
    dealer_value = calculateDeckValue(cards)
    print(f"Dealer cards are: {cards}")
    while dealer_value < value:
        cards.append(deck.pop())
        print(f"Dealer cards are: {cards}")
        dealer_value = calculateDeckValue(cards)
        if dealer_value > 21:
            print("Dealer busted")
            return "Busted"
    return dealer_value


def double_down(cards, value, deck):
    cards += [deck.pop()]
    value = calculateDeckValue(cards)
    print("Your hand is " + str(cards))
    print("Your current value is " + str(value))
    return cards, value


def split():
    pass


def main():
    Bank = 1000
    result = new_match()
    print(f"Match result is {result}")


if __name__ == "__main__":
    main()
