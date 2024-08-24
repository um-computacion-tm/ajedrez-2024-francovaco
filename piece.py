class Piece:

    def __init__(self, color):
        '''
        Constructor de la clase
        Funcionamiento:
        Crea una instancia de la clase Piece 
        Atributos:
        color: Recibe el parametro color para crear el atributo __color__ del objeto
        '''
        self.__color__ = color

    def get_color(self):
        '''
        La función retorna el valor del atributo privado __color__ de la pieza.
        Funcionamiento:
        Retorna el valor del atributo __color__
        '''
        return self.__color__