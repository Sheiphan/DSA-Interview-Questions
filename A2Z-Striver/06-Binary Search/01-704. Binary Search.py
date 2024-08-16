# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high > low:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


class Recursion:
    def search(self, nums: List[int], target: int, low: int, high: int) -> int:
        if high < low:
            return -1
        
        mid = high - (high - low) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search(nums, target, mid + 1, high)
        else:
            return self.search(nums, target, low, mid - 1)


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))

nums = [5]
low = 0
high = len(nums) - 1
print(Recursion().search(nums, 5, low, high))
