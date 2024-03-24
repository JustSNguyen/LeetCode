from typing import List 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_ith_bit(num, i):
            return (num >> i) & 1 
        
        def set_ith_bit_to_1(num, i):
            return num | (1 << i)

        self.cols = 0 
        self.add_diags = 0 
        self.minus_diags = 0 
        results = []
        def backtrack(i, result):
            if i == n:
                results.append(result)
                return 
            
            original_cols = self.cols 
            original_add_diags = self.add_diags
            original_minus_diags = self.minus_diags
            for j in range(n):
                if get_ith_bit(self.cols, j) == 1:
                    continue 

                if get_ith_bit(self.add_diags, i + j) == 1:
                    continue 
                
                if get_ith_bit(self.minus_diags, i - j + 2 * n) == 1:
                    continue 

                self.cols = set_ith_bit_to_1(self.cols, j)
                self.add_diags = set_ith_bit_to_1(self.add_diags, i + j)
                self.minus_diags = set_ith_bit_to_1(self.minus_diags, i - j + 2 * n)

                row = []
                for k in range(n):
                    if k != j:
                        row.append(".")
                    else:
                        row.append("Q")

                row = "".join(row)
                new_result = result[:]
                new_result.append(row)
                backtrack(i + 1, new_result)

                self.cols = original_cols
                self.add_diags = original_add_diags
                self.minus_diags = original_minus_diags
        
        backtrack(0, [])

        return results 
