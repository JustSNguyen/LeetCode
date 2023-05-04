from typing import List 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_rows = len(grid)
        number_of_cols = len(grid[0])

        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        visited = [[False for _ in range(number_of_cols)] for _ in range(number_of_rows)]

        number_of_islands = 0 
        for i in range(number_of_rows):
            for j in range(number_of_cols):
                if visited[i][j] or grid[i][j] == "0": continue 

                number_of_islands += 1 

                stack = []
                stack.append((i, j)) 

                while stack: 
                    cur_i, cur_j = stack.pop() 
                    if visited[cur_i][cur_j]: continue 

                    visited[cur_i][cur_j] = True 

                    for offset in offsets: 
                        offset_x, offset_y = offset 
                        next_i, next_j = cur_i + offset_x, cur_j + offset_y 

                        if next_i < 0 or next_i >= number_of_rows: continue 
                        if next_j < 0 or next_j >= number_of_cols: continue 
                        if grid[next_i][next_j] == "0": continue 
                        if visited[next_i][next_j]: continue 

                        stack.append((next_i, next_j))
        
        return number_of_islands
    
if __name__ == "__main__":
    sol = Solution()
    grid = [
  ['1']
]
    result = sol.numIslands(grid)
    print(result)

                        