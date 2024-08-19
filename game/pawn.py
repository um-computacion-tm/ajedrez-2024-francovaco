from piece import Piece


class Pawn(Piece):
    
    def __str__(self):
        return 'P' if self.__color__ == 'WHITE' else 'p'
    
    def possible_moves(self, from_row, from_col):
        moves = []
        direction = -1 if self.__color__ == 'WHITE' else 1
        start_row = 6 if self.__color__ == 'WHITE' else 1
        
        # Movimiento hacia adelante
        new_row = from_row + direction
        if 0 <= new_row < 8:
            moves.append((new_row, from_col))
            if from_row == start_row:
                new_row += direction
                if 0 <= new_row < 8:
                    moves.append((new_row, from_col))
        
        # Movimiento diagonal
        for col_offset in [-1, 1]:
            new_col = from_col + col_offset
            if 0 <= new_col < 8 and 0 <= new_row < 8:
                moves.append((new_row, new_col))
        
        return moves