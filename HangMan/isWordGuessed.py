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


secretWord = 'apple'
lettersGuessed = ['a','p','p','l','e']
print(isWordGuessed(secretWord, lettersGuessed))
