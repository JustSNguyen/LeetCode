from typing import List

class Solution:
    def print_square_matrix(self, matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end = " ")
            
            print("")
        
    def reverse(self, matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][N - j - 1] = matrix[i][N - j - 1], matrix[i][j]

    def transpose(self, matrix: List[List[int]]):
        N = len(matrix)
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.print_square_matrix(matrix)
        self.transpose(matrix)
        self.reverse(matrix)

if __name__ == '__main__':
    sol = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix)