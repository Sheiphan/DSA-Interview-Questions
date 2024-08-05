from typing import List


class BruteForce:
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = []

        for i in range(len(height)):
            max = height[i]
            for j in range(i, len(height)):
                if height[j] > max:
                    max = height[j]
            rightmax.append(max)

            max = height[0]
            for j in range(i):
                if height[j] > max:
                    max = height[j]
            leftmax.append(max)

        total_water = 0
        for i in range(len(height)):
            water_height = min(leftmax[i], rightmax[i]) - height[i]
            if water_height > 0:
                total_water += water_height

        return total_water
    
class Better:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n
        
        # Fill leftmax array
        leftmax[0] = height[0]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        
        # Fill rightmax array
        rightmax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])
        
        # Calculate total water trapped
        total_water = 0
        for i in range(n):
            water_height = min(leftmax[i], rightmax[i]) - height[i]
            if water_height > 0:
                total_water += water_height
        
        return total_water


# Example usage
s = BruteForce()
print(s.trap([4, 2, 0, 3, 2, 5]))  # Output: 9
b = Better()
print(b.trap([2, 0, 3, 2]))
