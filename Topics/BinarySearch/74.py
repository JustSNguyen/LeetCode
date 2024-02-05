from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       M = len(matrix)
       N = len(matrix[0])

       if target < matrix[0][0] or target > matrix[M - 1][N - 1]:
           return False

       lf = 0
       rg = M * N
       while rg - lf > 1:
           mid = (lf + rg) // 2
           i = mid // N
           j = mid % N
           if matrix[i][j] == target:
               return True

           if matrix[i][j] > target:
               rg = mid
           else:
               lf = mid + 1

       i = lf // N
       j = lf % N
       if matrix[i][j] == target:
           return True

       return False