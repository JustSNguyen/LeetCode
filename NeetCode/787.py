from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10**9
        min_dist = [INF for _ in range(n)]
        min_dist[src] = 0

        for i in range(k + 1):
            new_min_dist = [min_dist[j] for j in range(n)]
            for flight in flights:
                u, v, w = flight

                new_min_dist[v] = min(min_dist[u] + w, new_min_dist[v])

            min_dist = new_min_dist.copy()

        return min_dist[dst] if min_dist[dst] != INF else -1


if __name__ == '__main__':
    sol = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1

    result = sol.findCheapestPrice(n, flights, src, dst, k)
    print(result)

