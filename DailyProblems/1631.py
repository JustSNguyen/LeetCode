import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def is_invalid_cell(row_index, col_index):
            return row_index < 0 or col_index < 0 or row_index >= len(heights) or col_index >= len(heights[0])

        number_of_rows = len(heights)
        number_of_columns = len(heights[0])
        processed_cells = [[False for _ in range(number_of_columns)] for _ in range(number_of_rows)]

        INF = 10**6
        minimum_effort_to_cell = [[INF for _ in range(number_of_columns)] for _ in range(number_of_rows)]
        minimum_effort_to_cell[0][0] = 0

        weights_min_heap = []

        # first element is the weight, second is the row_index and third is the col_index
        heapq.heappush(weights_min_heap, (0, 0, 0))

        while weights_min_heap:
            min_effort, row_index, col_index = heapq.heappop(weights_min_heap)
            if processed_cells[row_index][col_index]:
                continue

            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for offset in offsets:
                next_row_index = row_index + offset[0]
                next_col_index = col_index + offset[1]
                if is_invalid_cell(next_row_index, next_col_index):
                    continue

                effort_between_two_cells = abs(heights[row_index][col_index] - heights[next_row_index][next_col_index])
                effort = max(effort_between_two_cells, min_effort)
                if effort < minimum_effort_to_cell[next_row_index][next_col_index]:
                    minimum_effort_to_cell[next_row_index][next_col_index] = effort
                    heapq.heappush(weights_min_heap, (effort, next_row_index, next_col_index))

        return minimum_effort_to_cell[number_of_rows - 1][number_of_columns - 1]

if __name__ == '__main__':
    sol = Solution()
    heights = [[1,10,6,7,9,10,4,9]]
    print(sol.minimumEffortPath(heights))