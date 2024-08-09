# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class BruteForce:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for i in range(len(nums)):
            x = nums[i]
            count = 1
            while self.ls(nums, x + 1):
                x += 1
                count += 1
            longest = max(count, longest)
        return longest

    def ls(self, arr, num):
        for j in range(len(arr)):
            if num == arr[j]:
                return True
        return False


class Optimal:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        longest = 1
        unordered_set = set(nums)
        # for i in range(n):
        #     unordered_set.add(nums[i])

        for i in unordered_set:
            if i - 1 not in unordered_set:
                count = 1
                x = i
                while x + 1 in unordered_set:
                    x += 1
                    count += 1
                longest = max(longest, count)
        return longest


nums = [100,4,200,1,3,2, 101,102]
print(Optimal().longestConsecutive(nums))
