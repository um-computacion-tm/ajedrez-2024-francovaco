from piece import Piece


class Knight(Piece):
    
    def __str__(self):
        return 'N' if self.__color__ == 'WHITE' else 'n'