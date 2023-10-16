from typing import List
from functools import lru_cache

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        number_of_walls = len(cost)
        cost_sum = sum(cost)

        @lru_cache(number_of_walls * number_of_walls)
        def calculate_minimum_cost(wall_index: int, time_diff: int) -> int:
            if wall_index == number_of_walls and time_diff >= 0:
                return 0

            if wall_index == number_of_walls:
                return cost_sum

            new_time_diff_first_option = min(time_diff + time[wall_index], number_of_walls - wall_index)
            first_option = calculate_minimum_cost(wall_index + 1, new_time_diff_first_option) + cost[wall_index]

            second_option = calculate_minimum_cost(wall_index + 1, time_diff - 1)
            return min(first_option, second_option)

        return calculate_minimum_cost(0, 0)

if __name__ == '__main__':
    sol = Solution()
    cost = [49,35,32,20,30,12,42]
    time = [1,1,2,2,1,1,2]
    result = sol.paintWalls(cost, time)
    print(result)
