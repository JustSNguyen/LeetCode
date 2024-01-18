from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = math.pow(10, 12)

        costs = [INF for _ in range(n)]
        costs[src] = 0

        for i in range(k + 1):
            new_costs = [cost for cost in costs]
            for flight in flights:
                u, v, w = flight
                if costs[u] + w < new_costs[v]:
                    new_costs[v] = costs[u] + w

            costs = new_costs

        if costs[dst] == INF:
            return -1

        return costs[dst]

if __name__ == '__main__':
    sol = Solution()
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    n = 4
    src = 0
    dst = 3
    k = 1
    result = sol.findCheapestPrice(n, flights, src, dst, k)
    print(result)
