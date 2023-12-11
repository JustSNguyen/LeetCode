from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        result = 0
        processed = set()
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1 or (i, j) in processed:
                    continue

                is_closed_island = True

                stack = [(i, j)]

                while stack:
                    coordinates = stack.pop()

                    if coordinates in processed:
                        continue

                    if coordinates[0] == N - 1 or coordinates[1] == M - 1 or coordinates[0] == 0 or coordinates[1] == 0:
                        is_closed_island = False

                    processed.add(coordinates)

                    for offset in offsets:
                        ni, nj = coordinates[0] + offset[0], coordinates[1] + offset[1]

                        if ni < 0 or nj < 0 or ni >= N or nj >= M or grid[ni][nj] == 1 or (ni, nj) in processed:
                            continue

                        stack.append((ni, nj))

                if is_closed_island:
                    result += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    test = [[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[0,1,1,1,0]]
    result = sol.closedIsland(test)
    print(result)