def sortDutch(numbers):
    # Time: O(n)
    # Space: O(1)
    curr = 0
    start = 0
    end = len(numbers)-1

    while curr <= end:
        if numbers[curr] == 0:
            temp = numbers[curr]
            numbers[curr] = numbers[start]
            numbers[start] = temp
            curr += 1
            start += 1

        elif numbers[curr] == 1:
            curr += 1

        elif numbers[curr] == 2:
            temp = numbers[curr]
            numbers[curr] = numbers[end]
            numbers[end] = temp
            end -= 1
        else:
            return -1
    return numbers


num = [0, 0, 1, 0, 2, 1, 2, 1, 2, 2]
print(sortDutch(num))
