import unittest
from queen import Queen

class TestQueen(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method is a unit test that verifies that the __str__ method of the Queen class returns 'Q' for a white piece and 'q' for a black piece.
        '''
        queen_white = Queen('WHITE')
        queen_black = Queen('BLACK')
        self.assertEqual(str(queen_white), 'Q')
        self.assertEqual(str(queen_black), 'q')

    def test_possible_moves_center_white(self):
        '''
        The function test_possible_moves_center is a unit test that verifies the possible moves of a queen from the center of the board.
        It calls the possible_moves method of the Queen class with a starting row and column and verifies that the returned moves are as expected.
        '''
        queen = Queen('WHITE')
        # Moves from the center of the board (4, 4)
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Upper left diagonal
            (3, 5), (2, 6), (1, 7),          # Upper right diagonal
            (5, 3), (6, 2), (7, 1),          # Lower left diagonal
            (5, 5), (6, 6), (7, 7),          # Lower right diagonal
            (3, 4), (2, 4), (1, 4), (0, 4),  # Vertical up
            (5, 4), (6, 4), (7, 4),          # Vertical down
            (4, 3), (4, 2), (4, 1), (4, 0),  # Horizontal left
            (4, 5), (4, 6), (4, 7)           # Horizontal right
        ]
        self.assertCountEqual(queen.possible_moves(4, 4), expected_moves)

    def test_possible_moves_corner_white(self):
        '''
        The function test_possible_moves_corner is a unit test that verifies the possible moves of a queen from a corner of the board.
        It calls the possible_moves method of the Queen class with a starting row and column and verifies that the returned moves are as expected.
        '''
        queen = Queen('WHITE')
        # Moves from the upper left corner (0, 0)
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),  # Lower right diagonal
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Vertical down
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Horizontal right
        ]
        self.assertCountEqual(queen.possible_moves(0, 0), expected_moves)

    def test_possible_moves_edge_white(self):
        '''
        The function test_possible_moves_edge is a unit test that verifies the possible moves of a queen from the edge of the board.
        It calls the possible_moves method of the Queen class with a starting row and column and verifies that the returned moves are as expected.
        '''
        queen = Queen('WHITE')
        # Moves from the edge of the board (0, 4)
        expected_moves = [
            (1, 3), (2, 2), (3, 1), (4, 0),  # Lower left diagonal
            (1, 5), (2, 6), (3, 7),          # Lower right diagonal
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),  # Vertical down
            (0, 3), (0, 2), (0, 1), (0, 0),  # Horizontal left
            (0, 5), (0, 6), (0, 7)           # Horizontal right
        ]
        self.assertCountEqual(queen.possible_moves(0, 4), expected_moves)

    def test_possible_moves_center_black(self):
        '''
        The function test_possible_moves_center is a unit test that verifies the possible moves of a queen from the center of the board.
        It calls the possible_moves method of the Queen class with a starting row and column and verifies that the returned moves are as expected.
        '''
        queen = Queen('WHITE')
        # Moves from the center of the board (4, 4)
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Upper left diagonal
            (3, 5), (2, 6), (1, 7),          # Upper right diagonal
            (5, 3), (6, 2), (7, 1),          # Lower left diagonal
            (5, 5), (6, 6), (7, 7),          # Lower right diagonal
            (3, 4), (2, 4), (1, 4), (0, 4),  # Vertical up
            (5, 4), (6, 4), (7, 4),          # Vertical down
            (4, 3), (4, 2), (4, 1), (4, 0),  # Horizontal left
            (4, 5), (4, 6), (4, 7)           # Horizontal right
        ]
        self.assertCountEqual(queen.possible_moves(4, 4), expected_moves)

    def test_possible_moves_corner_black(self):
        '''
        The function test_possible_moves_corner is a unit test that verifies the possible moves of a queen from a corner of the board.
        It calls the possible_moves method of the Queen class with a starting row and column and verifies that the returned moves are as expected.
        '''
        queen = Queen('WHITE')
        # Moves from the upper left corner (0, 0)
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),  # Lower right diagonal
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Vertical down
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Horizontal right
        ]
        self.assertCountEqual(queen.possible_moves(0, 0), expected_moves)

    def test_possible_moves_edge_black(self):
        '''
        The function test_possible_moves_edge is a unit test that verifies the possible moves of a queen from the edge of the board.
        It calls the possible_moves method of the Queen class with a starting row and column and verifies that the returned moves are as expected.
        '''
        queen = Queen('WHITE')
        # Moves from the edge of the board (0, 4)
        expected_moves = [
            (1, 3), (2, 2), (3, 1), (4, 0),  # Lower left diagonal
            (1, 5), (2, 6), (3, 7),          # Lower right diagonal
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),  # Vertical down
            (0, 3), (0, 2), (0, 1), (0, 0),  # Horizontal left
            (0, 5), (0, 6), (0, 7)           # Horizontal right
        ]
        self.assertCountEqual(queen.possible_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()