from typing import List 
import math 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def set_ith_bit_to_1(num, i):
            return num | (1 << i)
        
        def get_ith_bit_of_num(i, num):
            return (num >> i) & 1 
        
        N = len(board)
        sqrt_N = int(math.sqrt(N))

        rows = [0 for _ in range(N)]
        cols = [0 for _ in range(N)]
        boxes = [0 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                value = board[i][j]

                if value == ".":
                    continue

                value = int(value)

                if get_ith_bit_of_num(value, rows[i]) == 1:
                    return False 
                
                if get_ith_bit_of_num(value, cols[j]) == 1:
                    return False 

                box_index = (i // sqrt_N) * sqrt_N + j // sqrt_N

                if get_ith_bit_of_num(value, boxes[box_index]) == 1:
                    return False 
                
                rows[i] = set_ith_bit_to_1(rows[i], value)
                cols[j] = set_ith_bit_to_1(cols[j], value)
                boxes[box_index] = set_ith_bit_to_1(boxes[box_index], value)
            
        return True 