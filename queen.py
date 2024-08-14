from piece import Piece


class Queen(Piece):

    def __str__(self):
        return 'Q' if self.__color__ == 'WHITE' else 'q'