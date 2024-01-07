from typing import List 

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        if n == 1:
            return [0, 1]
        
        result = [0, 1]
        p = 1 
        k = 2 

        while k <= n:
            if p * 2 == k:
                p = k 
                result.append(1)
            else:
                temp = result[p] + result[k - p]
                result.append(temp)
            k += 1 
        
        return result 