from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        decreasing_stack = deque()
        max_sum = -10**12

        for i, num in enumerate(nums):
            j = i - k
            while decreasing_stack and decreasing_stack[0][1] < j:
                decreasing_stack.popleft()

            max_sum_ends_at_i = num
            if decreasing_stack:
                max_sum_ends_at_i += max(decreasing_stack[0][0], 0)

            while decreasing_stack and decreasing_stack[-1][0] <= max_sum_ends_at_i:
                decreasing_stack.pop()

            decreasing_stack.append((max_sum_ends_at_i, i))

            max_sum = max(max_sum, max_sum_ends_at_i)

        return max_sum

if __name__ == '__main__':
    sol = Solution()
    test = [10,-2,-10,-5,20]
    k = 2
    result = sol.constrainedSubsetSum(test, k)
    print(result)