def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # return quickSort(left) + middle + quickSort(right)
    sorted_left = quickSort(left)
    sorted_right = quickSort(right)

    result = sorted_left + middle + sorted_right
    return result

arr = [3, 2, 4, 1, 3]
sorted_arr = quickSort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 3, 4]


# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []

#     for x in arr:
#         if x < pivot:
#             left.append(x)
#         elif x == pivot:
#             middle.append(x)
#         else:
#             right.append(x)

#     sorted_left = quickSort(left)
#     sorted_right = quickSort(right)

#     result = sorted_left + middle + sorted_right
#     return result

arr = [3, 2, 4, 1, 3]
sorted_arr = quickSort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 3, 4]
