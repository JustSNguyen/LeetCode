from typing import List
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            distance = math.sqrt(point[0] * point[0] + point[1] * point[1])

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, point))
            elif -max_heap[0][0] > distance:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, point))

        result = []
        while max_heap:
            _, point = heapq.heappop(max_heap)
            result.append(point)

        return result

if __name__ == '__main__':
    sol = Solution()
    points = [[1,3],[-2,2]]
    k = 1
    result = sol.kClosest(points, k)
    print(result)

