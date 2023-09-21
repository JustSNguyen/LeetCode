from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_of_removed_part = sum(nums) - x

        prefix_sum_position = dict()
        current_prefix_sum = 0
        length_of_removed_part = -1
        for i, num in enumerate(nums):
            current_prefix_sum += num
            prefix_sum_position[current_prefix_sum] = i
            left_sum = current_prefix_sum - sum_of_removed_part

            if left_sum == 0:
                length_of_removed_part = max(length_of_removed_part, i + 1)

            if left_sum in prefix_sum_position:
                possible_length_of_removed_part = i - prefix_sum_position[left_sum]
                length_of_removed_part = max(length_of_removed_part, possible_length_of_removed_part)

        if length_of_removed_part == -1:
            return -1

        return len(nums) - length_of_removed_part

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,4,2,3]
    x = 5
    result = sol.minOperations(nums, x)
    print(result)
