class Solution:
    def floorSqrt(self, n): 
        low = 1
        high = n
        # Binary search on the answers:
        while low <= high:
            mid = (low + high) // 2
            val = mid * mid
            if val <= n:
                # Eliminate the left half:
                low = mid + 1
            else:
                # Eliminate the right half:
                high = mid - 1
        return high

print(Solution().floorSqrt(30))