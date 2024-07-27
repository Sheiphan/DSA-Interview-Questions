def sumFirstNNumber(i, sum):
    if i == 0:
        return sum
    return sumFirstNNumber(i - 1, sum + i)


print(sumFirstNNumber(i=3, sum=0))


def sumFirstNNumber2(n):
    if n == 0:
        return 0
    return n + sumFirstNNumber2(n - 1)


print(sumFirstNNumber2(n=3))
