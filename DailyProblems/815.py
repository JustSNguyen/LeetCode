from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        buses = defaultdict(set)
        N = len(routes)
        for i in range(N):
            for stop in routes[i]:
                buses[stop].add(i)

        q = deque()
        processed = set()
        for bus in buses[source]:
            q.append(bus)

        cur_dist = 0
        while q:
            cur_size = len(q)
            cur_dist += 1
            for _ in range(cur_size):
                cur_bus = q.popleft()

                if cur_bus in processed:
                    continue

                processed.add(cur_bus)

                for stop in routes[cur_bus]:
                    if stop == target:
                        return cur_dist

                    for neighbor in buses[stop]:
                        if neighbor != cur_bus:
                            q.append(neighbor)

        return -1

if __name__ == '__main__':
    sol = Solution()
    routes = [[1,2,7],[3,6,7]]
    source = 1
    target = 6

    result = sol.numBusesToDestination(routes, source, target)
    print(result)
