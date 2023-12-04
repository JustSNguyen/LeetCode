from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i, point in enumerate(points):
            if i == 0:
                continue

            prev = points[i - 1]

            row_diff = abs(prev[0] - point[0])
            col_diff = abs(prev[1] - point[1])

            result += max(row_diff, col_diff)

        return result