#Slot Machine

#init
import random
symbols = ["♬", "⚡", "7",]
credits = 5
#Main

#Intro
print("Welcome to Gambletown. We're broke as hell so we only have a slot machine")
print("Wanna take a go? (Y/N)")
print("You have 5 credits.")
ans = input().lower()
if ans == "yes" or ans == "y":
    while True:
        print("How many credits would you like to gamble?")
        while True:
            gamble = input()
            try:
                gamble = int(gamble)
                if gamble > credits:
                    print("You don't got enough credits for that, boy or maam. Enter another number.")
                elif gamble <= 0:
                    print("What in tarnation? You cant do that! Enter another number.")
                elif gamble <= credits:
                    print("Okay, let's spin it!")
                    break
            except:
                print("Oopsie! That ain't a whole number")
        credits -= gamble
        #I'm making 7 common and the rest more rare
        num1 = random.choices(symbols, [2,1,4])
        num2 = random.choices(symbols, [2,1,4])
        num3 = random.choices(symbols, [2,1,4])
        print(num1[0] + num2[0] + num3[0])
        if num1[0] == num2[0] and num2[0] == num3[0]:
            if num1[0] == "♬":
                print("Musical Mayhem! You get a buy one get one free deal on half a guitar!")
                print("+" + str(gamble*3) + " credits")
                credits += gamble*3
            elif num1[0] == "⚡":
                print("Jackpot 2: Electric Boogaloo! You have won the greatest prize of all: A Sense of Accomplishment!")
                print("+" + str(gamble*5) + " credits")
                credits += gamble*5
            elif num1[0] == "7":
                print("Jackpot! You get the spare change in my pocket!")
                print("+" + str(gamble*2.5) + " credits")
                credits += gamble*2.5
        elif num1[0] == num2[0] or num2[0] == num3[0] or num1[0] == num3[0]:
            print("Two of a kind! + 2")
            credits += 2
        else:
            print("Ooh! So close! Better luck is coming your way soon. I can feel it")
        if credits > 0:
            print("You have " + str(credits) + " credits. Go again? (Y/N)")
            ans = input().lower()
            if ans == "no" or ans == "n":
                print("Aw, well, I'll see you round stranger.")
                break
        else:
            print("You're too broke to continue.")
            break
else:
    print("Aw, well, I'll see you round stranger.")
