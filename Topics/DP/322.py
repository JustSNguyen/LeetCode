from typing import List 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**12
        dp = [INF for _ in range(amount + 1)]
        dp[0] = 0 

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
            
        if dp[amount] == INF:
            return -1 
        
        return dp[amount]