from personaje import Personaje

class Jugador(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado)

    def tomar_llave(self, llave):
        if self.rect.colliderect(llave.rect):
            llave.tomado = True

    def abrir_cofre(self,cofre,llave):
        if llave.tomado:
            if self.rect.colliderect(cofre.rect):
                cofre.tomado = True