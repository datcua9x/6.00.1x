"""
Ex2:
Write a recursive Python function, given a non-negative integer n,
to calculate the no. of occurrences of digit 7 in n.
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
This function has to be recursive; you may not use loops!
This function takes in one integer and returns one integer.
"""


def count7(n):
    """
    n: non-negative integer
    returns :
    """
    if n == 0:
        return 0
    elif n % 10 == 7:
        return 1 + count7(n // 10)
    else:
        return 0 + count7(n // 10)


print(count7(7213712))
