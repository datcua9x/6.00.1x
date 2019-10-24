def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    """
    if aStr != '':
        if char == aStr[0]:
            return True
        elif len(aStr) == 1:
            return False
        else:
            return isIn(char, aStr[1:])
    else:
        return False


print(isIn('a', 'abcdefghik'))
