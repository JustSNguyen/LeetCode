from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        lf = [-1 for i in range(N)]

        increasing_stack = []
        for i, height in enumerate(heights):
            while increasing_stack and heights[increasing_stack[-1]] >= height:
                increasing_stack.pop()

            if increasing_stack:
                lf[i] = increasing_stack[-1]

            increasing_stack.append(i)

        result = 0
        increasing_stack = []
        for i in range(N - 1, -1, -1):
            height = heights[i]

            while increasing_stack and heights[increasing_stack[-1]] >= height:
                increasing_stack.pop()

            rg = N
            if increasing_stack:
                rg = increasing_stack[-1]

            width = rg - lf[i] - 1

            result = max(result, width * height)

            increasing_stack.append(i)

        return result

if __name__ == '__main__':
    sol = Solution()
    heights = [2,1,5,6,2,3]
    result = sol.largestRectangleArea(heights)
    print(result)