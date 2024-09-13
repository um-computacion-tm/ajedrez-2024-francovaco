import unittest
from piece import Piece

class TestPiece(unittest.TestCase):

    def test_piece_white(self):
        '''
        The function test_piece_white is a unit test that verifies that the color of the piece is white.
        The function receives the color of the piece and creates an instance of the Piece class.
        '''
        color = 'WHITE'
        piece = Piece(color)
        self.assertEqual(piece.__color__, color)

    def test_piece_black(self):
        '''
        The function test_piece_black is a unit test that verifies that the color of the piece is black.
        The function receives the color of the piece and creates an instance of the Piece class.
        '''
        color = 'BLACK'
        piece = Piece(color)
        self.assertEqual(piece.__color__, color)

    def test_get_color_white(self):
        '''
        The function test_get_color_white is a unit test that verifies that when creating an instance of the Piece class with the color white, the get_color function returns the color white.
        '''
        piece = Piece("WHITE")
        self.assertEqual(piece.get_color(), "WHITE")
    
    def test_get_color_black(self):
        '''
        The function test_get_color_black is a unit test that verifies that when creating an instance of the Piece class with the color black, the get_color function returns the color black.
        '''
        piece = Piece("BLACK")
        self.assertEqual(piece.get_color(), "BLACK")
        
if __name__ == '__main__':
    unittest.main()