import unittest
from chess import Chess
from exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

class TestChess(unittest.TestCase):
    def test_init(self):
        '''
        The function test_init is a unit test method that verifies the correct initialization of a Chess object.
        The function ensures that when a new chess game is created, the initial turn is for the white pieces and the board is correctly initialized.
        '''
        game = Chess()
        self.assertEqual(game.turn, "WHITE")
        board = game.get_board()
        self.assertIsNotNone(board)

    def test_move_valid_pawn(self):
        '''
        The function test_move_valid_pawn verifies that a white pawn can move correctly on the chessboard.
        The function ensures that the new position of the pawn is not empty, indicating that the pawn has moved correctly to that position.
        '''
        game = Chess()
        game.move(6, 0, 4, 0)
        self.assertEqual(game.turn, "BLACK")
        self.assertEqual(game.get_board()[6][0], '.')
        self.assertIsNotNone(game.get_board()[4][0])

    def test_move_valid_knight(self):
        '''
        The function test_move_valid_knight is a unit test method that verifies that a knight can move correctly on the chessboard.
        The function ensures that the new position of the knight is not empty, indicating that the knight has moved correctly to that position.
        '''
        game = Chess()
        game.move(7, 1, 5, 2)
        self.assertEqual(game.turn, "BLACK")
        self.assertEqual(game.get_board()[7][1], '.')
        self.assertIsNotNone(game.get_board()[5][2])

    def test_move_no_piece1(self):
        '''
        The function test_move_no_piece1 is a unit test that verifies the behavior of the move method of the Chess class when there is no piece at the origin position.
        The function ensures that a NonPieceOriginError exception is raised with the message "There is no piece at the origin position."
        '''
        game = Chess()
        with self.assertRaises(NonPieceOriginError) as context:
            game.move(3, 3, 4, 3)
        self.assertEqual(str(context.exception), "There is no piece at the origin position.")

    def test_move_no_piece2(self):
        '''
        The function test_move_no_piece2 is a unit test that verifies the behavior of the move method of the Chess class when there is no piece at the origin position.
        The function ensures that a NonPieceOriginError exception is raised with the message "There is no piece at the origin position."
        '''
        game = Chess()
        with self.assertRaises(NonPieceOriginError) as context:
            game.move(3, 4, 4, 4)
        self.assertEqual(str(context.exception), "There is no piece at the origin position.")

    def test_move_turn_invalid(self):
        '''
        The function test_move_turn_invalid is a unit test that verifies the behavior of the move method of the Chess class when attempting to move a piece that does not belong to the player in turn.
        The function ensures that a WrongTurnError exception is raised with the message "It is not the turn of the selected piece."
        '''
        game = Chess()
        game.move(6, 0, 4, 0)
        with self.assertRaises(WrongTurnError) as context:
            game.move(6, 1, 5, 2)
        self.assertEqual(str(context.exception), "It is not the turn of the selected piece.")

    def test_move_invalid(self):
        '''
        The function test_move_invalid is a unit test that verifies the behavior of the move method of the Chess class when attempting to move a piece to an invalid position.
        The function ensures that an InvalidPieceMoveError exception is raised with the message "Invalid move for the selected piece."
        '''
        game = Chess()
        with self.assertRaises(InvalidPieceMoveError) as context:
            game.move(6, 0, 3, 0)
        self.assertEqual(str(context.exception), "Invalid move for the selected piece.")

    def test_change_turn(self):
        '''
        The function test_change_turn is a unit test that verifies that the change_turn method of the Chess class correctly changes the turn of the pieces.
        The function ensures that the change_turn method of the Chess class correctly changes the turn of the pieces after each valid move.
        '''
        game = Chess()
        game.move(6, 0, 4, 0)
        self.assertEqual(game.turn, "BLACK")
        game.move(1, 0, 3, 0)
        self.assertEqual(game.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()