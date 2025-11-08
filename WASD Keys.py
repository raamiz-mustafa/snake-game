import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))

player = pygame.Rect((350, 350, 50, 50))

run = True 
while run:

     screen.fill((0, 0, 0))

     pygame.draw.rect(screen, (255, 0, 0), player)
     
     key = pygame.key.get_pressed()
     
     if key[pygame.K_a] == True:
          player.move_ip(-1,0)

     elif key[pygame.K_d] == True:
          player.move_ip(1,0)              #The normal WASD key setup, looking for pressing key events to then carry out an action.
    
     elif key[pygame.K_w] == True:
          player.move_ip(0, -1)
    
     elif key[pygame.K_s] == True:
          player.move_ip(0, 1)

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False

     pygame.display.update()

pygame.Quit()