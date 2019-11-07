import string


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


lettersGuessed = ['a','p,']
print(getAvailableLetters(lettersGuessed))
