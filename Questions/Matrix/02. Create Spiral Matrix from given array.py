def createSpiralMatrix(arr, row, column):
    matrix = [[0 for i in range(column)] for j in range(row)]
    top, left, bottom, right = 0, 0, row - 1, column - 1
    direction = 0
    idx = 0  # loop in the original array arr
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                matrix[left][i] = arr[idx]
                idx += 1
            top += 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                matrix[i][right] = arr[idx]
                idx += 1
            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = arr[idx]
                idx += 1
            bottom -= 1

        else:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = arr[idx]
                idx += 1
            left += 1

        direction = (direction + 1) % 4

    return matrix

def generateMatrix(n) :

    arr = [i for i in range(1, n * n + 1)]

    matrix = [[0 for i in range(n)] for j in range(n)]
    top, left, bottom, right = 0, 0, n - 1, n - 1
    direction = 0
    idx = 0  # loop in the original array arr
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                matrix[left][i] = arr[idx]
                idx += 1
            top += 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                matrix[i][right] = arr[idx]
                idx += 1
            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = arr[idx]
                idx += 1
            bottom -= 1

        else:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = arr[idx]
                idx += 1
            left += 1

        direction = (direction + 1) % 4

    return matrix


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(createSpiralMatrix(arr, 3, 3))
print(generateMatrix(3))
