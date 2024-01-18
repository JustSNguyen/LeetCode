from typing import List
import math
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = math.pow(10, 12)
        costs = [[INF for _ in range(n)] for _ in range(n)]
        processed = [[False for _ in range(n)] for _ in range(n)]

        costs[0][0] = grid[0][0]
        min_heap = [(costs[0][0], 0, 0)]

        while min_heap:
            _, i, j = heapq.heappop(min_heap)

            if processed[i][j]:
                continue

            processed[i][j] = True

            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]

                if ni < 0 or nj < 0 or ni >= n or nj >= n or processed[ni][nj]:
                    continue

                new_cost = max(costs[i][j], grid[ni][nj])
                if new_cost < costs[ni][nj]:
                    costs[ni][nj] = new_cost
                    heapq.heappush(min_heap, (costs[ni][nj], ni, nj))

        return costs[n - 1][n - 1]

if __name__ == '__main__':
    sol = Solution()
    grid = [[3,2],[0,1]]
    result = sol.swimInWater(grid)
    print(result)





