guess = 0
cube = 127
epsilon = 0.01
increment = 0.0001
count = 0

while abs(guess**3-cube) >= epsilon:
    guess += increment
    count += 1
print('number of iterations is', count)
if abs(guess**3-cube) >= epsilon:
    print('failed on the value ', cube)
else:
    print(guess, 'is close to the value of', cube)