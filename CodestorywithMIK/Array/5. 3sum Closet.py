# https://leetcode.com/problems/3sum-closest/description/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float("inf")
        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                Sum = nums[k] + nums[i] + nums[j]
                if abs(target - Sum) < abs(target - closest_sum):
                    closest_sum = Sum
                if Sum > target:
                    j -= 1
                elif Sum < target:
                    i += 1
                else:
                    return target

        return int(closest_sum)


arr = [1, 1, -1]
s = Solution()
print(s.threeSumClosest(arr, 12))
