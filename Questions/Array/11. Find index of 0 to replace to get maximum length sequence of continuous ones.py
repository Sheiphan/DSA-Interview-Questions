def findIndexToReplace(nums):
    count = 0  # current max count of consecutive ones.
    max_count = 0  # all the max count of consecutive ones.
    previous_idx_0 = -1  # previous index at which 0 was present.
    ans_idx = -1  # optimal index at which i should convert 0 to 1 to get the max_count.

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = i - previous_idx_0
            previous_idx_0 = i
        if count > max_count:
            max_count = count
            ans_idx = previous_idx_0
    return max_count


def findIndexToReplace2(nums):
    flip = i = j = ans = 0
    n = len(nums)

    while i < n:
        if nums[i] == 0:
            flip += 1
        while flip > 1:
            if nums[j] == 0:
                flip -= 1
            j += 1
        ans = max(ans, i - j + 1)
        i += 1
    return ans


nums = [0, 1, 0, 1, 1, 0, 1, 1]
print(findIndexToReplace(nums))
print(findIndexToReplace2(nums))
