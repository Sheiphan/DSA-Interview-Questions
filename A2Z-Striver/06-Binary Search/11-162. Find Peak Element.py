# https://leetcode.com/problems/find-peak-element/description/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1

        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


nums = [1, 2, 1, 3, 5, 6, 4]
print(Solution().findPeakElement(nums))
