from objeto import Objeto
class Llave(Objeto):
    def __init__(self, animaciones, posicion, tamaño, estado="idle"):
        super().__init__(animaciones, posicion, tamaño, estado)

    def update(self, screen):
        self.animacion_actual = self.animaciones[self.estado]
        if not self.tomado:
            self.animar(screen)