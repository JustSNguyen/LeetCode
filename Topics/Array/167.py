from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lf = 0
        rg = len(numbers) - 1

        while lf < rg:
            current = numbers[lf] + numbers[rg]
            if current == target:
                return [lf + 1, rg + 1]

            if current > target:
                rg -= 1

            if current < target:
                lf += 1

