from game.board import Board, GameOverException


class Chess:
    def __init__(self):
        '''
        La función crea una instancia de la clase Chess.
        Funcionamiento:
        La función crea el atributo privado __board__ de la clase Board.
        La función crea el atributo privado __turn__ que indica el turno del jugador.
        '''
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def get_board(self):
        '''
        La función retorna el tablero del juego.
        Funcionamiento:
        Retorna el tablero del juego.
        '''
        return self.__board__.get_board()
        
    def move(self, from_row, from_col, to_row, to_col):
        '''
        La función mueve una pieza del tablero.
        Funcionamiento:
        Se obtiene el color de la pieza en la posición de origen.
        Se verifica que haya una pieza en la posición de origen.
        Se verifica que la pieza pertenezca al jugador actual.
        Se verifica que el movimiento sea válido y se mueve la pieza.
        Se cambia el turno.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición de destino.
        to_col: Recibe la columna de la posición de destino.
        '''
        try:
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

        except GameOverException as e:
            raise e    
   
    @property
    def turn(self):
        '''
        La función retorna el turno del jugador.
        Funcionamiento:
        Retorna el valor del atributo __turn__.
        '''
        return self.__turn__

    def change_turn(self):
        '''
        La función cambia el turno del jugador.
        Funcionamiento:
        Se verifica si el turno es blanco.
        Si es blanco, se cambia a negro.
        Si no se cambia a blanco.
        '''
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE" 