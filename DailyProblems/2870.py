from typing import List
from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1 
        
        min_operations = 0 
        for num in count:
            if count[num] < 2:
                return -1 
            
            if count[num] % 3 != 1:
                second_operations = count[num] // 3 
                first_operations = (count[num] - second_operations * 3) // 2 
            else:
                first_operations = 2 
                second_operations = (count[num] - first_operations * 2) // 3 
            
            min_operations += (second_operations + first_operations)
        
        return min_operations