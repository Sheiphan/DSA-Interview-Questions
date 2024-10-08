# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1

        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (
                mid % 2 == 0 and nums[mid + 1] == nums[mid]
            ):
                low = mid + 1
            else:
                high = mid - 1
        return -1


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(Solution().singleNonDuplicate(nums))
