from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        number_of_rows = len(matrix)
        number_of_cols = len(matrix[0])

        self.prefix_sum = [[matrix[i][j] for j in range(number_of_cols)] for i in range(number_of_rows)]

        for i in range(number_of_rows):
            for j in range(number_of_cols):
                if i == 0 and j > 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i][j - 1]
                if j == 0 and i > 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i - 1][j]
                if i > 0 and j > 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i - 1][j] + self.prefix_sum[i][j - 1] - self.prefix_sum[i - 1][j - 1]

    def sumRegion(self, i1: int, j1: int, i2: int, j2: int) -> int:
        result = self.prefix_sum[i2][j2]
        if i1 > 0:
            result -= self.prefix_sum[i1 - 1][j2]
        if j1 > 0:
            result -= self.prefix_sum[i2][j1 - 1]
        if i1 > 0 and j1 > 0:
            result += self.prefix_sum[i1 - 1][j1 - 1]

        return result


if __name__ == "__main__":
    test = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    sol = NumMatrix(test)

    print(sol.sumRegion(0, 1, 4, 1))

