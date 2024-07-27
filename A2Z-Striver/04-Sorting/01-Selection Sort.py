# Select min and swap
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr



# TC -> worst - O(N^2)  best - O(N^2)
arr = [13, 46, 24, 52, 20, 9]
print(selectionSort(arr))
