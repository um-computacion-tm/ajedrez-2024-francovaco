from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

# La función show_board_with_icons() tiene como objetivo mostrar un tablero de ajedrez utilizando iconos para representar las piezas.
# Funcionamiento

# 1- Diccionario de Iconos:
# La función define un diccionario llamado piece_icons que mapea cada tipo de pieza de ajedrez (representada por un carácter) a su 
# correspondiente icono Unicode. Esto incluye tanto piezas blancas como negras, así como casillas vacías.

# 2- Mostrar el Tablero:
# La función itera sobre cada fila del tablero (board), y para cada fila, convierte cada pieza en su icono correspondiente utilizando el diccionario piece_icons.
# Luego, imprime cada fila del tablero con los iconos de las piezas separados por espacios.

# Atributos
# board: La función recibe un único parámetro llamado board, que es una lista de listas (matriz) donde cada sublista representa una fila del 
# tablero de ajedrez. Cada elemento de la sublista es un carácter que representa una pieza de ajedrez o una casilla vacía.

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

# La función play() se encarga de gestionar una jugada en una partida de ajedrez
# Funcionamiento
#1- Mostrar el Tablero y el Turno Actual:
# La función llama a show_board_with_icons(chess.get_board()) para mostrar el tablero de ajedrez actual utilizando iconos.
# Luego, imprime el turno actual (chess.turn).

# 2- Solicitar Coordenadas de Movimiento:
# La función solicita al usuario que ingrese las coordenadas de la pieza que desea mover (from_row y from_col) y las coordenadas de destino (to_row y to_col).

#3- Validar Entradas:
# Verifica que todas las entradas sean números utilizando el método isdigit().
# Si alguna entrada no es un número, lanza una excepción ValueError con el mensaje "Debe ingresar valores numéricos entre 0 y 7."

#4- Convertir Entradas a Enteros:
# Convierte las entradas de coordenadas de cadenas de texto a enteros.

#5- Validar Rango de Coordenadas:
# Verifica que todas las coordenadas estén en el rango permitido (0 a 7).
# Si alguna coordenada está fuera de este rango, lanza una excepción ValueError con el mensaje "Los valores de fila y columna deben estar entre 0 y 7."

# Atributos
# chess: La función recibe un único parámetro llamado chess, que es un objeto que represente el estado actual de la partida de ajedrez.

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
        chess.move(from_row, from_col, to_row, to_col)

    #Errores
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Error", e)


if __name__ == '__main__':
    main()