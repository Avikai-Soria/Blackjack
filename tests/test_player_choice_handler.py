import unittest
from unittest.mock import patch
from src.game_logic.game_logic import get_valid_bet, handle_split


class TestGetValidBet(unittest.TestCase):
    @patch('builtins.input', side_effect=['10'])
    def test_valid_bet(self, mock_input):
        result = get_valid_bet(50)
        self.assertEqual(result, 10)  # Valid bet within the bank limit

    @patch('builtins.input', side_effect=['60', '50.5', '20'])
    def test_multiple_attempts(self, mock_input):
        result = get_valid_bet(50)
        self.assertEqual(result, 20)  # Valid bet after two invalid attempts


class TestHandleSplit(unittest.TestCase):
    @patch('builtins.input', side_effect=['y'])
    def test_can_and_want_to_split(self, mock_input):
        result = handle_split([2, 2], 10, 100)
        self.assertTrue(result)  # Player can and wants to split

    @patch('builtins.input', side_effect=['N'])
    def test_do_not_want_to_split(self, mock_input):
        result = handle_split([2, 3], 10, 100)
        self.assertFalse(result)  # Player does not want to split

    @patch('builtins.input', side_effect=['l', 'n'])
    def test_invalid_second_input(self, mock_input):
        result = handle_split([2, 2], 10, 100)
        self.assertFalse(result)  # Player wants to split, but invalid second input


if __name__ == '__main__':
    unittest.main()
