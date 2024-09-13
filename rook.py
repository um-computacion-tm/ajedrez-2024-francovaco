from piece import Piece

class Rook(Piece):

    # Letter representing the rook on the board
    def __str__(self):
        '''
        The function returns the letter representing the rook on the board.
        Functionality:
        It checks if the rook's color is white.
        If it is white, it returns 'R'.
        Otherwise, it returns 'r'.
        '''
        return 'R' if self.__color__ == 'WHITE' else 'r'
    
    # Possible moves of the rook
    def possible_moves(self, from_row, from_col):
        '''
        The function returns the possible moves of the rook.
        Functionality:
        It creates a list with the directions in which the rook can move.
        It calls the possible_moves_general function with the parameters from_row, from_col, self.__rook__directions__.
        Parameters:
        from_row: Receives the row of the rook's current position.
        from_col: Receives the column of the rook's current position.
        '''
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
        return super().possible_moves_general(from_row, from_col, directions)