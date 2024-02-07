from typing import List 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        should_set_first_row_to_zero = False 
        should_set_first_col_to_zero = False 

        for i in range(N):
            if matrix[0][i] == 0:
                should_set_first_row_to_zero = True 
                break 
        
        for i in range(M):
            if matrix[i][0] == 0:
                should_set_first_col_to_zero = True 
                break 
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 
                    matrix[0][j] = 0 
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 
        
        if should_set_first_row_to_zero:
            for j in range(N):
                matrix[0][j] = 0 
        
        if should_set_first_col_to_zero:
            for i in range(M):
                matrix[i][0] = 0 
        