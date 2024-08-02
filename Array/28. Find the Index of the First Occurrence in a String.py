class Solution:
    def strStr(self, haystack, needle):
        # Return 0 if needle is an empty string
        if not needle:
            return 0
        
        i = j = k = 0  # Initializing the pointers and length of matched substring
        while j < len(haystack):
            if needle[i] == haystack[j]:
                i += 1
                j += 1
                if i == len(needle):  # Full match found
                    return j - i
            else:
                # Reset i and k, move j back to the next character after the first matched character
                j = j - i + 1
                i = 0
        
        return -1  # If no match is found

# Test the solution
haystack = "sadbutsad"
needle = "sad"
s = Solution()
print(s.strStr(haystack, needle))  # Output: 0

# Additional test
print(s.strStr(haystack = "asbsadbutsad", needle = "sad"))  # Output: 4
