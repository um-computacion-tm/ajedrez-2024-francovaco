from rook import Rook
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from exceptions import GameOverException, NonCaptureOwnPieceError, NonPassOverPieceError, NonCaptureForwardError

class Board:
    # Initialize board
    def __init__(self):
        '''
        The function creates an instance of the Board class.
        Functionality:
        The function creates the private attribute __positions__ which is an 8x8 matrix.
        The function places the pieces in their initial positions on the board.
        '''
        self.__positions__ = []

        # 8x8 matrix
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        # Rooks
        self.__positions__[0][0] = Rook("BLACK") 
        self.__positions__[0][7] = Rook("BLACK") 
        self.__positions__[7][7] = Rook("WHITE") 
        self.__positions__[7][0] = Rook("WHITE")

        # Pawns
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")

        # Knights
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")  
        self.__positions__[7][6] = Knight("WHITE")

        # Bishops
        self.__positions__[0][2] = Bishop("BLACK")  
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        # Queens
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        # Kings
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    # Get board
    def get_board(self):
        '''
        The function returns the game board.
        Functionality:
        The function iterates through the positions matrix and creates a new matrix with the representations of the pieces on the board.
        Returns the new matrix with the representations of the pieces on the board.
        '''
        for row in self.__positions__:
            return [[str(piece) if piece is not None else '.' for piece in row] for row in self.__positions__]

    # Get piece
    def get_piece(self, row, col):
        '''
        The function gets the piece at the given position.
        Functionality:
        The function returns the piece at the given position.
        Parameters:
        row: Receives the row of the position.
        col: Receives the column of the position.
        '''
        return self.__positions__[row][col]
    
    # Get piece color
    def get_piece_color(self, row, col):
        '''
        The function gets the color of the piece at the given position.
        Functionality:
        The function gets the piece at the given position and returns the color of the piece.
        Parameters:
        row: Receives the row of the position.
        col: Receives the column of the position.
        '''
        piece = self.get_piece(row, col)
        if piece is not None:
            return piece.get_color()
        return None

    # Validate move
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        '''
        The function checks if a move is valid.
        Functionality:
        The function gets the piece at the origin position.
        The function gets the possible moves of the piece at the origin position.
        The function checks if the destination position is in the possible moves of the piece.
        Returns True if the move is valid, False otherwise.
        Parameters:
        from_row: Receives the row of the origin position.
        from_col: Receives the column of the origin position.
        to_row: Receives the row of the destination position.
        to_col: Receives the column of the destination position.
        '''
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            return False
        possible_moves = piece.possible_moves(from_row, from_col)
        return (to_row, to_col) in possible_moves

    # Move piece
    def move_piece(self, from_row, from_col, to_row, to_col):
        '''
        The function moves a piece on the board.
        Functionality:
        The function gets the piece at the origin position.
        The function checks if there is a piece at the origin position.
        The function checks if the piece at the destination position is the same color as the piece at the origin position.
        The function checks if there are pieces in the way.
        The function moves the piece to the destination position.
        The function checks if the game is over.
        Parameters:
        from_row: Receives the row of the origin position.
        from_col: Receives the column of the origin position.
        to_row: Receives the row of the destination position.
        to_col: Receives the column of the destination position.
        '''
        piece = self.__positions__[from_row][from_col]
        target_piece = self.__positions__[to_row][to_col]
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise NonCaptureOwnPieceError()

        # Check if there are pieces in the way
        if not self.is_path_clear(from_row, from_col, to_row, to_col):
            raise NonPassOverPieceError()

        # Check if the pawn tries to capture forward
        if isinstance(piece, Pawn):
            direction = -1 if piece.get_color() == 'WHITE' else 1
            if to_row == from_row + direction and to_col == from_col and target_piece is not None:
                raise NonCaptureForwardError()

        # Move the piece
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None

        # Check if the game is over
        self.check_game_over()

    # Check if the path is clear
    def is_path_clear(self, from_row, from_col, to_row, to_col):
        '''
        The function checks if the path between the origin position and the destination position is clear.
        Functionality:
        The function gets the piece at the origin position.
        The function checks if the piece is a knight.
        The function calculates the step in rows and columns.
        The function iterates through the intermediate positions between the origin position and the destination position.
        The function checks if there is a piece at the intermediate position.
        The function returns True if the path is clear, False otherwise.
        Parameters:
        from_row: Receives the row of the origin position.
        from_col: Receives the column of the origin position.
        to_row: Receives the row of the destination position.
        to_col: Receives the column of the destination position.
        '''
        piece = self.__positions__[from_row][from_col]
        
        # Check if the piece is a knight
        if piece is not None and piece.__str__() == 'n' or piece.__str__() == 'N':
            return True
        row_step = 1 if to_row > from_row else -1 if to_row < from_row else 0
        col_step = 1 if to_col > from_col else -1 if to_col < from_col else 0
        current_row, current_col = from_row + row_step, from_col + col_step
        while current_row != to_row or current_col != to_col:
            if self.__positions__[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step
        return True

    # Check game over
    def check_game_over(self):
        '''
        The function checks if the game is over.
        Functionality:
        The function counts the number of white and black pieces on the board.
        The function raises a GameOverException with the message "White wins" if there are no black pieces on the board.
        The function raises a GameOverException with the message "Black wins" if there are no white pieces on the board.
        '''
        white_pieces = 0
        black_pieces = 0
        for row in self.__positions__:
            for piece in row:
                if piece is not None:
                    if piece.get_color() == 'WHITE':
                        white_pieces += 1
                    elif piece.get_color() == 'BLACK':
                        black_pieces += 1
        if white_pieces == 0:
            raise GameOverException("Black wins")
        elif black_pieces == 0:
            raise GameOverException("White wins")