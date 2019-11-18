def Calculate(MinWage, MaxHours):
    while True:
        hours = int(input("enter the number of hours = "))
        if hours <= MaxHours:
            if hours < 40:
                return hours * MinWage
            else:
                return 40 * MinWage + (hours - 40) * (MinWage * 1.5)
            break


print(Calculate(8, 60))
