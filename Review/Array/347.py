from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_with_frequency = defaultdict(list)
        frequency_of = defaultdict(int)

        for num in nums:
            frequency_of[num] += 1

        for num in frequency_of:
            freq = frequency_of[num]
            nums_with_frequency[freq].append(num)

        result = []
        for freq in range(len(nums), -1, -1):
            for num in nums_with_frequency[freq]:
                result.append(num)
                if len(result) == k:
                    return result


