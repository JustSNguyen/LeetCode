from typing import List
from collections import defaultdict

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = defaultdict(int)
        col_sum = defaultdict(int)

        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]

        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    result += 1

        return result