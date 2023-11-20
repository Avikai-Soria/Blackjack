import unittest
from src.utils import is_busted, valid_bet, is_blackjack, initialize_deck, deal_initial_cards, calculate_deck_value


class TestIsBusted(unittest.TestCase):
    def test_not_busted(self):
        result = is_busted(15)
        self.assertFalse(result)

    def test_busted(self):
        result = is_busted(22)
        self.assertTrue(result)

    def test_equal_to_blackjack_value(self):
        result = is_busted(21)
        self.assertFalse(result)


class TestValidBet(unittest.TestCase):
    def test_valid_bet(self):
        result = valid_bet(10, 100)
        self.assertTrue(result)

    def test_invalid_bet_string(self):
        result = valid_bet("abc", 100)
        self.assertFalse(result)

    def test_invalid_bet_negative(self):
        result = valid_bet(-10, 100)
        self.assertFalse(result)

    def test_invalid_bet_zero(self):
        result = valid_bet(0, 100)
        self.assertFalse(result)

    def test_invalid_bet_exceeds_bank(self):
        result = valid_bet(150, 100)
        self.assertFalse(result)


class TestIsBlackjack(unittest.TestCase):
    def test_not_blackjack(self):
        result = is_blackjack(15)
        self.assertFalse(result)

    def test_blackjack(self):
        result = is_blackjack(21)
        self.assertTrue(result)


class TestInitializeDeck(unittest.TestCase):
    def test_deck_length(self):
        deck = initialize_deck()
        self.assertEqual(len(deck), 52)

    def test_deck_shuffled(self):
        deck1 = initialize_deck()
        deck2 = initialize_deck()
        self.assertNotEqual(deck1, deck2)


class TestDealInitialCards(unittest.TestCase):
    def test_deal_initial_cards(self):
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A']
        player_cards, dealer_cards = deal_initial_cards(deck)
        self.assertEqual(len(player_cards), 2)
        self.assertEqual(len(dealer_cards), 2)


class TestCalculateDeckValue(unittest.TestCase):
    def test_calculate_deck_value_numeric(self):
        result = calculate_deck_value([2, 3, 4])
        self.assertEqual(result, 9)

    def test_calculate_deck_value_with_ace(self):
        result = calculate_deck_value([2, 'A', 8])
        self.assertEqual(result, 21)

    def test_calculate_deck_value_with_multiple_aces(self):
        result = calculate_deck_value(['A', 'A', 8])
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()
