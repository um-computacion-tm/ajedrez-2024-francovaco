from chess import Chess
from exceptions import InvalidMove, OutOfBoundsError, NonNumericInputError, GameOverException

# Main function
def main():
    '''
    The function main() is the entry point of the program.
    '''
    chess = Chess()
    while True: 
        try:
            play(chess)
        except GameOverException as e:
            print(str(e))
            exit()

# Show board with icons
def show_board_with_icons(board):
    '''
    The function show_board_with_icons() aims to display a chessboard using icons to represent the pieces.
    Functionality:
    The function defines a dictionary called piece_icons that maps each type of chess piece (represented by a character) to its 
    corresponding Unicode icon. This includes both white and black pieces, as well as empty squares.
    The function iterates over each row of the board, and for each row, converts each piece to its corresponding icon using the piece_icons dictionary.
    Then, it prints each row of the board with the piece icons separated by spaces.
    Parameters:
    board: The function receives a single parameter called board, which is a list of lists (matrix) where each sublist represents a row of the 
    chessboard. Each element of the sublist is a character representing a chess piece or an empty square.
    '''
    # Dictionary of icons for the pieces
    piece_icons = {
        'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
        'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
        '.': '·'  # Empty square
    }
    # Replace letters with icons
    for row in board:
        print(' '.join(piece_icons[piece] for piece in row))

# Chess game
def play(chess):
    '''
    The function play() is responsible for managing a move in a chess game.
    Functionality:
    The function calls show_board_with_icons(chess.get_board()) to display the current chessboard using icons.
    Then, it prints the current turn (chess.turn).
    The function asks the user to enter the coordinates of the piece they want to move (from_row and from_col) and the destination coordinates (to_row and to_col).
    It checks that all inputs are numbers using the isdigit() method.
    If any input is not a number, it raises a ValueError with the message "You must enter numeric values between 0 and 7."
    It converts the coordinate inputs from strings to integers.
    It checks that all coordinates are within the allowed range (0 to 7).
    If any coordinate is out of this range, it raises a ValueError with the message "Row and column values must be between 0 and 7."
    Parameters:
    chess: The function receives a single parameter called chess, which is an object representing the current state of the chess game. 
    '''
    try: 
        # Display board and current turn and request coordinates
        show_board_with_icons(chess.get_board())
        print("Enter the coordinates of the piece you want to move and its destination.")
        print("Enter EXIT to end the game.")
        print("Turn:", chess.turn)
        from_row = input("From row: ")
        if from_row.upper() == "EXIT":
            print("Game over.")
            exit()
        from_col = input("From column: ")
        if from_col.upper() == "EXIT":
            print("Game over.")
            exit()
        to_row = input("To row: ")
        if to_row.upper() == "EXIT":
            print("Game over.")
            exit()
        to_col = input("To column: ")
        if to_col.upper() == "EXIT":
            print("Game over.")
            exit()
        # Validate that the coordinates are numbers
        if not (from_row.isdigit() and from_col.isdigit() and to_row.isdigit() and to_col.isdigit()):
            raise NonNumericInputError()      
        # Convert coordinates to integers
        from_row = int(from_row)
        from_col = int(from_col)
        to_row = int(to_row)
        to_col = int(to_col)
        # Validate that the coordinates are within the allowed range
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise OutOfBoundsError()       
        # Move the piece on the board
        chess.move(from_row, from_col, to_row, to_col)
    # Exceptions 
    except InvalidMove as e:
        print("Error:", e)

if __name__ == "__main__":
    main()