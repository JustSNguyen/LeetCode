from typing import List
from functools import lru_cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_pos = 0
        for i, num in enumerate(nums):
            if furthest_pos < i:
                return False

            furthest_pos = max(furthest_pos, i + num)

        return True

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 1, 0, 4]
    result = sol.canJump(nums)
    print(result)
