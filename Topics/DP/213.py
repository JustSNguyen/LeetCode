from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        dp[n - 1][0] = nums[n - 1] 
        dp[n - 1][1] = 0 

        for i in range(n - 2, -1, -1):
            if i == 0:
                dp[i][1] = nums[i] + dp[i + 2][1]
                dp[i][0] = dp[i + 1][0]
            else:
                dp[i][1] = max(nums[i] + dp[i + 2][1], dp[i + 1][1])
                dp[i][0] = max(nums[i] + dp[i + 2][0], dp[i + 1][0])
        
        return max(dp[0][1], dp[0][0])