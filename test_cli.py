import unittest
import sys
from io import StringIO
from cli import play, show_board_with_icons
from unittest.mock import patch, MagicMock

class TestCli(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_with_icons(self, mock_stdout):
        '''
        La función test_show_board_with_icons es una prueba unitaria que verifica si el tablero de ajedrez se muestra correctamente con los iconos de las piezas.
        La función test_show_board_with_icons verifica que, cuando se llama a la función show_board_with_icons con un tablero de ajedrez como argumento, 
        el tablero se imprime correctamente con los iconos de las piezas. El parámetro mock_stdout es un objeto simulado que reemplaza la salida estándar durante la prueba.
        '''
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        show_board_with_icons(board)
        expected_output = (
            '♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n'
            '♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n'
            '♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['SALIR'])
    @patch('builtins.print')
    def test_exit_from_row(self, mock_print, mock_input):
        '''
        La función test_salir es una prueba unitaria que verifica cómo se maneja la entrada "SALIR" en el tablero de ajedrez.
        La función test_salir verifica que, cuando se simula la entrada del usuario con el valor "SALIR" en lugar de la cooerdenada de la fila origen, 
        el programa maneja la entrada correctamente sin intentar mover ninguna pieza, muestra el mensaje "Juego terminado." y finaliza el juego. 
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        mock_print.assert_called_with("Juego terminado.")

    @patch('builtins.input', side_effect=['1', 'SALIR'])
    @patch('builtins.print')
    def test_exit_from_col(self, mock_print, mock_input):
        '''
        La función test_salir es una prueba unitaria que verifica cómo se maneja la entrada "SALIR" en el tablero de ajedrez.
        La función test_salir verifica que, cuando se simula la entrada del usuario con el valor "SALIR" en lugar de la cooerdenada de la columna origen,
        el programa maneja la entrada correctamente sin intentar mover ninguna pieza, muestra el mensaje "Juego terminado." y finaliza el juego.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        mock_print.assert_called_with("Juego terminado.")

    @patch('builtins.input', side_effect=['1', '1', 'SALIR'])
    @patch('builtins.print')
    def test_exit_to_row(self, mock_print, mock_input):
        '''
        La función test_salir es una prueba unitaria que verifica cómo se maneja la entrada "SALIR" en el tablero de ajedrez.
        La función test_salir verifica que, cuando se simula la entrada del usuario con el valor "SALIR" en lugar de la cooerdenada de la fila destino,
        el programa maneja la entrada correctamente sin intentar mover ninguna pieza, muestra el mensaje "Juego terminado." y finaliza el juego.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        mock_print.assert_called_with("Juego terminado.")

    @patch('builtins.input', side_effect=['1', '1', '2', 'SALIR'])
    @patch('builtins.print')
    def test_exit_to_col(self, mock_print, mock_input):
        '''
        La función test_salir es una prueba unitaria que verifica cómo se maneja la entrada "SALIR" en el tablero de ajedrez.
        La función test_salir verifica que, cuando se simula la entrada del usuario con el valor "SALIR" en lugar de la cooerdenada de la columna destino,
        el programa maneja la entrada correctamente sin intentar mover ninguna pieza, muestra el mensaje "Juego terminado." y finaliza el juego.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        mock_print.assert_called_with("Juego terminado.")

    @patch('builtins.input', side_effect=['6', '0', '4', '0'])
    @patch('cli.show_board_with_icons')
    def test_valid_move_pawn(self, mock_show_board, mock_input):
        '''
        La función test_movimiento_valido es una prueba unitaria que verifica si un movimiento válido en el tablero de ajedrez se maneja correctamente.
        La función test_movimiento_valido verifica que, cuando se simula la entrada del usuario para mover una pieza de ajedrez desde la posición (fils, columna) 
        a la posición (fila, columna), el método move del objeto chess se llama con los parámetros correctos. Los parámetros mock_show_board y mock_input son 
        objetos simulados que reemplazan las funciones reales durante la prueba.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        play(chess)
        chess.move.assert_called_with(6, 0, 4, 0)

    @patch('builtins.input', side_effect=['7', '1', '5', '0'])
    @patch('cli.show_board_with_icons')
    def test_valid_move_knight1(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        play(chess)
        chess.move.assert_called_with(7, 1, 5, 0)

    @patch('builtins.input', side_effect=['7', '1', '5', '2'])
    @patch('cli.show_board_with_icons')
    def test_valid_move_knight2(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        play(chess)
        chess.move.assert_called_with(7, 1, 5, 2)

    @patch('builtins.input', side_effect=['a', '0', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_non_numeric_coordinates_from_row(self, mock_show_board, mock_input):
        '''
        La función test_coordenadas_no_numericas es una prueba unitaria que verifica cómo se maneja una entrada no numérica inválida en el tablero de ajedrez.
        La función test_coordenadas_no_numericas verifica que, cuando se simula la entrada del usuario con un valor no numérico, 
        el programa maneja la entrada incorrecta adecuadamente sin intentar mover ninguna pieza y mostrando el error. Los parámetros mock_show_board y mock_input son 
        objetos simulados que reemplazan las funciones reales durante la prueba.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())
    
    @patch('builtins.input', side_effect=['0', 'a', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_non_numeric_coordinates_from_col(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '0', 'a', '1'])
    @patch('cli.show_board_with_icons')
    def test_non_numeric_coordinates_to_row(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', 'a'])
    @patch('cli.show_board_with_icons')
    def test_non_numeric_coordinates_to_col(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['&', '0', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_symbol_coordinates_from_row(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())
    
    @patch('builtins.input', side_effect=['0', '&', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_symbol_coordinates_from_col(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '&', '1'])
    @patch('cli.show_board_with_icons')
    def test_symbol_coordinates_to_row(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', '&'])
    @patch('cli.show_board_with_icons')
    def test_symbol_coordinates_to_col(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '8', '1'])
    @patch('cli.show_board_with_icons')
    def test_out_of_range_coordinates_to_row(self, mock_show_board, mock_input):
        '''
        La función test_coordenadas_fuera_de_rango es una prueba unitaria que verifica cómo se maneja una entrada fuera del rango válido en el tablero de ajedrez.
        La función test_coordenadas_fuera_de_rango verifica que, cuando se simula la entrada del usuario con un valor fuera del rango permitido (0-7), 
        el programa maneja la entrada incorrecta adecuadamente sin intentar mover ninguna pieza y mostrando el error. Los parámetros mock_show_board y mock_input son 
        objetos simulados que reemplazan las funciones reales durante la prueba.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Los valores de fila y columna deben estar entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['9', '0', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_out_of_range_coordinates_from_row(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Los valores de fila y columna deben estar entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '9', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_out_of_range_coordinates_from_col(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Los valores de fila y columna deben estar entre 0 y 7.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', '12'])
    @patch('cli.show_board_with_icons')
    def test_out_of_range_coordinates_to_col(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Los valores de fila y columna deben estar entre 0 y 7.", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()