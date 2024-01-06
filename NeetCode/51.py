from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        taken_col = [False for _ in range(n)]
        taken_sum_diags = [False for _ in range(2 * n)]
        taken_minus_diags = [False for _ in range(2 * n)]
        all_results = []

        def generate_answers(row_index, temp_result):
            if row_index == n:
                all_results.append(temp_result)
                return

            for col_index in range(n):
                if taken_col[col_index]:
                    continue

                if taken_sum_diags[row_index + col_index]:
                    continue

                minus_diag = row_index - col_index
                if minus_diag < 0:
                    minus_diag += 2 * n

                if taken_minus_diags[minus_diag]:
                    continue

                row_string = []
                for i in range(n):
                    if i == col_index:
                        row_string.append("Q")
                    else:
                        row_string.append(".")

                row_string = "".join(row_string)
                new_result = temp_result + [row_string]

                taken_col[col_index] = True
                taken_sum_diags[row_index + col_index] = True
                taken_minus_diags[minus_diag] = True

                generate_answers(row_index + 1, new_result)

                taken_col[col_index] = False
                taken_sum_diags[row_index + col_index] = False
                taken_minus_diags[minus_diag] = False

        generate_answers(0, [])

        return all_results

if __name__ == '__main__':
    sol = Solution()
    n = 4
    result = sol.solveNQueens(n)
    print(result)





