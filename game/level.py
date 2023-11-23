from tiles import TileMap

class Level:
    def __init__(self, nivel):
        self.level = nivel

    def iniciar_nivel(self):
        return TileMap(f'./game/assets/levels/level_{self.level}.csv')