# https://leetcode.com/problems/sort-colors/


def sort012(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid<=high:
        if nums[mid] == 1:
            mid+=1
        elif nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid+=1
            low+=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1

nums = [2,0,1]
sort012(nums)
print(nums)