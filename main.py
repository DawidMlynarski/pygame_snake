import pygame, sys

# Initializing pygame and window
pygame.init()
screen = pygame.display.set_mode((400,500))

# Setting up clock object
clock = pygame.time.Clock()

# Creating surface
test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))

x_pos = 200

while True:
    # Drawing all elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x_pos+=1
    screen.fill((175,215,70))
    screen.blit(test_surface,(x_pos,250))
    pygame.display.update()
    
    # Setting up maximum fps
    clock.tick(60)