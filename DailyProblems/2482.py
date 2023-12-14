from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ones_row = [0 for _ in range(m)]
        ones_col = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ones_row[i] += grid[i][j]
                ones_col[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                grid[i][j] = ones_row[i] + ones_col[j] - (n - ones_row[i]) - (m - ones_col[j])

        return grid