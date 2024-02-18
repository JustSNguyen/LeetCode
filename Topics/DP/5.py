class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_result = 0 
        start = 0 
        end = 0 

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True 
                elif i == j - 1:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = dp[i + 1][j - 1] if s[i] == s[j] else False

                if dp[i][j] and j - i + 1 > max_result:
                    max_result = j - i + 1 
                    start = i 
                    end = j 

        return s[start: end + 1]