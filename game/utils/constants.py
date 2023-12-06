SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

BG_URI = './game/assets/bg.png'
TILES_TERRAIN_URI = './game/assets/tileset/terrain'
PLAYER_URI = './game/assets/characters/player'
ENEMY_URI = './game/assets/characters/enemy'
LLAVE_URI = './game/assets/objects/key'
COFRE_URI = './game/assets/objects/chest'
SCORES_URI = './game/assets/scores.json'
MUSIC_URI = './game/assets/sounds/musica.wav'
PLAYER_SOUNDS_BASE_URI = './game/assets/sounds/player'
PLAYER_SOUNDS_URI = {
    "morir": f"{PLAYER_SOUNDS_BASE_URI}/morir.mp3", 
    "saltar": f"{PLAYER_SOUNDS_BASE_URI}/saltar.mp3", 
    "correr": f"{PLAYER_SOUNDS_BASE_URI}/correr.mp3", 
    "matar": f"{PLAYER_SOUNDS_BASE_URI}/matar.mp3",
    "llave": f"{PLAYER_SOUNDS_BASE_URI}/llave.mp3",
    "cofre": f"{PLAYER_SOUNDS_BASE_URI}/cofre.mp3",
    "cofre_2": f"{PLAYER_SOUNDS_BASE_URI}/cofre_2.mp3",
    }

TARGET_FPS = 60
GAME_FONT = "Cambria"
COLOR_FONT = (255,255,255)
TITLE_COORD = (275,150)
SUBTITLE_COORD = (210,220)
PLAY_COORD = (350,250,50,30)
SCORE_COORD = (348,280,50,30)
BACK_COORD = (310,500,100,30)

ENEMY_RANGE = 30