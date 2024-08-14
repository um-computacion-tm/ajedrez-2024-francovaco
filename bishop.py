from piece import Piece


class Bishop(Piece):

    def __str__(self):
        return 'B' if self.__color__ == 'WHITE' else 'b'