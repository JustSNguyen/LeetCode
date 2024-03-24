from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == j:
                return True 
            
            if i == j - 1:
                return s[i] == s[j]
            
            if s[i] != s[j]:
                return False 
            
            return dp(i + 1, j - 1)

        result = 0 
        for i in range(n):
            for j in range(i, n):
                result += dp(i, j)
        
        return result 