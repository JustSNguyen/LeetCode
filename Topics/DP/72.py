from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                if i == n1:
                    if j != n2:
                        dp[i][j] = n2 - j
                    continue

                if j == n2:
                    dp[i][j] = n1 - i
                    continue

                insert_option = 1 + dp[i][j + 1]
                replace_option = 1 + dp[i + 1][j + 1] if word1[i] != word2[j] else dp[i + 1][j + 1]
                delete_option = 1 + dp[i + 1][j]
                dp[i][j] = min(insert_option, replace_option, delete_option)

        return dp[0][0]


