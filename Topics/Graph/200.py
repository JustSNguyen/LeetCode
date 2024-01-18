from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        processed = [[False for _ in range(N)] for _ in range(M)]

        number_of_islands = 0
        for i in range(M):
            for j in range(N):
                if processed[i][j] or grid[i][j] == "0":
                    continue

                number_of_islands += 1
                stack = []
                stack.append((i, j))

                while stack:
                    ci, cj = stack.pop()
                    if processed[ci][cj]:
                        continue

                    processed[ci][cj] = True

                    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for offset in offsets:
                        ni, nj = ci + offset[0], cj + offset[1]
                        if ni >= M or ni < 0 or nj >= N or nj < 0 or grid[ni][nj] == "0" or processed[ni][nj]:
                            continue

                        stack.append((ni, nj))

        return number_of_islands

if __name__ == '__main__':
    sol = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    result = sol.numIslands(grid)
    print(result)