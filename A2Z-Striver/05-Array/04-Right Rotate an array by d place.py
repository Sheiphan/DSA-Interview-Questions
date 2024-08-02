# https://leetcode.com/problems/rotate-array/description/


class Solution:
    def rotate(self, nums, k):
        rotated_array = [0] * len(nums)
        for i in range(len(nums)):
            rotated_array[(i + k) % len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = rotated_array[i]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s = Solution()
s.rotate(nums, k)
print(nums)
