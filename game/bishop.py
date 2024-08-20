from game.piece import Piece


class Bishop(Piece):

    def __str__(self):
        return 'B' if self.__color__ == 'WHITE' else 'b'
    
    #Movimientos posibles del alfil
    def possible_moves(self, from_row, from_col):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 
        
        for direction in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += direction[0]
                new_col += direction[1]
                
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))
                else:
                    break
              
        return moves