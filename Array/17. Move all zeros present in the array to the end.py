def moveZeros(nums):
    # Time: O(n)
    # Space: O(n)
    n = len(nums)
    ans = [0] * n
    j = 0
    for i in range(n):
        if nums[i] != 0:
            ans[j] = nums[i]
            j += 1
    return ans


def moveZeros2(nums):
    # Time: O(n)
    # Space: O(1)
    start = 0
    end = len(nums) - 1
    while start <= end:
        if nums[start] != 0:
            start += 1
        else:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            end -= 1
    return nums


arr = [0, 4, 0, 7, 8, 0]
print(moveZeros(arr))
print(moveZeros2(arr))

