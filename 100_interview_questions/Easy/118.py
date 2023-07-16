from typing import List 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev_row = []

        pascal_triangle = []

        for row in range(numRows):
            cur_row = []
            if row == 0: 
                cur_row.append(1)
            else:
                for i in range(row + 1):
                    if i == 0 or i == row: 
                        cur_row.append(1)
                    else:
                        cur_row.append(prev_row[i] + prev_row[i - 1])
            
            pascal_triangle.append(cur_row)
            prev_row = cur_row 
        
        return pascal_triangle

if __name__ == "__main__":
    sol = Solution()
    numRows = 5 
    result = sol.generate(numRows)
    print(result)