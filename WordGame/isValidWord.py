WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def flatten(aList):
    """
    aList: The list contains other lists, strings,or ints
    returns: flattened list(eliminate the redundancy elements)
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


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    list1 = []
    list2 = []
    list3 = []
    for key, val in hand.items():
        list1.append(key * val)
    for i in list1:
        i = list(i)
        list2.append(i)
    list2 = flatten(list2)
    for i in word:
        if i in list2:
            list3.append(i)
            list2.remove(i)
    if len(list3) == len(word) and (word in wordList):
        return True
    else:
        return False


def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure = False
    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()

    if not isValidWord(word, handCopy, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print("FAILURE: test_isValidWord()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified wordList?")
            wordInWL = word in wordList
            print("The word", word, "should be in wordList - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True

    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    word = "rapture"

    if isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

        # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
    word = "honey"

    if not isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

        # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
    word = "honey"

    if isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    word = "evil"

    if not isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "even"

    if isValidWord(word, hand, wordList):
        print("FAILURE: test_isValidWord()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)")

        failure = True

    if not failure:
        print("SUCCESS: test_isValidWord()")


wordList = loadWords()
test_isValidWord(wordList)
