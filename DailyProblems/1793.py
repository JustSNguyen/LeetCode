from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums_length = len(nums)

        nearest_left_index_with_smaller_value = [-1 for _ in range(nums_length)]
        strictly_increasing_stack = []
        for i in range(nums_length):
            while strictly_increasing_stack and nums[strictly_increasing_stack[-1]] >= nums[i]:
                strictly_increasing_stack.pop()

            if strictly_increasing_stack:
                nearest_left_index_with_smaller_value[i] = strictly_increasing_stack[-1]

            strictly_increasing_stack.append(i)

        nearest_right_index_with_smaller_value = [nums_length for _ in range(nums_length)]
        strictly_increasing_stack = []
        for i in range(nums_length - 1, -1, -1):
            while strictly_increasing_stack and nums[strictly_increasing_stack[-1]] >= nums[i]:
                strictly_increasing_stack.pop()

            if strictly_increasing_stack:
                nearest_right_index_with_smaller_value[i] = strictly_increasing_stack[-1]

            strictly_increasing_stack.append(i)

        max_score = 0
        for i in range(nums_length):
            start_of_good_subarray = nearest_left_index_with_smaller_value[i] + 1
            end_of_good_subarray = nearest_right_index_with_smaller_value[i] - 1

            if start_of_good_subarray <= k <= end_of_good_subarray:
                current_good_subarray_score = nums[i] * (end_of_good_subarray - start_of_good_subarray + 1)
                max_score = max(max_score, current_good_subarray_score)

        return max_score


if __name__ == '__main__':
    sol = Solution()
    nums = [5,5,4,5,4,1,1,1]
    k = 0
    result = sol.maximumScore(nums, k)
    print(result)
