from objeto import Objeto
from utils.config import *
from utils.constants import *

class Cofre(Objeto):
    def __init__(self, animaciones, posicion, tamaño, estado):
        super().__init__(animaciones, posicion, tamaño, estado)

    def abrir(self):
        if self.tomado:
            self.estado = "unlocked"
            

    def reset(self):
        self.tomado = False
        self.estado = "locked"
