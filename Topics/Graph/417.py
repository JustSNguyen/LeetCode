from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])

        pacific = [[False for _ in range(N)] for _ in range(M)]
        atlantic = [[False for _ in range(N)] for _ in range(M)]
        processed_pacific = [[False for _ in range(N)] for _ in range(M)]
        processed_atlantic = [[False for _ in range(N)] for _ in range(M)]

        def dfs_and_update(si, sj, array, processed):
            stack = [(si, sj)]

            while stack:
                ci, cj = stack.pop()
                if processed[ci][cj]:
                    continue

                processed[ci][cj] = True
                array[ci][cj] = True

                offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for offset in offsets:
                    ni, nj = ci + offset[0], cj + offset[1]
                    if ni < 0 or nj < 0 or ni >= M or nj >= N or processed[ni][nj] or heights[ni][nj] < heights[ci][cj]:
                        continue

                    stack.append((ni, nj))

        for j in range(N):
            dfs_and_update(0, j, pacific, processed_pacific)
            dfs_and_update(M - 1, j, atlantic, processed_atlantic)

        for i in range(M):
            dfs_and_update(i, 0, pacific, processed_pacific)
            dfs_and_update(i, N - 1, atlantic, processed_atlantic)

        result = []
        for i in range(M):
            for j in range(N):
                if atlantic[i][j] and pacific[i][j]:
                    result.append([i, j])

        return result
