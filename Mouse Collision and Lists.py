import pygame
import random
pygame.init()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255) #Setting up the screen.
screen = pygame.display.set_mode((800, 800))
col = blue 


rect1 = pygame.Rect((400, 400, 50, 50))
obstacles = []
for x in range(15):
    obs = pygame.Rect((random.randint(0, 500), random.randint(0, 300), 50, 50)) #Makiking the rectanlge generate randomly.
    obstacles.append(obs)

run = True
while run:

    screen.fill((0, 0, 0))

    col = blue # Setting the rectangle colour as blue.

    for obstacle in obstacles:
        if rect1.colliderect(obstacle):
            col = red #If it collides, then the rectangle will turn red
    
    pos = pygame.mouse.get_pos() #Mouse x and y cords
    rect1.center = pos

    for obstacle in obstacles:
        pygame.draw.rect(screen, green, obstacle)
    pygame.draw.rect(screen, col, rect1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() 

pygame.quit()
