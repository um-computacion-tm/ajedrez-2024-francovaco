import unittest
from knight import Knight

class TestKnight(unittest.TestCase):

    def test_str_method(self):
        '''
        La función test_str_method verifica que el método __str__ de la clase Knight devuelva 'N' para una pieza blanca y 'n' para una pieza negra.
        '''
        knight_white = Knight('WHITE')
        knight_black = Knight('BLACK')
        self.assertEqual(str(knight_white), 'N')
        self.assertEqual(str(knight_black), 'n')

    def test_possible_moves_center(self):
        '''
        La función test_possible_moves_center es una prueba unitaria que verifica los movimientos posibles de un caballo desde el centro del tablero.
        '''
        knight = Knight('WHITE')
        # Movimientos desde el centro del tablero (4, 4)
        expected_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2) 
        ]
        self.assertCountEqual(knight.possible_moves(4, 4), expected_moves)

    def test_possible_moves_corner(self):
        '''
        La función test_possible_moves_corner es una prueba unitaria que verifica los movimientos posibles de un caballo desde una esquina del tablero.
        '''
        knight = Knight('WHITE')
        # Movimientos desde la esquina superior izquierda (0, 0)
        expected_moves = [(2, 1), (1, 2)]
        self.assertCountEqual(knight.possible_moves(0, 0), expected_moves)

    def test_possible_moves_edge(self):
        '''
        La función test_possible_moves_edge es una prueba unitaria que verifica los movimientos posibles de un caballo desde el borde del tablero.
        '''
        knight = Knight('WHITE')
        # Movimientos desde el borde del tablero (0, 4)
        expected_moves = [(2, 5), (2, 3), (1, 6), (1, 2)] 
        self.assertCountEqual(knight.possible_moves(0, 4), expected_moves)

if __name__ == '__main__':
    unittest.main()