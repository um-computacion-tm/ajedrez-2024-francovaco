from game.piece import Piece

class Pawn(Piece):
    
    def __str__(self):
        '''
        La función retorna la letra que representa al peón en el tablero.
        Funcionamiento:
        Se verifica si el color del peón es blanco.
        Si es blanco, retorna 'P'.
        Si no, retorna 'p'.
        '''
        return 'P' if self.__color__ == 'WHITE' else 'p'
    
    def possible_moves(self, row, col):
        '''
        La función retorna una lista con las posiciones a las que el peón puede moverse.
        Funcionamiento:
        Se crea una lista vacía llamada moves.
        Se crea una variable direction que almacena -1 si el color del peón es blanco.
        Se crea una variable start_row que almacena 6 si el color del peón es blanco.
        Se agrega la posición hacia adelante a la lista moves.
        Se agrega la posición hacia adelante a la lista moves si la posición es la inicial.
        Se agrega la posición diagonal izquierda a la lista moves.
        Se agrega la posición diagonal derecha a la lista moves.
        Parámetros:
        row: Recibe la fila de la posición actual del peón.
        col: Recibe la columna de la posición actual del peón.
        '''
        moves = []
        direction = -1 if self.__color__ == 'WHITE' else 1
        start_row = 6 if self.__color__ == 'WHITE' else 1

        # Movimiento hacia adelante
        moves.append((row + direction, col))
        if row == start_row:
            moves.append((row + 2 * direction, col))

        # Movimientos diagonales solo si no es la posición inicial
        if row != start_row:
            moves.append((row + direction, col - 1))
            moves.append((row + direction, col + 1))
        return moves