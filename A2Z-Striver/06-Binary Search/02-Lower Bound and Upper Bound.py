def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upperBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


arr = [1, 3, 6, 7, 9, 15]
x = 7
n = len(arr)
print(lowerBound(arr, n, x))
print(upperBound(arr, n, x))
