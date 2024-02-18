from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = 0 
        dp_1 = nums[n - 1]
        dp_2 = 0  

        for i in range(n - 2, -1, -1):
            dp = max(nums[i] + dp_2, dp_1)
            dp_2 = dp_1 
            dp_1 = dp 
        
        return dp_1 