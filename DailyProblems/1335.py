from typing import List
from functools import lru_cache

class Solution:
    def minDifficulty(self, difficulties: List[int], d: int) -> int:
        N = len(difficulties)
        INF = 10**6

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == d - 1:
                return max(difficulties[i:])

            min_result = INF
            max_so_far = 0
            for k in range(i, N - d + j + 1):
                max_so_far = max(max_so_far, difficulties[k])
                min_result = min(min_result, max_so_far + dp(k + 1, j + 1))

            return min_result

        return -1 if N < d else dp(0, 0)


if __name__ == '__main__':
    sol = Solution()
    jobDifficulty = [1]
    d = 2
    result = sol.minDifficulty(jobDifficulty, d)
    print(result)