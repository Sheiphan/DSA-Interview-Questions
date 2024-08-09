from typing import List


class Brute:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        maxCount = 2
        for i in range(n - 2):
            count = 0
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    count += 1
                if count == maxCount:
                    ans[i] = nums[j]
                    break
        return ans


class Optimal:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        st1:List = []  # monotonic decreasing first stack.
        st2:List = [] # Monotonic decreasing second stack.(having only that elements which have first greater)
        helper = []# monotonic increasing helper stack(help in moving elements from st1 to st2 with maintaining monotonicity of st2)

        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            while st2 and nums[i] > nums[st2[-1]]:  # if element can be second largest for st2 elements
                ans[st2.pop()] = nums[i]

            while st1 and nums[i] > nums[st1[-1]]:  # if element can be second largest for st2 elements
                helper.append(st1.pop())

            while helper:
                st2.append(helper.pop())  # for maintain monotonicity of st2
            st1.append(i)

        return ans


# Example usage
arr = [2, 4, 0, 9, 6]
s = Optimal()
print(s.secondGreaterElement(arr))  # Output: [5, -1, 5, -1, -1]


nums = [1, 17, 18, 0, 18, 10, 20, 0]
s = Optimal()
print(s.secondGreaterElement(nums))
