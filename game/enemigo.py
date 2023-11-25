from utils.config import * 
from personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle", limites=False):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado, limites)
        self.flag_direccion = "R"
        self.limites = limites

    def desplazar(self):
        limite_izquierdo, limite_derecho = self.limites[0], self.limites[1]
        if self.rect.x >= limite_izquierdo and self.flag_direccion == "R":
            self.rect.x -= self.velocidad
        elif self.rect.x >= (limite_izquierdo - 8) and self.flag_direccion == "R":
            self.flag_direccion = "L"
        elif self.rect.x <= limite_derecho and self.flag_direccion == "L":
            self.rect.x += self.velocidad
        else:
            self.flag_direccion = "R"

    def reset(self):
        self.muerto = False
        self.estado = "run"
