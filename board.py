from rook import Rook
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight

class Board:
    def __init__(self):
        self.__positions__ = []

        # Matriz de 8x8
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        # Torres
        self.__positions__[0][0] = Rook("BLACK") 
        self.__positions__[0][7] = Rook("BLACK") 
        self.__positions__[7][7] = Rook("WHITE") 
        self.__positions__[7][0] = Rook("WHITE")

        # Peones 
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")

        # Caballos
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")  
        self.__positions__[7][6] = Knight("WHITE")

        # Alfiles
        self.__positions__[0][2] = Bishop("BLACK")  
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        # Reinas
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        # Reyes
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    # Obtener tablero
    def get_board(self):
        for row in self.__positions__:
            return [[str(piece) if piece is not None else '.' for piece in row] for row in self.__positions__]

    # Obtener piezas
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    # Obtener color de la pieza
    def get_piece_color(self, row, col):
        piece = self.get_piece(row, col)
        if piece is not None:
            return piece.get_color()
        return None

    # Validar movimiento
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            return False
        
        possible_moves = piece.possible_moves(from_row, from_col)
        return (to_row, to_col) in possible_moves

    # Mover pieza
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None

    # Iterador
    def iter(self):
        return iter(self.__positions__)