def countTheOccurence(number, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == number:
            count += 1
    return count


def allCount(arr):
    d = {}
    for i in arr:
        d[i] = countTheOccurence(i, arr)
    return d


arr = [1, 4, 3, 5, 4]
print(allCount(arr))
