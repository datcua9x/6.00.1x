def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if aStr == ' ':
        return False
    if aStr <= 1:
        return aStr == char

    midchar = str[int(len(aStr)/2)]
    midindex= len(aStr)//2





