def fancy_divide(list_of_numbers, index):
    try:
        denom = list_of_numbers[index]
    except IndexError:
        return fancy_divide(list_of_numbers, len(list_of_numbers) - 1)
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


print(fancy_divide([0, 2, 9], 3))
