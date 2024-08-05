def largestSubArrayConsecutiveInt(nums):
    n = len(nums)
    max_length = 0
    for i in range(n):
        for j in range(1+i, n):
            diff = (max(nums[i:j]) - min(nums[i:j]))
            if j-i == diff:
                max_length = max(max_length, j-i+1)
    return max_length


arr = [5,14,13,11,12,7,6,5,3,4]
print(largestSubArrayConsecutiveInt(arr))
