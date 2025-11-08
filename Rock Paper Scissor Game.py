import random
score = 0
run = True
while run:
    rand = random.randint(1,3)
    rps = str(input("Rock, paper, or scissor."))
    if rps == "Rock" and rand == 1: 
        quit = input("Both rock, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False
    elif rps == "Rock" and rand == 2:
        quit = input("Paper beats rock, you lost, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False
    
    elif rps == "Rock" and rand == 3:
        score += 1
        quit = input("Rock beats scissors, you won, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False
    
    elif rps == "Paper" and rand == 2:
        quit = input("Both paper, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False
    
    elif rps == "Paper" and rand == 1:
        score += 1
        quit = input("Paper beats rock, you won, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False

    elif rps == "Paper" and rand == 3:
        quit = input("Scissor beats paper, you lost, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False
    
    elif rps == "Scissor" and rand == 1:
        quit = input("Rock beats scissor,you lost, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False

    elif rps == "Scissor" and rand == 2:
        score += 1
        quit = input("Scissor beats paper, you won, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True
        else:
            run = False

    else:
        quit = input("Both scissor, would you like to continue.?")
        if quit == "Yes" or quit == "yes":
            run = True

print("Your final score was " + str(score))



              
    