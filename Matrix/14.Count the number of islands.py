def countNumberOfIsland(matrix, r, c):
    count = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                count += 1
                breadthFirstSearch(matrix, r, c, i, j)
    return count


def breadthFirstSearch(matrix, r, c, startX, startY):
    queue = [(startX, startY)]
    idx = 0
    matrix[startX][startY] = -1
    while idx < len(queue):
        currentCell = queue[idx]
        idx += 1
        x, y = currentCell
        xaxis = [-1, 1, 0, 0, -1, -1, 1, 1]
        yaxis = [0, 0, 1, -1, 1, -1, -1, 1]
        for i in range(8):
            newX = x + xaxis[i]
            newY = y + yaxis[i]
            if 0 <= newX < r and 0 <= newY < c and matrix[newX][newY] == 1:
                queue.append((newX, newY))
                matrix[newX][newY] = -1


arr = [[1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 1],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0]]

print(countNumberOfIsland(arr, len(arr), len(arr[0])))
