from typing import List 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing_numbers = dict()
        for num in nums:
            if num in existing_numbers: 
                return True 

            existing_numbers[num] = True 

        return False