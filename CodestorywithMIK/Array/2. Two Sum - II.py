def TwoSum(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            return [i + 1, j + 1]


TwoSum([2,7,11,15], 9)
