from typing import List
from collections import defaultdict


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_pos = defaultdict(int)
        count = defaultdict(int)

        prefix_sum = []
        cur_prefix_sum = 0
        for time in travel:
            cur_prefix_sum += time
            prefix_sum.append(cur_prefix_sum)

        for i, house in enumerate(garbage):
            for char in house:
                count[char] += 1
                last_pos[char] = i

        total = 0
        for char in count:
            total += count[char]

            if last_pos[char] - 1 >= 0:
                total += prefix_sum[last_pos[char] - 1]

        return total
