from piece import Piece

class King(Piece):

    # Letra que representa al rey en el tablero
    def __str__(self):
        '''
        La función retorna la letra que representa al rey en el tablero.
        Funcionamiento:
        Se verifica si el color del rey es blanco.
        Si es blanco, retorna 'K'.
        Si no, retorna 'k'.
        '''
        return 'K' if self.__color__ == 'WHITE' else 'k'
    
    # Movimientos posibles del rey
    def possible_moves(self, from_row, from_col):
        directions = [
            (-1, -1), (-1, 1), (1, -1), (1, 1), 
            (-1, 0), (1, 0), (0, -1), (0, 1)    
        ]          
        return super().possible_moves_general(from_row, from_col, directions)