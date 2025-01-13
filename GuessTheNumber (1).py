#Oliver Giron

#init
import random
#Functions
EasyGame = ["1 and 5", 1, 5]
MediumGame = ["1 and 10", 1, 10]
HardGame = ["1 and 20", 1, 20]

#Individual Game
def GuessGame(list):
    print("Guess the number between " + list[0] + " (Inclusive)")
    print("You have 3 guesses")
    number = random.randint(list[1], list[2])
    for i in range(3):
        Guess = int(input())
        if Guess == number:
            print("You got it correct!")
            return True
        elif Guess > number:
            print("Too high")
        elif Guess < number:
            print("Too low")
    print("Oh no! You ran out of guesses")

#Determines game difficulty
def GuessTheNumber():
    EasyGame = ["1 and 5", 1, 5]
    MediumGame = ["1 and 10", 1, 10]
    HardGame = ["1 and 20", 1, 20]
    oogie = False
    while oogie == False:
        difficulty = input("Easy, Medium, or Hard?")
        if difficulty.lower() == "easy":
            GuessGame(EasyGame)
            oogie = True
        elif difficulty.lower() == "medium":
            GuessGame(MediumGame)
            oogie = True
        elif difficulty.lower() == "hard":
            GuessGame(HardGame)
            oogie = True
        else:
            print("You typed in some weird shizz. Try Again")



#Main
GuessTheNumber()

