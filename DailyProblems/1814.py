import math

from typing import List
from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            result = 0
            number_of_digits = 1 if num <= 1 else math.floor(math.log10(num)) + 1
            power_of_ten = 10**(number_of_digits - 1)

            while num:
                digit = num % 10
                result += digit * power_of_ten

                power_of_ten //= 10
                num //= 10

            return result

        diffs = [num - rev(num) for num in nums]
        count = defaultdict(int)
        result = 0
        MOD = 10**9 + 7

        for diff in diffs:
            result += count[diff]
            count[diff] += 1

        result %= MOD

        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [13,10,35,24,76]
    result = sol.countNicePairs(nums)
    print(result)