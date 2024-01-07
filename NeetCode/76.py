from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        M = len(t)
        expected_count = defaultdict(int)
        count = defaultdict(int)

        for char in t:
            expected_count[char] += 1 

        l = 0 
        r = 0 
        result = (0, N + 1)
        while r < N:
            count[s[r]] += 1 
            valid = True 
            for char in expected_count:
                if expected_count[char] > count[char]:
                    valid = False 
                    break 
            
            if valid:
                new_length = r - l + 1 
                if new_length < result[1] - result[0] + 1:
                    result = (l, r)
                
                while valid and l < r:
                    count[s[l]] -= 1 
                    for char in expected_count:
                        if expected_count[char] > count[char]:
                            valid = False 
                            break 
                    
                    l += 1 
                    if valid:
                        new_length = r - l + 1 
                        if new_length < result[1] - result[0] + 1:
                            result = (l, r)
            
            r += 1
        
        if result[1] == N + 1:
            return ""
        
        return s[result[0]:result[1] + 1]