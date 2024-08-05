def TwoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in hashmap:
            return [hashmap[remaining], i]
        else:
            hashmap[nums[i]] = i


TwoSum([3,2,4], 6)
