#Madlib Generator

#init
import random
#Big list of words
adjectives = ["Charming","Charismatic","Moronic","Imbecilic","Foolish","Powerful", "Scary", "Horrifying", "Bone-chilling", "Awesome", "Rad", "Radical", "Extraordinary", "Impossible", "Run-of-the-mill", "Everyday", "Money-making", "Jaw-dropping"]
nouns = ["Man", "Woman", "Zombie", "Family", "Bus", "Car", "Apple", "Orange", "Knife", "Child", "Baby", "Truck", "Toilet", "Fool", "Genius", "Steel rod", "Monk", "Warrior of 1000 punches", "Skeleton", "Gorbgalorb", "Dingleberry", '"Penis-head"', '"Berry-boy"', '"Dung-Lord"',]
verbs = ["Makes", "Kills", "Wants", "Absorbs", "Destroys", "Maliciously buys", "Sells", "Eats", "Gobbles", "Finds love with", '"Never knew they needed"', "Obtains power of"]
#functions

#Generates an Adjective - Noun - Verb - Adjective - Noun sentence
#Lets the user choose one of the 5 words at random
def madLib():
    go = True
    while go == True:
        #determines which word we will be letting the user choose
        which = random.randint(1, 5)
        if which == 1:
            #First Adjective in the sentence
            adj1 = input("Give me an adjective")
            #Second Adjective in the sentence
            adj2 = adjectives[random.randint(0, (len(adjectives) - 1))]
            #First Noun
            noun1 = nouns[random.randint(0, (len(nouns) - 1))]
            #Second Noun
            noun2 = nouns[random.randint(0, (len(nouns) - 1))]
            #The Verb
            verb = verbs[random.randint(0, (len(verbs) - 1))]
            print(adj1 + " " + noun1.lower() + " " + verb.lower() + " " + adj2.lower() + " " + noun2.lower())
        if which == 2:
            adj2 = input("Give me an adjective")
            adj1 = adjectives[random.randint(0, (len(adjectives) - 1))]
            noun1 = nouns[random.randint(0, (len(nouns) - 1))]
            noun2 = nouns[random.randint(0, (len(nouns) - 1))]
            verb = verbs[random.randint(0, (len(verbs) - 1))]
            print(adj1 + " " + noun1.lower() + " " + verb.lower() + " " + adj2.lower() + " " + noun2.lower())
        if which == 3:
            adj2 = adjectives[random.randint(0, (len(adjectives) - 1))]
            adj1 = adjectives[random.randint(0, (len(adjectives) - 1))]
            noun1 = input("Give me a singular noun")
            noun2 = nouns[random.randint(0, (len(nouns) - 1))]
            verb = verbs[random.randint(0, (len(verbs) - 1))]
            print(adj1 + " " + noun1.lower() + " " + verb.lower() + " " + adj2.lower() + " " + noun2.lower())
        if which == 4:
            adj2 = adjectives[random.randint(0, (len(adjectives) - 1))]
            adj1 = adjectives[random.randint(0, (len(adjectives) - 1))]
            noun2 = input("Give me a singular noun")
            noun1 = nouns[random.randint(0, (len(nouns) - 1))]
            verb = verbs[random.randint(0, (len(verbs) - 1))]
            print(adj1 + " " + noun1.lower() + " " + verb.lower() + " " + adj2.lower() + " " + noun2.lower())
        if which == 5:
            adj2 = adjectives[random.randint(0, (len(adjectives) - 1))]
            adj1 = adjectives[random.randint(0, (len(adjectives) - 1))]
            noun1 = nouns[random.randint(0, (len(nouns) - 1))]
            noun2 = nouns[random.randint(0, (len(nouns) - 1))]
            verb = input("Give me a verb")
            print(adj1 + " " + noun1.lower() + " " + verb.lower() + " " + adj2.lower() + " " + noun2.lower())
        print("Madlib again? (Y/N)")
        again = input()
        if again.lower() == "n":
            break
        if again.lower() != "y":
            print("Please enter Y or N")
#main
madLib()

