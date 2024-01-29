from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def generate(temp, temp_sum, index):
            if index == len(candidates):
                if temp_sum == target:
                    result.append(temp)

                return

            candidate = candidates[index]
            remaining_target = target - temp_sum
            max_choices = remaining_target // candidate
            for i in range(max_choices + 1):
                new_temp = temp[:]
                new_temp.extend([candidate] * i)
                new_temp_sum = temp_sum + candidate * i
                generate(new_temp, new_temp_sum, index + 1)

        generate([], 0, 0)
        return result