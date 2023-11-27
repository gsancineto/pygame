from utils.config import *
from sonido import Sonido

class Personaje:
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle", limites=False):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rect = pygame.Rect(*posicion, *tamaño)
        x,y = posicion
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

        self.estado = estado
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones[estado]
        self.direccion = 1 #1 = derecha, -1 = izquierda
        self.animacion_actual_flip = girar_imagenes(self.animaciones[estado],True,False)

        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -12
        self.limite_velocidad_salto = 12
        self.esta_saltando = False

        self.muerto = False
        self.vacio_mapa = pygame.rect.Rect(-800,650,SCREEN_WIDTH*3, 1)
        self.sonido = Sonido()

    def desplazar(self):
        self.rect.x += self.velocidad * self.direccion

    def aplicar_gravedad(self, screen, map):
        if self.esta_saltando:
            self.animar(screen)
            self.rect.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for tile in map.tiles:
            if self.hitbox["bot"].colliderect(tile.rect) and self.rect.colliderect(tile.rect):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.rect.bottom = tile.rect.top + 10
                break
            else:
                self.esta_saltando = True


    def animar(self, screen):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        self.draw(screen)
        self.contador_pasos += 0.3

    def update(self, screen, map):
        if not self.esta_saltando:
            if self.direccion == 1:
                self.animacion_actual = self.animaciones[self.estado]
            else:
                self.animacion_actual = self.animacion_actual_flip
            self.animar(screen)

        if self.estado == "run":
            self.desplazar()
        elif self.estado == "jump":
            if not self.esta_saltando:
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
        
        self.aplicar_gravedad(screen, map)

    def draw(self,screen):
        self.calculate_hitbox()
        screen.blit(self.animacion_actual[int(self.contador_pasos)], self.rect)

    def calculate_hitbox(self):
        rect = self.rect
        bot = pygame.Rect(rect.x+2, (rect.y + rect.height - 10),rect.width-4, 12)
        top = pygame.Rect(rect.x+2, rect.y, rect.width-4, 12)
        left = pygame.Rect(rect.x, rect.y+2, 12, rect.height-4)
        right = pygame.Rect((rect.x + rect.width - 10), rect.y+2, 12, rect.height-4)
        hitbox = {"left": left, "right": right, "top": top, "bot": bot}
        self.hitbox = hitbox
 
    def morir(self):
        self.estado = "dead"
        self.muerto = True