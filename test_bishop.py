import unittest
from bishop import Bishop

class TestBishop(unittest.TestCase):

    def test_str_method(self):
        bishop_white = Bishop('WHITE')
        bishop_black = Bishop('BLACK')
        self.assertEqual(str(bishop_white), 'B')
        self.assertEqual(str(bishop_black), 'b')

    def test_possible_moves(self):
        bishop = Bishop('WHITE')
        expected_moves = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(bishop.possible_moves(3, 3), expected_moves)

if __name__ == '__main__':
    unittest.main()