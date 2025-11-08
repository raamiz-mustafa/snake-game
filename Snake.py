import pygame, random, time
pygame.init(), pygame.mixer.init() #Initialising

eating = pygame.mixer.Sound("mixkit-hungry-man-eating-2252.wav")
gameOversound = pygame.mixer.Sound("mixkit-arcade-retro-game-over-213.wav")

gameState = "Menu" 

git = "Hub"

score = 0
screenW = 500
screenH = 500
screen = pygame.display.set_mode((screenW, screenH)) #Colours, screen, and the score
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
col = green

mouse = pygame.Rect((225, 225, 1, 1))
start = pygame.Rect((150, 150, 100, 100))


clock = pygame.time.Clock()
player = [(200, 200)]
direction = (20, 0)
food = (random.randrange(0, 500 - 20, 20), random.randrange(0, 500 - 20, 20))
textFont = pygame.font.SysFont("Arial", 30)
gameOver = pygame.font.SysFont("Arial", 75, bold = True)

def displayText(text, font, textCol, x, y):
    image = font.render(text, True, textCol)
    screen.blit(image, (x, y))

run = True
while run:
    screen.fill(black)
    
    if gameState == "Menu":
        pos = pygame.mouse.get_pos()
        mouse.center = pos
        pygame.draw.rect(screen, green, mouse)
        pygame.draw.rect(screen, green, start)
        displayText("Start", textFont, black, 170, 165)
        for event in pygame.event.get():
            if mouse.colliderect(start) and event.type == pygame.MOUSEBUTTONDOWN:
                gameState = "Playing"
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
        
        
            
        
        
    if gameState == "Playing":
        #The general direction of the player  
        displayText(str(score), textFont, white, 0, 0)
        pygame.draw.rect(screen, red, (*food, 20, 20))
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = (0, -20)
                elif event.key == pygame.K_d:
                    direction = (20, 0)
                elif event.key == pygame.K_a:
                    direction = (-20, 0)
                elif event.key == pygame.K_s:
                    direction = (0, 20)
                elif event.key == pygame.K_ESCAPE:
                    gameState = "Menu"           
            if event.type == pygame.QUIT:
                run = False   
        #The player is playerx + the distance moved in x and playery + the distance moved in y - the last one
        player = [(player[0][0] + direction[0], player[0][1] + direction[1])] + player[:-1] #Normal movement add head to next chunk and cut off tail

        #Eating and growing
        if player[0] == food:
            food = (random.randrange(0, 500 - 20, 20), random.randrange(0, 500 - 20, 20)) 
            eating.play()   
            player.append(player[-1]) #Eating movement player[-1] = the last segment of player and appending it is just adding it after it gets reomved in normal movement
            score = score + 1

        #wall collison check line
        if player[0][0] >= 500 or player[0][0] < 0  or player[0][1] >= 500 or player[0][1] < 0: #Remember non empty tuple is always true  
            gameOversound.play()
            displayText("Game Over", gameOver, white, 125, 125)
            pygame.display.flip()
            time.sleep(1)
            run = False
        
        for segment in player:
            pygame.draw.rect(screen, red, (*segment, 20, 20))
            pygame.draw.rect(screen, red, (*segment, 20, 20))
        pygame.display.flip()


        

        clock.tick(10) # Just FPS

pygame.quit()




                                                        

