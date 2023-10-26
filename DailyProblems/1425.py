from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        nums_length = len(nums)
        max_numbers_so_far = deque()
        max_subsequence_sum_ends_at = [0 for _ in range(nums_length)]

        max_subsequence_sum_ends_at[0] = nums[0]
        max_numbers_so_far.append(0)

        for i in range(1, nums_length):
            while max_numbers_so_far and max_numbers_so_far[0] < i - k:
                max_numbers_so_far.popleft()

            j = max_numbers_so_far[0]
            max_subsequence_sum_ends_at[i] = max(max_subsequence_sum_ends_at[j] + nums[i], nums[i])

            while max_numbers_so_far and max_subsequence_sum_ends_at[max_numbers_so_far[-1]] <= max_subsequence_sum_ends_at[i]:
                max_numbers_so_far.pop()

            max_numbers_so_far.append(i)

        return max(max_subsequence_sum_ends_at)


if __name__ == '__main__':
    sol = Solution()
    nums = [-3, -2, -1]
    k = 1
    result = sol.constrainedSubsetSum(nums, k)
    print(result)


