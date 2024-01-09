# -.- coding: utf8 -.-
import pygame
import math as m
import pygame.draw as pd
import sys
from main import *

screen_color = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill(screen_color)
    FPS = 30

    # draw the face
    face = Face(screen)
    face.draw_face()

    pygame.display.update()
    clock = pygame.time.Clock()

    while True:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                print('Left and Right')

if __name__ == '__main__':
    main()