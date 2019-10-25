def Calculate(balance, annual_Interest_Rate, monthly_Interest_rate, i):
    b = (balance - (monthly_Interest_rate * balance)) + (balance - (monthly_Interest_rate * balance)) * (
            annual_Interest_Rate / 12.0)
    if i == 1:
        return b
    if i == 0:
        return balance
    else:
        return Calculate(b, annual_Interest_Rate, monthly_Interest_rate, i - 1)


print("Reamaing balence",round(Calculate(5000, 0.18, 0.02, 12), 1))
