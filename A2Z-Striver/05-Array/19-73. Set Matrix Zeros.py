# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        k = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    k.append((i, j))

        for i, j in k:
            matrix[i] = [0] * len(matrix[i])
            for i in range(len(matrix)):
                matrix[i][j] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(Solution().setZeroes(matrix=matrix))
print(matrix)
