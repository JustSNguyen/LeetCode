from typing import List 

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        number_of_rows, number_of_columns = len(grid), len(grid[0])

        non_qualified_i = -1 
        non_qualified_j = -1 

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if grid[i][j] > 1:
                    non_qualified_i = i 
                    non_qualified_j = j 
        
        if non_qualified_i == -1 and non_qualified_j == -1:
            return 0 

        min_result = 10**9 

        new_grid = [[row[i] for i in range(number_of_columns)] for row in grid]

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if grid[i][j] == 0:
                    dist = abs(i - non_qualified_i) + abs(j - non_qualified_j)
                    new_grid[i][j] = 1 
                    new_grid[non_qualified_i][non_qualified_j] -= 1 

                    min_result = min(min_result, self.minimumMoves(new_grid) + dist)

                    new_grid[i][j] = grid[i][j]
                    new_grid[non_qualified_i][non_qualified_j] += 1 
        
        return min_result 
    
if __name__ == '__main__':
    sol = Solution()
    grid =  [[1,3,0],[1,0,0],[1,0,3]]
    result = sol.minimumMoves(grid)
    print(result)