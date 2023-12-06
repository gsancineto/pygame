import pygame
from utils.constants import *

class Sonido:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(64)

    def reproducir_efecto(self,sonido):
        efecto = pygame.mixer.Sound(PLAYER_SOUNDS_URI[sonido])
        efecto.play()
        efecto.set_volume(0.2)

    def reproducir_musica(self):
        pygame.mixer.music.load(MUSIC_URI)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.03)