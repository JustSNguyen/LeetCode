from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_stack = deque()
        max_stack = deque()
        max_length = 0
        j = 0

        for i, num in enumerate(nums):
            while min_stack and nums[min_stack[-1]] >= num:
                min_stack.pop()

            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] <= num:
                max_stack.pop()

            max_stack.append(i)

            while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                j += 1
                if max_stack[0] < j:
                    max_stack.popleft()

                if min_stack[0] < j:
                    min_stack.popleft()

            max_length = max(max_length, i - j + 1)

        return max_length

if __name__ == '__main__':
    sol = Solution()
    test = [8,2,4,7]
    limit = 4
    result = sol.longestSubarray(test, limit)