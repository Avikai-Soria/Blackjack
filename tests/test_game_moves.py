import unittest
from unittest.mock import patch
from src.game_logic.game_logic import hit, double_down


class TestHit(unittest.TestCase):
    @patch('builtins.input', side_effect=['h', 's'])
    def test_hit_stand(self, mock_input):
        cards = [2, 3]
        result = hit(cards, [4, 5, 6])
        self.assertEqual(result, 16)  # Player chooses to hit once and then stand

    @patch('builtins.input', side_effect=['h', 'h'])
    def test_bust(self, mock_input):
        cards = [2, 3]
        result = hit(cards, [9, 5, 6])
        self.assertEqual(result, 25)  # Player busts after three hits


class TestDoubleDown(unittest.TestCase):
    def test_double_down(self):
        cards = [2, 3]
        result = double_down(cards, [4, 5, 6])
        self.assertEqual(result, 11)  # Player doubles down and gets one more card


if __name__ == '__main__':
    unittest.main()
