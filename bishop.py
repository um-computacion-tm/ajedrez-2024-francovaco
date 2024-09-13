from piece import Piece

class Bishop(Piece):

    # Letter representing the bishop on the board
    def __str__(self):
        '''
        The function returns the letter representing the bishop on the board.
        Functionality:
        It checks if the bishop's color is white.
        If it is white, it returns 'B'.
        Otherwise, it returns 'b'.
        '''
        return 'B' if self.__color__ == 'WHITE' else 'b'
    
    # Possible moves of the bishop
    def possible_moves(self, from_row, from_col):
        '''
        The function returns the possible moves of the bishop.
        Functionality:
        It creates a list with the directions in which the bishop can move.
        It calls the possible_moves_general function with the parameters from_row, from_col, directions.
        Parameters:
        from_row: Receives the row of the bishop's current position.
        from_col: Receives the column of the bishop's current position.
        '''
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self.possible_moves_general(from_row, from_col, directions)