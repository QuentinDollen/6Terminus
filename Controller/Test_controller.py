from curses import KEY_RIGHT
import sys
from turtle import clear
import pygame

pygame.init()

index = 0
screen = pygame.display.set_mode((800, 800))

running = True

while running:

    keys = pygame.key.get_pressed()
    if keys[KEY_RIGHT]:
        print("ca marche")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Faire appel à la fonction Quitter le jeu dans la partie logique
        elif event.type == pygame.KEYUP:
            print("Siuuuuu")

sys.exit()
