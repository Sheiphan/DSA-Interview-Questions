# https://leetcode.com/problems/target-sum/

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            Sum = 0
            for j in range(len(nums)):
                if i != j:
                    Sum = Sum + nums[j]
                else:
                    Sum -= nums[j]
            if Sum == target:
                count += 1

        return count


nums = [1, 1, 1, 1, 1]
target = 3

print(Solution().findTargetSumWays(nums, target))
