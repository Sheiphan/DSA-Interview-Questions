def countMaxZeros(arr):
    count = 0
    maxCount = 0
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
        i += 1
            
    maxCount = max(maxCount, count)
    return maxCount


arr = [1]
print(countMaxZeros(arr))
