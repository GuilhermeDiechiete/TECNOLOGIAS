# ADICIONANDO AUDIO

#IMPORTAR O PYGAME, QUE É DE JOGOS, ENTÃO TEM A PARTE DE AUDIO.
import pygame
pygame.init() #inicia o pygame
pygame.mixer.music.load('audio.mp3') # adiciona a musica
pygame.mixer.music.play() #da o play

import time
time.sleep(360) # para rodar
