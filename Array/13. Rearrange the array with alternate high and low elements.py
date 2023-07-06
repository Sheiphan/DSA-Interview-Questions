def rearrangeArrayAlter(nums):
    nums.sort()
    n = len(nums)
    i = 0
    l = [0] * n
    while i < n:
        if len(nums) % 2 != 0:
            l[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                l[2 * i + 1] = nums[n - 1]
        else:
            l[2 * i] = nums[i]
            l[2 * i + 1] = nums[n - 1]
        n -= 1
        i += 1
    return l


def rearrangeArrayAlter2(nums):
    n = len(nums)
    i = 1
    while i < n:
        if nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
        if i+1 < n and nums[i+1] > nums[i]:
            nums[i + 1], nums[i] = nums[i], nums[i + 1]
        i += 2
    return nums


arr = [1, 2, 8, 6, 5, 9, 12]
print(rearrangeArrayAlter(arr))
print(rearrangeArrayAlter2(arr))

