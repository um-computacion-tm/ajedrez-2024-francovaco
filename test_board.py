import unittest
from board import Board
from exceptions import NonPieceOriginError, NonCaptureOwnPieceError, NonPassOverPieceError, GameOverException

class TestBoard(unittest.TestCase):
    def test_is_valid_move_no_piece(self):
        '''
        The function test_is_valid_move_no_piece is a unit test that verifies the behavior of the is_valid_move method of the Board class when there is no piece at the origin position.
        The function ensures that the is_valid_move method of the Board class returns False when there is no piece at the origin position.
        '''
        board = Board()
        self.assertFalse(board.is_valid_move(3, 3, 4, 4))

    def test_move_piece_capture_own_piece(self):
        '''
        The function test_move_piece_capture_own_piece is a unit test that verifies the behavior of the move_piece method of the Board class when attempting to capture one's own piece.
        The function ensures that a NonCaptureOwnPieceError exception is raised with the message "You cannot capture your own pieces." when attempting to capture one's own piece.
        '''
        board = Board()
        board.board = [[None for _ in range(8)] for _ in range(8)]
        board.board[7][0] = 'R'
        board.board[6][0] = 'P' 
        with self.assertRaises(NonCaptureOwnPieceError) as context:
            board.move_piece(7, 0, 6, 0)
        self.assertEqual(str(context.exception), "You cannot capture your own pieces.")

    def test_move_piece_over_other(self):
        '''
        The function test_move_piece_raises_value_error verifies that a NonPassOverPieceError is raised with the message "You cannot pass over other pieces." when a piece attempts to move through another.
        The function creates a board with a rook at position (0, 0) and a pawn at position (0, 1). Then, it attempts to move the rook to position (0, 2) and verifies that a NonPassOverPieceError is raised with the message "You cannot pass over other pieces."
        '''
        board = Board()
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[0][0] = 'R'
        board.__positions__[0][1] = 'P'
        with self.assertRaises(NonPassOverPieceError) as context:
            board.move_piece(0, 0, 0, 2)
        self.assertEqual(str(context.exception), "You cannot pass over other pieces.")

    def test_game_over_white_wins(self):
        '''
        The function test_game_over_white_wins verifies that a GameOverException is raised with the message "White wins" when black has no pieces left.
        The function creates a board with a white rook at position (7, 7), calls the check_game_over method to check if the game has ended, and raises a GameOverException saying that white has won.
        '''
        board = Board()
        class Rook:
            def get_color(self):
                return 'WHITE'
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[7][7] = Rook()
        with self.assertRaises(GameOverException) as context:
            board.check_game_over()
        self.assertEqual(str(context.exception), "White wins")

    def test_game_over_black_wins(self):
        '''
        The function test_game_over_black_wins verifies that a GameOverException is raised with the message "Black wins" when white has no pieces left.
        The function creates a board with a black rook at position (0, 0), calls the check_game_over method to check if the game has ended, and raises a GameOverException saying that black has won.
        '''
        board = Board()
        class Rook:
            def get_color(self):
                return 'BLACK'  
        board.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        board.__positions__[0][0] = Rook()
        with self.assertRaises(GameOverException) as context:
            board.check_game_over()
        self.assertEqual(str(context.exception), "Black wins")

if __name__ == '__main__':
    unittest.main()