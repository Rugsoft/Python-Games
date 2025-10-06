import pygame
from sys import exit

pygame.init()

width = 1280
height = 720
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/Super_Sliced.ttf", 55)

sky_surface = pygame.image.load("graphics/Sky.jpg")
ground_surface = pygame.image.load("graphics/Ground.png")
text_surface = test_font.render("Rugsoft", True, "Black")

zombi_surface = pygame.image.load("graphics/zombie/zombie_run1.png")
zombie_x_pos = 1300

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 575))   
    screen.blit(text_surface, (525, 50))
    zombie_x_pos -= 3
    if zombie_x_pos < -200: zombie_x_pos = 1400
    screen.blit(zombi_surface,(zombie_x_pos, 349))
    
    pygame.display.update()
    clock.tick(fps)