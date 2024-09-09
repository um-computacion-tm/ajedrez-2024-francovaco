import unittest
from bishop import Bishop

class TestBishop(unittest.TestCase):

    def test_str_method(self):
        '''
        La función test_str_method es una prueba unitaria que verifica que el método __str__ de la clase Bishop devuelva 'B' para una pieza blanca y 'b' para una pieza negra.
        '''
        bishop_white = Bishop('WHITE')
        bishop_black = Bishop('BLACK')
        self.assertEqual(str(bishop_white), 'B')
        self.assertEqual(str(bishop_black), 'b')

    def test_possible_moves_white(self):
        '''
        La función test_possible_moves es una prueba unitaria que verifica los movimientos posibles de un alfil desde el centro del tablero.
        Llama al método possible_moves de la clase Bishop con una fila y columna de origen y verifica que los movimientos devueltos sean los esperados.
        '''
        bishop = Bishop('WHITE')
        expected_moves = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(bishop.possible_moves(3, 3), expected_moves)

    def test_possible_moves_black(self):
        '''
        La función test_possible_moves_black es una prueba unitaria que verifica los movimientos posibles de un alfil negro desde el centro del tablero.
        Llama al método possible_moves de la clase Bishop con una fila y columna de origen y verifica que los movimientos devueltos sean los esperados.
        '''
        bishop = Bishop('BLACK')
        expected_moves = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(bishop.possible_moves(3, 3), expected_moves)

if __name__ == '__main__':
    unittest.main()