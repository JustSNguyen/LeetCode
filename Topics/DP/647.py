class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        result = 0 

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i <= 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] if s[i] == s[j] else False 

                if dp[i][j]:
                    result += 1 
        
        return result 