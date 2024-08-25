import unittest
from chess import Chess  

class TestChess(unittest.TestCase):
    def test_init(self):
        game = Chess()
        self.assertEqual(game.turn, "WHITE")
        board = game.get_board()
        self.assertIsNotNone(board)

    def test_movimiento_valido_peon_blanco(self):
        game = Chess()
        game.move(6, 0, 4, 0)
        self.assertEqual(game.turn, "BLACK")
        self.assertEqual(game.get_board()[6][0], '.')
        self.assertIsNotNone(game.get_board()[4][0])

    def test_movimiento_valido_caballo(self):
        game = Chess()
        game.move(7, 1, 5, 2)
        self.assertEqual(game.turn, "BLACK")
        self.assertEqual(game.get_board()[7][1], '.')
        self.assertIsNotNone(game.get_board()[5][2])

    def test_movimiento_sin_pieza1(self):
        game = Chess()
        with self.assertRaises(ValueError) as context:
            game.move(3, 3, 4, 3)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen.")

    def test_movimiento_sin_pieza2(self):
        game = Chess()
        with self.assertRaises(ValueError) as context:
            game.move(3, 4, 4, 4)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen.")

    def test_movimiento_turno_erroneo(self):
        game = Chess()
        game.move(6, 0, 4, 0)
        with self.assertRaises(ValueError) as context:
            game.move(6, 1, 5, 2)
        self.assertEqual(str(context.exception), "No es el turno de la pieza seleccionada.")

    def test_movimiento_invalido(self):
        game = Chess()
        with self.assertRaises(ValueError) as context:
            game.move(6, 0, 3, 0)
        self.assertEqual(str(context.exception), "Movimiento no válido para la pieza seleccionada.")

    def test_cambio_de_turno(self):
        game = Chess()
        game.move(6, 0, 4, 0)
        self.assertEqual(game.turn, "BLACK")
        game.move(1, 0, 3, 0)
        self.assertEqual(game.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()    