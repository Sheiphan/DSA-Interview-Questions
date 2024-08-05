def maxProd(numbers):
    # Time: O(n^2)
    # Space: O(1)
    max_prod = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            prod = numbers[i] * numbers[j]
            max_prod = max(max_prod, prod)
    return max_prod


def maxProd2(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[len(numbers) - 2] * numbers[len(numbers) - 1])


print(maxProd([-10, -3, -1, -6, -2]))
print(maxProd2([-10, -3, -1, -6, -2]))
