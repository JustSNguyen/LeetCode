from functools import lru_cache

class Solution:
    def knightDialer(self, n: int) -> int:
        max_rows = 4
        max_cols = 3

        offsets = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]

        MOD = 10**9 + 7

        def is_valid_cell(i, j):
            if i < 0 or j < 0 or i >= max_rows or j >= max_cols:
                return False

            value = 3 * i + j + 1

            if value == 10 or value == 12:
                return False

            return True


        @lru_cache(12 * n)
        def count_phone_number(i, j, n):
            if n == 1:
                return 1

            result = 0
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]

                if not is_valid_cell(ni, nj):
                    continue

                result += count_phone_number(ni, nj, n - 1)
                result %= MOD

            return result

        result = 0
        for i in range(4):
            for j in range(3):
                if is_valid_cell(i, j):
                    result += count_phone_number(i, j, n)
                    result %= MOD

        return result

if __name__ == '__main__':
    sol = Solution()
    n = 1
    result = sol.knightDialer(n)
    print(result)