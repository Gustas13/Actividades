from algoritmos import distancia_euclidiana
class Particula:
    def __init__(self, id, origen_x, origen_y,destino_x, destino_y, velocidad, red, green, blue, distancia):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x,origen_y,destino_x,destino_y)
 
    def __str__(self):
        return (
            'ID: ' + self.__id + '\n' +
            'Origen en X: ' + self.__origen_x + '\n' +
            'Origen en Y: ' + self.__origen_y + '\n' +
            'Destino en X: ' + self.__destino_x + '\n'
            'Destino en Y: ' + self.__destino_y + '\n' +
            'Velocidad: ' + self.__velocidad + '\n' +
            'Red: ' + self.__red + '\n'
            'Green: ' + self.__green+ '\n'
            'Blue: ' + self.__blue + '\n' +
            'Distancia: ' + self.__distancia + '\n' 
        )