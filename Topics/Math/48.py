from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix):
            N = len(matrix)
            for i in range(N):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        
        def reverse_cols(matrix):
            N = len(matrix) 
            for j1 in range(N // 2):
                j2 = N - j1 - 1
                for i in range(N):
                    matrix[i][j1], matrix[i][j2] = matrix[i][j2], matrix[i][j1]
        
        transpose(matrix)
        reverse_cols(matrix)
        