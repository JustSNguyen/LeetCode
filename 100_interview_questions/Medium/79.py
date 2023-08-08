from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        number_of_rows, number_of_columns = len(board), len(board[0])

        def dfs(i, j, visited, cur_word_index):
            if i< 0 or j < 0 or i>= number_of_rows or j >= number_of_columns or visited[i][j]:
                return False
                
            matching_char = word[cur_word_index]
            if board[i][j] != matching_char:
                return False 

            if cur_word_index == len(word) - 1:
                return True 
            
            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]


            visited[i][j] = True 
            for offset in offsets:
                next_i = i + offset[0]
                next_j = j + offset[1]
                temp_result = dfs(next_i, next_j, visited, cur_word_index + 1)
                if temp_result:
                    return True 
            
            visited[i][j] = False 
            return False 
        
        for i in range(number_of_rows):
            for j in range(number_of_columns):
                visited = [[False for _ in range(number_of_columns)] for _ in range(number_of_rows)]
                exist = dfs(i, j, visited, 0)
                if exist:
                    return True 

        return False 
    
if __name__ == "__main__":
    sol = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCEFSADEESE"
    print(sol.exist(board, word))
                
