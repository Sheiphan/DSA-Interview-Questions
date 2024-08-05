# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

class Solution:
    def answerQueries(self, nums, queries):
        
        numsSorted = sorted(nums)
        res = []
		
        for q in queries:
            total = 0
            count = 0
            for num in numsSorted:
                total += num
                count += 1
                if total > q:
                    count -= 1
                    break
            res.append(count)
        
        return res


nums = [4,5,2,1]
queries = [3,10,21]
s=Solution()
print(s.answerQueries(nums, queries))