low = 0
high = 100
guess = (low + high) / 2.0
print("Please think of a number between 0 and 100!")
print("Is your secret number", guess, '?')
x = input
while x != 'c':
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
              "indicate I guessed correctly. Your choice is =")
    if x == 'h':
        high = guess
        guess = int((low + high) / 2)
        print("is your secrete number is", guess, '?')
    if x == 'l':
        low = guess
        guess = int((low + high) / 2)
        print("is your secrete number is", guess, '?')
    if x != 'l' and x!= 'h' and x!='c':
        print("Sorry, I did not understand your input")
    if x == 'c':
        print("game over,your secrete number is ", guess)
