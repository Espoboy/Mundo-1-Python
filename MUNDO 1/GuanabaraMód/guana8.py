# Ex 21 abrir um arquivo mp3

import pygame
# .init para iniciar o módulo
pygame.init()
# pygame.mixer.music.load('omans.mp3') carrega a música e o play toca
pygame.mixer.music.load('omans.mp3')
pygame.mixer.music.play()
# input() espera uma entrada de um usuário e toca música até o usuário digitar algo
input()

