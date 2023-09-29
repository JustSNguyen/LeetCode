from typing import List

class Solution:
    def maximumSumOfHeights(self, max_heights: List[int]) -> int:
        N = len(max_heights)
        left = [0 for _ in range(N)]
        left_sum = 0
        stack = []
        for i in range(N):
            while stack and max_heights[i] < max_heights[stack[-1]]:
                j = stack.pop()

                multiply = j + 1
                if stack:
                    multiply = j - stack[-1]

                left_sum -= max_heights[j] * multiply
                left_sum += max_heights[i] * multiply

            stack.append(i)
            left_sum += max_heights[i]
            left[i] = left_sum

        right = [0 for _ in range(N)]
        right_sum = 0
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and max_heights[i] < max_heights[stack[-1]]:
                j = stack.pop()

                multiply = N - j
                if stack:
                    multiply = stack[-1] - j

                right_sum -= max_heights[j] * multiply
                right_sum += max_heights[i] * multiply

            stack.append(i)
            right_sum += max_heights[i]
            right[i] = right_sum

        max_result = 0
        for i in range(N):
            max_result = max(max_result, left[i] + right[i] - max_heights[i])

        return max_result

if __name__ == '__main__':
    sol = Solution()
    maxHeights = [6,5,3,9,2,7]
    result = sol.maximumSumOfHeights(maxHeights)
    print(result)