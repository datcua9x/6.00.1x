animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    count = 0
    for i in aDict.values():
        count += len(i)
    return count


def biggest(aDict):
    result = None
    biggest = 0
    for i in aDict.keys():
        if len(aDict[i]) > biggest:
            result = i
            biggest = len(aDict[i])
    return result


print(how_many(animals))
print(biggest(animals))

