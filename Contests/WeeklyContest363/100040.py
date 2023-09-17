import bisect
from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(nums))
        number_of_nums = len(sorted_nums)
        existed = dict()

        for num in nums:
            existed[num] = True

        total_ways = 0

        for i in range(number_of_nums + 1):
            if i in existed:
                continue

            number_of_nums_smaller_than_i = bisect.bisect_right(sorted_nums, i)
            if number_of_nums_smaller_than_i == i:
                total_ways += 1

        return total_ways

if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    result = sol.countWays(nums)
    print(result)