from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        max_area = 0
        processed = [[False for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if processed[i][j] or grid[i][j] == 0:
                    continue

                stack = []
                stack.append((i, j))
                area = 0
                while stack:
                    ci, cj = stack.pop()

                    if processed[ci][cj]:
                        continue

                    processed[ci][cj] = True
                    area += 1

                    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for offset in offsets:
                        ni, nj = ci + offset[0], cj + offset[1]
                        if ni < 0 or ni >= M or nj < 0 or nj >= N or processed[ni][nj] or grid[ni][nj] == 0:
                            continue

                        stack.append((ni, nj))

                max_area = max(max_area, area)

        return max_area