import pygame
pygame.init(), pygame.mixer.init()
sw = 800
sh = 800
screen = pygame.display.set_mode((sw, sh))
gameOver = pygame.mixer.Sound("mixkit-arcade-retro-game-over-213.wav")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameOver.play()

pygame.quit()