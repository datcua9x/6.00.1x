def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    for i in hand:
        count += 1
    return count


hand = {}
print(calculateHandlen(hand))
