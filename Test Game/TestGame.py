import pygame
from sys import exit

pygame.init()

width = 1280
height = 720
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(fps)