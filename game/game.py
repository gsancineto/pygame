import pygame
from utils.constants import *
from tiles import *
from utils.config import *
from jugador import Jugador
from enemigo import Enemigo
from llave import Llave
from cofre import Cofre
from level import Level
from inicio import Inicio
from sonido import Sonido

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
bg_image = pygame.image.load(BG_URI)
bg_rect = bg_image.get_rect()

sonido = Sonido()
sonido.reproducir_musica()

stage = "inicio"
inicio = Inicio(screen)
nivel = 1
level = Level(nivel)
map = level.iniciar_nivel()

diccionario_animaciones_jugador = load_anim_dictionary(PLAYER_URI)
diccionario_animaciones_enemigo = load_anim_dictionary(ENEMY_URI)
diccionario_animaciones_llave = load_anim_dictionary(LLAVE_URI,["idle"])
diccionario_animaciones_cofre = load_anim_dictionary(COFRE_URI,["locked","unlocked"])

player = Jugador(diccionario_animaciones_jugador,(map.start_x,map.start_y - 10),(40,40),7)
enemigos = []
for enemigo_start in map.enemies_start:
    enemigos.append(Enemigo(diccionario_animaciones_enemigo,(enemigo_start),(75,50),3, "run",(enemigo_start[0]-ENEMY_RANGE,enemigo_start[0]+ENEMY_RANGE)))
llave = Llave(diccionario_animaciones_llave,(map.key_x,map.key_y),(40,40))
cofre = Cofre(diccionario_animaciones_cofre,(map.chest_x,map.chest_y),(40,40),"locked")

sonido_correr_timer = 0

vidas = player.vidas
puntaje = player.score
while running:
    dt = clock.tick(30) * .001 * TARGET_FPS

    if sonido_correr_timer > 0:
        sonido_correr_timer -=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and stage != "play":
            stage = inicio.select_opcion(pygame.mouse.get_pos())
            sonido.reproducir_efecto("llave")
        
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            player.estado = "run"
            player.direccion = 1
            if not player.esta_saltando and stage == "play":
                sonido_correr(sonido_correr_timer,sonido)
        elif teclas[pygame.K_LEFT]:
            player.estado = "run"
            player.direccion = -1
            if not player.esta_saltando and stage == "play":
                sonido_correr(sonido_correr_timer,sonido)
        else:
            player.estado = "idle"
        
        if teclas[pygame.K_SPACE]:
            player.estado = "jump"
            stage = "play"
            if not player.esta_saltando:
                sonido.reproducir_efecto("saltar")

    if stage == "inicio":
        nivel = player.nuevo_juego(map)
        inicio.mostrar_inicio()
    elif stage == "score":
        inicio.mostrar_score()
    elif stage == "play":
        load_bg(screen)
        map.draw_map(screen)
        mostrar_score(player,screen)
        player.abrir_cofre(cofre,llave)
        cofre.abrir()
        cofre.update(screen)
        player.update(screen, map)
        for enemigo in enemigos:
            enemigo.update(screen,map)
        player.tomar_llave(llave)
        llave.update(screen)

        player.check_colisiones(enemigos,map)
        player.aumentar_score(enemigos,cofre)

        if player.muerto:
            stage = inicio.set_score(player)
        
        vidas = player.vidas
        puntaje = player.score

        if cofre.tomado:
            nivel += 1
            if nivel == 4:
                player.muerto = True
                stage = inicio.set_score(player)
            else:
                level = Level(nivel)
                map = level.iniciar_nivel()
                cofre.reset()
                llave.reset()
                enemigos = []
                player.proximo_nivel(map)
                player = Jugador(diccionario_animaciones_jugador,(map.start_x,map.start_y - 10),(40,40),7)
                player.vidas = vidas
                player.score = puntaje
                for enemigo_start in map.enemies_start:
                    enemigos.append(Enemigo(diccionario_animaciones_enemigo,(enemigo_start),(75,50),3, "run",(enemigo_start[0]-ENEMY_RANGE,enemigo_start[0]+ENEMY_RANGE)))
                llave = Llave(diccionario_animaciones_llave,(map.key_x,map.key_y),(40,40))
                cofre = Cofre(diccionario_animaciones_cofre,(map.chest_x,map.chest_y),(40,40),"locked")

        
    pygame.display.flip()

pygame.quit()