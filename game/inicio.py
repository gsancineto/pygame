from utils.config import *
from utils.constants import *
import pygame, json

class Inicio:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont(GAME_FONT,48, True)
        self.text_font = pygame.font.SysFont(GAME_FONT,16,True)
        self.subtitle_font = pygame.font.SysFont(GAME_FONT,32,True)
        self.scores = []
        
    def mostrar_score(self):
        load_bg(self.screen)
        if not self.scores:
            self.get_scores()
        
        title = self.title_font.render("SCORE",True,COLOR_FONT)
        self.screen.blit(title,(TITLE_COORD[0]+25,TITLE_COORD[1]))

        subtitle = self.subtitle_font.render(f"NOMBRE          PUNTAJE",True,COLOR_FONT)
        self.screen.blit(subtitle,SUBTITLE_COORD)

        y = 270
        index = 1
        for score in self.scores:
            score_text = f"{score['name']}........................................{score['score']}"
            scores = self.text_font.render(score_text, True, COLOR_FONT)
            self.screen.blit(scores,(250,y))
            y+= 30
            index += 1
            if index == 8:
                break

        back = self.subtitle_font.render("Volver",True,COLOR_FONT)
        self.screen.blit(back,BACK_COORD)



    def mostrar_inicio(self):
        load_bg(self.screen)
        title = self.title_font.render("PIRATULIS",True,COLOR_FONT)
        self.screen.blit(title,TITLE_COORD)
        play = self.text_font.render("Jugar",True,COLOR_FONT)
        score = self.text_font.render("Score",True,COLOR_FONT)
        self.screen.blit(play,(PLAY_COORD[0],PLAY_COORD[1]))
        self.screen.blit(score,(SCORE_COORD[0],SCORE_COORD[1]))

    def select_opcion(self, posicion):
        if is_coord_in_range(posicion,PLAY_COORD):
            return "play"
        elif is_coord_in_range(posicion,SCORE_COORD):
            return "score"
        elif is_coord_in_range(posicion,BACK_COORD):
            return "inicio"
        
    def get_scores(self):
        self.scores = leer_json(SCORES_URI)

    def set_score(self, jugador):
        if jugador.muerto:
            jugador.score += jugador.vidas * 10
            self.get_scores()
            index = len(self.scores)
            nuevo_score = {"name": f"piratuli_{index}", "score": jugador.score}
            self.scores.append(nuevo_score)
            self.scores = sorted(list(self.scores), key=lambda x: x["score"], reverse= True)
            generar_json(SCORES_URI,self.scores)
            return "score"