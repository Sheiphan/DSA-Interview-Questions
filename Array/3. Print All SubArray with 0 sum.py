def allZeroSumSubarrays(numbers):
    hashmap = {}
    n = len(numbers)
    prefix_sum_array = [0] * n
    # Cumulative sum
    for i in range(n):
        if i == 0:
            prefix_sum_array[i] = numbers[i]
        else:
            prefix_sum_array[i] = numbers[i] + prefix_sum_array[i - 1]

    # Add number of occurrence of an item in prefix_sum_array
    for i in range(n):
        if prefix_sum_array[i] not in hashmap:
            hashmap[prefix_sum_array[i]] = [i]
        else:
            hashmap[prefix_sum_array[i]].append(i)

    # index of the subarray with sum of zero
    answer = []
    for key, value in hashmap.items():
        if len(value) > 1 or key == 0:
            # zero in itself is a subarray with sum zero
            if key == 0:
                for val in value:
                    answer.append((0, val))
                for j in range(len(value) - 1):
                    for k in range(j + 1, len(value)):
                        answer.append((value[j] + 1, value[k]))
            # when key != 0 get all the pair (successive value + 1, preceding value)
            else:
                for j in range(len(value) - 1):
                    for k in range(j + 1, len(value)):
                        answer.append((value[j] + 1, value[k]))
    return answer


num = [4, -1, 8, 0, 4, -4, -6, 3, 3]
print(allZeroSumSubarrays(num))