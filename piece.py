class Piece:

    # Constructor de la clase
    def __init__(self, color):
        '''
        Constructor de la clase.
        Funcionamiento:
        Crea una instancia de la clase Piece .
        Parámetros:
        color: Recibe el parametro color para crear el atributo __color__ del objeto.
        '''
        self.__color__ = color

    # Obtener color de la pieza
    def get_color(self):
        '''
        La función retorna el valor del atributo privado __color__ de la pieza.
        Funcionamiento:
        Retorna el valor del atributo __color__.
        '''
        return self.__color__
    
    def possible_moves_general(self, from_row, from_col, directions):
        '''
        La función retorna una lista con las posiciones a las que el rey puede moverse.
        Funcionamiento:
        Se crea una lista vacía llamada moves.
        Se crea una lista llamada directions con las posiciones a las que el rey puede moverse.
        Se recorre la lista directions.
        Se crea una variable new_row que almacena la suma de la posición de la fila actual y la fila de la dirección.
        Se crea una variable new_col que almacena la suma de la posición de la columna actual y la columna de la dirección.
        Se verifica si la nueva posición está dentro del tablero.
        Se agrega la nueva posición a la lista moves.
        Parámetros:
        from_row: Recibe la fila de la posición actual del rey.
        from_col: Recibe la columna de la posición actual.
        '''
        moves = []

        for direction in directions:
            new_row = from_row + direction[0]
            new_col = from_col + direction[1]      
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))          
        return moves