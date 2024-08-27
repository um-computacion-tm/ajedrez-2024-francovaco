import unittest
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

    def test_possible_moves_center(self):
        '''
        La función test_possible_moves_center es una prueba unitaria que verifica los movimientos posibles de una torre desde el centro del tablero.
        '''
        rook = Rook('WHITE')
        # Movimientos desde el centro del tablero (4, 4)
        expected_moves = [
            (3, 4), (2, 4), (1, 4), (0, 4),  # Vertical hacia arriba
            (5, 4), (6, 4), (7, 4),          # Vertical hacia abajo
            (4, 3), (4, 2), (4, 1), (4, 0),  # Horizontal hacia la izquierda
            (4, 5), (4, 6), (4, 7)           # Horizontal hacia la derecha
        ]
        self.assertCountEqual(rook.possible_moves(4, 4), expected_moves)

    def test_possible_moves_corner(self):
        '''
        La función test_possible_moves_corner es una prueba unitaria que verifica los movimientos posibles de una torre desde una esquina del tablero.
        '''
        rook = Rook('WHITE')
        # Movimientos desde la esquina superior izquierda (0, 0)
        expected_moves = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Vertical hacia abajo
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Horizontal hacia la derecha
        ]
        self.assertCountEqual(rook.possible_moves(0, 0), expected_moves)

    def test_possible_moves_edge(self):
        '''
        La función test_possible_moves_edge es una prueba unitaria que verifica los movimientos posibles de una torre desde el borde del tablero.
        '''
        rook = Rook('WHITE')
        # Movimientos desde el borde del tablero (0, 4)
        expected_moves = [
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),  # Vertical hacia abajo
            (0, 3), (0, 2), (0, 1), (0, 0),  # Horizontal hacia la izquierda
            (0, 5), (0, 6), (0, 7)           # Horizontal hacia la derecha
        ]
        self.assertCountEqual(rook.possible_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()