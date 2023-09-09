from functools import lru_cache
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=1005)
        def count_number_of_combination_of(target):
            if target < 0:
                return 0

            if target == 0:
                return 1 

            result = 0 
            for num in nums:
                result += count_number_of_combination_of(target - num) 

            return result 
        
        return count_number_of_combination_of(target)