from typing import List 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = 0 
        dp_1 = cost[n - 1]
        dp_2 = 0 

        for i in range(n - 2, -1, -1):
            dp = cost[i] + min(dp_1, dp_2)
            dp_2 = dp_1 
            dp_1 = dp 
        
        return min(dp_1, dp_2)