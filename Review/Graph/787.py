from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = math.pow(10, 12)

        min_distances = [INF for _ in range(n)]
        min_distances[src] = 0

        for i in range(k + 1):
            new_min_distances = min_distances[:]
            for u, v, w in flights:
                if min_distances[u] + w < new_min_distances[v]:
                    new_min_distances[v] = min_distances[u] + w

            min_distances = new_min_distances

        return -1 if min_distances[dst] == INF else min_distances[dst]
