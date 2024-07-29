def minimumOperations(nums):

    numsorted = mergeSort(nums)
    count = 0
    for i in range(len(numsorted)):
        if numsorted[i] != 0:
            count += 1
            numsorted = [x - numsorted[i] if x>0 else 0 for x in numsorted]

        if i == (len(numsorted) - 1):
            return count


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_side = mergeSort(arr[:mid])
    right_side = mergeSort(arr[mid:])

    return merge(arr, left_side, right_side)


def merge(arr, left, right):
    i = j = k = 0
    merged = [0] * (len(left) + len(right))

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        merged[k] = right[j]
        k += 1
        j += 1

    return merged


nums = [0]
print(minimumOperations(nums))
