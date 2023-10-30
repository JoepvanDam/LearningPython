# Imports
import random

# Main function
def guesser():
    print("\nRANDOM NUMBER GUESSER\n")

    randomNum = random.randint(0,10)
    userGuess = int(input("A random number between 0 and 10 has been generated, you have 3 guesses. Input your first guess here: \n"))
    if userGuess == randomNum:
        print("\nThat's it! You guessed correctly in 1 try.")
        repeater(True)
    else:
        userGuess = int(input("\nThat's not it, try again! You have 2 guesses left, input your second guess here: \n"))
        if userGuess == randomNum:
            print("\nThat's it! You guessed correctly in 2 tries.")
            repeater(True)
        else:
            userGuess = int(input("\nThat's not it either, only 1 guess left... Input your last guess here: \n"))
            if userGuess == randomNum:
                print("\nThat's it! You guessed correctly in 3 tries.")
                repeater(True)
            else:
                repeater(False)

# Function to repeat the guessing (or not)
def repeater(guessed):
    if guessed:
        tryAgain = input("Good job! Would you like to go again? Y/N\n")
    else:
        tryAgain = input("\nYou couldn't guess the number, try again? Y/N\n")
    
    if tryAgain == "Y":
        guesser()
    else:
        exit()

# Start
guesser()