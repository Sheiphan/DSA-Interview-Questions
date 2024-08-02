def largestNumAppearOnce(arr):
    hashmap = {}
    for i in range(len(arr)):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1
        else:
            hashmap[arr[i]] += 1

    for num, count in hashmap.items():
        if count == 1:
            return num

    return -1


arr = [4, 1, 2, 1, 2]
print(largestNumAppearOnce(arr))
