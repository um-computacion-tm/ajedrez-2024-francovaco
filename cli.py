from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def show_board_with_icons(board):
    piece_icons = {
        'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
        'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
        '.': '·'  #Casillas vacias
    }
    for row in board:
        print(' '.join(piece_icons[piece] for piece in row))

def play(chess):
    try:
        show_board_with_icons(chess.get_board())
        print("Turno: ", chess.turn)
        from_row = int(input("Desde fila: "))
        from_col = int(input("Desde columna: "))
        to_row = int(input("A fila: "))
        to_col = int(input("A columna: "))
        
        chess.move( from_row, from_col, to_row, to_col)
    except Exception as e:
        print("Error", e)



if __name__ == '__main__':
    main()