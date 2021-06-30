import sys
from random import randint

roundOver = False
houseWins = False
playerWins = False
pointOn = False
playerBank = 10000
betAmount = 0

name = input("\nHello, what's your name? ")
print ("\nHi " + name + ", welcome to the DigitalCrafts Casino. Let's play some craps!")

# adding something real quick
def roll():
    global pointOn
    global point
    global roundOver, houseWins, playerWins

    if not pointOn:
        wager()

    d1 = randint(1, 6)
    d2 = randint(1, 6)

    value = d1 + d2
    print (name + " rolls a: " + str(value))

    if pointOn:
        if point == value:
            print (name + " hit the point, " + name + " wins.")
            roundOver = True
            houseWins = False
            playerWins = True
        elif value == 7:
            print (name + " rolled a 7, house wins.")
            roundOver = True
            houseWins = True
            playerWins = False
    else:
        if value == 2 or value == 3 or value == 12:
            houseWins = True
            playerWins = False
            roundOver = True
            print (name + " crapped out, house wins.")
        elif value == 7 or value == 11:
            houseWins = False
            playerWins = True
            roundOver = True
            print (name + " rolled a 7 or 11, " + name + " wins.")
        else:
            point = value
            pointOn = True
            print ("The point is on and set to: " + str(point))


def startGame():
    global roundOver, point, pointOn, betAmount, playerBank
    point = 0
    roundOver = False
    pointOn = False

    while not roundOver:
        roll()

    if houseWins:
        playerBank = playerBank - betAmount
    elif playerWins:
        playerBank = playerBank + betAmount

    print ("\nYou now have $" + str(playerBank))

    if playerBank == 0:
        print("You're out of money! Press p to play again or e to exit!")
        inp = input()
        if inp == "p":
            playerBank = 10000
            startGame()
        elif inp == "e":
            print ("\nGame Over")
            sys.exit()

    startGame()

    # inp = input(
    #     "\nEnter 'r' to roll or any other key to exit the game:   ")
    # if inp.lower() == 'r':
    #     startGame()
    # else:
    #     print ("\nGame Over")


def wager():
    global playerBank, betAmount
    print ("\n")
    print ("You have $" + str(playerBank))
    print ("\n")

    

    betAmount = input("Place your bet: ")
    betAmount = int(betAmount)

    if betAmount > playerBank:
        print ("Please enter a smaller wager")
        wager()

    if betAmount <= 0:
        print ("Please enter a number > 0")
        wager()

startGame()

