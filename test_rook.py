import unittest
from unittest.mock import MagicMock
from rook import Rook

class TestRook(unittest.TestCase):

    def test_str_method(self):
        '''
        La función test_str_method es una prueba unitaria que verifica que el método __str__ de la clase Rook devuelva 'R' para una pieza blanca y 'r' para una pieza negra.
        '''
        rook_white = Rook('WHITE')
        rook_black = Rook('BLACK')
        self.assertEqual(str(rook_white), 'R')
        self.assertEqual(str(rook_black), 'r')

    def test_possible_moves_white(self):
        '''
        La función test_possible_moves es una prueba unitaria que verifica los movimientos posibles de una torre desde el centro del tablero.
        Llama al método possible_moves de la clase Rook con una fila y columna de origen y verifica que los movimientos devueltos sean los esperados.
        '''
        rook = Rook('WHITE')
        from_row, from_col = 4, 4
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        result = rook.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

    def test_possible_moves_black(self):
        '''
        La función test_possible_moves es una prueba unitaria que verifica los movimientos posibles de una torre desde el centro del tablero.
        Llama al método possible_moves de la clase Rook con una fila y columna de origen y verifica que los movimientos devueltos sean los esperados.
        '''
        rook = Rook('BLACK')
        from_row, from_col = 4, 4
        expected_moves = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        result = rook.possible_moves(from_row, from_col)
        self.assertEqual(sorted(result), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()