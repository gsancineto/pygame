from utils.config import *
from utils.constants import *
import pygame

class Inicio:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont(GAME_FONT,48, True)
        self.text_font = pygame.font.SysFont(GAME_FONT,24,True)
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

        y = 300
        for score in self.scores:
            score_text = f"{score['name']}................{score['score']}"
            scores = self.text_font.render(score_text, True, COLOR_FONT)
            self.screen.blit(scores,(250,y))
            y+= 30

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
