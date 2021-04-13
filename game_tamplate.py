import pygame
import random

 # size
WIDTH = 360
HEIGHT = 480
FPS = 30

 # color (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init() # turn on pygame
pygame.mixer.init() # music
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # prog screen
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

running = True
while running: # game cycle

    clock.tick(FPS) # set cycle speed

    for event in pygame.event.get(): # now we can close screen
        if event.type == pygame.QUIT:
            running = False

    screen.fill(RED) # rendering

    pygame.display.flip() # flip screen

pygame.quit() # close screen