from typing import List 
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        ans = 0 
        for i in range(N):
            for j in range(i):
                d = nums[j] - nums[i]
                dp[i][d] += dp[j][d] + 1
                ans += dp[j][d]

        return ans 