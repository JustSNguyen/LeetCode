from typing import List
from collections import defaultdict

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        all_nums = sorted(count.keys(), reverse=True)

        result = 0
        for i, num in enumerate(all_nums):
            if i == len(all_nums) - 1:
                return result

            if i > 0:
                count[num] += count[all_nums[i - 1]]

            result += count[num]



