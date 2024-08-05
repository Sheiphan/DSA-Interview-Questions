def sortCount(numbers):
    n = len(numbers)
    answer = []
    count = 0
    for i in numbers:
        if i == 0: count += 1

    # Method 1 using a new list answer
    for j in range(count):
        answer.append(0)
    for k in range(n - count):
        answer.append(1)
    return answer

    # Method 2 using the original array
    for i in range(n):
        if count:
            numbers[i] = 0
            count -= 1
        else:
            numbers[i] = 1
    return numbers


def sortSwap(numbers):
    start = 0
    idx = 0
    while idx < len(numbers):
        if numbers[idx] == 0:
            temp = numbers[idx]
            numbers[idx] = numbers[start]
            numbers[start] = temp
            # start will only be incremented when the idx is zero.
            # number[start] will always have '1'
            start += 1
        idx += 1
    return numbers


num = [1, 0, 1, 0, 0, 1, 1]
print(sortCount(num))
print(sortSwap(num))
