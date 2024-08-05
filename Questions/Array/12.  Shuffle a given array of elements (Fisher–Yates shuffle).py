from random import randrange


def arrayShuffleFisherYate(nums):
    n = len(nums)
    max_value = n
    for i in range(n):
        random_idx = randrange(max_value)
        nums[i], nums[random_idx] = nums[random_idx], nums[i]
        max_value -= 1
    return nums


nums = [1, 2, 3, 4, 5]
print(arrayShuffleFisherYate(nums))
