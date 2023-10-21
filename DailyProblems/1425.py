import bisect

from functools import lru_cache
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        nums_length = len(nums)
        indexes_with_non_negative_value = []
        for i, num in enumerate(nums):
            if num >= 0:
                indexes_with_non_negative_value.append(i)

        def get_first_non_negative_value_index_from(index: int) -> int:
            if not indexes_with_non_negative_value:
                return -1

            if index < indexes_with_non_negative_value[0] or index > indexes_with_non_negative_value[-1]:
                return -1

            j = bisect.bisect_left(indexes_with_non_negative_value, index)
            return indexes_with_non_negative_value[j]

        @lru_cache(maxsize=nums_length)
        def max_subsequence_sum_from(index: int) -> int:
            if index == nums_length - 1:
                return nums[index]

            first_non_negative_value_index = get_first_non_negative_value_index_from(index + 1)

            if first_non_negative_value_index == -1 or first_non_negative_value_index - index > k:
                return nums[index]

            return nums[index] + max_subsequence_sum_from(first_non_negative_value_index)

        max_subsequence_sum = nums[0]
        for i in range(nums_length):
            max_subsequence_sum = max(max_subsequence_sum_from(i), max_subsequence_sum)

        return max_subsequence_sum


if __name__ == '__main__':
    sol = Solution()
    nums = [-3, -2, -1]
    k = 1
    result = sol.constrainedSubsetSum(nums, k)
    print(result)


