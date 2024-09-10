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
        '''
        La función retorna los movimientos posibles del rey.
        Funcionamiento:
        Se llama a la función possible_moves_general con los parámetros from_row, from_col, self.__queen__king__directions__, single_step=True.
        Parámetros:
        from_row: Recibe la fila de la posición actual del rey.
        from_col: Recibe la columna de la posición actual del rey.
        '''
        return super().possible_moves_general(from_row, from_col, self.__queen_king_directions__, single_step=True)