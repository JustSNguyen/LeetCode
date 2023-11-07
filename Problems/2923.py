from typing import List
from functools import cmp_to_key

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        def compare(i, j):
            if grid[i][j] == 1:
                return 1

            return -1

        N = len(grid)
        teams = [i for i in range(N)]
        sorted_teams = sorted(teams, key=cmp_to_key(compare))
        return sorted_teams[-1]