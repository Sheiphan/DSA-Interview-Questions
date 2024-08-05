class BruteForce:
    def UnionTwoArray(self, arr1, arr2):
        union_set = set()
        # for i in range(len(arr1)):
        #     union_set.add(arr1[i])
        # for j in range(len(arr2)):
        #     union_set.add(arr2[j])
        return list(set(arr1 + arr2))


class Optimal:
    def UnionTwoArray(self, arr1, arr2):
        i = j = 0
        n, m = len(arr1), len(arr2)
        union_set = []

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not union_set or union_set[-1] != arr1[i]:
                    union_set.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union_set or union_set[-1] != arr1[j]:
                    union_set.append(arr2[j])
                j += 1
            else:
                if not union_set or union_set[-1] != arr1[i]:
                    union_set.append(arr1[i])
                i += 1
                j += 1

        while i < n:
            if not union_set or union_set[-1] != arr1[i]:
                union_set.append(arr1[i])
            i += 1

        while j < m:
            if not union_set or union_set[-1] != arr2[j]:
                union_set.append(arr2[j])
            j += 1

        return union_set


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
s = BruteForce()
print(s.UnionTwoArray(arr1, arr2))
