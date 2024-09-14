import unittest
from io import StringIO
from cli import play, show_board_with_icons, play, instructions_menu
from unittest.mock import patch, MagicMock

class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_exit_option(self, mock_print, mock_input):
        '''
        The function test_exit_option is a unit test that verifies how the exit option is handled in the main menu.
        '''
        with self.assertRaises(SystemExit):
            instructions_menu()
        mock_print.assert_any_call("Goodbye!")

    @patch('builtins.input', side_effect=['invalid', '2'])
    @patch('builtins.print')
    def test_invalid_option(self, mock_print, mock_input):
        '''
        The function test_invalid_option is a unit test that verifies how an invalid option is handled in the main menu.
        '''
        with self.assertRaises(SystemExit):
            instructions_menu()
        mock_print.assert_any_call("Invalid option. Please try again.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_with_icons(self, mock_stdout):
        '''
        The function test_show_board_with_icons is a unit test that verifies if the chessboard is correctly displayed with the piece icons.
        The function test_show_board_with_icons verifies that, when the function show_board_with_icons is called with a chessboard as an argument,
        the board is correctly printed with the piece icons. The parameter mock_stdout is a mock object that replaces the standard output during the test.
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

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['EXIT'])
    def test_exit_from_row(self, mock_input, mock_stdout):
        '''
        The function test_exit_from_row is a unit test that verifies how the "EXIT" input is handled in the chessboard.
        The function test_exit_from_row verifies that, when the user input is simulated with the value "EXIT" instead of the origin row coordinate,
        the program handles the input correctly without attempting to move any piece, displays the message "Game over." and ends the game.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Game over.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'EXIT'])
    def test_exit_from_col(self, mock_input, mock_stdout):
        '''
        The function test_exit_from_col is a unit test that verifies how the "EXIT" input is handled in the chessboard.
        The function test_exit_from_col verifies that, when the user input is simulated with the value "EXIT" instead of the origin column coordinate,
        the program handles the input correctly without attempting to move any piece, displays the message "Game over." and ends the game.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Game over.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '1', 'EXIT'])
    def test_exit_to_row(self, mock_input, mock_stdout):
        '''
        The function test_exit_to_row is a unit test that verifies how the "EXIT" input is handled in the chessboard.
        The function test_exit_to_row verifies that, when the user input is simulated with the value "EXIT" instead of the destination row coordinate,
        the program handles the input correctly without attempting to move any piece, displays the message "Game over." and ends the game.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Game over.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', '1', '2', 'EXIT'])
    def test_exit_to_col(self, mock_input, mock_stdout):
        '''
        The function test_exit_to_col is a unit test that verifies how the "EXIT" input is handled in the chessboard.
        The function test_exit_to_col verifies that, when the user input is simulated with the value "EXIT" instead of the destination column coordinate,
        the program handles the input correctly without attempting to move any piece, displays the message "Game over." and ends the game.
        '''
        chess = MagicMock()
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Game over.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6', '0', '4', '0', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_valid_move_pawn(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        '''
        The function test_valid_move_pawn is a unit test that verifies if a valid move on the chessboard is handled correctly.
        The function test_valid_move_pawn verifies that, when the user input is simulated to move a chess piece from position (row, column)
        to position (row, column), the move method of the chess object is called with the correct parameters. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        chess.move.assert_called_with(6, 0, 4, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '1', '5', '0', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_valid_move_knight1(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        '''
        The function test_valid_move_knight1 is a unit test that verifies if a valid knight move on the chessboard is handled correctly.
        The function test_valid_move_knight1 verifies that, when the user input is simulated to move a knight piece from position (7, 1)
        to position (5, 0), the move method of the chess object is called with the correct parameters. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        chess.move.assert_called_with(7, 1, 5, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '1', '5', '2', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_valid_move_knight2(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        chess.move.assert_called_with(7, 1, 5, 2)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['a', '0', '1', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_non_numeric_coordinates_from_row(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        '''
        The function test_non_numeric_coordinates_from_row is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        The function test_non_numeric_coordinates_from_row verifies that, when the user input is simulated with a non-numeric value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', 'a', '1', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_non_numeric_coordinates_from_col(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        '''
        The function test_non_numeric_coordinates_from_col is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        The function test_non_numeric_coordinates_from_col verifies that, when the user input is simulated with a non-numeric value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', '0', 'a', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_non_numeric_coordinates_to_row(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        '''
        The function test_non_numeric_coordinates_to_row is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        The function test_non_numeric_coordinates_to_row verifies that, when the user input is simulated with a non-numeric value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0', '0', '1', 'a', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('builtins.exit', side_effect=SystemExit)
    def test_non_numeric_coordinates_to_col(self, mock_exit, mock_show_board, mock_input, mock_stdout):
        '''
        The function test_non_numeric_coordinates_to_col is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        The function test_non_numeric_coordinates_to_col verifies that, when the user input is simulated with a non-numeric value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['&', '0', '1', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_symbol_coordinates_from_row(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_symbol_coordinates_from_row is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '&', '1', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_symbol_coordinates_from_col(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_symbol_coordinates_from_col is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '&', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_symbol_coordinates_to_row(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_symbol_coordinates_to_row is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        The function test_symbol_coordinates_to_row verifies that, when the user input is simulated with a non-numeric value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', '&', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_symbol_coordinates_to_col(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_symbol_coordinates_to_col is a unit test that verifies how an invalid non-numeric input is handled on the chessboard.
        The function test_symbol_coordinates_to_col verifies that, when the user input is simulated with a non-numeric value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '8', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_out_of_range_coordinates_to_row(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_out_of_range_coordinates_to_row is a unit test that verifies how an out-of-range input is handled on the chessboard.
        The function test_out_of_range_coordinates_to_row verifies that, when the user input is simulated with an out-of-range value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Row and column values must be between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['9', '0', '1', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_out_of_range_coordinates_from_row(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_out_of_range_coordinates_from_row is a unit test that verifies how an out-of-range input is handled on the chessboard.
        The function test_out_of_range_coordinates_from_row verifies that, when the user input is simulated with an out-of-range value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Row and column values must be between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '9', '1', '1', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_out_of_range_coordinates_from_col(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_out_of_range_coordinates_from_col is a unit test that verifies how an out-of-range input is handled on the chessboard.
        The function test_out_of_range_coordinates_from_col verifies that, when the user input is simulated with an out-of-range value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Row and column values must be between 0 and 7.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['0', '0', '1', '12', 'EXIT'])
    @patch('cli.show_board_with_icons')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.exit', side_effect=SystemExit)
    def test_out_of_range_coordinates_to_col(self, mock_exit, mock_stdout, mock_show_board, mock_input):
        '''
        The function test_out_of_range_coordinates_to_col is a unit test that verifies how an out-of-range input is handled on the chessboard.
        The function test_out_of_range_coordinates_to_col verifies that, when the user input is simulated with an out-of-range value,
        the program handles the incorrect input appropriately without attempting to move any piece and displays the error. The parameters mock_show_board and mock_input
        are mock objects that replace the real functions during the test.
        '''
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        with self.assertRaises(SystemExit):
            play(chess)
        self.assertIn("Row and column values must be between 0 and 7.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()