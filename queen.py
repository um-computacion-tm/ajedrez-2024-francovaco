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
        '''
        La función retorna los movimientos posibles de la reina.
        Funcionamiento:
        Se llama a la función possible_moves_general con los parámetros from_row, from_col, self.__queen__king__directions__.
        Parámetros:
        from_row: Recibe la fila de la posición actual de la reina.
        from_col: Recibe la columna de la posición actual de la reina.
        '''
        return self.possible_moves_general(from_row, from_col, self.__queen_king_directions__)