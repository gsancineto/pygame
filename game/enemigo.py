from utils.config import * 
from personaje import Personaje
import pygame

class Enemigo(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado)
        self.flag_direccion = "R"
        self.muerto = False

    def desplazar(self):
        if self.rect.x >= 298 and self.flag_direccion == "R":
            self.rect.x -= self.velocidad
        elif self.rect.x >= 290 and self.flag_direccion == "R":
            self.flag_direccion = "L"
        elif self.rect.x <= 420 and self.flag_direccion == "L":
            self.rect.x += self.velocidad
        else:
            self.flag_direccion = "R"

    def morir(self):
        self.estado = "dead"
        self.muerto = True
        self.rect.x = 900

    def reset(self, map):
        self.muerto = False
        self.estado = "run"
        self.rect.x = map.enemy_start_x