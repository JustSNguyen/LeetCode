import math
from functools import lru_cache


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def get_kth_word_at_nth_row(k: int) -> int:
            if k == 1:
                return 0

            parent_word_from_last_row = get_kth_word_at_nth_row(math.ceil(k / 2))
            if k % 2 == 0:
                return 1 - parent_word_from_last_row

            return parent_word_from_last_row

        return get_kth_word_at_nth_row(k)

if __name__ == '__main__':
    sol = Solution()
    n = 10
    k = 1
    result = sol.kthGrammar(n, k)
    print(result)