from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreasing_stack = []
        n = len(temperatures)
        result = [0 for _ in range(n)]

        for i, temperature in enumerate(temperatures):
            while decreasing_stack and temperatures[decreasing_stack[-1]] < temperature:
                j = decreasing_stack.pop()
                result[j] = i - j

            decreasing_stack.append(i)

        return result