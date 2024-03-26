from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        processed = set()
        min_heap = []

        INF = 10**12
        min_distances = [INF for _ in range(len(points))]
        min_distances[0] = 0
        heapq.heappush(min_heap, (min_distances[0], 0))

        while min_heap:
            distance, i = heapq.heappop(min_heap)
            if i in processed:
                continue

            processed.add(i)

            for j, other in enumerate(points):
                if j in processed:
                    continue

                point = points[i]
                distance_from_point_to_other = abs(other[0] - point[0]) + abs(other[1] - point[1])
                if distance_from_point_to_other < min_distances[j]:
                    min_distances[j] = distance_from_point_to_other
                    heapq.heappush(min_heap, (min_distances[j], j))

        return sum(min_distances)