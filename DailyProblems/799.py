from functools import lru_cache


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def invalid_glass_number(row: int, glass_number: int) -> bool:
            return glass_number > row or glass_number < 0

        @lru_cache(maxsize=10005)
        def total_poured_cups_of_champagne_overflow(row: int, glass_number: int) -> float:
            if invalid_glass_number(row, glass_number):
                return 0

            if row == 0:
                return max(0, poured - 1)

            total_poured_cups_of_champagne_received: float = (0.5 * total_poured_cups_of_champagne_overflow(row - 1,
                                                                                                            glass_number - 1) + 0.5 * total_poured_cups_of_champagne_overflow(
                row - 1, glass_number))

            return max(0.0, total_poured_cups_of_champagne_received - 1.0)

        if query_row == 0:
            return min(poured, 1)

        total_poured_cups_of_champagne_received = 0.5 * total_poured_cups_of_champagne_overflow(query_row - 1, query_glass) \
                + 0.5 * total_poured_cups_of_champagne_overflow(query_row - 1, query_glass - 1)

        return min(total_poured_cups_of_champagne_received, 1)

if __name__ == '__main__':
    sol = Solution()
    poured = 1
    query_row = 0
    query_glass = 0
    result = sol.champagneTower(poured, query_row, query_glass)
    print(result)
