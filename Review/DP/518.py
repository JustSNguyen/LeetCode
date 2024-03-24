from typing import List 
from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(amount, i):
            if amount == 0:
                return 1
            
            if i == 0:
                if amount % coins[i] == 0:
                    return 1
                
                return 0 

            result = 0 
            
            for r in range(amount // coins[i] + 1):
                result += dp(amount - r * coins[i], i - 1)
            
            return result 
        
        return dp(amount, len(coins) - 1)

if __name__ == '__main__':
    sol = Solution()
    amount = 5 
    coins = [1, 2, 5]
    result = sol.change(amount, coins)
    print(result)