from piece import Piece

class Queen(Piece):

    # Letra que representa a la reina en el tablero
    def __str__(self):
        '''
        La función retorna la letra que representa a la reina en el tablero.
        Funcionamiento:
        Se verifica si el color de la reina es blanco.
        Si es blanco, retorna 'Q'.
        Si no, retorna 'q'.
        '''
        return 'Q' if self.__color__ == 'WHITE' else 'q'
    
    #Movimientos posibles de la reina
    def possible_moves(self, from_row, from_col):
        return self.possible_moves_general(from_row, from_col, self.__queen_king_directions__)