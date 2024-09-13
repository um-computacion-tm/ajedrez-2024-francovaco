import unittest
from king import King

class TestKing(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method is a unit test that verifies that the __str__ method of the King class returns 'K' for a white piece and 'k' for a black piece.
        '''
        king_white = King('WHITE')
        king_black = King('BLACK')
        self.assertEqual(str(king_white), 'K')
        self.assertEqual(str(king_black), 'k')

    def test_possible_moves_white(self):
        '''
        The function test_possible_moves is a unit test that verifies the possible moves of a king from the center of the board.
        It calls the possible_moves method of the King class with a starting row and column and verifies that the returned moves are as expected.
        '''
        king = King('WHITE')
        from_row, from_col = 4, 4
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        result = king.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

    def test_possible_moves_black(self):
        '''
        The function test_possible_moves_black is a unit test that verifies the possible moves of a black king from the center of the board.
        It calls the possible_moves method of the King class with a starting row and column and verifies that the returned moves are as expected.
        '''
        king = King('BLACK')
        from_row, from_col = 4, 4
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        result = king.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()