from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == n and j == m:
                return 0
            
            min_result = m + n 
            if j < m:
                min_result = min(min_result, dp(i, j + 1) + 1)
            
            if i < n:
                min_result = min(min_result, dp(i + 1, j) + 1)
            
            if i < n and j < m:
                cost = 1 if word1[i] != word2[j] else 0
                min_result = min(min_result, dp(i + 1, j + 1) + cost)
            
            return min_result

        return dp(0, 0)