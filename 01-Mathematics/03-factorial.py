def cal_factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


print(cal_factorial(5))


def cal_factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * cal_factorial_recursive(n - 1)


print(cal_factorial_recursive(5))
