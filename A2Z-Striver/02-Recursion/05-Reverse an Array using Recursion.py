def reverseArray(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverseArray(arr, left + 1, right - 1)


arr = [1, 2, 4, 5]
print(reverseArray(arr, 0, len(arr) - 1))


def reverseArraySinglePointer(arr, i):
    n = len(arr)
    if i == n // 2:
        return arr
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return reverseArraySinglePointer(arr, i + 1)


arr = [1, 2, 4, 5, 9]
print((reverseArraySinglePointer(arr, i=0)))
