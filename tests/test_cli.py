import unittest
from io import StringIO
import sys 
sys.path.append('../game')
from cli import play
from unittest.mock import patch, MagicMock

class TestCLI(unittest.TestCase):

    # La función test_movimiento_valido es una prueba unitaria que verifica si un movimiento válido en el tablero de ajedrez se maneja correctamente.
    # La función test_movimiento_valido verifica que, cuando se simula la entrada del usuario para mover una pieza de ajedrez desde la posición (0, 0) 
    # a la posición (1, 1), el método move del objeto chess se llama con los parámetros correctos. Los parámetros mock_show_board y mock_input son 
    # objetos simulados que reemplazan las funciones reales durante la prueba.

    @patch('builtins.input', side_effect=['0', '0', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_movimiento_valido(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        play(chess)
        chess.move.assert_called_with(0, 0, 1, 1)

    # La función test_coordenadas_no_numericas es una prueba unitaria que verifica cómo se maneja una entrada no numérica inválida en el tablero de ajedrez.
    # La función test_coordenadas_no_numericas verifica que, cuando se simula la entrada del usuario con un valor no numérico, 
    # el programa maneja la entrada incorrecta adecuadamente sin intentar mover ninguna pieza y mostrando el error. Los parámetros mock_show_board y mock_input son 
    # objetos simulados que reemplazan las funciones reales durante la prueba.

    @patch('builtins.input', side_effect=['a', '0', '1', '1'])
    @patch('cli.show_board_with_icons')
    def test_coordenadas_no_numericas(self, mock_show_board, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        captured_output = StringIO()
        sys.stdout = captured_output
        play(chess)
        sys.stdout = sys.__stdout__
        self.assertIn("Debe ingresar valores numéricos entre 0 y 7.", captured_output.getvalue())

    # La función test_coordenadas_fuera_de_rango es una prueba unitaria que verifica cómo se maneja una entrada fuera del rango válido en el tablero de ajedrez.
    # La función test_coordenadas_fuera_de_rango verifica que, cuando se simula la entrada del usuario con un valor fuera del rango permitido (0-7), 
    # el programa maneja la entrada incorrecta adecuadamente sin intentar mover ninguna pieza y mostrando el error. Los parámetros mock_show_board y mock_input son 
    # objetos simulados que reemplazan las funciones reales durante la prueba.

    @patch('builtins.input', side_effect=['0', '0', '8', '1'])
    @patch('cli.show_board_with_icons')
    def test_coordenadas_fuera_de_rango(self, mock_show_board, mock_input):
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