from piece import Piece

class Queen(Piece):

    # Letter representing the queen on the board
    def __str__(self):
        '''
        The function returns the letter representing the queen on the board.
        Functionality:
        It checks if the queen's color is white.
        If it is white, it returns 'Q'.
        Otherwise, it returns 'q'.
        '''
        return 'Q' if self.__color__ == 'WHITE' else 'q'
    
    # Possible moves of the queen
    def possible_moves(self, from_row, from_col):
        '''
        The function returns the possible moves of the queen.
        Functionality:
        It calls the possible_moves_general function with the parameters from_row, from_col, self.__queen_king_directions__.
        Parameters:
        from_row: Receives the row of the queen's current position.
        from_col: Receives the column of the queen's current position.
        '''
        return self.possible_moves_general(from_row, from_col, self.__queen_king_directions__)