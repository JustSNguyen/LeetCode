from typing import List 
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(list)
        for i, num in enumerate(nums): 
            indexes[num].append(i)
        
        for num in nums:
            other = target - num  
            if other == num and len(indexes[num]) >= 2:
                return [indexes[num][0], indexes[num][1]] 
            
            if other != num and len(indexes[other]) >= 1:
                return [indexes[num][0], indexes[other][0]]

            