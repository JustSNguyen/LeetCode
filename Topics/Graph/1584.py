from typing import List
import heapq
import math

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        INF = math.pow(10, 12)
        cost = [INF for _ in range(N)]

        cost[0] = 0
        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        processed = [False for _ in range(N)]

        while min_heap:
            _, i = heapq.heappop(min_heap)

            if processed[i]:
                continue

            processed[i] = True

            for j in range(N):
                new_cost = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                if new_cost < cost[j] and not processed[j]:
                    cost[j] = new_cost
                    heapq.heappush(min_heap, (cost[j], j))

        return sum(cost)

if __name__ == '__main__':
    sol = Solution()
    test = [[0,0],[1,1],[1,0],[-1,1]]
    result = sol.minCostConnectPoints(test)
    print(result)
