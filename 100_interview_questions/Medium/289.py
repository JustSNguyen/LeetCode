from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        stack = list()
        stack.append((0, 0))

        while stack:
            i, j = stack.pop()

            if board[i][j] >= 10:
                continue 

            
            alive_cells = 0 

            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1] 
                if ni < 0 or ni >= m or nj < 0 or nj >= n: 
                    continue

                value = board[ni][nj]

                if value == 1 or 10 <= value < 12: 
                    alive_cells += 1 
                
                if value < 10:
                    stack.append((ni, nj))
            
            value = board[i][j]

            if value == 1:
                if 2 <= alive_cells <= 3:
                    board[i][j] = 11 

                else: 
                    board[i][j] = 10 
            
            elif alive_cells == 3: 
                board[i][j] = 13 

            else: 
                board[i][j] = 12

        for i in range(m):
            for j in range(n):
                if board[i][j] == 10 or board[i][j] == 12:
                    board[i][j] = 0 
                else:
                    board[i][j] = 1 

if __name__ == '__main__':
    sol = Solution()
    board = [[1,1],[1,0]]
    sol.gameOfLife(board)
    print(board)
                

            

