def leftRotate(arr, d):
    return revArr(revArr(arr[:d]) + revArr(arr[d:]))


def revArr(arr):
    n = len(arr)
    i = 0
    while i < (len(arr) // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        i += 1
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print(leftRotate(arr, 3))
