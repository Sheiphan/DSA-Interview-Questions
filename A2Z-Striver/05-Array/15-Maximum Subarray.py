from typing import List


class MajorityVote:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxi = float("-inf")
        for i in nums:
            s += i
            if s > maxi:
                maxi = s
            if s < 0:
                s = 0
                start = i

        return int(maxi)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

            current_sum = max(nums[i], current_sum + nums[i])

            max_sum = max(max_sum, current_sum)

        return max_sum


def maxSubarraySum(arr):
    maxi = float("-inf")  # maximum sum
    sum = 0
    n = len(arr)
    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")

    # To consider the sum of the empty subarray
    # uncomment the following check:

    # if maxi < 0:
    #     maxi = 0

    return maxi


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubarraySum(arr)
print("The maximum subarray sum is:", maxSum)
