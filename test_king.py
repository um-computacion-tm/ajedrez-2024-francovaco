import unittest
from king import King

class TestKing(unittest.TestCase):

    def test_str_method(self):
        '''
        La función test_str_method es una prueba unitaria que verifica que el método __str__ de la clase King devuelva 'K' para una pieza blanca y 'k' para una pieza negra.
        '''
        king_white = King('WHITE')
        king_black = King('BLACK')
        self.assertEqual(str(king_white), 'K')
        self.assertEqual(str(king_black), 'k')

    def test_possible_moves(self):
        '''
        La función test_possible_moves es una prueba unitaria que verifica los movimientos posibles de un rey desde el centro del tablero.
        '''
        king = King('WHITE')
        expected_moves = [
            (2, 2), (2, 4), (4, 2), (4, 4), # Diagonales
            (2, 3), (4, 3), (3, 2), (3, 4) # Laterales
        ]
        self.assertEqual(king.possible_moves(3, 3), expected_moves)

if __name__ == '__main__':
    unittest.main()