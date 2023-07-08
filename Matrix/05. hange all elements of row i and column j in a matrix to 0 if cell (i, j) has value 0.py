def changeZero(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                for k in range(col):
                    matrix[i][k] = -1
                for l in range(row):
                    matrix[l][j] = -1
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix


def changeZero2(matrix):
    row = len(matrix)
    col = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in zero_rows:
        matrix[i] = [0] * col

    for j in zero_cols:
        for i in range(row):
            matrix[i][j] = 0

    return matrix


def changeZero3(matrix, r, c):
    # Time: O(r*c)
    # Space: O(1)
    rowFlag = False
    columnFlag = False
    for i in range(c):
        if matrix[0][i] == 0:
            rowFlag = True
            break
    for i in range(r):
        if matrix[i][0] == 0:
            columnFlag = True
            break
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if rowFlag:
        for i in range(r):
            matrix[0][i] = 0
    if columnFlag:
        for i in range(c):
            matrix[i][0] = 0

    return matrix


arr = [[1,1,1],
       [1,0,1],
       [1,1,1],
       [0,1,1]]

# print(changeZero(arr))
# print(changeZero2(arr))
print(changeZero3(arr, len(arr), len(arr[0])))


# [[0, 0, 1], [0, 0, 0], [0, 0, 1], [0, 0, 0]]


