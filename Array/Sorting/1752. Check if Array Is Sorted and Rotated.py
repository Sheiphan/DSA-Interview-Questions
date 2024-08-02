class Solution1:
    # O(n)
    def check(self, nums):
        count = 0

        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count += 1
            if count > 1:
                return False

        return True


class Solution2:
    def check(self, nums):
        a = nums.copy()
        a.sort()
        n = len(nums)
        for i in range(n):
            if nums == a:
                return True
            nums = nums[1:] + nums[:1]

        return False


s = Solution2()
s.check([3, 4, 5, 1, 2])
