import unittest
from piece import Piece

class TestPiece(unittest.TestCase):

    def test_piece_wite(self):

        '''
        La función test_piece_white verifica que el color de la pieza sea blanco.
        La función recibe el color de la pieza y crea una instancia de la clase Piece.
        '''
        color = 'WHITE'
        pieza = Piece(color)
        self.assertEqual(pieza.__color__, color)

    def test_piece_black(self):

        '''
        La función test_piece_black verifica que el color de la pieza sea negro.
        La función recibe el color de la pieza y crea una instancia de la clase Piece.
        '''
        color = 'BLACK'
        pieza = Piece(color)
        self.assertEqual(pieza.__color__, color)
if __name__ == '__main__':
    unittest.main()