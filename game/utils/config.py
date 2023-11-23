import pygame
import os, json
from utils.constants import *

def load_animaciones(ruta):
    animaciones = []

    for archivo in os.scandir(ruta):
        if archivo.is_file():
            animacion = pygame.image.load(archivo.path)
            animaciones.append(animacion)
    
    return animaciones

def load_anim_dictionary(ruta, actions=["dead","fall","hit","idle","jump","run"]):
    diccionario_animaciones = {}

    for action in actions:
        diccionario_animaciones[action] = load_animaciones(f"{ruta}/{action}/")

    return diccionario_animaciones

def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_girada

def mostrar_score(jugador, screen):
    font = pygame.font.SysFont(GAME_FONT,24)
    text = font.render(str(jugador.score),True,COLOR_FONT)
    screen.blit(text,(750,50))

def load_bg(screen):
    bg_image = pygame.image.load(BG_URI)
    bg_rect = bg_image.get_rect()
    screen.blit(bg_image, bg_rect)

def get_x(item):
    return (item[0],item[0]+item[2])

# Recibe: un item en pantalla
# Devuelve: una tupla correspondiente a sus limites en el eje Y
def get_y(item):
    return (item[1], item[1]+item[3])

# Recibe: un item en pantalla
# Devuelve: sus coordenadas especificas
def get_item_coordinates(item):
    return (get_x(item),get_y(item))

# Recibe: Las coordenadas donde se clickeo la pantalla y un item especifico de la pantalla
# Devuelve:
    # True: si las coordenadas estan dentro de las coordenadas de ese item
    # False: si no corresponden
def is_coord_in_range(input_coordinates, item):
    x = input_coordinates[0]
    y = input_coordinates[1]

    coord_range = get_item_coordinates(item)

    x_range = coord_range[0]
    y_range = coord_range[1]

    if (x>=x_range[0] and x<=x_range[1]) and (y>=y_range[0] and y<= y_range[1]):
        return True
    
    return False

def leer_archivo(nombre_archivo:str):
    try:
        archivo = open(nombre_archivo, "r",-1,"UTF-8")
        texto = archivo.read()
        if archivo.closed:
            archivo.close()
        
        return texto
    except:
        return False
    
def leer_json(nombre_archivo):
    lectura = leer_archivo(nombre_archivo)
    if lectura:
        try:
            json_result = json.loads(lectura)
            return json_result
        except:
            pass
    return lectura

def guardar_archivo(nombre_archivo:str, contenido:str):
    try:
        archivo = open(nombre_archivo, "w+", -1, "UTF-8")
        archivo.write(contenido)
        print("Se creo el archivo: " + nombre_archivo)
        return True
    except:
        print("Error al crear el archivo: " + nombre_archivo)
        return False

def generar_json(nombre_archivo, lista_superheroes, nombre_lista):
    if not lista_superheroes:
        return False
    
    texto_json = {nombre_lista: lista_superheroes}
    texto_json = json.dumps(texto_json,indent=4)
    
    guardar_archivo(nombre_archivo,texto_json)