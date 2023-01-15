from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums_length = 0 
        prev = -101
        for num in nums: 
            if num != prev: 
                nums[new_nums_length] = num 
                new_nums_length += 1 
            
            prev = num 
        return new_nums_length
        