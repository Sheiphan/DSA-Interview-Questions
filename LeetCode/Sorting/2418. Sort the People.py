class Solution:
    def sortPeople(self, names, heights):
        people_sorted = sorted(zip(heights, names), reverse=True)
        
        # Extract and return the names from the sorted list
        sorted_names = [name for _, name in people_sorted]
        
        return sorted_names

# Example usage
names = ["Alice","Bob","Bob"]
heights = [155,185,150]

s = Solution()
sorted_names = s.sortPeople(names, heights)
print(sorted_names)  # Output should be the names sorted by heights in descending order
