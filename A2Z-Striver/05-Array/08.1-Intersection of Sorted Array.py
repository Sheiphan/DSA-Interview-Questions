def intersection(arr1, arr2):
    i = j = 0
    n, m = len(arr1), len(arr2)
    intersection_set = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            intersection_set.append(arr1[i])
            i += 1
            j += 1

    return intersection_set


arr1 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 4, 5, 6, 6, 11, 12]
print(intersection(arr1, arr2))
