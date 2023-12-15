import bisect
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = 0
        MOD = 10**9 + 7


        for i, num in enumerate(nums):
            max_min = target - num

            if num > target or max_min < nums[0]:
                return result

            if i == 0:
                result += 1
                result %= MOD
                continue

            j = bisect.bisect_left(nums, max_min, 0, i)
            if nums[j] > max_min:
                j -= 1

            if i != j:
                first_half = (2**(j + 1) - 1) % MOD
                second_half = 2**(i - j - 1) % MOD
                addition = (first_half * second_half) % MOD
            else:
                addition = 2**j % MOD

            result += addition
            result %= MOD

        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [3,3,6, 8]
    target = 10
    result = sol.numSubseq(nums, target)
    print(result)