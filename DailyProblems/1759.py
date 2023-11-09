class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        prev_char = ""
        N = 0
        for char in s:
            if char != prev_char:
                delta = (N * (N + 1) // 2) % MOD
                total += delta
                total %= MOD
                N = 1
            else:
                N += 1

            prev_char = char

        delta = (N * (N + 1) // 2) % MOD
        total += delta
        total %= MOD

        return total

if __name__ == '__main__':
    sol = Solution()
    s = "a"
    result = sol.countHomogenous(s)
    print(result)