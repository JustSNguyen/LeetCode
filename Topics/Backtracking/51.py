from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_ith_bit_of_num(num, i):
            return (num >> i) & 1

        def set_ith_bit_to_1(num, i):
            return num | (1 << i)

        self.cols = 0
        self.add_diags = 0
        self.minus_diags = 0

        result = []
        def generate(temp, row_index):
            if row_index == n:
                result.append(temp)
                return

            for col_index in range(n):
                col_is_taken = get_ith_bit_of_num(self.cols, col_index)
                add_diag_is_taken = get_ith_bit_of_num(self.add_diags, row_index + col_index)

                minus_diag_index = row_index - col_index
                if minus_diag_index < 0:
                    minus_diag_index += 2 * n
                minus_diag_is_taken = get_ith_bit_of_num(self.minus_diags, minus_diag_index)

                if col_is_taken or add_diag_is_taken or minus_diag_is_taken:
                    continue

                original_cols = self.cols
                original_add_diags = self.add_diags
                original_minus_diags = self.minus_diags

                self.cols = set_ith_bit_to_1(self.cols, col_index)
                self.add_diags = set_ith_bit_to_1(self.add_diags, row_index + col_index)
                self.minus_diags = set_ith_bit_to_1(self.minus_diags, minus_diag_index)

                new_temp = temp[:]
                row = ["." for _ in range(n)]
                row[col_index] = "Q"
                new_temp.append("".join(row))
                generate(new_temp, row_index + 1)

                self.cols = original_cols
                self.add_diags = original_add_diags
                self.minus_diags = original_minus_diags

        generate([], 0)
        return result

if __name__ == '__main__':
    sol = Solution()
    n = 4
    result = sol.solveNQueens(n)
    print(result)