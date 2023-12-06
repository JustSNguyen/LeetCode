class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        l = n - k * 7

        return 28 * k + 7 * k * (k - 1) // 2 + (2 * k + l + 1) * l // 2
