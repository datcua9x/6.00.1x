# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str = []
    for i in secretWord:
        if i in lettersGuessed:
            str.append(i)
        else:
            str.append('_')
    return "".join(str)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = []
    str = string.ascii_lowercase
    for i in str:
        if i not in lettersGuessed:
            s.append(i)
    return "".join(s)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    lettersGuessed = []
    live = 8
    WrongLetters = []
    while True:
        print("---------------------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        elif live == 0:
            print("Sorry, you ran out of guesses.The answer is", secretWord)
            break
        # WrongLetters is the list of wrong guesses
        # LetterGuessed is the lis of correct guesses
        Used = WrongLetters + lettersGuessed
        print("you have", live, "guesses left")
        print("Available letters:", getAvailableLetters(Used))
        word = input("Please guess a letter: ")
        guess = word.lower()  # turn guess word into lower case
        if guess in Used:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        if (guess in secretWord) and (guess not in Used):
            lettersGuessed.append(guess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        if (guess not in secretWord) and (guess not in Used) and (guess in string.ascii_lowercase):
            WrongLetters.append(guess)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            live -= 1
        if guess not in string.ascii_lowercase:
            print("Please enter a word from a to z")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
