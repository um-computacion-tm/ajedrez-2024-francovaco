import unittest
from board import Board, GameOverException

class TestBoard(unittest.TestCase):
    def test_is_valid_move_no_piece(self):
        '''
        La función test_is_valid_move_no_piece es una prueba unitaria que verifica el comportamiento del método is_valid_move de la clase Board cuando no hay ninguna pieza en la posición de origen.
        La función asegura que el método is_valid_move de la clase Board retorna False cuando no hay ninguna pieza en la posición de origen.
        '''
        board = Board()
        self.assertFalse(board.is_valid_move(3, 3, 4, 4))

    def test_move_piece_no_piece(self):
        '''
        La función test_move_piece_no_piece es una prueba unitaria que verifica el comportamiento del método move_piece de la clase Board cuando se intenta mover una pieza desde una posición vacía.
        La función asegura que se lanza una excepción ValueError con el mensaje "No hay ninguna pieza en la posición de origen." cuando se intenta mover una pieza desde una posición vacía.
        '''
        board = Board()
        with self.assertRaises(ValueError) as context:
            board.move_piece(3, 3, 4, 4)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen.")

    def test_move_piece_capture_own_piece(self):
        '''
        La función test_move_piece_capture_own_piece es una prueba unitaria que verifica el comportamiento del método move_piece de la clase Board cuando se intenta capturar una pieza propia.
        La función asegura que se lanza una excepción ValueError con el mensaje "No puedes capturar tus propias piezas." cuando se intenta capturar una pieza propia.
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
        La función crea un tablero con una torre en la posición (0, 0) y un peón en la posición (0, 1). Luego, intenta mover la torre a la posición (0, 2) y verifica que se lanza un ValueError con el mensaje "No puedes pasar por encima de otras piezas.".
        '''
        board = Board()
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[0][0] = 'R'
        board.__positions__[0][1] = 'P'
        with self.assertRaises(ValueError) as context:
            board.move_piece(0, 0, 0, 2)
        self.assertEqual(str(context.exception), "No puedes pasar por encima de otras piezas.")

    def test_game_over_white_wins(self):
        '''
        La función test_game_over_white_wins verifica que se lanza una excepción GameOverException con el mensaje "Ha ganado el Blanco" cuando el negro se queda sin piezas.
        La función crea un tablero con una torre blanca en la posición (7, 7) llama al método check_game_over para chequear si el juego ha finalizado y lanza un GameOverException diciendo que ha ganado el blanco.
        '''
        board = Board()
        class Rook:
            def get_color(self):
                return 'WHITE'
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[7][7] = Rook()
        with self.assertRaises(GameOverException) as context:
            board.check_game_over()
        self.assertEqual(str(context.exception), "Ha ganado el Blanco")

    def test_game_over_black_wins(self):
        '''
        La función test_game_over_black_wins verifica que se lanza una excepción GameOverException con el mensaje "Ha ganado el Negro" cuando el blanco se queda sin piezas.
        La función crea un tablero con una torre negra en la posición (0, 0) llama al método check_game_over para chequear si el juego ha finalizado y lanza un GameOverException diciendo que ha ganado el negro.
        '''
        board = Board()
        class Rook:
            def get_color(self):
                return 'BLACK'  
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[0][0] = Rook()
        with self.assertRaises(GameOverException) as context:
            board.check_game_over()
        self.assertEqual(str(context.exception), "Ha ganado el Negro")

if __name__ == '__main__':
    unittest.main()