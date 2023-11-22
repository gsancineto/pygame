from utils.config import * 
from personaje import Personaje
import pygame

class Enemigo(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado)

    def avanzar(self, direccion):
        self.rect.x += self.velocidad * direccion
        self.estado = "run"