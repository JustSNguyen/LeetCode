from typing import List 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_cell(start_row, start_col):
            available_numbers = dict()
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    character = board[i][j]

                    if character == ".":
                        continue 

                    num = int(character)

                    if num in available_numbers:
                        return False 

                    available_numbers[num] = True 
            
            return True 
        
        def check_line(line_index, is_row):
            available_numbers = dict()
            for j in range(9):
                character = board[line_index][j]

                if not is_row: 
                    character = board[j][line_index]

                if character == ".":
                    continue 

                number = int(character)
                if number in available_numbers:
                    return False 
                
                available_numbers[number] = True

            return True 
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                valid_cell = check_cell(i, j)
                if not valid_cell:
                    return False 
        
        for i in range(9):
            valid_row = check_line(i, True)
            if not valid_row:
                return False 
            
            valid_column = check_line(i, False)
            if not valid_column:
                return False
        
        return True 

if __name__ == '__main__':
    board = [[".",".","4",".",".",".","6","3","."],
             [".",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".","9","."],
             [".",".",".","5","6",".",".",".","."],
             ["4",".","3",".",".",".",".",".","1"],
             [".",".",".","7",".",".",".",".","."],
             [".",".",".","5",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]

    sol = Solution()

    result = sol.isValidSudoku(board)
    print(result)
