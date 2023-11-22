from utils.config import *

class Personaje:
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
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

        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -12
        self.limite_velocidad_salto = 12
        self.esta_saltando = False

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
            self.animacion_actual = self.animaciones[self.estado]
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
        if self.direccion == -1:
            self.animaciones[self.estado] = girar_imagenes(self.animaciones[self.estado], True,False)
        screen.blit(self.animacion_actual[int(self.contador_pasos)], self.rect)
        pygame.draw.rect(screen,"green",self.rect,3)
        pygame.draw.rect(screen,"magenta",self.hitbox["top"],3)
        pygame.draw.rect(screen,"blue",self.hitbox["bot"],3)
        pygame.draw.rect(screen,"yellow",self.hitbox["left"],3)
        pygame.draw.rect(screen,"orange",self.hitbox["right"],3)

    def calculate_hitbox(self):
        rect = self.rect
        bot = pygame.Rect(rect.x+2, (rect.y + rect.height - 10),rect.width-4, 12)
        top = pygame.Rect(rect.x+2, rect.y, rect.width-4, 12)
        left = pygame.Rect(rect.x, rect.y+2, 12, rect.height-4)
        right = pygame.Rect((rect.x + rect.width - 10), rect.y+2, 12, rect.height-4)
        hitbox = {"left": left, "right": right, "top": top, "bot": bot}
        self.hitbox = hitbox

    def check_colisiones(self, enemigo):
        if self.hitbox["bot"].colliderect(enemigo.hitbox["top"]):
            return 1
        elif self.rect.colliderect(enemigo.rect):
            return -1