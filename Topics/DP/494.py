from typing import List 
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(target, j):
            if j == 0:
                result = 0 
                if target == nums[j]:
                    result += 1 
                if target == -nums[j]:
                    result += 1 
                
                return result 
            
            return dp(target - nums[j], j - 1) + dp(target + nums[j], j - 1)

        
        return dp(target, len(nums) - 1)