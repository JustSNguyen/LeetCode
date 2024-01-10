from typing import List 
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0 
        j = 0 
        count = defaultdict(int)

        for i in range(len(fruits)):
            count[fruits[i]] += 1 

            while len(count) > 2 and j != i:
                count[fruits[j]] -= 1 
                if count[fruits[j]] == 0:
                    del count[fruits[j]] 
                
                j += 1 
            
            if len(count) <= 2:
                max_length = max(max_length, i - j + 1)
        
        return max_length