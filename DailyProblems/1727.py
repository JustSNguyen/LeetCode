from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        max_result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]

                sorted_row = sorted(matrix[i], reverse=True)

                for k in range(n):
                    max_result = max(max_result, sorted_row[k] * (k + 1))

        return max_result
