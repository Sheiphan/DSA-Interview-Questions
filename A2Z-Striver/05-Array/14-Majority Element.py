# https://leetcode.com/problems/majority-element/


def majorityElement(nums):
    current = 0
    count = 0
    for i in range(len(nums)):
        if count == 0:
            current = nums[i]
        elif current == nums[i]:
            count += 1
        else:
            count -= 1

    return current


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
