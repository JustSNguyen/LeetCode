from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        k = len(s3)

        if m + n != k:
            return False 

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == n and j == m:
                return True 
            
            if i < n and s1[i] == s3[i + j] and dp(i + 1, j):
                return True 
            
            if j < m and s2[j] == s3[i + j] and dp(i, j + 1):
                return True 
            
            return False 
        
        return dp(0, 0)
