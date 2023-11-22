from personaje import Personaje

class Jugador(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado)