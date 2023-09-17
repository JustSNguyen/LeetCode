from typing import List
from functools import lru_cache
import math

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def is_complete_square(num):
            sqrt_num = math.ceil(math.sqrt(num))
            return sqrt_num * sqrt_num == num

        N = len(nums)


        @lru_cache(maxsize = 10**5)
        def maximum_sum_dp(index):
            result = 0
            for j in range(index + 1, N + 1):
                if is_complete_square(index * j):
                    result_j = maximum_sum_dp(j)
                    result = max(result, result_j)

            result += nums[index - 1]

            return result

        max_result = 0
        for i in range(1, N + 1):
            result = maximum_sum_dp(i)
            max_result = max(result, max_result)

        return max_result

if __name__ == '__main__':
    sol = Solution()
    nums =  [8,7,3,5,7,2,4,9]
    result = sol.maximumSum(nums)
    print(result)




