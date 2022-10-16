#First we import random
import random
#Name players
currentPlayer = 0 #0 = Human, 1 = Computer
playerScore = 0
computerScore = 0
roll = 0
#Make script for score
while (playerScore < 10) and (computerScore < 10):
    #Add button for dice roll
    if(currentPlayer == 0):
        input ("Press enter to roll...")
        roll = random.randrange(1, 6)
        playerScore += roll
        print("You rolled a {}".format(roll))
        print ("Player score : {}".format(playerScore))
        print("Computer score : {}".format(computerScore))
        currentPlayer = 1
    elif(currentPlayer == 1):
        input ("Press enter to let computer roll ...")
        roll = random.randrange (1, 6)
        computerScore += roll
        print("The computer rolled a {}".format(roll))
        print("Player score : {}".format(playerScore))
        print("Computer score : {}".format(computerScore))
        currentPlayer = 0
        #Add function for game end
        if (playerScore >= 10):
            print ("Congratulations, you won!")
        elif(computerScore >= 10):
            print("Sorry, computer won !")