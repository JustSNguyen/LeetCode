from typing import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_of_num = defaultdict(int)
        count_of_identical_pairs = 0

        for num in nums:
            count_of_identical_pairs += count_of_num[num]
            count_of_num[num] += 1

        return count_of_identical_pairs

