class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            dp[i][n2] = 1

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]