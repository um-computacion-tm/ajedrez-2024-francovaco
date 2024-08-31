from rook import Rook
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight

class Board:
    # Inicializar tablero
    def __init__(self):
        '''
        La función crea una instancia de la clase Board.
        Funcionamiento:
        La función crea el atributo privado __positions__ que es una matriz de 8x8.
        La función coloca las piezas en sus posiciones iniciales en el tablero.
        '''
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
        '''
        La función retorna el tablero del juego.
        Funcionamiento:
        La función recorre la matriz de posiciones y crea una nueva matriz con las representaciones de las piezas en el tablero.
        Retorna la nueva matriz con las representaciones de las piezas en el tablero.
        '''
        for row in self.__positions__:
            return [[str(piece) if piece is not None else '.' for piece in row] for row in self.__positions__]

    # Obtener piezas
    def get_piece(self, row, col):
        '''
        La función obtiene la pieza en la posición dada.
        Funcionamiento:
        La función retorna la pieza en la posición dada.
        Parámetros:
        row: Recibe la fila de la posición.
        col: Recibe la columna de la posición.
        '''
        return self.__positions__[row][col]
    
    # Obtener color de la pieza
    def get_piece_color(self, row, col):
        '''
        La función obtiene el color de la pieza en la posición dada.
        Funcionamiento:
        La función obtiene la pieza en la posición dada y retorna el color de la pieza.
        Parámetros:
        row: Recibe la fila de la posición.
        col: Recibe la columna de la posición.
        '''
        piece = self.get_piece(row, col)
        if piece is not None:
            return piece.get_color()
        return None

    # Validar movimiento
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        '''
        La función verifica si un movimiento es válido.
        Funcionamiento:
        La función obtiene la pieza en la posición de origen.
        La función obtiene los posibles movimientos de la pieza en la posición de origen.
        La función verifica si la posición de destino está en los posibles movimientos de la pieza.
        Retorna True si el movimiento es válido, False en caso contrario.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición de destino.
        to_col: Recibe la columna de la posición de destino.
        '''
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            return False
        possible_moves = piece.possible_moves(from_row, from_col)
        return (to_row, to_col) in possible_moves

    # Mover pieza
    def move_piece(self, from_row, from_col, to_row, to_col):
        '''
        La función mueve una pieza en el tablero.
        Funcionamiento:
        La función obtiene la pieza en la posición de origen.
        La función verifica si hay una pieza en la posición de origen.
        La función verifica si la pieza en la posición de destino es del mismo color que la pieza en la posición de origen.
        La función verifica si hay piezas en el camino.
        La función mueve la pieza a la posición de destino.
        La función verifica si el juego ha terminado.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición de destino.
        to_col: Recibe la columna de la posición de destino.
        '''
        piece = self.__positions__[from_row][from_col]
        if piece is None:
            raise ValueError("No hay ninguna pieza en la posición de origen.")
        target_piece = self.__positions__[to_row][to_col]
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise ValueError("No puedes capturar tus propias piezas.")

        # Verificar si hay piezas en el camino
        if not self.is_path_clear(from_row, from_col, to_row, to_col):
            raise ValueError("No puedes pasar por encima de otras piezas.")

        # Mover la pieza
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None

        # Verificar si el juego ha terminado
        self.check_game_over()

    def is_path_clear(self, from_row, from_col, to_row, to_col):
        '''
        La función verifica si el camino entre la posición de origen y la posición de destino está libre.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición de destino.
        to_col: Recibe la columna de la posición de destino.
        Retorna:
        True si el camino está libre, False en caso contrario.
        '''
        piece = self.__positions__[from_row][from_col]
        
        # Verificar si la pieza es un caballo
        if piece is not None and piece.__str__() == 'n' or piece.__str__() == 'N':
            return True

        row_step = 1 if to_row > from_row else -1 if to_row < from_row else 0
        col_step = 1 if to_col > from_col else -1 if to_col < from_col else 0

        current_row, current_col = from_row + row_step, from_col + col_step
        while current_row != to_row or current_col != to_col:
            if self.__positions__[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step

        return True

    def check_game_over(self):
        '''
        La función verifica si el juego ha terminado.
        Funcionamiento:
        La función cuenta el número de piezas blancas y negras en el tablero.
        La función lanza una excepción GameOverException con el mensaje "Ha ganado el Blanco" si no hay piezas negras en el tablero.
        La función lanza una excepción GameOverException con el mensaje "Ha ganado el Negro" si no hay piezas blancas en el tablero.
        '''
        white_pieces = 0
        black_pieces = 0
        for row in self.__positions__:
            for piece in row:
                if piece is not None:
                    if piece.get_color() == 'WHITE':
                        white_pieces += 1
                    elif piece.get_color() == 'BLACK':
                        black_pieces += 1
        if white_pieces == 0:
            raise GameOverException("Ha ganado el Negro")
        elif black_pieces == 0:
            raise GameOverException("Ha ganado el Blanco")

class GameOverException(Exception):
    def __init__(self, message):
        '''
        La función __init__ es el constructor de la excepción GameOverException.
        Inicializa la excepción con un mensaje específico.
        Parámetros:
        message: Un mensaje de tipo str que describe la razón por la cual se lanza la excepción.
        '''
        self.__message__ = message
        super().__init__(self.__message__)