from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        minutes = 0
        q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            K  = len(q)
            for i in range(K):
                ci, cj, time = q.popleft()

                minutes = max(minutes, time)

                offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for offset in offsets:
                    ni, nj = ci + offset[0], cj + offset[1]
                    if ni < 0 or nj < 0 or ni >= M or nj >= N or grid[ni][nj] != 1:
                        continue

                    grid[ni][nj] = 2
                    q.append((ni, nj, time + 1))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1

        return minutes

if __name__ == '__main__':
    sol = Solution()
    grid = [[2,1,1],[1,1,1],[0,1,2]]
    result = sol.orangesRotting(grid)
    print(result)