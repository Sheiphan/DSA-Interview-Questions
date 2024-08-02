def largestArray(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


arr = [4, 2, 7, 1, 4]
print(largestArray(arr))
