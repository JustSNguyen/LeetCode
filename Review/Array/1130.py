from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        decreasing_stack = []
        total = 0
        for value in arr:
            while decreasing_stack and decreasing_stack[-1] <= value:
                leaf1 = decreasing_stack.pop()
                leaf2 = value
                if decreasing_stack and decreasing_stack[-1] <= value:
                    leaf2 = decreasing_stack[-1]

                total += leaf1 * leaf2

            decreasing_stack.append(value)

        while decreasing_stack:
            if len(decreasing_stack) == 1:
                decreasing_stack.pop()
            else:
                leaf1 = decreasing_stack.pop()
                leaf2 = decreasing_stack.pop()
                total += leaf1 * leaf2
                decreasing_stack.append(max(leaf1, leaf2))

        return total
