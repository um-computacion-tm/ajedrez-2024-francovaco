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
        '''
        The function test_generate_knight_directions verifies that the generate_knight_directions method of the Knight class returns the correct list of directions for a knight piece.
        '''
        knight = Knight('WHITE')
        expected_directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        self.assertEqual(knight.generate_knight_directions(), expected_directions)



if __name__ == '__main__':
    unittest.main()