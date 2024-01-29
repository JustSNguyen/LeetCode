from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        processed = None

        def dfs(i, j, k):
            if board[i][j] != word[k] or processed[i][j]:
                return False

            if k == len(word) - 1:
                return True

            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            processed[i][j] = True
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if ni < 0 or nj < 0 or ni >= M or nj >= N or processed[ni][nj]:
                    continue

                if dfs(ni, nj, k + 1):
                    return True
                processed[ni][nj] = False

            return False

        for i in range(M):
            for j in range(N):
                processed = [[False for _ in range(N)] for _ in range(M)]
                if dfs(i, j, 0):
                    return True

        return False

if __name__ == '__main__':
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = sol.exist(board, word)
    print(result)