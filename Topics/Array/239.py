from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decreasing_queue = deque()
        result = []
        for j in range(len(nums)):
            i = j - k + 1

            while i >= 0 and decreasing_queue and decreasing_queue[0] < i:
                decreasing_queue.popleft()

            while decreasing_queue and nums[decreasing_queue[-1]] <= nums[j]:
                decreasing_queue.pop()

            decreasing_queue.append(j)

            if i >= 0:
                result.append(nums[decreasing_queue[0]])

        return result
