import heapq
from typing import List

class Solution:
    def kWeakestRows(self, matrix: List[List[int]], k: int) -> List[int]:
        number_of_rows = len(matrix)
        current_k_weakest_rows_max_heap = []
        number_of_soldiers_at_row = [sum(row) for row in matrix]

        for i in range(number_of_rows):
            if len(current_k_weakest_rows_max_heap) < k:
                heapq.heappush(current_k_weakest_rows_max_heap,(-number_of_soldiers_at_row[i], -i))
            else:
                strongest_row_in_current_k_weakest_rows = -(current_k_weakest_rows_max_heap[0][0])
                if strongest_row_in_current_k_weakest_rows > number_of_soldiers_at_row[i]:
                    heapq.heappop(current_k_weakest_rows_max_heap)
                    heapq.heappush(current_k_weakest_rows_max_heap, (-number_of_soldiers_at_row[i], -i))

        result = []
        while current_k_weakest_rows_max_heap:
            result.append(-heapq.heappop(current_k_weakest_rows_max_heap)[1])

        return result[::-1]

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,0,0,0],
              [1,1,1,1],
              [1,0,0,0],
              [1,0,0,0]]
    k = 2
    result = sol.kWeakestRows(matrix, k)
    print(result)