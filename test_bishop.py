import unittest
from bishop import Bishop

class TestBishop(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method is a unit test that verifies that the __str__ method of the Bishop class returns 'B' for a white piece and 'b' for a black piece.
        '''
        bishop_white = Bishop('WHITE')
        bishop_black = Bishop('BLACK')
        self.assertEqual(str(bishop_white), 'B')
        self.assertEqual(str(bishop_black), 'b')

    def test_possible_moves_white(self):
        '''
        The function test_possible_moves_white is a unit test that verifies the possible moves of a bishop from the center of the board.
        It calls the possible_moves method of the Bishop class with a starting row and column and verifies that the returned moves are as expected.
        '''
        bishop = Bishop('WHITE')
        expected_moves = [
            (2, 2), (1, 1), (0, 0),  # Upper left diagonal
            (2, 4), (1, 5), (0, 6),  # Upper right diagonal
            (4, 2), (5, 1), (6, 0),  # Lower left diagonal
            (4, 4), (5, 5), (6, 6), (7, 7)  # Lower right diagonal
        ]
        self.assertEqual(bishop.possible_moves(3, 3), expected_moves)

    def test_possible_moves_black(self):
        '''
        The function test_possible_moves_black is a unit test that verifies the possible moves of a black bishop from the center of the board.
        It calls the possible_moves method of the Bishop class with a starting row and column and verifies that the returned moves are as expected.
        '''
        bishop = Bishop('BLACK')
        expected_moves = [
            (2, 2), (1, 1), (0, 0),  # Upper left diagonal
            (2, 4), (1, 5), (0, 6),  # Upper right diagonal
            (4, 2), (5, 1), (6, 0),  # Lower left diagonal
            (4, 4), (5, 5), (6, 6), (7, 7)  # Lower right diagonal
        ]
        self.assertEqual(bishop.possible_moves(3, 3), expected_moves)

if __name__ == '__main__':
    unittest.main()