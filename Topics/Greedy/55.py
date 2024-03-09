from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_pos = 0
        for i, num in enumerate(nums):
            if furthest_pos < i:
                return False

            furthest_pos = max(furthest_pos, i + num)

        return True 