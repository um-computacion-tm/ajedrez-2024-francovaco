from game.piece import Piece

class Rook(Piece):

    def __str__(self):
        '''
        La función retorna la letra que representa a la torre en el tablero.
        Funcionamiento:
        Se verifica si el color de la torre es blanco.
        Si es blanco, retorna 'R'.
        Si no, retorna 'r'.
        '''
        return 'R' if self.__color__ == 'WHITE' else 'r'
    
    #Movimientos posibles de la torre
    def possible_moves(self, from_row, from_col):
        '''
        La función retorna una lista con las posiciones a las que la torre puede moverse.
        Funcionamiento:
        Se crea una lista vacía llamada moves.
        Se crea una lista llamada directions con las posiciones a las que la torre puede moverse.
        Se recorre la lista directions.
        Se crea una variable new_row que almacena la suma de la posición de la fila actual y la fila de la dirección.
        Se crea una variable new_col que almacena la suma de la posición de la columna actual y la columna de la dirección.
        Se verifica si la nueva posición está dentro del tablero.
        Se agrega la nueva posición a la lista moves.
        Parámetros:
        from_row: Recibe la fila de la posición actual de la torre.
        from_col: Recibe la columna de la posición actual de la torre.
        '''
        moves = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1) 
        ]
        for direction in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += direction[0]
                new_col += direction[1]   
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))
                else:
                    break     
        return moves