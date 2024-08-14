from piece import Piece


class King(Piece):
    
    def __str__(self):
        return 'K' if self.__color__ == 'WHITE' else 'k'