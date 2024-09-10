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
        '''
        La función retorna los movimientos posibles de la torre.
        Funcionamiento:
        Se crea una lista con las direcciones en las que se puede mover la torre.
        Se llama a la función possible_moves_general con los parámetros from_row, from_col, self.__rook__directions__.
        Parámetros:
        from_row: Recibe la fila de la posición actual de la torre.
        from_col: Recibe la columna de la posición actual de la torre.
        '''
        directions = self.get_directions('rook')   
        return super().possible_moves_general(from_row, from_col, directions)