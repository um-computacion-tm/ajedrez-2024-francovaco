from piece import Piece

class Knight(Piece):

    #Letra que representa al caballo
    def __str__(self):
        '''
        La función retorna la letra que representa al caballo en el tablero.
        Funcionamiento:
        Se verifica si el color del caballo es blanco
        Si es blanco, retorna 'N'
        Si no, retorna 'n'
        '''
        return 'N' if self.__color__ == 'WHITE' else 'n'
    
    #Movimientos posibles del caballo
    def possible_moves(self, from_row, from_col):
        '''
        La función retorna una lista con las posiciones a las que el caballo puede moverse.
        Funcionamiento:
        Se crea una lista vacía llamada moves
        Se crea una lista llamada directions con las posiciones a las que el caballo puede moverse
        Se recorre la lista directions
        Se crea una variable new_row que almacena la suma de la posición de la fila actual y la fila de la dirección
        Se crea una variable new_col que almacena la suma de la posición de la columna actual y la columna de la dirección
        Se verifica si la nueva posición está dentro del tablero
        Se agrega la nueva posición a la lista moves
        Parametros:
        from_row: Recibe la fila de la posición actual del caballo
        from_col: Recibe la columna de la posición actual del caballo
        '''
        moves = []
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]  
        for direction in directions:
            new_row = from_row + direction[0]
            new_col = from_col + direction[1]
          
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))        
        return moves