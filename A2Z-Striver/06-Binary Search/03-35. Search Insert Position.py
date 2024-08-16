# https://leetcode.com/problems/search-insert-position/description/

from typing import List


class BinarySearch:
    def searchInsert(self, nums: List[int], target: int) -> int:
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


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1


nums = [1, 3, 5, 6]
target = 7
print(Solution().searchInsert(nums, target))
