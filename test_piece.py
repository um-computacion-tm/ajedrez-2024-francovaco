import unittest
from piece import Piece

class TestPiece(unittest.TestCase):

    def test_piece_wite(self):
        '''
        La función test_piece_white es una prueba unitaria que verifica que el color de la pieza sea blanco.
        La función recibe el color de la pieza y crea una instancia de la clase Piece.
        '''
        color = 'WHITE'
        pieza = Piece(color)
        self.assertEqual(pieza.__color__, color)

    def test_piece_black(self):
        '''
        La función test_piece_black es una prueba unitaria que verifica que el color de la pieza sea negro.
        La función recibe el color de la pieza y crea una instancia de la clase Piece.
        '''
        color = 'BLACK'
        pieza = Piece(color)
        self.assertEqual(pieza.__color__, color)

    def test_get_color_white(self):
        '''
        La función test_get_color_white es una prueba unitaria que verifica que al crear una instancia de la clase pieza del color blanco la función get_color devuelva el color blanco. 
        '''
        piece = Piece("WHITE")
        self.assertEqual(piece.get_color(), "WHITE")
    
    def test_get_color_black(self):
        '''
        La función test_get_color_black es una prueba unitaria que verifica que al crear una instancia de la clase pieza del color negro la función get_color devuelva el color negro.
        '''
        piece = Piece("BLACK")
        self.assertEqual(piece.get_color(), "BLACK")

if __name__ == '__main__':
    unittest.main()
