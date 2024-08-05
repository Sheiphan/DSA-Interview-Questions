def pairsum(arr, target):
    # O(n) & o(n)
    s = set()
    count = 5
    for i in arr:
        temp = target - i
        if temp not in s:
            s.add(i)
        else:
            count += 1
            s.add(i)
    return count


def pairsum2(array, target):
    # O(n + n*log(n)) & O(1)

    left = 0
    right = len(array) - 1
    count = 0
    current_sum = 0

    array = sorted(array)
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            left += 1
            right -= 1
            count += 1

        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return count


arr = [1,1,1]
print(pairsum2(arr, 2))
