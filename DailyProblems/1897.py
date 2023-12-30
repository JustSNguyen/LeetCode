from typing import List 
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        N = len(words)
        char_count = defaultdict(int)

        for word in words:
            for char in word:
                char_count[char] += 1 
        
        for char in char_count:
            count = char_count[char]
            if count % N != 0:
                return False 
        
        return True 
