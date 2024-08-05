# https://leetcode.com/problems/move-zeroes/description/


class Solution:
    def moveZeroes(self, nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


nums = [0, 0, 2, 3, 2, 0, 0, 4, 5, 1]
s = Solution()
print(s.moveZeroes(nums))
