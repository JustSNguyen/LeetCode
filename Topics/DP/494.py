from typing import List 
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], T: int) -> int:
        n = len(nums)

        S = sum(nums)
        if (S + T) % 2 != 0:
            return 0

        target = (S + T) // 2
        if target < 0:
            return 0

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for j in range(n - 1, -1, -1):
            for i in range(target, nums[j] - 1, -1):
                dp[i] += dp[i - nums[j]]

        return dp[target]

if __name__ == '__main__':
    sol = Solution()
    nums = [100]
    target = -100
    result = sol.findTargetSumWays(nums, target)
    print(result)
