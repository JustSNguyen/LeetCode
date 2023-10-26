from typing import List
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0 for _ in range(N)]
        dp[N - 1] = cost[N - 1]
        dp[N - 2] = cost[N - 2]

        for i in range(N - 3, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]

        return min(dp[0], dp[1])

