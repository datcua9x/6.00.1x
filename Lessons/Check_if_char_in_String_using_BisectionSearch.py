def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if aStr == ' ':
        return False
    if len(aStr) <= 1:
        return aStr == char
    midindex = len(aStr) // 2
    midchar = aStr[midindex]
    if char == midchar:
        return True
    elif char > midchar:
        return isIn(char, aStr[midindex:])
    else:
        return isIn(char, aStr[:midindex])


print(isIn('a ', ' '))
isIn('b', 'helloworld')