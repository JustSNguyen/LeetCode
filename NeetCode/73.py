from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        turn_first_row_to_zero = False
        for i in range(n):
            if matrix[0][i] == 0:
                turn_first_row_to_zero = True
                break

        turn_first_col_to_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                turn_first_col_to_zero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if turn_first_row_to_zero:
            for i in range(n):
                matrix[0][i] = 0

        if turn_first_col_to_zero:
            for i in range(m):
                matrix[i][0] = 0





        