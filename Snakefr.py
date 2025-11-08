import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

snake = [(200, 200)] # Head pos x and pos y
direction = (20, 0) # How much to move x and y

food = (random.randrange(0, 400, 20), random.randrange(0, 400, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: direction = (0, -20)
            if event.key == pygame.K_DOWN: direction = (0, 20)
            if event.key == pygame.K_LEFT: direction = (-20, 0)
            if event.key == pygame.K_RIGHT: direction = (20, 0)
        
    snake = [(snake[0][0] + direction[0], snake[0][1] + direction[1])] + snake[:-1]

    if snake[0] == food:
        food = (random.randrange(0, 400, 20), random.randrange(0, 400, 20))
        snake.append(snake[-1])
        
    screen.fill((0, 0, 0))
    for segment in snake: pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))
    pygame.display.flip()
    
    clock.tick(10)

