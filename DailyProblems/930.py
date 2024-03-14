from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        prefix_sum = 0
        result = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            other = prefix_sum - goal
            result += prefix_sum_count[other]
            prefix_sum_count[prefix_sum] += 1

        return result


    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     def count_subarrays_with_sum_at_most(K):
    #         cur_sum = 0
    #         result = 0
    #         j = 0
    #         for i, num in enumerate(nums):
    #             cur_sum += num
    #             while j <= i and cur_sum > K:
    #                 cur_sum -= nums[j]
    #                 j += 1
    #
    #             if j <= i:
    #                 result += i - j + 1
    #
    #         return result
    #
    #     return count_subarrays_with_sum_at_most(goal) - count_subarrays_with_sum_at_most(goal - 1)
