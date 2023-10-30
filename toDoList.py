# Starting list var
aList = ["Cat", "Dog", "Bird", "Couch", "Pig"]

# Main function
def someList():
    print("\nYOUR LIST")
    if len(aList) == 0:
        print("Your list has no items, add some!")
    else:
        i = 0
        for item in aList:
            i = i + 1
            print(str(i) + ". " + item)
    
    action = input("\nWhat would you like to do with your list? Enter: 'Add' to add an item to the list, 'Remove' to remove an item from the list, 'Move' to move an item up or down, 'Stop' to stop the application\n")
    if action == "Add":
        addToList()
    elif action == "Remove":
        removeFromList()
    elif action == "Move":
        moveInList()
    elif action == "Stop":
        exit()
    else:
        print("Invalid action, try again..")
        someList()

# Function to add an item to the list
def addToList():
    print("\nADD")
    newItem = input("Enter your new list item: \n")
    aList.append(newItem)

    someList()

# Function to remove an item from the list
def removeFromList():
    print("\nREMOVE")
    removeNum = int(input("Enter the number of the item you want to remove: \n"))
    if removeNum < 1:
        print("The number you put in does not correspond to an item, try again..")
        removeFromList()
    if removeNum > len(aList):
        print("The number you put in does not correspond to an item, try again..")
        removeFromList()
    else:
        aList.pop((removeNum - 1))
        someList()

# Function to move an item within the list
def moveInList():
    print("\nMOVE")
    moveFrom = int(input("Enter the number of the item you want to move: \n"))
    if moveFrom > len(aList):
        print("The number you put in does not correspond to an item, try again..")
        moveInList()
    else:
        print("Moving " + str(moveFrom) + ". '" + aList[(moveFrom - 1)] + "'")
        moveTo = int(input("Where would you like to move this item to? Enter here: \n"))
        if moveTo > len(aList):
            print("Target position out of list range! Try again..")
            moveInList()
        elif moveTo == moveFrom:
            print("The target position cannot be the same as the item position. Try again..")
            moveInList()
        else:
            placeHolder = aList[(moveFrom - 1)]
            aList.pop((moveFrom - 1))
            aList.insert((moveTo - 1), placeHolder)
            someList()

# Start
someList()