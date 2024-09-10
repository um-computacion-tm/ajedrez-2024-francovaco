from piece import Piece

class Bishop(Piece):

    # Letra que representa al alfil en el tablero
    def __str__(self):
        '''
        La función retorna la letra que representa al alfil en el tablero.
        Funcionamiento:
        Se verifica si el color del alfil es blanco.
        Si es blanco, retorna 'B'.
        Si no, retorna 'b'.
        '''
        return 'B' if self.__color__ == 'WHITE' else 'b'
    
    # Movimientos posibles del alfil
    def possible_moves(self, from_row, from_col):
        '''
        La función retorna los movimientos posibles del alfil.
        Funcionamiento:
        Se crea una lista con las direcciones en las que se puede mover el alfil.   
        Se llama a la función possible_moves_general con los parámetros from_row, from_col, directions.
        Parámetros:
        from_row: Recibe la fila de la posición actual del alfil.
        from_col: Recibe la columna de la posición actual del alfil.
        '''
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return self.possible_moves_general(from_row, from_col, directions)