#ToDo List
#Oliver Giron

#init
list = ["Do laundry", "Complete homework", "Survive the zombie apocalypse", "Die in a meteor strike"]
exit = False
#function

#main

print("Welcome to your To Do list! Hopefully you'll actually do your stuff now!")
while True:
    if exit == True:
        break
    print("Current Tasks:")
    for item in list:
        print(str(list.index(item)+1) + ". " + item)
    print("""Would you like to
A. Add a task
B. Remove a task
C. Sort the tasks alphabetically
D. Exit Program""")
    while True:
        ans = input().lower()
        if ans == "a":
            print("What task would you like to add?")
            addTask = input()
            list.append(addTask)
            break
        elif ans == "b":
            print("What task would you like to remove (Please select using task number)")
            if len(list) == 0:
                print("No tasks in list")
                break
            while True:
                removeTask = input()
                try:
                    removeTask = int(removeTask)
                    list.pop(removeTask-1)
                    break
                except:
                    print("Invalid task position. Try again.")
            break
        elif ans == "c":
            list.sort()
            break
        elif ans == "d":
            exit = True
            break
        else:
            print("Invalid Input. Try again")

