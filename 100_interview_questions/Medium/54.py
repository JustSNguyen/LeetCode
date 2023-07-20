from typing import List 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        cur_row = 0 
        cur_col = 0 

        visited = [[False for _ in range(n)] for _ in range(m)]
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_offset_index = 0 


        result = []

        while True:
            cur_num = matrix[cur_row][cur_col]
            visited[cur_row][cur_col] = True 

            result.append(cur_num)

            if len(result) == m * n:
                return result 

            next_row, next_col = cur_row + offsets[cur_offset_index][0], cur_col + offsets[cur_offset_index][1]

            if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n or visited[next_row][next_col]:
                cur_offset_index = (cur_offset_index + 1) % len(offsets) 
                next_row, next_col = cur_row + offsets[cur_offset_index][0], cur_col + offsets[cur_offset_index][1]
            
            cur_row, cur_col = next_row, next_col

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    result = sol.spiralOrder(matrix)
    print(result)
