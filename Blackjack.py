import random

def new_match():
    # bet = int(input("Please place your bet: ")) # Need to make sure it's lower tha bank and valid number
    deck = initialDeck()
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]
    player_value = calculateDeckValue(player_cards)
    print("Your hand is " + str(player_cards))
    print("Your current value is " + str(player_value))
    print("Dealer's face-up card is " + str(dealer_cards[1]))
    print("Press h to hit")
    print("Press d to double")
    if player_cards[0] == player_cards[1]:
        print("Press s to split")
    print("Press anything else to stand")
    choice = input()
    match choice:
        case 'h':
            player_cards, player_value = hit(player_cards, player_value, deck)
        case 's':
            if player_cards[0] == player_cards[1]:
                split()
            else:
                pass
        case 'd':
            # bet *= 2
            player_cards, player_value = double_down()
    print("Your turn is over. Dealer's turn now.")
    stand(player_value)
    

def initialDeck():
    deck = []
    for i in range (2,10):
        deck += [i] * 4
    deck += [10] * 4 * 4
    deck += ['A'] * 4
    random.shuffle(deck)
    return deck

def calculateDeckValue(deck):
    value = 0
    for card in deck:
        if isinstance(card, int):
            value += card
        else: # This is an ace
            value += 1 if value + 11 > 21 else 11
    return value

def hit(cards, value, deck):
    while choice == 'h':
        cards += [deck.pop()]
        value = calculateDeckValue(cards)
        if value > 21:
            return "Busted"
        print("Your hand is " + str(cards))
        print("Your current value is " + str(value))
        choice = input("Press h to hit again, anything else to stand")
    return cards, value
    
def stand(value):
    if 
    pass

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
    
    



    
    

if __name__ == "__main__":
    main()