from functools import lru_cache

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        m = 5
        dp = [[0 for _ in range(n + 1)] for _ in range(m)]

        for i in range(m):
            dp[i][1] = 1 

        for j in range(2, n + 1):
            for i in range(m):
                if i == 2:
                    for k in range(m):
                        if k == i:
                            continue 

                        dp[i][j] += dp[k][j - 1]  
                        dp[i][j] %= MOD 
                
                elif i == 0:
                    dp[i][j] = dp[i + 1][j - 1]
                
                elif i == 4:
                    dp[i][j] = dp[0][j - 1]
                
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i + 1][j - 1]) % MOD 
        
        final_result = 0 
        for i in range(m):
            final_result += dp[i][n] 
            final_result %= MOD 
        
        return final_result
            
if __name__ == '__main__':
    sol = Solution()
    n = 5 
    result = sol.countVowelPermutation(n)
    print(result)