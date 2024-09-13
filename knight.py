from piece import Piece

class Knight(Piece):

    # Letter representing the knight on the board
    def __str__(self):
        '''
        The function returns the letter representing the knight on the board.
        Functionality:
        It checks if the knight's color is white.
        If it is white, it returns 'N'.
        Otherwise, it returns 'n'.
        '''
        return 'N' if self.__color__ == 'WHITE' else 'n'  
    
    # Generate possible directions for the knight
    def generate_knight_directions(self):
        '''
        The function returns a list with the directions in which the knight can move.
        Functionality:
        It creates an empty list called directions.
        It creates a list with the values 2, 1, -1, -2.
        It iterates over the list of values.
        It checks if the absolute value of i is different from the absolute value of j.
        It adds the direction to the directions list.
        It returns the directions list.
        '''
        directions = []
        moves = [2, 1, -1, -2]
        for i in moves:
            for j in moves:
                if abs(i) != abs(j):
                    directions.append((i, j))
        return directions

    # Possible moves of the knight
    def possible_moves(self, from_row, from_col):
        '''
        The function returns the possible moves of the knight.
        Functionality:
        It creates a list with the directions in which the knight can move.
        It calls the possible_moves_general function with the parameters from_row, from_col, directions.
        Parameters:
        from_row: Receives the row of the knight's current position.
        from_col: Receives the column of the knight's current position.
        '''
        directions = self.generate_knight_directions()
        return super().possible_moves_general(from_row, from_col, directions)