# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

from typing import List


class BruteForce:
    def maxDistance(self, colors: List[int]) -> int:
        maxDiff = 0
        for i in range(len(colors)):
            start = i
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    end = j

            maxDiff = max(maxDiff, abs(end - start))

        return maxDiff


class Optimal:
    def maxDistance(self, colors: List[int]) -> int:
        maxDist = 0
        n = len(colors)

        for i in range(1, n):
            if colors[i] != colors[0]:
                maxDist = i
        for i in range(n):
            if colors[i] != colors[-1]:
                maxDist = max(maxDist, n - i - 1)

        return maxDist
