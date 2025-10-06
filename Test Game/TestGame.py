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

sky_surface = pygame.image.load("graphics/Sky.jpg").convert()
ground_surface = pygame.image.load("graphics/Ground.png").convert_alpha()
text_surface = test_font.render("Rugsoft", True, "Black")

zombi_surface = pygame.image.load("graphics/zombie/zombie_run1.png").convert_alpha()
zombie_rect = zombi_surface.get_rect(midbottom = (1400, 600))


player_surf = pygame.image.load("graphics/character/character_walk1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (85, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 575))   
    screen.blit(text_surface, (525, 50))
    
    zombie_rect.x -= 4
    if zombie_rect.right <= 0: zombie_rect.left = 1380
    screen.blit(zombi_surface, zombie_rect)
    screen.blit(player_surf, player_rect)
    
    if player_rect.colliderect(zombie_rect):
        print("colision")
    
    pygame.display.update()
    clock.tick(fps)