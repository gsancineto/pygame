from utils.config import *

class Objeto:
    def __init__(self, animaciones,posicion, tamaño, estado):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rect = pygame.Rect(*posicion, *tamaño)
        x,y = posicion
        self.rect.x = x
        self.rect.y = y
        self.estado = estado
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones[estado]
        self.tomado = False

    def draw(self,screen):
        screen.blit(self.animacion_actual[int(self.contador_pasos)], self.rect)

    def animar(self, screen):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        self.draw(screen)
        self.contador_pasos += 0.2

    def update(self, screen):
        self.animacion_actual = self.animaciones[self.estado]
        self.animar(screen)

    def reset(self):
        self.tomado = False