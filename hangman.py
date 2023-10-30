# Imports
from random_word import RandomWords
import re
from functools import reduce

# Main function
def hangman():
    # Variables
    wordList = RandomWords()
    randomWord = wordList.get_random_word()

    # Guess preview prep
    letterList = []
    currentGuess = ""
    num1 = 0
    while num1 < len(randomWord):
        currentGuess = currentGuess + "_"
        num1 = num1 + 1

    # Other prep
    guessNum = len(randomWord)
    print("\nHANGMAN\nA random word has been generated. You get one guess for every letter it contains. Try to guess it!")
    print(currentGuess)

    # User guessing a letter
    while guessNum > 1:
        print("\nYou have " + str(guessNum) + " guesses left!")
        letterGuess = input("Input 'Word' if you are ready to guess, otherwise input one letter: \n")

        # 'Emergency' exit
        if letterGuess == "Stop":
            exit()

        # User guesses a word
        elif letterGuess == "Word":
            wordGuess = input("You chose to try to guess the word. Input your guess here: \n").lower()
            if wordGuess == randomWord:
                userRepeat = input("That is correct! Would you like to go again? Y/N \n")
                if userRepeat == "Y":
                    hangman()
                else:
                    exit()
            else:
                print("\nThat's not it..")
                guessNum = guessNum - 1

        # User guessed a letter
        elif len(letterGuess) == 1:
            # Search for guessed letter in the random word
            letterGuess = letterGuess.lower()
            letterList.append(letterGuess)
            searchLetter = re.finditer(letterGuess, randomWord)
            letterRes = reduce(lambda x, y: x + [y.start()], searchLetter, [])

            # Change word preview with newly guessed letter
            currentList = list(currentGuess)
            num2 = 0
            while num2 < len(letterRes):
                currentList[letterRes[num2]] = letterGuess
                num2 = num2 + 1
            currentGuess = ''.join(currentList)

            # Show word preview
            print("\nYour letter revealed this: \n" + currentGuess)
            print("You have guessed these letters: " + str(letterList))

            # Search for blank spaces in preview
            searchBlank = re.finditer("_", currentGuess)
            blankRes = reduce(lambda x, y: x + [y.start()], searchBlank, [])
            if len(blankRes) == 0:
                userRepeat = input("\nYou found the word! Would you like to go again? Y/N \n")
                if userRepeat == "Y":
                    hangman()
                else:
                    exit()

            # End
            guessNum = guessNum - 1

        else:
            print("That is not one letter! Try again...\n")

    # Last guess
    if (guessNum == 1):
        wordGuess = input("\nThis is your last guess, you'll have to try to guess the word: \n").lower()
        if wordGuess == randomWord:
            userRepeat = input("\nThat is correct! Would you like to go again? Y/N \n")
            if userRepeat == "Y":
                hangman()
            else:
                exit()
        else:
            userRepeat = input("\nThat's not it, the word was: " + randomWord + ". Would you like to try again? Y/N \n")
            if userRepeat == "Y":
                hangman()
            else:
                exit()

    # Repeat question
    userRepeat = input("You couldn't guess the word within the allowed amount of guesses.. Try again? Y/N \n")

# Start
hangman()