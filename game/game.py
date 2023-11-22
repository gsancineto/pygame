import pygame
from utils.constants import *
from tiles import *
from utils.config import *
from jugador import Jugador
from enemigo import Enemigo

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
bg_image = pygame.image.load(BG_URI)
bg_rect = bg_image.get_rect()

map = TileMap('./game/assets/level_1.csv')
diccionario_animaciones_jugador = load_anim_dictionary(PLAYER_URI)
diccionario_animaciones_enemigo = load_anim_dictionary(ENEMY_URI)
player = Jugador(diccionario_animaciones_jugador,(map.start_x,map.start_y - 10),(40,40),7)
enemigo = Enemigo(diccionario_animaciones_enemigo,ENEMY_START,(75,50),3)

while running:
    dt = clock.tick(30) * .001 * TARGET_FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
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

    if player.rect.x - enemigo.rect.x <= 10:
        enemigo.avanzar(-1)
    else:
        enemigo.avanzar(1)

    screen.blit(bg_image, bg_rect)
    map.draw_map(screen)
    player.update(screen, map)
    enemigo.update(screen,map)
    if player.check_colisiones(enemigo) == 1:
        enemigo.estado = "dead"
    elif player.check_colisiones(enemigo) == -1:
        player.estado = "dead"
    
    pygame.display.flip()

pygame.quit()