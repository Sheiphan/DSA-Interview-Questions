# Takes an element and place it in the correct order
def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr

# TC -> worst - O(N^2)  best - O(N)
arr = [13, 46, 24, 52, 20, 9]
print(insertionSort(arr))
