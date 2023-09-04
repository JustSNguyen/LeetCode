from functools import lru_cache


class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)

        if n == 1:
            return 1

        if n == 2 and int(num) % 25 == 0:
            return 0

        if n == 2 and (num[0] == '0' or num[1] == '0'):
            return 1

        if n == 2:
            return 2

        @lru_cache(maxsize=100000)
        def minimum_operations_dp(index, last_three_digits):
            if index == 0:
                new_last_three_digits = num[index] + last_three_digits
                if int(new_last_three_digits) % 25 == 0:
                    return 0

                if last_three_digits == '0':
                    return 1

                return 1 + len(last_three_digits)

            digit = num[index]
            new_last_three_digits = digit + last_three_digits
            if len(new_last_three_digits) == 3:
                last_three_digits_num = int(new_last_three_digits)
                if last_three_digits_num % 25 == 0:
                    return 0

                return 1 + minimum_operations_dp(index - 1, last_three_digits)

            return min(1 + minimum_operations_dp(index - 1, last_three_digits),
                       minimum_operations_dp(index - 1, new_last_three_digits))

        return minimum_operations_dp(n - 1, "")


if __name__ == '__main__':
    sol = Solution()
    num = "2908305"
    result = sol.minimumOperations(num)
    print(result)
