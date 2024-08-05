# A = [2,0,3,5,0,0,6,0,0]
# B = [1,7,8,15,17]
# Output = [1,2,3,5,6,7,8,15,17]

def mergeTwoSortedInPlace(A, B):
    # Time: O(m+n)
    # Space: O(1)

    # Firstly gather all elements of A at the start
    idx = 0
    n = len(A)
    for i in range(n):
        if A[i] != 0:
            A[idx] = A[i]
            idx += 1

    A = A[:idx]
    A.extend(len(B) * [0])

    # Merge A and B using the mergesort solution
    i = idx - 1
    j = len(B) - 1
    k = len(A) - 1

    while i >= 0 and j >= 0:
        if A[i] < B[j]:
            A[k] = B[j]
            j -= 1
            k -= 1
        else:
            A[k] = A[i]
            i -= 1
            k -= 1

    # Check for leftover elements in the array B
    while j >= 0:
        A[k] = B[j]
        k -= 1
        j -= 1

    return A


A = [2, 3, 0, 5, 6, 0, 0]
B = [1, 7, 8, 15, 17]
print(mergeTwoSortedInPlace(A, B))
