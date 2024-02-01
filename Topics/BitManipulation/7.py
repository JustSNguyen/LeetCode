import math
class Solution:
    def reverse(self, x: int) -> int:
        MAX_POS = 2147483647
        MAX_NEG = -2147483648

        if x == MAX_NEG:
            return 0

        res = 0
        while x != 0:
            digit = abs(x) % 10

            if res > MAX_POS / 10 or (res == MAX_POS / 10 and digit >= 7):
                return 0
            if res < MAX_NEG / 10 or (res == MAX_NEG / 10 and digit >= 8):
                return 0

            if x < 0:
                digit = -digit

            res = res * 10 + digit
            x = math.trunc(x / 10)

        return res

if __name__ == '__main__':
    sol = Solution()
    test = -123
    result = sol.reverse(test)
    print(result)
