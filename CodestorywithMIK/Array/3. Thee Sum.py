from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total_res = []
        
        for k in range(len(nums)):
            # Skip the same element to avoid duplicate triplets
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            n1 = nums[k]
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                sum_val = n1 + nums[i] + nums[j]
                if sum_val < 0:
                    i += 1   
                elif sum_val > 0:
                    j -= 1
                else:
                    total_res.append([n1, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    
                    # Skip duplicates for the second number
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    # Skip duplicates for the third number
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        
        return total_res

# Example usage
s = Solution()
print(s.threeSum([-4, -1, -1, 0, 0, 1, 2, 2]))  # Output: [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1]]
