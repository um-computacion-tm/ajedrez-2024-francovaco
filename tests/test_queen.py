import unittest
from game.queen import Queen

class TestQueen(unittest.TestCase):

    def test_str_method(self):
        '''
        La función test_str_method es una prueba unitaria que verifica que el método __str__ de la clase Queen devuelva 'Q' para una pieza blanca y 'q' para una pieza negra.
        '''
        queen_white = Queen('WHITE')
        queen_black = Queen('BLACK')
        self.assertEqual(str(queen_white), 'Q')
        self.assertEqual(str(queen_black), 'q')

    def test_possible_moves_center(self):
        '''
        La función test_possible_moves_center es una prueba unitaria que verifica los movimientos posibles de una reina desde el centro del tablero.
        '''
        queen = Queen('WHITE')
        # Movimientos desde el centro del tablero (4, 4)
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal superior derecha
            (5, 3), (6, 2), (7, 1),          # Diagonal inferior izquierda
            (5, 5), (6, 6), (7, 7),          # Diagonal inferior derecha
            (3, 4), (2, 4), (1, 4), (0, 4),  # Vertical hacia arriba
            (5, 4), (6, 4), (7, 4),          # Vertical hacia abajo
            (4, 3), (4, 2), (4, 1), (4, 0),  # Horizontal hacia la izquierda
            (4, 5), (4, 6), (4, 7)           # Horizontal hacia la derecha
        ]
        self.assertCountEqual(queen.possible_moves(4, 4), expected_moves)

    def test_possible_moves_corner(self):
        '''
        La función test_possible_moves_corner es una prueba unitaria que verifica los movimientos posibles de una reina desde una esquina del tablero.
        '''
        queen = Queen('WHITE')
        # Movimientos desde la esquina superior izquierda (0, 0)
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),  # Diagonal inferior derecha
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Vertical hacia abajo
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Horizontal hacia la derecha
        ]
        self.assertCountEqual(queen.possible_moves(0, 0), expected_moves)

    def test_possible_moves_edge(self):
        '''
        La función test_possible_moves_edge es una prueba unitaria que verifica los movimientos posibles de una reina desde el borde del tablero.
        '''
        queen = Queen('WHITE')
        # Movimientos desde el borde del tablero (0, 4)
        expected_moves = [
            (1, 3), (2, 2), (3, 1), (4, 0),  # Diagonal inferior izquierda
            (1, 5), (2, 6), (3, 7),          # Diagonal inferior derecha
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),  # Vertical hacia abajo
            (0, 3), (0, 2), (0, 1), (0, 0),  # Horizontal hacia la izquierda
            (0, 5), (0, 6), (0, 7)           # Horizontal hacia la derecha
        ]
        self.assertCountEqual(queen.possible_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()