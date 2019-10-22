num = -19

if num < 0:
    check = True
    num = abs(num)
else:
    check = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if check:
    result = '-' + result

print(result)

