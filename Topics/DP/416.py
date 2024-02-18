from typing import List 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)

        if SUM % 2 == 1:
            return False

        N = len(nums)
        dp = [[False for _ in range(N)] for _ in range(SUM + 1)]
        
        for temp in range(SUM // 2 + 1):
            for i in range(N - 1, -1, -1):
                if temp == 0:
                    dp[temp][i] = True 
                    continue

                if i == N - 1:
                    dp[temp][i] = (nums[i] == temp)
                else:
                    if dp[temp][i + 1]: 
                        dp[temp][i] = True 
                    if nums[i] <= temp and dp[temp - nums[i]][i + 1]:
                        dp[temp][i] = True 
        
        return dp[SUM // 2][0]