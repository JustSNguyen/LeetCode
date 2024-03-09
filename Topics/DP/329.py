from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        @lru_cache(maxsize=None)
        def dp(i, j):
            result = 1
            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if ni < 0 or nj < 0 or ni == m or nj == n or matrix[ni][nj] <= matrix[i][j]:
                    continue

                result = max(result, 1 + dp(ni, nj))

            return result

        max_result = 1
        for i in range(m):
            for j in range(n):
                max_result = max(max_result, dp(i, j))

        return max_result
