from functools import lru_cache

class Solution:
    def integerBreak(self, n: int) -> int:

        @lru_cache(maxsize=n)
        def maximum_product_of(n: int) -> int:
            if n == 1:
                return 1

            current_max_product = 1
            for num in range(1, n):
                max_product_1 = maximum_product_of(n - num) * num
                max_product_2 = num * (n - num)
                current_max_product = max(current_max_product, max_product_1, max_product_2)

            return current_max_product

        return maximum_product_of(n)

if __name__ == '__main__':
    sol = Solution()
    n = 10
    result = sol.integerBreak(n)
    print(result)