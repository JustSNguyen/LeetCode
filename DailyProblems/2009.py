from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        sorted_nums = list(sorted(nums))
        distinct_sorted_nums = []
        existed = dict()

        for num in sorted_nums:
            if num not in existed:
                existed[num] = True
                distinct_sorted_nums.append(num)

        def count_values_in_ranges(min_value, max_value):
            number_of_values_smaller_than_min = bisect.bisect_left(distinct_sorted_nums, min_value)
            number_of_values_greater_than_max = len(distinct_sorted_nums) - bisect.bisect_right(distinct_sorted_nums, max_value)
            return len(distinct_sorted_nums) - number_of_values_smaller_than_min - number_of_values_greater_than_max

        def calculate_min_operations(index):
            min_value = sorted_nums[index] - index
            max_value = sorted_nums[index] + N - index - 1
            option1 = N - count_values_in_ranges(min_value, max_value)

            min_value = sorted_nums[index]
            max_value = sorted_nums[index] + N - 1
            option2 = N - count_values_in_ranges(min_value, max_value)

            min_value = sorted_nums[index] - N + 1
            max_value = sorted_nums[index]
            option3 = N

            if min_value >= 1:
                option3 = N - count_values_in_ranges(min_value, max_value)

            return min(option1, option2, option3)

        min_operations = N
        for i in range(N):
            operations = calculate_min_operations(i)
            min_operations = min(min_operations, operations)

        return min_operations

if __name__ == '__main__':
    sol = Solution()
    nums = [10,49,16,22,28,34,35,7]
    result = sol.minOperations(nums)
    print(result)