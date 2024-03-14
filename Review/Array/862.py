from typing import List
import bisect

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        decreasing_stack_by_value = [0]
        decreasing_stack_by_index = [-1]
        prefix_sum = 0
        INF = len(nums) + 1
        min_length = INF
        for i, num in enumerate(nums):
            prefix_sum += num
            max_other = prefix_sum - k
            if max_other >= decreasing_stack_by_value[0]:
                insert_position = bisect.bisect_right(decreasing_stack_by_value, max_other) - 1
                j = decreasing_stack_by_index[insert_position]
                min_length = min(min_length, i - j)

            while decreasing_stack_by_value and prefix_sum <= decreasing_stack_by_value[-1]:
                decreasing_stack_by_value.pop()
                decreasing_stack_by_index.pop()

            decreasing_stack_by_value.append(prefix_sum)
            decreasing_stack_by_index.append(i)

        if min_length == INF:
            return -1

        return min_length

if __name__ == '__main__':
    nums = [17,85,93,-45,-21]
    k = 150
    sol = Solution()
    result = sol.shortestSubarray(nums, k)
    print(result)