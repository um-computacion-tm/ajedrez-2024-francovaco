from piece import Piece


class Pawn(Piece):
    
    def __str__(self):
        return 'P' if self.__color__ == 'WHITE' else 'p'
    
    def possible_moves(self, row, col):
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