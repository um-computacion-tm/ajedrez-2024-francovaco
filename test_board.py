import unittest
from board import Board, GameOverException

class TestBoard(unittest.TestCase):
    def test_is_valid_move_no_piece(self):
        '''
        La función test_is_valid_move_no_piece es una prueba unitaria que verifica el comportamiento del método is_valid_move de la clase Board cuando no hay ninguna pieza en la posición de origen.
        '''
        board = Board()
        self.assertFalse(board.is_valid_move(3, 3, 4, 4))

    def test_move_piece_no_piece(self):
        '''
        La función test_move_piece_no_piece es una prueba unitaria que verifica el comportamiento del método move_piece de la clase Board cuando se intenta mover una pieza desde una posición vacía.
        '''
        board = Board()
        with self.assertRaises(ValueError) as context:
            board.move_piece(3, 3, 4, 4)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen.")

    def test_move_piece_capture_own_piece(self):
        '''
        La función test_move_piece_capture_own_piece es una prueba unitaria que verifica el comportamiento del método move_piece de la clase Board cuando se intenta capturar una pieza propia.
        '''
        board = Board()
        board.board = [[None for _ in range(8)] for _ in range(8)]
        board.board[7][0] = 'R'
        board.board[6][0] = 'P' 
        with self.assertRaises(ValueError) as context:
            board.move_piece(7, 0, 6, 0)
        self.assertEqual(str(context.exception), "No puedes capturar tus propias piezas.")

    def test_move_piece_over_other(self):
        '''
        La función test_move_piece_raises_value_error verifica que se lanza un ValueError con el mensaje "No puedes pasar por encima de otras piezas." cuando una pieza intenta moverse a través de otra.
        '''
        board = Board()
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[0][0] = 'P'
        board.__positions__[0][1] = 'P'
        with self.assertRaises(ValueError) as context:
            board.move_piece(0, 0, 0, 2)
        self.assertEqual(str(context.exception), "No puedes pasar por encima de otras piezas.")

    def test_game_over_exception_message(self):
        message = "Ha ganado el Blanco"
        exception = GameOverException(message)
        self.assertEqual(exception.__message__, message)
        self.assertEqual(str(exception), message)

if __name__ == '__main__':
    unittest.main()