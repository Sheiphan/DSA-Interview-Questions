from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return []

        # Initialize the result array with -1 for the last element
        ans = [-1] * n

        # Initialize the maximum element to the right with the last element
        max_to_right = arr[-1]

        # Iterate from the second-to-last element to the first element
        for i in range(n - 2, -1, -1):
            # Update the current element in the result array with max_to_right
            ans[i] = max_to_right
            # Update max_to_right with the maximum of the current element and max_to_right
            max_to_right = max(max_to_right, arr[i])

        return ans
