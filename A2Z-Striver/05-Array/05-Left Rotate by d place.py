class BruteForce:
    def leftRotate(self, arr, d):
        temp = arr[:d]
        n = len(arr)
        for i in range(d, n):
            arr[i - d] = arr[i]
        for i in range(n - d, n):
            arr[i] = temp[i - (n - d)]
        return arr


class Optimal:
    def leftRotate(self, arr, d):
        return self.revArr(self.revArr(arr[:d]) + self.revArr(arr[d:]))

    def revArr(self, arr):
        n = len(arr)
        i = 0
        while i < (len(arr) // 2):
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
            i += 1
        return arr


arr = [1, 2, 3, 4, 5, 6, 7]
# print(leftRotate(arr, 3))

s = BruteForce()
print(s.leftRotate(arr, d=3))
