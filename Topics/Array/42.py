from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        total = 0
        left = 0
        right = len(heights) - 1
        max_left = heights[left]
        max_right = heights[right]
        cur = left

        while left <= right:
            min_left_right = min(max_left, max_right)
            if heights[cur] < min_left_right:
                total += min_left_right - heights[cur]

            max_left = max(max_left, heights[left])
            max_right = max(max_right, heights[right])

            if max_left <= max_right:
                left += 1
                cur = left
            else:
                right -= 1
                cur = right

        return total

if __name__ == '__main__':
    sol = Solution()
    test = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = sol.trap(test)
    print(result)
