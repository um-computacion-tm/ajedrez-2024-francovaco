from board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def get_board(self):
        return self.__board__.get_board()
        
    def move(self, from_row, from_col, to_row, to_col):
        
        # Obtener el color de la pieza en la posición de origen
        piece_color = self.__board__.get_piece_color(from_row, from_col)
        if piece_color is None:
            raise ValueError("No hay ninguna pieza en la posición de origen.")
        
        # Verificar que la pieza pertenece al jugador actual
        if piece_color != self.__turn__:
            raise ValueError("No es el turno de la pieza seleccionada.")
        
        # Verificar que el movimiento es válido y mover la pieza
        if not self.__board__.is_valid_move(from_row, from_col, to_row, to_col):
            raise ValueError("Movimiento no válido para la pieza seleccionada.")
        
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        
        # Cambiar el turno
        self.change_turn()        
   
    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE" 