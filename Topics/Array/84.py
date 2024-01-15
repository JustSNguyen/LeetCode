from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        first_smaller_on_left = [-1 for _ in range(N)]
        first_smaller_on_right = [N for _ in range(N)]

        increasing_stack = []
        for i in range(N):
            while increasing_stack and heights[i] <= heights[increasing_stack[-1]]:
                increasing_stack.pop()

            if increasing_stack:
                first_smaller_on_left[i] = increasing_stack[-1]

            increasing_stack.append(i)

        increasing_stack = []
        for i in range(N - 1, -1, -1):
            while increasing_stack and heights[i] <= heights[increasing_stack[-1]]:
                increasing_stack.pop()

            if increasing_stack:
                first_smaller_on_right[i] = increasing_stack[-1]

            increasing_stack.append(i)

        max_so_far = 0
        for i in range(N):
            start = first_smaller_on_left[i] + 1
            end = first_smaller_on_right[i] - 1
            width = end - start + 1
            height = heights[i]
            max_so_far = max(max_so_far, width * height)

        return max_so_far

if __name__ == '__main__':
    sol = Solution()
    heights = [1, 1]
    result = sol.largestRectangleArea(heights)
    print(result)
