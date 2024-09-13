import unittest
from unittest.mock import MagicMock
from rook import Rook

class TestRook(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method is a unit test that verifies that the __str__ method of the Rook class returns 'R' for a white piece and 'r' for a black piece.
        '''
        rook_white = Rook('WHITE')
        rook_black = Rook('BLACK')
        self.assertEqual(str(rook_white), 'R')
        self.assertEqual(str(rook_black), 'r')

    def test_possible_moves_white(self):
        '''
        The function test_possible_moves is a unit test that verifies the possible moves of a rook from the center of the board.
        It calls the possible_moves method of the Rook class with a starting row and column and verifies that the returned moves are as expected.
        '''
        rook = Rook('WHITE')
        from_row, from_col = 4, 4
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        result = rook.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

    def test_possible_moves_black(self):
        '''
        The function test_possible_moves is a unit test that verifies the possible moves of a rook from the center of the board.
        It calls the possible_moves method of the Rook class with a starting row and column and verifies that the returned moves are as expected.
        '''
        rook = Rook('BLACK')
        from_row, from_col = 4, 4
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        result = rook.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()