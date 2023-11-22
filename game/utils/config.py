import pygame
import os
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