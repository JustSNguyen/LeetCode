from typing import List 
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_length = len(nums) + 1 
        increasing_queue = deque()

        prefix_sum = [nums[i] for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i - 1] + nums[i]

            if prefix_sum[i] >= k:
                min_length = min(min_length, i + 1)

        for i, num in enumerate(nums):
            j = -1

            while increasing_queue and prefix_sum[i] - prefix_sum[increasing_queue[0]] >= k:
                j = increasing_queue[0] + 1
                increasing_queue.popleft()

            if j != -1:
                min_length = min(min_length, i - j + 1)

            while increasing_queue and prefix_sum[i] <= prefix_sum[increasing_queue[-1]]:
                increasing_queue.pop()

            increasing_queue.append(i)

        if min_length == len(nums) + 1:
            return -1

        return min_length

if __name__ == '__main__':
    sol = Solution()
    test = [1]
    k = 1
    result = sol.shortestSubarray(test, k)
    print(result)