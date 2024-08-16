# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Find out how many times has an array been rotated
from typing import List
import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = sys.maxsize

        while low <= high:
            mid = (high + low) // 2

            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1

        return nums.index(ans)


nums = [3, 3, 4, 1, 2, 3]
print(Solution().findMin(nums))
