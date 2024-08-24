import unittest
from pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_str_method(self):
        pawn_white = Pawn('WHITE')
        pawn_black = Pawn('BLACK')
        self.assertEqual(str(pawn_white), 'P')
        self.assertEqual(str(pawn_black), 'p')

    def test_possible_moves_white(self):
        pawn = Pawn('WHITE')
        # Movimientos desde la posición inicial (6, 3)
        expected_moves_initial = [(5, 3), (4, 3)]
        self.assertEqual(pawn.possible_moves(6, 3), expected_moves_initial)
        
        # Movimientos desde una posición intermedia (5, 3)
        expected_moves_intermediate = [(4, 3), (4, 2), (4, 4)]  # Incluyendo movimientos diagonales
        self.assertEqual(pawn.possible_moves(5, 3), expected_moves_intermediate)
        
        # Movimientos diagonales desde (5, 3)
        possible_moves = pawn.possible_moves(5, 3)
        self.assertIn((4, 2), possible_moves)
        self.assertIn((4, 4), possible_moves)

    def test_possible_moves_black(self):
        pawn = Pawn('BLACK')
        # Movimientos desde la posición inicial (1, 3)
        expected_moves_initial = [(2, 3), (3, 3)]
        self.assertEqual(pawn.possible_moves(1, 3), expected_moves_initial)
        
        # Movimientos desde una posición intermedia (2, 3)
        expected_moves_intermediate = [(3, 3), (3, 2), (3, 4)]  # Incluyendo movimientos diagonales
        self.assertEqual(pawn.possible_moves(2, 3), expected_moves_intermediate)
        
        # Movimientos diagonales desde (2, 3)
        possible_moves = pawn.possible_moves(2, 3)
        self.assertIn((3, 2), possible_moves)
        self.assertIn((3, 4), possible_moves)

if __name__ == '__main__':
    unittest.main()