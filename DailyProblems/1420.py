from functools import lru_cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=500000)
        def prefix(i, remain, current_max):
            result = 0
            for j in range(current_max + 1):
                result += dp(i, remain, j)
                result = result % MOD

            return result

        @lru_cache(maxsize=500000)
        def dp(i, remain, max_so_far):
            if i == n:
                if remain == 0:
                    return 1

                return 0

            ans = (max_so_far * dp(i + 1, remain, max_so_far)) % MOD
            ans += prefix(i + 1, remain - 1, m) - prefix(i + 1, remain - 1, max_so_far)
            ans = ans % MOD

            return ans

        return dp(0,k, 0)

if __name__ == '__main__':
    sol = Solution()
    n = 2
    m = 3
    k = 1
    res = sol.numOfArrays(n, m, k)
    print(res)