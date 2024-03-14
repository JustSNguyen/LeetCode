from typing import List
import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_ith_bit_of_num(num, i):
            return (num >> i) & 1

        def set_ith_bit_to_1(num, i):
            return num | (1 << i)

        N = len(board)
        sqrt_N = math.sqrt(N)

        cols = [0 for _ in range(N)]
        rows = [0 for _ in range(N)]
        boxes = [0 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    continue

                value = int(board[i][j])
                if get_ith_bit_of_num(cols[j], value) == 1:
                    return False

                if get_ith_bit_of_num(rows[i], value) == 1:
                    return False

                box_index = int((i // sqrt_N) * sqrt_N + j // sqrt_N)
                if get_ith_bit_of_num(boxes[box_index], value) == 1:
                    return False

                cols[j] = set_ith_bit_to_1(cols[j], value)
                rows[i] = set_ith_bit_to_1(rows[i], value)
                boxes[box_index] = set_ith_bit_to_1(boxes[box_index], value)

        return True

if __name__ == '__main__':
    board = "hasagi"
    sol = Solution()
    print(sol.isValidSudoku(board))