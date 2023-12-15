from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        sum = 0
        for i in range(m):
            sum += mat[i][i] + mat[i][n - i - 1]
            if n - i - 1 == i:
                sum -= mat[i][i]

        return sum