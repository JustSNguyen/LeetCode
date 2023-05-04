from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_majority_element = 0 
        count = 0 
        for num in nums: 
            if count == 0:
                current_majority_element = num 
                count += 1 
            
            elif num != current_majority_element:
                count -= 1 
            
            else: 
                count += 1 

        return current_majority_element