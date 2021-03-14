
# ROCK == 0
# PAPER == 1
# SCISSOR == 2

# GOOD LUCK

import random

player = input()
player = int(player)

rock = 0
paper = 1
scissors = 2

computer = random.randint(0,2)
#computer = 2

# 0 == rock, 1 == paper, 2 == scissors

while rock or paper or scissors:
    #if player == rock and computer == rock:
    
    # All Tie 
    if player == computer:
        print ("Tie.")
        break
        
        # All player winning..
    if player == paper and computer == rock:
        print ("You won")
        break 
    if player == rock and computer == scissors:
        print ("You won")
        break
    if player == scissors and computer == paper:
        print ("You won")
        break

        # All computer winning
    if computer == paper and player == rock:
        print ("You lost")
        break 
    if computer == rock and player == scissors:
        print ("You lost")
        break
    if computer == scissors and player == paper:
        print ("You lost.")
        break