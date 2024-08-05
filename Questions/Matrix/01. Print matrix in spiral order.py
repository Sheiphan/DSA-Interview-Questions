def spiralMatrix(matrix, row, column):
    direction = 0
    top, left, bottom, right = 0, 0, row - 1, column - 1

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                print(matrix[left][i])
            top += 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                print(matrix[i][right])
            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i])
            bottom -= 1

        else:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4


arr = [[1,  2,  3,  4], #top = 0
       [5,  6,  7,  8],
       [9,  10, 11, 12],
       [13, 14, 15, 16]] #bottom = len(arr)
    #left=0        #right = len(arr)

row = col = len(arr)
spiralMatrix(arr, row, col)

# 1
# 2
# 3
# 4

# 8
# 12
# 16

# 15
# 14
# 13

# 9
# 5

# 6
# 7

# 11
# 10
