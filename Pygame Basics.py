import pygame

#Intitializing the library of pygame
pygame.init()

screenWidth = 800
screenHeight = 600



#Making the screen
screen = pygame.display.set_mode((screenWidth, screenHeight)) #Remember that width comes before height.

player = pygame.Rect((300, 250, 50, 50)) #Player creation, just a circle for now

run = True
while run:

    screen.fill((0, 0, 0)) #Making screen black so there are no tracers

    pygame.draw.rect(screen, (250, 0, 0), player) # RGB values 250 for red, 0 for blue and green. Calling the draw rectangle function.

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
        if event.type == pygame.QUIT: #Iterate through all the events that pygame picks up, eg: Pressing the x in the top right corner.
            run = False

    pygame.display.update() #Update the screen(refresh the screen to the new event that happens on screen.)

pygame.quit()

