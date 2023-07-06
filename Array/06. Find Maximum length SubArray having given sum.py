def duplicateMax(numbers, target):
    # Time: O(n)
    # Space: O(n)
    n = len(numbers)
    prefix_sum_array = [0] * n
    for i in range(n):
        if i == 0:
            prefix_sum_array[i] = numbers[i]
        else:
            prefix_sum_array[i] = prefix_sum_array[i - 1] + numbers[i]
    # prefix_sum_array = [5, 11, 6, 11, 14, 19, 22, 20, 20]

    hashmap = {}
    max_length = 0
    for i in range(n):
        # Edge case
        if prefix_sum_array[i] == target:
            max_length = max(max_length, i)
        # Normal
        if prefix_sum_array[i] not in hashmap:
            hashmap[prefix_sum_array[i]] = i
        key = prefix_sum_array[i] - target
        if key in hashmap:
            max_length = max(max_length, i - hashmap[key])

    return max_length


num = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8
print(duplicateMax(num, target))


def max_length_subarray_with_sum(arr, target_sum):
    start = 0
    end = 0
    maxLength = 0
    currentSum = arr[0]

    while end < len(arr):
        if currentSum == target_sum:
            maxLength = max(maxLength, end - start + 1)

        if currentSum <= target_sum:
            end += 1
            if end < len(arr):
                currentSum += arr[end]

        else:
            currentSum -= arr[start]
            start += 1

    return maxLength


arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target_sum = 8
result = max_length_subarray_with_sum(arr, target_sum)
print(result)  # Output: 4
