def reverseAnArray(arr):
    n = len(arr)
    i = 0
    while i < (len(arr) // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        i += 1
    return arr

arr = [1, 2, 3]
reverseAnArray(arr)
print(arr)
