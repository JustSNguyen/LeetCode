from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1 for _ in range(N)]
        prefix = 1
        for i, num in enumerate(nums):
            result[i] = prefix
            prefix *= num

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                result[i] = suffix
            else:
                result[i] *= suffix

            suffix *= nums[i]

        return result
