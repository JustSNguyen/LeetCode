from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        ones = [0 for _ in range(N)]
        for i, string in enumerate(strs):
            for char in string:
                ones[i] += (char == "1")

        dp2 = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(N - 1, -1, -1):
            for cur_m in range(m + 1):
                for cur_n in range(n + 1):
                    if cur_m == 0 and cur_n == 0:
                        dp[cur_m][cur_n] = 0
                        continue

                    number_of_ones = ones[i]
                    number_of_zeros = len(strs[i]) - number_of_ones
                    if number_of_ones > cur_n or number_of_zeros > cur_m:
                        dp[cur_m][cur_n] = dp2[cur_m][cur_n]
                    else:
                        new_m = cur_m - number_of_zeros
                        new_n = cur_n - number_of_ones
                        dp[cur_m][cur_n] = max(dp2[cur_m][cur_n], dp2[new_m][new_n] + 1)

            for cur_m in range(m + 1):
                for cur_n in range(n + 1):
                    dp2[cur_m][cur_n] = dp[cur_m][cur_n]

        return dp[m][n]

if __name__ == '__main__':
    sol = Solution()
    strs = ["10","0001","111001","1","0"]
    m = 4
    n = 3
    result = sol.findMaxForm(strs, m, n)
    print(result)