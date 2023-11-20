import unittest
from unittest.mock import patch
from src.game_logic.game_logic import handle_insurance, handle_blackjack


class TestHandleInsurance(unittest.TestCase):
    @patch('builtins.input', side_effect=['y'])
    def test_insurance_win(self, mock_input):
        result = handle_insurance([10, 'A'], 10, 100)
        self.assertEqual(result, 20)  # Player wins with insurance

    @patch('builtins.input', side_effect=['y'])
    def test_insurance_loss(self, mock_input):
        result = handle_insurance([2, 'A'], 10, 100)
        self.assertEqual(result, -5)  # Player loses with insurance

    @patch('builtins.input', side_effect=['n'])
    def test_no_insurance(self, mock_input):
        result = handle_insurance([10, 'A'], 10, 100)
        self.assertFalse(result)  # Player didn't bet insurance


class TestHandleBlackjack(unittest.TestCase):
    def test_blackjack_win(self):
        result = handle_blackjack(21, 18, 10, 100)
        self.assertEqual(result, ("Win", 115))  # Player wins with blackjack

    def test_blackjack_push(self):
        result = handle_blackjack(21, 21, 10, 100)
        self.assertEqual(result, ("Push", 100))  # Blackjack tie

    def test_no_blackjack(self):
        result = handle_blackjack(18, 21, 10, 100)
        self.assertFalse(result)  # Player didn't get blackjack


if __name__ == '__main__':
    unittest.main()
