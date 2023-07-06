def equilibriumIndex(nums):
    n = len(nums)
    equilibrium_list = []

    for i in range(n):
        left_sum = sum(nums[0:i])
        right_sum = sum(nums[i + 1:])
        if left_sum == right_sum:
            equilibrium_list.append(i)

    return equilibrium_list


def equilibriumIndex2(nums):
    # Time: O(n)
    # Space: O(1)
    n = len(nums)
    equilibrium_list = []

    for i in range(1, n):
        nums[i] = nums[i] + nums[i - 1]

    for idx in range(n):
        # left hand side sum
        right = idx - 1
        if idx - 1 == -1:
            left_sum = 0
        left_sum = nums[right]

        # right had side sum
        right = n - 1
        left = idx
        right_sum = nums[right] - nums[idx]

        if left_sum == right_sum:
            equilibrium_list.append(idx)

    return equilibrium_list


arr = [-3, 5, -4, -2, 3, 1, 0]
print(equilibriumIndex(arr))
print(equilibriumIndex2(arr))
