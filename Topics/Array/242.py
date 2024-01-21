from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for char in s: 
            count_s[char] += 1 
        
        for char in t:
            count_t[char] += 1 
        
        for char in s: 
            if count_s[char] != count_t[char]:
                return False 
        
        for char in t: 
            if count_t[char] != count_s[char]:
                return False 
        
        return True 