from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        L = len(word)

        def dfs(i, j, k):
            if k == L - 1:
                return True 

            board[i][j] = "#"

            offsets = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if ni < 0 or nj < 0 or ni == m or nj == n or board[ni][nj] == "#" or board[ni][nj] != word[k + 1]:
                    continue 

                if dfs(ni, nj, k + 1):
                    return True 
            
            board[i][j] = word[k]
            return False 
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True 

        return False 