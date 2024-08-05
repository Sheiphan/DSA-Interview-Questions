# Using Operators
def replaceProdOperators(nums):
    # Time: O(n)
    # Space: O(1)
    total_prod = 1
    for i in range(len(nums)):
        total_prod = total_prod * nums[i]
    for i in range(len(nums)):
        nums[i] = total_prod // nums[i]
    return nums


# Without using Operators
def replaceProdOperators2(nums):
    # Time: O(n)
    # Space: O(1)
    n = len(nums)
    prefix_product_array = [1] * (n + 1)
    suffix_product_array = [1] * (n + 1)
    for i in range(n + 1):
        if i == 0:
            prefix_product_array[i] = 1
            suffix_product_array[-i] = 1
        else:
            prefix_product_array[i] = prefix_product_array[i - 1] * nums[i - 1]
            suffix_product_array[-i - 1] = suffix_product_array[-i] * nums[-i]
    for i in range(1, n+1):
        nums[i-1] = prefix_product_array[i-1] * suffix_product_array[i]

    return nums


arr = [2, 5, 4, 3, 7]
print(replaceProdOperators(arr))
print(replaceProdOperators2(arr))
