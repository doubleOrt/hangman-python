
import os
import random

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
toad trout turkey turtle weasel whale wolf wombat zebra'''.split(' ')

clearConsole = lambda: os.system("clear")

def startGame():
    word = random.choice(words)
    letters = list(word)
    numLetters = len(word)
    hiddenWord = list("_" * numLetters)
    numLives = numLetters + 3
    guessResultString = ""

    def displayHiddenWord(userHasWon = False):
        # just a simple conditional so that we print something a little fancier when the user wins
        if not userHasWon:
            print(' '.join(hiddenWord))
        else:
            print("~~~ " + (''.join(hiddenWord)).upper() + " ~~~")

    def userHasWon():
        print("\n")
        print("You are now a certified genius (though your mom knew all along, trust your mom, live a healthy life)!")

    def displayStatusToConsole(userHasWon = False):
        clearConsole()
        print("Number of lives: " + str(numLives))
        print(word)
        displayHiddenWord(userHasWon)
        print(guessResultString)

    correctGuesses = 0
    while True:
        displayStatusToConsole()
        if numLives > 0:
            print("\n")
            userGuess = input("Enter letter: ")
            if userGuess in letters:
                indexOfGuessInWord = letters.index(userGuess)
                hiddenWord[indexOfGuessInWord] = userGuess
                correctGuesses += 1

                # without this, already-guessed letters will count as correct guesses; if you delete the element
                # from letters instead, then it will cause another bug in the game. This is the fix for both.
                letters[indexOfGuessInWord] = str(random.random())

                if correctGuesses == numLetters:
                    displayStatusToConsole(True)
                    userHasWon()
                    break
                guessResultString = "Good!"
            else:
                numLives -= 1
                guessResultString = "Nope!"
        else:
            print("Poor fucker's gonna hang :(")
            break

    return "\n\nThank you for playing!!! Have a good one now!"


print(startGame())
