def positiveSlopeDiagonalElement(matrix, r, c):
    for i in range(r):
        x = i
        y = 0
        while x >= 0 and y <= i:  # or y < c
            print(matrix[x][y], end=" ")
            x -= 1
            y += 1
        print()
    for i in range(1, c):
        x = 4
        y = i
        while x >= i and y < c:  # or x >= 0
            print(matrix[x][y], end=" ")
            x -= 1
            y += 1
        print()


arr = [[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6],
       [3, 4, 5, 6, 7],
       [4, 5, 6, 7, 8],
       [5, 6, 7, 8, 9]]

positiveSlopeDiagonalElement(arr, len(arr), len(arr[0]))


# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 
# 7 7 7 
# 8 8 
# 9 
