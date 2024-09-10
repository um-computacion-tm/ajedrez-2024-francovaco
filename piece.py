class Piece:
    
    # Constructor de la clase
    def __init__(self, color):
        '''
        Constructor de la clase.
        Funcionamiento:
        Crea una instancia de la clase Piece.
        Parámetros:
        color: Recibe el parametro color para crear el atributo __color__ del objeto.
        ''' 
        self.__color__ = color
        self.__queen_king_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        
    # Obtener color de la pieza
    def get_color(self):
        '''
        La función retorna el valor del atributo privado __color__ de la pieza.
        Funcionamiento:
        Retorna el valor del atributo __color__.
        '''
        return self.__color__

    # Movimientos posibles de las piezas
    def possible_moves_general(self, from_row, from_col, directions, single_step=False):
        '''
        La función retorna los movimientos posibles de la pieza.
        Funcionamiento:
        Se crea una lista vacía llamada moves.
        Se recorre la lista directions.
        Se crea una variable new_row y new_col con los valores de from_row y from_col.
        Se recorre la lista directions.
        Se actualiza new_row y new_col.
        Se verifica si la nueva posición está dentro del tablero.
        Se agrega la nueva posición a la lista moves.
        Se verifica si single_step es True.
        Parámetros:
        from_row: Recibe la fila de la posición actual de la pieza.
        from_col: Recibe la columna de la posición actual de la pieza.
        directions: Recibe una lista con las direcciones posibles de movimiento.
        single_step: Recibe un valor booleano que indica si la pieza puede moverse una sola posición.
        '''
        moves = []
        for direction in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += direction[0]
                new_col += direction[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))
                    if single_step:
                        break
                else:
                    break
        return moves