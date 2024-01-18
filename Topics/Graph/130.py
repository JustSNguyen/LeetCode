from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M = len(board)
        N = len(board[0])

        should_flip = [[True for _ in range(N)] for _ in range(M)]

        def dfs_and_update(si, sj):
            stack = [(si, sj)]

            while stack:
                ci, cj = stack.pop()
                if not should_flip[ci][cj]:
                    continue

                should_flip[ci][cj] = False

                offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for offset in offsets:
                    ni, nj = ci + offset[0], cj + offset[1]

                    if ni < 0 or nj < 0 or ni >= M or nj >= N or not should_flip[ni][nj] or board[ni][nj] == "X":
                        continue

                    stack.append((ni, nj))

        for i in range(M):
            if should_flip[i][0] and board[i][0] == "O":
                dfs_and_update(i, 0)

            if should_flip[i][N - 1] and board[i][N - 1] == "O":
                dfs_and_update(i, N - 1)

        for j in range(N):
            if should_flip[0][j] and board[0][j] == "O":
                dfs_and_update(0, j)

            if should_flip[M - 1][j] and board[M - 1][j] == "O":
                dfs_and_update(M - 1, j)

        for i in range(M):
            for j in range(N):
                if should_flip[i][j]:
                    board[i][j] = "X"

