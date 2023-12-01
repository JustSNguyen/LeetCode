from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = [0 for _ in range(max_num + 1)]

        for num in nums:
            count[num] += 1

        sorted_nums = []
        for i in range(len(count)):
            if count[i] != 0:
                for j in range(count[i]):
                    sorted_nums.append(i)

        N = len(nums)
        max_sum = 0
        for i in range(N // 2):
            cur_sum = sorted_nums[i] + sorted_nums[N - i - 1]
            max_sum = max(max_sum, cur_sum)

        return max_sum
