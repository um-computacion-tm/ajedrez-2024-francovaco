from piece import Piece

class Rook(Piece):

    # Letra que representa a la torre en el tablero
    def __str__(self):
        '''
        La función retorna la letra que representa a la torre en el tablero.
        Funcionamiento:
        Se verifica si el color de la torre es blanco.
        Si es blanco, retorna 'R'.
        Si no, retorna 'r'.
        '''
        return 'R' if self.__color__ == 'WHITE' else 'r'
    
    # Movimientos posibles de la torre
    def possible_moves(self, from_row, from_col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
        return super().possible_moves_general(from_row, from_col, directions)