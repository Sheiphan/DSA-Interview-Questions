class BruteForce:
    def secondLargest(self, arr):
        self.bubbleSort(arr)
        arr = list(set(arr))
        return arr[len(arr) - 2]

    def bubbleSort(self, arr):
        n = len(arr)
        for k in range(len(arr)):
            i = 0
            j = 1
            while i <= n - k and j <= n - k - 1:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
        return arr


class Optimal:
    def secondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1
        large = float("-inf")
        second_large = float("-inf")
        for i in range(n):
            if arr[i] > large:
                second_large = large
                large = arr[i]
            elif arr[i] > second_large and arr[i] != large:
                second_large = arr[i]
        return second_large


arr = [3, 1, 5, 3, 6, 6, 2]
b = Optimal()
print(b.secondLargest(arr))
