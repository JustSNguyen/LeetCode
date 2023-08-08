from typing import List 
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        maximum_safeness_factor = [[-1 for _ in range(N)] for _ in range(N)]

        queue = deque()

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1: 
                    maximum_safeness_factor[i][j] = 0 
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()

            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for offset in offsets:
                new_i = i + offset[0]
                new_j = j + offset[1]

                if new_i < 0 or new_j < 0 or new_i >= N or new_j >= N:
                    continue 

                if maximum_safeness_factor[new_i][new_j] == -1:
                    queue.append((new_i, new_j))
                
                if maximum_safeness_factor[i][j] > maximum_safeness_factor[new_i][new_j]:
                    maximum_safeness_factor[new_i][new_j] = maximum_safeness_factor[i][j]
                
        
        return maximum_safeness_factor[N - 1][N - 1]
        

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,1],[0,0,0],[0,0,0]]
    result = sol.maximumSafenessFactor(grid)
    print(result)