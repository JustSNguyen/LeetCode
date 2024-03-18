from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        max_y_so_far = points[0][1]
        cnt = 0
        for point in points:
            if point[0] > max_y_so_far:
                cnt += 1
                max_y_so_far = max(max_y_so_far, point[1])

        cnt += 1
        return cnt

