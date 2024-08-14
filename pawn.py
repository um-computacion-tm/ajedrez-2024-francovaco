from piece import Piece


class Pawn(Piece):
    
    def __str__(self):
        return 'P' if self.__color__ == 'WHITE' else 'p'