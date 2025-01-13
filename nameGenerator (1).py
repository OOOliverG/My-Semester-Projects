#Oliver Giron

#init

#Functions
#Quiz to determine your new name

#Each question is it's own function that loops if you don't input a valid answer

#Once you get to the end, all of the loops end and you get your final name
#Last Question
def awe_or_epi():
    answer = input("Would you say you're more Awesomesauce(1) or Epicburger(2)?")
    if answer.lower() == "awesomesauce" or answer == "1":
        print('Your new name is: John Coolio!')
        return True
    elif answer.lower() == "epicburger" or answer == "2":
        print("You are now The WHAMburglar!")
        return True
    else:
        print("Please enter a valid response")
#Last Question
def rei_or_hea():
    answer = input("Reincarnation(1) or Heaven(2)?")
    if answer.lower() == "reincarnation" or answer == "1":
        print('You have become: Nine Live Norris')
        return True
    elif answer.lower() == "heaven" or answer == "2":
        print("You have been dubbed: Holy Broly")
        return True
    else:
        print("Please enter a valid response")
        return False
#Last Question
def spo_or_sca():
    answer = input("Are you Spooky(1) or Scary(2)?")
    if answer.lower() == "spooky" or answer == "1":
        print('You are the second coming of Skizzy Skellington!')
        return True
    elif answer.lower() == "scary" or answer == "2":
        print("Oh the horror! The world trembles in the wake of you, Jonathan Evil!")
        return True
    else:
        print("Please enter a valid response")
        return False
#Last Question
def big_or_sma():
    answer = input("Are you Big(1) or Small(2)?")
    if answer.lower() == "big" or answer == "1":
        print('You are now known as: Stupid Samson')
        return True
    elif answer.lower() == "small" or answer == "2":
        print("Welcome back: Dumb Dave")
        return True
    else:
        print("Please enter a valid response")
        return False
#2nd Question
def rad_or_rel():
    answer = input("Are you Rad(1) or Religious(2)")
    if answer.lower() == "rad" or answer == "1":
        go = False
        while go == False:
            go = awe_or_epi()
    elif answer.lower() == "religious" or answer == "2":
        go = False
        while go == False:
            go = rei_or_hea()
    else:
        print("Please enter a valid response")
        return False
#2nd Question
def mal_or_ign():
    answer = input("Are you Malicious(1) or Ignorant(2)")
    if answer.lower() == "malicious" or answer == "1":
        go = False
        while go == False:
            go = spo_or_sca()
    elif answer.lower() == "ignorant" or answer == "2":
        go = False
        while go == False:
            go = big_or_sma()
    else:
        print("Please enter a valid response")
        return False
#First Question
def goo_or_evi():
    answer = input("Are you Good(1) or Evil(2)")
    if answer.lower() == "good" or answer == "1":
        go = False
        while go == False:
            go = rad_or_rel()
    elif answer.lower() == "evil" or answer == "2":
        go = False
        while go == False:
            go = mal_or_ign()
    else:
        print("Please enter a valid response")
        return False

def quizzington():
    go = False
    while go == False:
        go = goo_or_evi()
#main

quizzington()
