# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        else:
            return [lb, self.upperBound(nums, target) - 1]

    def lowerBound(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while high >= low:
            mid = (high + low) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upperBound(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while high >= low:
            mid = (high + low) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


class BinarySearch:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccurence(nums, target)
        last = self.lastOccurence(nums, target)

        if nums[first] != target or first == len(nums):
            return [-1, -1]

        return [first, last]

    def firstOccurence(self, nums, target):
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def lastOccurence(self, nums, target):
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high


nums = [1, 1, 2, 2, 2, 2, 3]
print(BinarySearch().searchRange(nums, 4))
