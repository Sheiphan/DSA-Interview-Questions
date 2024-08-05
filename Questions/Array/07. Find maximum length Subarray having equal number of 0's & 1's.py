def findMaxLength(nums):
    maxLen = 0
    count_dict = {}
    count = 0

    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count == 0:
            maxLen = i + 1
        elif count in count_dict:
            maxLen = max(maxLen, i - count_dict[count])
        else:
            count_dict[count] = i

    return maxLen


# Function to find the largest sublist having an equal number of 0's and 1's
def findLargestSublist(nums):
    n = len(nums)
    prefix_sum = [0]*n
    for i in range(n):
        if nums[i] == 0:
            nums[i] = -1

    for i in range(n):
        if i == 0:
            prefix_sum[i] = nums[i]
        else:
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

    hashmap = {}
    max_length = 0
    for i in range(n):
        if prefix_sum[i] == 0:
            max_length = max(max_length, i + 1)

        if prefix_sum[i] not in hashmap:
            hashmap[prefix_sum[i]] = i
        else:
            max_length = max(max_length, i - hashmap[prefix_sum[i]])

    return max_length


arr = [0, 0, 1, 0, 1, 0, 1]
print(findMaxLength(arr))
print(findLargestSublist(arr))
