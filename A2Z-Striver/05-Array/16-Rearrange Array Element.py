from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        posidx = 0
        negidx = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[posidx] = nums[i]
                posidx += 2
            else:
                ans[negidx] = nums[i]
                negidx += 2
        return ans


nums = [3, 1, -2, -5, 2, -4]
s = Solution()
print(s.rearrangeArray(nums))
