def zeroSumSubarray(numbers):
    numbers_set = set()
    n = len(numbers)
    prefix_sum_array = [0] * n
    for i in range(n):
        if i == 0:
            prefix_sum_array[i] = numbers[i]
        else:
            prefix_sum_array[i] = numbers[i] + prefix_sum_array[i - 1]

    for i in range(n):
        if prefix_sum_array[i] in numbers_set:
            return True
        numbers_set.add(prefix_sum_array[i])
    if 0 in numbers_set:
        return True
    else:
        return False


num = [10, 20, -30, 1, 7]
print(zeroSumSubarray(num))
