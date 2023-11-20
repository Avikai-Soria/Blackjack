def calculate_deck_value(cards):
    """
    Gets a list of cards and calculates their value, with consideration to aces
    :param cards: A list that contains numbers or 'A' for ace
    :return: The value of the card's list
    """
    cards_value = 0
    for card in cards:
        if isinstance(card, int):  # The only non int is Ace
            cards_value += card
        else:  # This is an ace
            cards_value += 1 if cards_value + 11 > 21 else 11
    return cards_value
