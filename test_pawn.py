import unittest
from pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method is a unit test that verifies that the __str__ method of the Pawn class returns 'P' for a white piece and 'p' for a black piece.
        '''
        pawn_white = Pawn('WHITE')
        pawn_black = Pawn('BLACK')
        self.assertEqual(str(pawn_white), 'P')
        self.assertEqual(str(pawn_black), 'p')

    def test_possible_moves_white(self):
        '''
        The function test_possible_moves_white is a unit test that verifies the possible moves of a white pawn from different positions.
        It calls the possible_moves method of the Pawn class with a starting row and column and verifies that the returned moves are as expected.
        '''
        pawn = Pawn('WHITE')
        # Moves from the initial position (6, 3)
        expected_moves_initial = [(5, 3), (4, 3)]
        self.assertEqual(pawn.possible_moves(6, 3), expected_moves_initial)
        
        # Moves from an intermediate position (5, 3)
        expected_moves_intermediate = [(4, 3), (4, 2), (4, 4)]  # Including diagonal moves
        self.assertEqual(pawn.possible_moves(5, 3), expected_moves_intermediate)
        
        # Diagonal moves from (5, 3)
        possible_moves = pawn.possible_moves(5, 3)
        self.assertIn((4, 2), possible_moves)
        self.assertIn((4, 4), possible_moves)

    def test_possible_moves_black(self):
        '''
        The function test_possible_moves_black is a unit test that verifies the possible moves of a black pawn from different positions.
        It calls the possible_moves method of the Pawn class with a starting row and column and verifies that the returned moves are as expected.
        '''
        pawn = Pawn('BLACK')
        # Moves from the initial position (1, 3)
        expected_moves_initial = [(2, 3), (3, 3)]
        self.assertEqual(pawn.possible_moves(1, 3), expected_moves_initial)
        
        # Moves from an intermediate position (2, 3)
        expected_moves_intermediate = [(3, 3), (3, 2), (3, 4)]  # Including diagonal moves
        self.assertEqual(pawn.possible_moves(2, 3), expected_moves_intermediate)
        
        # Diagonal moves from (2, 3)
        possible_moves = pawn.possible_moves(2, 3)
        self.assertIn((3, 2), possible_moves)
        self.assertIn((3, 4), possible_moves)

if __name__ == '__main__':
    unittest.main()