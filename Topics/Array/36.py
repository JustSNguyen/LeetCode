from typing import List
import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_ith_bit_of_num(num, i):
            return (num >> i) & 1

        def set_ith_bit_of_num_to_1(num, i):
            return num | (1 << i)

        N = len(board)
        rows = [0 for _ in range(N)]
        cols = [0 for _ in range(N)]
        squares = [0 for _ in range(N)]
        sqrt_N = int(math.sqrt(N))

        for i in range(N):
            for j in range(N):
                if board[i][j] == ".": continue
                num = int(board[i][j])
                if get_ith_bit_of_num(rows[i], num) == 1: return False
                if get_ith_bit_of_num(cols[j], num) == 1: return False

                sr = i // sqrt_N
                sc = j // sqrt_N
                si = sr * sqrt_N + sc
                if get_ith_bit_of_num(squares[si], num) == 1: return False

                rows[i] = set_ith_bit_of_num_to_1(rows[i], num)
                cols[j] = set_ith_bit_of_num_to_1(cols[j], num)
                squares[si] = set_ith_bit_of_num_to_1(squares[si], num)

        return True

if __name__ == '__main__':
    sol = Solution()
    board = [[".",".","4",".",".",".","6","3","."],
             [".",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".","9","."],
             [".",".",".","5","6",".",".",".","."],
             ["4",".","3",".",".",".",".",".","1"],
             [".",".",".","7",".",".",".",".","."],
             [".",".",".","5",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]
    result = sol.isValidSudoku(board)
    print(result)


