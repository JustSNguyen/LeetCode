from typing import List
from collections import defaultdict
import heapq
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = math.pow(10, 12)
        costs = [INF for _ in range(n + 1)]

        costs[k] = 0

        min_heap = [(costs[k], k)]
        processed = set()

        adj = defaultdict(list)
        for time in times:
            u, v, w = time
            adj[u].append((v, w))

        while min_heap:
            _, u = heapq.heappop(min_heap)

            if u in processed:
                continue

            processed.add(u)

            for v, w in adj[u]:
                if costs[u] + w < costs[v]:
                    costs[v] = costs[u] + w
                    heapq.heappush(min_heap,(costs[v], v))

        max_cost = max(costs[1:])
        if max_cost == INF:
            return -1

        return max_cost

if __name__ == '__main__':
    sol = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    result = sol.networkDelayTime(times, n, k)
    print(result)
