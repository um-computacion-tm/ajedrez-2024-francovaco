from piece import Piece

class Knight(Piece):

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
        '''
        La función retorna los movimientos posibles del caballo.
        Funcionamiento:
        Se crea una lista con las direcciones en las que se puede mover el caballo.
        Se llama a la función possible_moves_general con los parámetros from_row, from_col, directions.
        Parámetros:
        from_row: Recibe la fila de la posición actual del caballo.
        from_col: Recibe la columna de la posición actual
        '''
        
        return super().possible_moves_general(from_row, from_col, Piece.knight_directions)