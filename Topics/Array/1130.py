from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        decreasing_stack = []
        cost = 0

        for num in arr:
            while decreasing_stack and decreasing_stack[-1] < num:
                pair = num if len(decreasing_stack) == 1 else min(num, decreasing_stack[-2])
                cost += pair * decreasing_stack[-1]
                decreasing_stack.pop()

            decreasing_stack.append(num)

        while decreasing_stack:
            if len(decreasing_stack) > 1:
                cost += decreasing_stack[-1] * decreasing_stack[-2]

            decreasing_stack.pop()

        return cost

if __name__ == '__main__':
    sol = Solution()
    arr = [4, 11]
    result = sol.mctFromLeafValues(arr)
    print(result)