class Piece:
    
    # Class constructor
    def __init__(self, color):
        '''
        Class constructor.
        Functionality:
        Creates an instance of the Piece class.
        Parameters:
        color: Receives the color parameter to create the __color__ attribute of the object.
        ''' 
        self.__color__ = color
        self.__queen_king_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        
    # Get piece color
    def get_color(self):
        '''
        The function returns the value of the private attribute __color__ of the piece.
        Functionality:
        Returns the value of the __color__ attribute.
        '''
        return self.__color__

    # Possible moves of the pieces
    def possible_moves_general(self, from_row, from_col, directions, single_step=False):
        '''
        The function returns the possible moves of the piece.
        Functionality:
        Creates an empty list called moves.
        Iterates over the directions list.
        Creates a variable new_row and new_col with the values of from_row and from_col.
        Iterates over the directions list.
        Updates new_row and new_col.
        Checks if the new position is within the board.
        Adds the new position to the moves list.
        Checks if single_step is True.
        Parameters:
        from_row: Receives the row of the current position of the piece.
        from_col: Receives the column of the current position of the piece.
        directions: Receives a list with the possible movement directions.
        single_step: Receives a boolean value indicating if the piece can move only one position.
        '''
        moves = []
        for direction in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += direction[0]
                new_col += direction[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))
                    if single_step:
                        break
                else:
                    break
        return moves