import pygame
import random
pygame.init()

sw = 800
sh = 600

blue = (0, 255, 0)
green = (0, 0, 255)
red = (255, 0, 0)
col = green


screen = pygame.display.set_mode((sw, sh))

rect1 = pygame.Rect((300, 300, 50, 50))
obstacles = []
for x in range(15):
    obs = pygame.Rect((random.randint(200, 600), random.randint(100, 500), 50, 50))
    obstacles.append(obs)

run = True
while run:
    screen.fill((0, 0, 0))
    
    for obstacle in obstacles:
        pygame.draw.rect(screen, blue, obstacle)
    
    pygame.draw.rect(screen, col, rect1)

    for obstacle in obstacles:
        if rect1.collidelist(obstacles):
            col = red
    
    pos = pygame.mouse.get_pos()
    rect1.center = pos

    result = rect1.collidelist(obstacles)
    print(result)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
    pygame.display.update()

pygame.quit()
