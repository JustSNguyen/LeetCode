from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        def smoothen(i, j):
            total = 0
            sum_value = 0
            offsets = [-1, 0, 1]

            for row_offset in offsets:
                for col_offset in offsets:
                    new_i = i + row_offset
                    new_j = j + col_offset
                    if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n:
                        continue

                    total += 1
                    sum_value += img[new_i][new_j] % 256

            return sum_value // total

        for i in range(m):
            for j in range(n):
                img[i][j] += smoothen(i, j) * 256

        for i in range(m):
            for j in range(n):
                img[i][j] //= 256

        return img
