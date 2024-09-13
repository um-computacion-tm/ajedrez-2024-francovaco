from piece import Piece

class Pawn(Piece):
    
    # Letter representing the pawn on the board
    def __str__(self):
        '''
        The function returns the letter representing the pawn on the board.
        Functionality:
        It checks if the pawn's color is white.
        If it is white, it returns 'P'.
        Otherwise, it returns 'p'.
        '''
        return 'P' if self.__color__ == 'WHITE' else 'p'
    
    # Possible moves of the pawn
    def possible_moves(self, row, col):
        '''
        The function returns a list with the positions the pawn can move to.
        Functionality:
        It creates an empty list called moves.
        It creates a variable direction that stores -1 if the pawn's color is white.
        It creates a variable start_row that stores 6 if the pawn's color is white.
        It adds the forward position to the moves list.
        It adds the forward position to the moves list if the position is the initial one.
        It adds the diagonal left position to the moves list.
        It adds the diagonal right position to the moves list.
        Parameters:
        row: Receives the row of the pawn's current position.
        col: Receives the column of the pawn's current position.
        '''
        moves = []
        direction = -1 if self.__color__ == 'WHITE' else 1
        start_row = 6 if self.__color__ == 'WHITE' else 1

        # Forward move
        moves.append((row + direction, col))
        if row == start_row:
            moves.append((row + 2 * direction, col))

        # Diagonal moves only if not in the initial position
        if row != start_row:
            moves.append((row + direction, col - 1))
            moves.append((row + direction, col + 1))
        return moves