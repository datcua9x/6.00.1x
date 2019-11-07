def getGuessedWord(secretWord, lettersGuessed):
    """'
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    ''"""
    str = []
    for i in secretWord:
        if i in lettersGuessed:
            str.append(i)
        else:
            str.append('_')
    return "".join(str)


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
