import unittest
from unittest.mock import patch
from src.game_logic import dealer_turn


class TestDealerTurn(unittest.TestCase):
    @patch('src.utility.calculate_deck_value', side_effect=[15, 18, 21])
    def test_dealer_turn_win(self, mock_calculate_deck_value):
        cards = [2, 3]
        result = dealer_turn(cards, 17, [6, 5, 4])
        self.assertEqual(result, 20)  # Dealer wins by reaching 21

    @patch('src.utility.calculate_deck_value', side_effect=[15, 18, 22])
    def test_dealer_turn_bust(self, mock_calculate_deck_value):
        cards = [2, 3]
        result = dealer_turn(cards, 17, [6, 7, 4])
        self.assertEqual(result, 22)  # Dealer busts

    @patch('src.utility.calculate_deck_value', side_effect=[15, 18, 19])
    def test_dealer_turn_tie(self, mock_calculate_deck_value):
        cards = [2, 3]
        result = dealer_turn(cards, 17, [5, 5, 4])
        self.assertEqual(result, 19)  # Dealer ties player's value


if __name__ == '__main__':
    unittest.main()
