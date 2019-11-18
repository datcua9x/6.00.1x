"""
Ex3:
Write a function to flatten a list. The list contains other lists, strings,
or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened
into [1,'a','cat',2,3,'dog',4,5] (order matters).
"""


def flatten(aList):
    """
    aList: The list contains other lists, strings,or ints
    returns: flattened list(eliminate the redundancy element)
    """
    if not aList:
        return []
    for i in aList:
        if type(i) == list:
            aList.remove(i)
            return flatten(aList) + flatten(i)
        else:
            aList.remove(i)
            return [i] + flatten(aList)


aList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

print(flatten(aList))
