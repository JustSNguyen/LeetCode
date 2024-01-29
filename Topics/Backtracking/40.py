from typing import List
from collections import defaultdict

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = defaultdict(int)
        for candidate in candidates:
            count[candidate] += 1

        result = []
        distinct_candidates = list(count.keys())
        def generate(temp, temp_sum, index):
            if temp_sum == target:
                result.append(temp)
                return

            if index == len(distinct_candidates):
                return

            remaining_sum = target - temp_sum
            candidate = distinct_candidates[index]
            max_choices = min(remaining_sum // candidate, count[candidate])
            for i in range(max_choices + 1):
                new_temp = temp[:]
                new_temp.extend([candidate] * i)
                new_temp_sum = temp_sum + candidate * i
                generate(new_temp, new_temp_sum, index + 1)

        generate([], 0, 0)
        return result

