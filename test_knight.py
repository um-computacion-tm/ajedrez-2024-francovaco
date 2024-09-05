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

if __name__ == '__main__':
    unittest.main()