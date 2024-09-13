from piece import Piece

class King(Piece):

    # Letter representing the king on the board
    def __str__(self):
        '''
        The function returns the letter representing the king on the board.
        Functionality:
        It checks if the king's color is white.
        If it is white, it returns 'K'.
        Otherwise, it returns 'k'.
        '''
        return 'K' if self.__color__ == 'WHITE' else 'k'
    
    # Possible moves of the king
    def possible_moves(self, from_row, from_col):
        '''
        The function returns the possible moves of the king.
        Functionality:
        It calls the possible_moves_general function with the parameters from_row, from_col, self.__queen__king__directions__, single_step=True.
        Parameters:
        from_row: Receives the row of the king's current position.
        from_col: Receives the column of the king's current position.
        '''
        return super().possible_moves_general(from_row, from_col, self.__queen_king_directions__, single_step=True)