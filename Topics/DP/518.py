from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(n)] for _ in range(amount + 1)]

        for i in range(amount + 1):
            for j in range(n):
                if i == 0:
                    dp[i][j] = 1
                    continue 

                if j == 0:
                    dp[i][j] = 1 if i % coins[j] == 0 else 0 
                else:
                    dp[i][j] = dp[i][j - 1]
                    if i >= coins[j]:
                        dp[i][j] += dp[i - coins[j]][j]

        return dp[amount][n - 1]
    
if __name__ == '__main__':
    sol = Solution()
    amount = 5 
    coins = [1,2,5]
    result = sol.change(amount, coins)
    print(result)