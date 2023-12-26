class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp_i_plus_1 = [0 for _ in range(target + 1)]
        dp_i_plus_1[0] = 1

        MOD = 10**9 + 7

        for i in range(n - 1, -1, -1):
            dp = [0 for _ in range(target + 1)]
            for cur_target in range(target + 1):
                if cur_target != 0:
                    for j in range(1, min(cur_target, k) + 1):
                        dp[cur_target] += dp_i_plus_1[cur_target - j]
                        dp[cur_target] %= MOD

            dp_i_plus_1 = dp.copy()

        return dp_i_plus_1[target]

if __name__ == '__main__':
    sol = Solution()
    n = 30
    k = 30
    target = 500
    result = sol.numRollsToTarget(n, k, target)
    print(result)