from typing import List
from functools import lru_cache

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        sorted_pairs = sorted(pairs)
        prev = [sorted_pairs[-1][1] + 1, sorted_pairs[-1][1] + 2]
        cur_length = 0

        for i in range(N - 1, -1, -1):
            cur = sorted_pairs[i]
            if cur[1] < prev[0]:
                cur_length += 1
                prev = cur

        return cur_length

if __name__ == '__main__':
    sol = Solution()
    pairs = [[1, 2], [7, 8], [4, 5]]
    result = sol.findLongestChain(pairs)
    print(result)
