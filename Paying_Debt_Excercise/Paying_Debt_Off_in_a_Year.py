def Calculate(balance, annual_Interest_Rate):
    monthly_Interest_Rate = annual_Interest_Rate / 12.
    time = 12
    for i in range(10, balance, 10):
        b = balance
        n = 0
        while n < time:
            n += 1
            b = (b - i) * (1 + monthly_Interest_Rate)
            if b <= 0:
                return i


print("the minimum payment each month is ", Calculate(3329, 0.2))
