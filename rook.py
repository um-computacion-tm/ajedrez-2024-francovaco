from piece import Piece


class Rook(Piece):

    def __str__(self):
        return 'R' if self.__color__ == 'WHITE' else 'r'