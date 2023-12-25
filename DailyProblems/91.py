class Solution:
    def numDecodings(self, s: str) -> int:
        num_to_char = {i: chr(i - 1 + ord('A')) for i in range(1, 27)}
        N = len(s)

        dp_i_plus_1 = 1
        dp_i_plus_2 = 0

        for i in range(N - 1, -1, -1):
            result = 0
            num = int(s[i])
            if num not in num_to_char:
                dp_i_plus_2 = dp_i_plus_1
                dp_i_plus_1 = 0
                continue

            result += dp_i_plus_1

            if i < N - 1 and int(s[i:i+2]) in num_to_char:
                result += dp_i_plus_2

            dp_i_plus_2 = dp_i_plus_1
            dp_i_plus_1 = result

        return dp_i_plus_1

if __name__ == '__main__':
    sol = Solution()
    s = "241687"
    result = sol.numDecodings(s)
    print(result)
