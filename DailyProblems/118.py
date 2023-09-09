from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = [[1]]
        cur_row_result = []
        prev_row = pascal_triangle[0]
        while len(pascal_triangle) < numRows:
            cur_row_result.append(1)

            for i in range(1, len(prev_row)):
                cur_row_result.append(prev_row[i - 1] + prev_row[i])

            cur_row_result.append(1)

            prev_row = cur_row_result
            pascal_triangle.append(cur_row_result)
            cur_row_result = []
        
        return pascal_triangle
        