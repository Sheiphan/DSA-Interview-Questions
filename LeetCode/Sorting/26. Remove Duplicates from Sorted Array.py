class Solution:
    def removeDuplicates(self, nums):
        res = nums.copy()
        nums = ["_"] * len(nums)
        i = 0
        j = 0
        count = 0
        while i < len(res) and j < len(res):
            if res[j] in nums:
                pass
            else:
                nums[i] = res[j]
                i += 1
                count += 1
            j += 1

        return count, nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()

print(s.removeDuplicates(nums))
