from typing import List
from collections import defaultdict
import heapq
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for time in times:
            u, v, w = time
            adj[u].append((v, w))

        INF = 10**12
        min_distances = [INF for _ in range(n + 1)]
        min_distances[0] = 0
        min_distances[k] = 0

        min_heap = [(min_distances[k], k)]
        processed = set()

        while min_heap:
            distance, i = heapq.heappop(min_heap)
            if i in processed:
                continue

            processed.add(i)

            for j, w in adj[i]:
                if distance + w < min_distances[j]:
                    min_distances[j] = distance + w
                    heapq.heappush(min_heap, (min_distances[j], j))

        return -1 if max(min_distances) >= INF else max(min_distances)

if __name__ == '__main__':
    sol = Solution()
    test = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    result = sol.networkDelayTime(test, n, k)
    print(result)