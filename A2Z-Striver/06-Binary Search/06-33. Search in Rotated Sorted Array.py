# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[high]:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                if target <= nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution().search(nums, target))
