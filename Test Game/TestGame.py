import pygame
from sys import exit

pygame.init()

width = 1280
height = 720
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("graphics/Sky.jpg")
ground_surface = pygame.image.load("graphics/Ground.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 575))   
    
    pygame.display.update()
    clock.tick(fps)