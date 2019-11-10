"""
Ex5
Write a Python function that returns a list of keys in aDict with the value
target. The list of keys you return should be sorted in increasing order.
The keys and values in aDict are both integers. (If aDict does not contain
the value target, you should return an empty list.)
This function takes in a dictionary and an integer and returns a list.
"""


def keysWithValue(aDict, value):
    """
    aDict: a dictionary
    value: an integer
    return: list of keys in aDict with the value target
    """
    s = []
    for i in aDict:
        if aDict[i] == value:
            s.append(i)

    return s


aDict = {1: 11, 2: 11, 3: 33, 5: 11, 4: 44}

print(keysWithValue(aDict, 11))
