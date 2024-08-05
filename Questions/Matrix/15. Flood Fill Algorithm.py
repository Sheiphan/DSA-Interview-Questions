def fill(matrix, r, c, target, replacement):
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == target:
                floodFillBreadthFirst(matrix, r, c, i, j, target, replacement)
    return matrix


def floodFillBreadthFirst(matrix, r, c, startX, startY, target, replacement):
    queue = [(startX, startY)]
    matrix[startX][startY] = replacement
    idx = 0
    while idx < len(queue):
        currentCell = queue[idx]
        idx += 1
        x, y = currentCell
        xaxis = [-1, 1, 0, 0, -1, -1, 1, 1]
        yaxis = [0, 0, 1, -1, 1, -1, -1, 1]
        for i in range(8):
            newX = x + xaxis[i]
            newY = y + yaxis[i]
            if 0 <= newX < r and 0 <= newY < c and matrix[newX][newY] == target:
                queue.append((newX, newY))
                matrix[newX][newY] = replacement
    return matrix


arr = [['p', 'p', 'p', 'g', 'g'],
       ['b', 'p', 'y', 'y', 'g'],
       ['y', 'p', 'p', 'y', 'g'],
       ['b', 'b', 'y', 'y', 'y']]

print(fill(arr, len(arr), len(arr[0]), 'y', 'z'))

# [['p', 'p', 'p', 'g', 'g'],
#  ['b', 'p', 'z', 'z', 'g'],
#  ['z', 'p', 'p', 'z', 'g'],
#  ['b', 'b', 'z', 'z', 'z']]

