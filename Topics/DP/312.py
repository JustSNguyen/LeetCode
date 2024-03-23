from typing import List 
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        N = len(nums)

        @lru_cache(maxsize=None)
        def dp(i, j):
            max_value = 0 
            for k in range(i + 1, j):
                max_value = max(max_value, dp(i, k) + dp(k, j) + nums[i] * nums[k] * nums[j])

            return max_value
        
        return dp(0, N - 1)
    
if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 5, 8]
    result = sol.maxCoins(nums)
    print(result)