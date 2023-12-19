from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        first_row_sum = sum(grid[0])

        first_row_sum_so_far = 0
        second_row_sum_so_far = 0
        min_second_robot_sum = -1
        for i in range(n):
            first_row_sum_so_far += grid[0][i]
            temp = max(first_row_sum - first_row_sum_so_far, second_row_sum_so_far)
            second_row_sum_so_far += grid[1][i]

            if min_second_robot_sum == -1:
                min_second_robot_sum = temp

            min_second_robot_sum = min(min_second_robot_sum, temp)

        return min_second_robot_sum
        