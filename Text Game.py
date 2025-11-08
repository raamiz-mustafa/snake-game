import random
rand = random.randint(0, 100)
g1 = int(input("Guess a number from 0 to 100."))
if g1 == rand:
    print("Nice first try.")
else:
    if rand > g1:
        g2 = int(input("Unlucky, buit it is higher."))
    elif rand < g1:
        g2 = int(input("Unlucky, but its lower."))
    if g2 == rand:
        print("Second time lucky.")
    else:
        if rand > g2:
            g3 = int(input("Unlucky, but its higher."))
        elif rand < g2:
            g3 = int(input("Unlucky bit its lower."))
        if rand == g3:
            print("3rd times the charm.")
        else:
            print("You failed. But the number was " + str(rand))

