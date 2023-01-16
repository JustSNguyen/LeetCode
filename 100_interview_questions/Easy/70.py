class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [-1 for _ in range(n + 1)]
        steps[0] = steps[1] = 1

        def climb_stairs_dp(n):
            if steps[n] != -1:
                return steps[n]
            
            steps[n] = climb_stairs_dp(n - 1) + climb_stairs_dp(n - 2)
            return steps[n]

        return climb_stairs_dp(n)

if __name__ == '__main__':
    sol = Solution()
    result = sol.climbStairs(3)
    print(result)
