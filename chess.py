from board import Board
from exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError, GameOverException

class Chess:
    # Initialize game
    def __init__(self):
        '''
        The function creates an instance of the Chess class.
        Functionality:
        The function creates the private attribute __board__ of the Board class.
        The function creates the private attribute __turn__ which indicates the player's turn.
        '''
        # Create board
        self.__board__ = Board()
        # Create turn
        self.__turn__ = "WHITE"

    # Get board
    def get_board(self):
        '''
        The function returns the game board.
        Functionality:
        Returns the game board.
        '''
        return self.__board__.get_board()

    # Move piece    
    def move(self, from_row, from_col, to_row, to_col):
        '''
        The function moves a piece on the board.
        Functionality:
        Gets the color of the piece at the origin position.
        Checks if there is a piece at the origin position.
        Checks if the piece belongs to the current player.
        Checks if the move is valid and moves the piece.
        Changes the turn.
        Parameters:
        from_row: Receives the row of the origin position.
        from_col: Receives the column of the origin position.
        to_row: Receives the row of the destination position.
        to_col: Receives the column of the destination position.
        '''
        try:
            # Get the color of the piece at the origin position
            piece_color = self.__board__.get_piece_color(from_row, from_col)
            if piece_color is None:
                raise NonPieceOriginError()
            
            # Check that the piece belongs to the current player
            if piece_color != self.__turn__:
                raise WrongTurnError()
            
            # Check that the move is valid and move the piece
            if not self.__board__.is_valid_move(from_row, from_col, to_row, to_col):
                raise InvalidPieceMoveError()
            
            self.__board__.move_piece(from_row, from_col, to_row, to_col)
            
            # Change turn
            self.change_turn()    

        except GameOverException as e:
            raise e    
   
    # Get turn
    @property
    def turn(self):
        '''
        The function returns the player's turn.
        Functionality:
        Returns the value of the __turn__ attribute.
        '''
        return self.__turn__

    # Change turn
    def change_turn(self):
        '''
        The function changes the player's turn.
        Functionality:
        Checks if the turn is white.
        If it is white, it changes to black.
        If not, it changes to white.
        '''
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE" 