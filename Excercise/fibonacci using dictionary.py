def cal_fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = cal_fib(n - 1, d) + cal_fib(n - 2, d)
        d[n] = ans  # store the value of ans in d[n] to reuse it instead of recompute
        print(d)
    return ans


d = {1: 1, 2: 2}
print(cal_fib(10, d))
