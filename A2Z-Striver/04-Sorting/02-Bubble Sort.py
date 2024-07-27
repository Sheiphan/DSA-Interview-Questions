# Push the max to the last by adjacent swap
def bubbleSort(arr):
    n = len(arr)
    for k in range(n):
        i = 0
        j = 1
        while i < (n - k - 1) and j < (n - k):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1

    return arr


arr = [13, 46, 24, 52, 20, 9]
print(bubbleSort(arr))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# TC -> worst - O(N^2)  best - O(N)
arr = [13, 46, 24, 52, 20, 9]
print(bubble_sort(arr))  # Output: [9, 13, 20, 24, 46, 52]
