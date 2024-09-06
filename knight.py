from piece import Piece

class Knight(Piece):

    __directions__ = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    # Letra que representa al caballo en el tablero
    def __str__(self):
        '''
        La función retorna la letra que representa al caballo en el tablero.
        Funcionamiento:
        Se verifica si el color del caballo es blanco.
        Si es blanco, retorna 'N'.
        Si no, retorna 'n'.
        '''
        return 'N' if self.__color__ == 'WHITE' else 'n'
    
    # Movimientos posibles del caballo
    def possible_moves(self, from_row, from_col):
        return super().possible_moves_general(from_row, from_col, self.__directions__)