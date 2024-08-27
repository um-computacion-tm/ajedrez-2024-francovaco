import unittest
from chess import Chess  

class TestChess(unittest.TestCase):
    def test_init(self):
        '''
        La función test_init es un método de prueba unitaria que verifica la correcta inicialización de un objeto de la clase Chess. 
        La función asegura que al crear un nuevo juego de ajedrez, el turno inicial es de las piezas blancas y el tablero está correctamente inicializado.
        '''
        game = Chess()
        self.assertEqual(game.turn, "WHITE")
        board = game.get_board()
        self.assertIsNotNone(board)

    def test_move_valid_pawn(self):
        '''
        La función test_move_valid_pawn verifica que un peón blanco puede moverse correctamente en el tablero de ajedrez.
        La función asegura que la nueva posición del peón no esté vacía, lo que indica que el peón se ha movido correctamente a esa posición.
        '''
        game = Chess()
        game.move(6, 0, 4, 0)
        self.assertEqual(game.turn, "BLACK")
        self.assertEqual(game.get_board()[6][0], '.')
        self.assertIsNotNone(game.get_board()[4][0])

    def test_move_valid_knight(self):
        '''
        La función test_move_valid_knight es un método de prueba unitaria que verifica que un caballo puede moverse correctamente en el tablero de ajedrez.
        La función asegura que la nueva posición del caballo no esté vacía, lo que indica que el caballo se ha movido correctamente a esa posición.
        '''
        game = Chess()
        game.move(7, 1, 5, 2)
        self.assertEqual(game.turn, "BLACK")
        self.assertEqual(game.get_board()[7][1], '.')
        self.assertIsNotNone(game.get_board()[5][2])

    def test_move_no_piece1(self):
        '''
        La función test_move_no_piece1 es una prueba unitaria que verifica el comportamiento del método move de la clase Chess cuando no hay ninguna pieza en la posición de origen.
        La función asegura que se lanza una excepción ValueError con el mensaje "No hay ninguna pieza en la posición de origen.".
        '''
        game = Chess()
        with self.assertRaises(ValueError) as context:
            game.move(3, 3, 4, 3)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen.")

    def test_move_no_piece2(self):
        '''
        La función test_move_no_piece2 es una prueba unitaria que verifica el comportamiento del método move de la clase Chess cuando no hay ninguna pieza en la posición de origen.
        La función asegura que se lanza una excepción ValueError con el mensaje "No hay ninguna pieza en la posición de origen.".
        '''
        game = Chess()
        with self.assertRaises(ValueError) as context:
            game.move(3, 4, 4, 4)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen.")

    def test_move_turn_invalid(self):
        '''
        La función test_move_turn_invalid es una prueba unitaria que verifica el comportamiento del método move de la clase Chess cuando se intenta mover una pieza que no pertenece al jugador en turno.
        La función asegura que se lanza una excepción ValueError con el mensaje "No es el turno de la pieza seleccionada.".
        '''
        game = Chess()
        game.move(6, 0, 4, 0)
        with self.assertRaises(ValueError) as context:
            game.move(6, 1, 5, 2)
        self.assertEqual(str(context.exception), "No es el turno de la pieza seleccionada.")

    def test_move_invalid(self):
        '''
        La función test_move_invalid es una prueba unitaria que verifica el comportamiento del método move de la clase Chess cuando se intenta mover una pieza a una posición no válida.
        La función asegura que se lanza una excepción ValueError con el mensaje "Movimiento no válido para la pieza seleccionada
        '''
        game = Chess()
        with self.assertRaises(ValueError) as context:
            game.move(6, 0, 3, 0)
        self.assertEqual(str(context.exception), "Movimiento no válido para la pieza seleccionada.")

    def test_change_turn(self):
        '''
        La función test_change_turn es una prueba unitaria que verifica que el método change_turn de la clase Chess cambia el turno de las piezas correctamente.
        La función asegura que el método change_turn de la clase Chess cambia el turno de las piezas correctamente después de cada movimiento válido.
        '''
        game = Chess()
        game.move(6, 0, 4, 0)
        self.assertEqual(game.turn, "BLACK")
        game.move(1, 0, 3, 0)
        self.assertEqual(game.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()    