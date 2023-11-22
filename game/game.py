import pygame
from utils.constants import *
from tiles import *
from utils.config import *
from jugador import Jugador
from enemigo import Enemigo
from llave import Llave
from cofre import Cofre
import math

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
bg_image = pygame.image.load(BG_URI)
bg_rect = bg_image.get_rect()

map = TileMap('./game/assets/level_1.csv')
diccionario_animaciones_jugador = load_anim_dictionary(PLAYER_URI)
diccionario_animaciones_enemigo = load_anim_dictionary(ENEMY_URI)
diccionario_animaciones_llave = load_anim_dictionary(LLAVE_URI,["idle"])
diccionario_animaciones_cofre = load_anim_dictionary(COFRE_URI,["locked","unlocked"])

player = Jugador(diccionario_animaciones_jugador,(map.start_x,map.start_y - 10),(40,40),7)
enemigo = Enemigo(diccionario_animaciones_enemigo,ENEMY_START,(75,50),3, "run")
llave = Llave(diccionario_animaciones_llave,(map.key_x,map.key_y),(40,40))
cofre = Cofre(diccionario_animaciones_cofre,(map.chest_x,map.chest_y),(40,40),"locked")

while running:
    dt = clock.tick(30) * .001 * TARGET_FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            player.estado = "run"
            player.direccion = 1
        elif teclas[pygame.K_LEFT]:
            player.estado = "run"
            player.direccion = -1
        else:
            player.estado = "idle"
        
        if teclas[pygame.K_SPACE]:
            player.estado = "jump"

    screen.blit(bg_image, bg_rect)
    map.draw_map(screen)
    player.abrir_cofre(cofre,llave)
    cofre.abrir()
    cofre.update(screen)
    player.update(screen, map)
    enemigo.update(screen,map)
    player.tomar_llave(llave)
    llave.update(screen)
    if player.check_colisiones(enemigo) == 1:
        enemigo.estado = "dead"
    elif player.check_colisiones(enemigo) == -1:
        player.estado = "dead"
    
    pygame.display.flip()

pygame.quit()