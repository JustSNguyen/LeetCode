from typing import List 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(target + 1)]

        for i in range(target + 1):
            for j in range(n):
                if j == 0:
                    if nums[i] == nums[j]:
                        dp[i][j] += 1 
                    if nums[i] == -nums[j]:
                        dp[i][j] += 1
                else:
                    dp[i][j] = dp[i - nums[j]][j - 1] + dp[i + nums[j]][j - 1]
        
        return dp[target][n - 1]