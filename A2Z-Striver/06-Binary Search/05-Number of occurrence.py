class Solution:
    def count(self, nums, target):
        first = self.firstOccurence(nums, target)

        if first == len(nums) or nums[first] != target:
            return 0

        last = self.lastOccurence(nums, target)
        return int(last - first) + 1

    def firstOccurence(self, nums, target):
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def lastOccurence(self, nums, target):
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high


nums = [1, 1, 2, 2, 2, 2, 3]
print(Solution().count(nums, 1))
