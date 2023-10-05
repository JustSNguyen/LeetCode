from typing import List
from functools import lru_cache

class Solution:
    def maximumSumOfHeights(self, max_heights: List[int]) -> int:
        N = len(max_heights)
        height_if_on_the_left = [0 for _ in range(N)]
        height_if_on_the_right = [0 for _ in range(N)]

        for i in range(N - 1, -1, -1):
            if i == N - 1:
                height_if_on_the_left[i] = max_heights[i]
            else:
                height_if_on_the_left[i] = min(height_if_on_the_left[i + 1], max_heights[i])

        for i in range(N):
            if i == 0:
                height_if_on_the_left[i] = max_heights[i]
            else:
                height_if_on_the_left[i] = min(height_if_on_the_right[i - 1], max_heights[i])

        max_possible_sum_heights = 0
        print(height_if_on_the_left)
        print(height_if_on_the_right)
        max_height = max(max_heights)
        for i in range(N):
            if max_heights[i] != max_height:
                continue

            sum_heights = sum(height_if_on_the_left[:i]) + sum(height_if_on_the_right[i + 1:]) + max_heights[i]
            max_possible_sum_heights = max(max_possible_sum_heights, sum_heights)

        return max_possible_sum_heights


if __name__ == '__main__':
    sol = Solution()
    maxHeights = [3,2,5,5,2,3]
    result = sol.maximumSumOfHeights(maxHeights)
    print(result)