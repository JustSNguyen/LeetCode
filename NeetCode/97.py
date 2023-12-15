class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if (m + n) != len(s3):
            return False

        dp = [False for _ in range(n + 1)]
        dp2 = [False for _ in range(n + 1)]

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                k = i + j
                dp[j] = False
                if i == m and j == n:
                    dp[n] = True
                if i < m and s1[i] == s3[k]:
                    dp[j] |= dp2[j]
                if j < n and s2[j] == s3[k]:
                    dp[j] |= dp[j + 1]

            dp2 = dp.copy()

        return dp[0]

if __name__ == "__main__":
    sol = Solution()
    s1 = "a"
    s2 = ""
    s3 = "c"
    result = sol.isInterleave(s1, s2, s3)
    print(result)
