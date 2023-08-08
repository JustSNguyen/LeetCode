from typing import List

class Solution:
    def trap(self, bars_height: List[int]) -> int:
        total_bars = len(bars_height)
        left_max = [bars_height[i] for i in range(total_bars)]
        right_max = [bars_height[i] for i in range(total_bars)]

        for i in range(1, total_bars):
            left_max[i] = max(left_max[i - 1], bars_height[i])
        
        for i in range(total_bars - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], bars_height[i])
        
        total_trapping_water = 0 
        for i, height in enumerate(bars_height):
            total_trapping_water += min(left_max[i], right_max[i]) - height

        return total_trapping_water

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    print(sol.trap(height))