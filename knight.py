from piece import Piece

class Knight(Piece):

    #Letra que representa al caballo
    def __str__(self):
        return 'N' if self.__color__ == 'WHITE' else 'n'
    
    #Movimientos posibles del caballo
    def possible_moves(self, from_row, from_col):
        moves = []
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]  
        for direction in directions:
            new_row = from_row + direction[0]
            new_col = from_col + direction[1]
          
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))        
        return moves