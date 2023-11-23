import pygame, os, csv
from utils.constants import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class TileMap():
    def __init__(self, filename):
        self.title_size = 32
        self.start_x, self.start_y = 0,0
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0,0,0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0,0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
            pygame.draw.rect(self.map_surface,"red",tile.rect,3)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x,y = 0,0

        for row in map:
            x = 0
            for tile in row:
                if tile == "P":
                    self.start_x, self.start_y = x* self.title_size, y * self.title_size
                elif tile == "K":
                    self.key_x, self.key_y = x* self.title_size, y * self.title_size
                elif tile == "C":
                    self.chest_x, self.chest_y = x* self.title_size, y * self.title_size
                elif tile =="E":
                    self.enemy_start_x, self.enemy_start_y = x* self.title_size, y* self.title_size
                elif tile != '-1':
                    tiles.append(Tile(f"{TILES_TERRAIN_URI}/{tile}.png", x * self.title_size, y * self.title_size))
                x += 1
            y += 1

        self.map_w, self.map_h = x * self.title_size, y * self.title_size
        return tiles
