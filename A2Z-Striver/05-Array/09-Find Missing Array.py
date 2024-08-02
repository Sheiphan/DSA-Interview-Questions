def findMissingArray(arr, n):
    total_sum_N = (n * (n + 1)) / 2

    sumNum = 0
    for i in arr:
        sumNum += i

    return int(total_sum_N - sumNum)


arr = [1, 2, 4, 5]
print(findMissingArray(arr, 5))
