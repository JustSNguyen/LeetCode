from collections import defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        def is_valid(count):
            return count["Q"] <= N // 4 and count["W"] <= N // 4 and count["E"] <= N // 4 and count["R"] <= N // 4

        count = defaultdict(int)
        for char in s:
            count[char] += 1 
        
        if is_valid(count):
            return 0 
        
        min_length = N 
        i = 0 
        for j in range(N):
            count[s[j]] -= 1 
            while is_valid(count) and i != j:
                count[s[i]] += 1 
                if is_valid(count):
                    i += 1 
                else:
                    count[s[i]] -= 1 
                    break 
            
            if is_valid(count):
                min_length = min(min_length, j - i + 1)
        
        return min_length

