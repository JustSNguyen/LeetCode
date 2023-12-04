from typing import List 
from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = defaultdict(int)

        for char in chars:
            count[char] +=1  
        
        total_characters = 0 
        for word in words:
            is_valid = True 
            temp_count = defaultdict(int)
            for char in word:
                temp_count[char] += 1 
                if temp_count[char] > count[char]:
                    is_valid = False 
                    break 
            
            if is_valid:
                total_characters += len(word)
            
        
        return total_characters
