from collections import deque
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        processed = set()

        q = deque()
        q.append((0, 0))

        while q:
            i, j = q.popleft()

            if (i, j) in processed:
                continue

            processed.add((i, j))

            result.append(nums[i][j])

            if i + 1 < len(nums) and j < len(nums[i + 1]):
                q.append((i + 1, j))

            if j + 1 < len(nums[i]):
                q.append((i, j + 1))

        return result