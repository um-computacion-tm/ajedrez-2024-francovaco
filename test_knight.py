import unittest
from knight import Knight

class TestKnight(unittest.TestCase):

    def test_str_method(self):
        '''
        The function test_str_method verifies that the __str__ method of the Knight class returns 'N' for a white piece and 'n' for a black piece.
        '''
        knight_white = Knight('WHITE')
        knight_black = Knight('BLACK')
        self.assertEqual(str(knight_white), 'N')
        self.assertEqual(str(knight_black), 'n')

    def test_generate_knight_directions(self):
        knight = Knight('WHITE')
        expected_directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        self.assertEqual(knight.generate_knight_directions(), expected_directions)

if __name__ == '__main__':
    unittest.main()