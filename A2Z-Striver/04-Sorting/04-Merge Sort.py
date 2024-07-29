def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Recursively split and sort the halves
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = [0] * (len(left) + len(right))
    i = j = k = 0

    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    # Add remaining elements from left array, if any
    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    # Add remaining elements from right array, if any
    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged


arr = [3, 2, 4, 1, 3]
sorted_arr = mergeSort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 3, 4]
