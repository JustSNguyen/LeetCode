from typing import List
from functools import lru_cache

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        existed = set()
        for num in nums:
            existed.add(num)

        @lru_cache(maxsize=None)
        def dp(num):
            if num + 1 in existed:
                return 1 + dp(num + 1)

            return 1

        max_result = 0
        for num in nums:
            max_result = max(max_result, dp(num))

        return max_result
