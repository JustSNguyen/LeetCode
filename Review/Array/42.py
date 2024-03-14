from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        max_left = 0
        max_right = 0
        lf = 0
        rg = len(heights) - 1
        total = 0

        while rg - lf > 1:
            max_left = max(max_left, heights[lf])
            max_right = max(max_right, heights[rg])
            if max_left < max_right:
                lf += 1
                if heights[lf] < max_left:
                    total += max_left - heights[lf]
            else:
                rg -= 1
                if heights[rg] < max_right:
                    total += max_right - heights[rg]

        return total

if __name__ == '__main__':
    sol = Solution()
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = sol.trap(heights)
    print(result)

