from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        left = 0
        right = N - 1
        max_area = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, width * height)

            if heights[left] <= heights[right]:
                while left < right and heights[left] <= height:
                    left += 1
            else:
                while left < right and heights[right] <= height:
                    right -= 1

        return max_area