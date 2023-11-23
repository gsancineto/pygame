from personaje import Personaje

class Jugador(Personaje):
    def __init__(self, animaciones, posicion, tamaño, velocidad, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, velocidad, estado)
        self.score = 0
        self.banderas = { "llave": False, "cofre": False, "enemigo": False }

    def tomar_llave(self, llave):
        if self.rect.colliderect(llave.rect):
            llave.tomado = True

    def abrir_cofre(self,cofre,llave):
        if llave.tomado:
            if self.rect.colliderect(cofre.rect):
                cofre.tomado = True

    def aumentar_score(self,enemigo,llave,cofre):
        if enemigo.muerto and not self.banderas["enemigo"]:
            self.score += 30
            self.banderas["enemigo"] = True
        elif llave.tomado and not self.banderas["llave"]:
            self.score += 10
            self.banderas["llave"] = True
        elif cofre.tomado and not self.banderas["cofre"]:
            self.score += 50
            self.banderas["cofre"] = True

    def morir(self,map):
        self.score -= 10
        self.rect.x, self.rect.y = map.start_x, map.start_y