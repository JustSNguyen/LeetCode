from typing import List 

class Solution:
    def trap(self, heights: List[int]) -> int:
        N = len(heights)
        max_left = [0 for _ in range(N)]
        max_right = [0 for _ in range(N)]

        for i in range(N):
            if i == 0: continue
            max_left[i] = max(max_left[i - 1], heights[i - 1])
        
        for j in range(N - 1, -1, -1):
            if j == N - 1: continue 
            max_right[j] = max(max_right[j + 1], heights[j + 1])
        
        result = 0 
        for i in range(1, N - 1):
            if heights[i] >= min(max_left[i], max_right[i]):
                continue 

            result += min(max_left[i], max_right[i]) - heights[i]
        
        return result 

if __name__ == '__main__':
    sol = Solution()
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = sol.trap(heights)
    print(result)