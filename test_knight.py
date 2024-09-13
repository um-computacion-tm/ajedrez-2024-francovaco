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

if __name__ == '__main__':
    unittest.main()