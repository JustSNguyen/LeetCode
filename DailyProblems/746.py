from typing import List
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        number_of_steps = len(cost)

        @lru_cache(maxsize=number_of_steps)
        def get_min_cost_climbing_from_step(index: int) -> int:
            if index >= number_of_steps:
                return 0

            return (min(get_min_cost_climbing_from_step(index + 1), get_min_cost_climbing_from_step(index + 2)) +
                    cost[index])

        return min(get_min_cost_climbing_from_step(0), get_min_cost_climbing_from_step(1))

