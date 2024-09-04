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
        moves = []

        for direction in directions:
            new_row = from_row + direction[0]
            new_col = from_col + direction[1]      
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))          
        return moves