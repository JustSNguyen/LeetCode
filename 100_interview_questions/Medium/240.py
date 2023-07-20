from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row_index = 0 
        column_index = n - 1 

        while row_index < m and column_index >= 0:
            value = matrix[row_index][column_index]
            if value == target:
                return True 
            
            if value > target:
                column_index -= 1 
            
            else: 
                row_index += 1
        
        return False 
    