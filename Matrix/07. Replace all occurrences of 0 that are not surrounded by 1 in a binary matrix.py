def depthFirstSearch(matrix, r, c, x, y):
    stack = [(x, y)]
    while stack:     # this will go until my stack is not empty
        currentCell = stack[-1]
        current_x, current_y = currentCell
        stack.pop()
        # Consider all the valid 8 neighbouring cells
        xaxis = [-1, 1, 0, 0, -1, -1, 1, 1]
        yaxis = [0, 0, 1, -1, 1, -1, -1, 1]
        # cells = [(x-1, y), (x+1, y), (x, y-1), (x, y+1),
        #          (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]

        # for x, y in cells:
        for i in range(8):
            x = current_x + xaxis[i]
            y = current_y + yaxis[i]
            if (0 <= x < r) and (0 <= y < c):
                if matrix[x][y] == 1:
                    continue
                else:
                    matrix[x][y] = 1
                    stack.append((x, y))


def replaceAllZerosNotSurroundedByOnes(matrix, r, c):
    #  traverse the first and last column
    for i in range(r):
        if matrix[i][0] == 0:
            matrix[i][0] = 1
            depthFirstSearch(matrix, r, c, i, 0)
        if matrix[i][c - 1] == 0:
            matrix[i][c - 1] = 1
            depthFirstSearch(matrix, r, c, i, c - 1)

    for i in range(c):
        if matrix[0][i] == 0:
            matrix[0][i] = 1
            depthFirstSearch(matrix, r, c, i, 0)
        if matrix[r - 1][i] == 0:
            matrix[r - 1][i] = 1
            depthFirstSearch(matrix, r, c, i, c - 1)
    return matrix


arr = [[1, 0, 1, 0, 1],
       [1, 1, 0, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 1],
       [1, 0, 1, 1, 1],
       [1, 1, 1, 1, 0]]

print(replaceAllZerosNotSurroundedByOnes(arr, len(arr), len(arr[0])))