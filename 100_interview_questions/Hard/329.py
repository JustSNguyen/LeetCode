from typing import List 

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        longest_increasing_path_dp_result = [[-1 for _ in range(n)] for _ in range(m)]

        def longest_increasing_path_dp(i, j):
            if i < 0 or j < 0 or i >= m or j >= n: 
                return 0 
        
            if longest_increasing_path_dp_result[i][j] != -1:
                return longest_increasing_path_dp_result[i][j]

            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            max_answer = 1
            for offset in offsets:
                next_cell_i, next_cell_j = i + offset[0], j + offset[1]

                if next_cell_i < 0 or next_cell_j < 0 or next_cell_i >= m or next_cell_j >= n:
                    continue 

                if matrix[next_cell_i][next_cell_j] > matrix[i][j]:
                    max_answer = max(max_answer, longest_increasing_path_dp(next_cell_i, next_cell_j) + 1 )

            longest_increasing_path_dp_result[i][j] = max_answer 
            return longest_increasing_path_dp_result[i][j] 
        
        max_answer = 1
        for i in range(m):
            for j in range(n):
                if longest_increasing_path_dp_result[i][j] == -1:
                    max_answer = max(max_answer, longest_increasing_path_dp(i, j))
                else:
                    max_answer = max(max_answer, longest_increasing_path_dp_result[i][j])
        
        return max_answer

if __name__ == "__main__":
    matrix = [[1]]
    sol = Solution()
    result = sol.longestIncreasingPath(matrix)
    print(result)