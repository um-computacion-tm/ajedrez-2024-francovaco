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

if __name__ == '__main__':
    unittest.main()