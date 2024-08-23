from piece import Piece

class King(Piece):
    
    def __str__(self):
        return 'K' if self.__color__ == 'WHITE' else 'k'

    #Movimientos posibles del rey
    def possible_moves(self, from_row, from_col):
        moves = []
        directions = [
            (-1, -1), (-1, 1), (1, -1), (1, 1), 
            (-1, 0), (1, 0), (0, -1), (0, 1)    
        ]  
        for direction in directions:
            new_row = from_row + direction[0]
            new_col = from_col + direction[1]      
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))          
        return moves