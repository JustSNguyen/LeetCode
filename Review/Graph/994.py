from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        minutes = 0
        while q:
            k = len(q)

            for i in range(k):
                i, j = q.popleft()
                offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for offset in offsets:
                    ni, nj = i + offset[0], j + offset[1]
                    if ni < 0 or nj < 0 or ni == m or nj == n or grid[ni][nj] != 1:
                        continue

                    grid[ni][nj] = 2
                    q.append((ni, nj))

            if q:
                minutes += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return minutes
