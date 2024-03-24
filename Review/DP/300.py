from typing import List 
from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(maxsize=None)
        def dp(i):
            max_length = 1 
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    max_length = max(max_length, dp(j) + 1)
            
            return max_length
        
        max_result = 0 
        for i in range(n):
            max_result = max(max_result, dp(i))
        
        return max_result 
    
if __name__ == '__main__':
    sol = Solution()
    nums = [7,7]
    result = sol.lengthOfLIS(nums)
    print(result)