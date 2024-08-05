# Constraints: if matrix[x][y] = k
# then only valid move is [x+k, y] / [x-k, y] / [x, y+k] / [x, y-k]

def shortestPathConstraints(matrix, row, column):
    queue = [(0, 0, 0)]  # (x, y, distance)
    idx = 0
    visited = set()
    while idx < len(queue):
        currentCell = queue[idx]
        x, y, distance = currentCell
        visited.add((x, y))
        idx += 1
        if x == row - 1 and y == column - 1:  # reached the destination value
            return distance
        else:
            # consider all the valid nodes we can go from x, y with the k = matrix[x][y]
            k = matrix[x][y]
            cells = [(x, y + k), (x, y - k), (x + k, y), (x - k, y)]
            for x, y in cells:
                if (0 <= x < row) and (0 <= y < column) and (x, y) not in visited:
                    queue.append((x, y, distance + 1))

    return False


matrix = [[2, 3, 2, 8],
       [4, 5, 6, 1],
       [3, 2, 1, 1],
       [3, 5, 6, 9]]
row = len(matrix)
column = len(matrix[0])
print(shortestPathConstraints(matrix, row, column))