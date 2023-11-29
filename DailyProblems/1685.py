from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_sum = [0 for _ in range(N)]

        for i, num in enumerate(nums):
            if i == 0:
                prefix_sum[i] = num
            else:
                prefix_sum[i] = prefix_sum[i - 1] + num

        result = []
        for k in range(N):
            temp = nums[k] * (2 * k + 2 - N) + prefix_sum[N - 1] - 2 * prefix_sum[k]
            result.append(temp)

        return result