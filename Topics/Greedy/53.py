from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = -10**12
        result = temp
        for num in nums:
            temp = max(num, num + temp)
            result = max(result, temp)

        return result