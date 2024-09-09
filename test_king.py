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

    def test_possible_moves_white(self):
        '''
        La función test_possible_moves es una prueba unitaria que verifica los movimientos posibles de un rey desde el centro del tablero.
        Llama al método possible_moves de la clase King con una fila y columna de origen y verifica que los movimientos devueltos sean los esperados.
        '''
        king = King('WHITE')
        from_row, from_col = 4, 4
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        result = king.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

    def test_possible_moves_black(self):
        '''
        La función test_possible_moves_black es una prueba unitaria que verifica los movimientos posibles de un rey negro desde el centro del tablero.
        Llama al método possible_moves de la clase King con una fila y columna de origen y verifica que los movimientos devueltos sean los esperados.
        '''
        king = King('BLACK')
        from_row, from_col = 4, 4
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        result = king.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()