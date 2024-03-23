from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N1 = len(s)
        N2 = len(p)

        @lru_cache(maxsize = None)
        def dp(i, j):
            if j == N2:
                return i == N1 

            if i == N1:
                for k in range(j, N2):
                    is_star_next = k < N2 - 1 and p[k + 1] == "*"
                    if p[k] != "*" and not is_star_next:
                        return False 
                    
                return True 

            
            is_star_next = j < N2 - 1 and p[j + 1] == "*"

            if not is_star_next:
                if p[j] == "." or s[i] == p[j]:
                    return dp(i + 1, j + 1)

                return False 

            max_repeat_time = N1 - i 
            match = False 
            for r in range(max_repeat_time + 1):
                for k in range(r):
                    if s[i + k] != p[j] and p[j] != ".":
                        return match 
                
                match |= dp(i + r, j + 2)

                if match:
                    return match 
            
            return match 
        
        return dp(0, 0)
                
