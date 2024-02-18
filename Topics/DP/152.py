from typing import List 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**12
        dp_max = [0 for _ in range(n)]
        dp_min = [INF for _ in range(n)]

        dp_max[n - 1] = nums[n - 1] 
        dp_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] < 0:
                dp_max[i] = max(nums[i], nums[i] * dp_min[i + 1])
                dp_min[i] = min(nums[i], nums[i] * dp_max[i + 1])
            else:
                dp_max[i] = max(nums[i], nums[i] * dp_max[i + 1])
                dp_min[i] = min(nums[i], nums[i] * dp_min[i + 1])
        
        return max(dp_max)
        