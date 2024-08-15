from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def show_board_with_icons(board):
    # Diccionario de iconos para las piezas
    piece_icons = {
        'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
        'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
        '.': '·'  #Casillas vacias
    }

    # Mostrar tablero con los iconos
    for row in board:
        print(' '.join(piece_icons[piece] for piece in row))

def play(chess):
    try:
        # Mostrar tablero y turno actual y pedir coordenadas
        show_board_with_icons(chess.get_board())
        print("Turno: ", chess.turn)
        from_row = input("Desde fila: ")
        from_col = input("Desde columna: ")
        to_row = input("A fila: ")
        to_col = input("A columna: ")

        # Validar que las entradas sean números
        if not (from_row.isdigit() and from_col.isdigit() and to_row.isdigit() and to_col.isdigit()):
            raise ValueError("Debe ingresar valores numéricos entre 0 y 7.")
        
        from_row = int(from_row)
        from_col = int(from_col)
        to_row = int(to_row)
        to_col = int(to_col)

        # Validar que las entradas estén en el rango permitido
        if not (0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7):
            raise ValueError("Los valores de fila y columna deben estar entre 0 y 7.")
        
        # Mover la pieza
        chess.move( from_row, from_col, to_row, to_col)
    #Errores
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Error", e)


if __name__ == '__main__':
    main()