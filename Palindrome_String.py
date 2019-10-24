import re


def Palindrome(c):
    if len(c) == 0 or len(c) == 1:
        return print("string is a Palindrome")
    else:
        return c[0] == c[-1] and Palindrome(c[1:-1])


c = 'Able was I,ere I  saw Elba'
c = c.lower()
c = re.sub('[^A-Za-z0-9]+', '', c)

print(Palindrome(c))