import unittest
from king import King

class TestKing(unittest.TestCase):

    def test_str_method(self):
        king_white = King('WHITE')
        king_black = King('BLACK')
        self.assertEqual(str(king_white), 'K')
        self.assertEqual(str(king_black), 'k')

    def test_possible_moves(self):
        king = King('WHITE')
        expected_moves = [
            (2, 2), (2, 4), (4, 2), (4, 4), 
            (2, 3), (4, 3), (3, 2), (3, 4)
        ]
        self.assertEqual(king.possible_moves(3, 3), expected_moves)

if __name__ == '__main__':
    unittest.main()