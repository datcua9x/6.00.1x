"""""
Ex1:
Write a Python function that returns the sublist of strings in aList
that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"],
your function should return: ["cat", "dog"]
This function takes in a list of string
"""""


def lessthan4(aList):
    """
    aList : list of strings
    returns : list of all strings that have less than 4 characters
    """
    s = []
    for i in aList:
        if len(i) < 4:
            s.append(i)
    return s


aList = ["apple", "cat", "dog", "banana"]
print(lessthan4(aList))
