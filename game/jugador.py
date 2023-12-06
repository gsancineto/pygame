from personaje import Personaje
from sonido import Sonido

class Jugador(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado)
        self.score = 0
        self.banderas = { "llave": False, "cofre": False, "enemigo": 0 }
        self.vidas = 3
        self.sonido = Sonido()

    def tomar_llave(self, llave):
        if self.rect.colliderect(llave.rect) and not llave.tomado:
            llave.tomado = True
            self.sonido.reproducir_efecto("llave")

    def abrir_cofre(self,cofre,llave):
        if llave.tomado:
            if self.rect.colliderect(cofre.rect) and not cofre.tomado:
                cofre.tomado = True
                self.sonido.reproducir_efecto("cofre_2")

    def aumentar_score(self,enemigos,cofre):
        for enemigo in enemigos:
            if enemigo.muerto and not self.banderas["enemigo"] == len(enemigos):
                self.score += 30
                self.banderas["enemigo"] += 1
        if cofre.tomado and not self.banderas["cofre"]:
            self.score += 50
            self.banderas["cofre"] = True

    def morir(self, map):
        self.sonido.reproducir_efecto("morir")
        self.estado = "dead"
        if self.vidas > 1:
            self.vidas -= 1
            self.reset(map)
        else:
            self.muerto = True
        
    def reset(self,map):
        self.rect.x, self.rect.y = map.start_x, map.start_y
        

    def nuevo_juego(self,map):
        self.reset(map)
        self.vidas = 3
        self.muerto = False
        return 1

    def proximo_nivel(self,map):
        self.banderas = { "llave": False, "cofre": False, "enemigo": 0 }
        self.reset(map)

    def check_colisiones(self, enemigos, map):
        for enemigo in enemigos:
            if self.hitbox["bot"].colliderect(enemigo.hitbox["top"]):
                if not enemigo.muerto:
                    self.sonido.reproducir_efecto("matar")
                enemigo.morir()
            elif (self.rect.colliderect(enemigo.rect) and not enemigo.muerto) or self.rect.colliderect(self.vacio_mapa):
                self.morir(map)