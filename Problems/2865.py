from typing import List

class Solution:
    def maximumSumOfHeights(self, max_heights: List[int]) -> int:
        def calculate_sum_mountain_heights_with_top_at(index: int) -> int:
            top_height = max_heights[index]
            sum_heights = 0

            previous_height = top_height
            for i in range(index - 1, -1, -1):
                possible_height = min(max_heights[i], previous_height)
                sum_heights += possible_height
                previous_height = possible_height

            previous_height = top_height
            for i in range(index + 1, len(max_heights)):
                possible_height = min(max_heights[i], previous_height)
                sum_heights += possible_height
                previous_height = possible_height

            return sum_heights + top_height

        max_sum_mountain_heights = 0
        for i in range(len(max_heights)):
            sum_mountain_heights = calculate_sum_mountain_heights_with_top_at(i)
            max_sum_mountain_heights = max(max_sum_mountain_heights, sum_mountain_heights)

        return max_sum_mountain_heights

if __name__ == '__main__':
    sol = Solution()
    maxHeights = [1, 2, 3, 4, 5]
    result = sol.maximumSumOfHeights(maxHeights)
    print(result)