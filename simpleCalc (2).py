#Oliver Giron

#Init
#Functions
def calced(string):
    x = 0
    firstNumber = ""
    secondNumber = ""
    #Determines first number to use
    for digit in string:
        if digit.isnumeric() or (digit == "."):
            firstNumber = firstNumber + digit
            x = x+1
        elif digit == " ":
            x = x+1
        else:
            break
    #New string to preserve the old one
    lastBit = list(string)
    #Finds second number
    for i in range(x+1):
        lastBit.pop(0)
    for digit in lastBit:
        if digit.isnumeric() or (digit == "."):
            secondNumber = secondNumber + digit
        elif digit == " ":
            x = x
        else:
            break
    #Finds operator
    if list(string)[x] == "+":
        print(float(firstNumber) + float(secondNumber))
    elif list(string)[x] == "-":
        print(float(firstNumber) - float(secondNumber))
    elif list(string)[x] == "/":
        print(float(firstNumber) / float(secondNumber))
    elif list(string)[x] == "*":
        print(float(firstNumber) * float(secondNumber))
    else:
        print("Error: Must use valid operator")

#The actual calculator
def Calculator():
    print("Welcome to Simple Calculator")
    print("You are allowed to add(+), subtract(-), multiply(*), or divide(/) two numbers")
    print("Type quit to quit")
    while True:
        calc = input()
        if calc.lower() == "quit":
            break
        else:
            calced(calc)


#Main

#Addition
#Subtraction
#Multiplication
#Division

Calculator()
