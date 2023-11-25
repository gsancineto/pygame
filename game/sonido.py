import pygame
from utils.constants import *

class Sonido:
    def __init__(self) -> None:
        pass

    def reproducir_efecto(self,sonido):
        pista = pygame.mixer.Sound(PLAYER_SOUNDS_URI[sonido])
        pygame.mixer.Sound.play(pista)
        pygame.mixer.Sound.set_volume(0.2)

    def reproducir_musica(self):
        pygame.mixer.music.load(MUSIC_URI)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)