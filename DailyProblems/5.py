from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        MOD = 10 ** 9 + 7
        N = len(s)
        base = 311

        base_with_power_of = [1 for _ in range(N)]

        for i in range(1, N):
            base_with_power_of[i] = (base_with_power_of[i - 1] * base) % MOD

        def calculate_string_hash(string: str) -> List[int]:
            N = len(string)
            hash = [0 for _ in range(N)]
            for i, char in enumerate(string):
                if i == 0:
                    hash[i] = ord(char)
                else:
                    hash[i] = (hash[i - 1] * base + ord(char)) % MOD

            return hash

        reversed_s = "".join(reversed(s))

        hash_s = calculate_string_hash(s)
        hash_reversed_s = calculate_string_hash(reversed_s)

        def calculate_hash(hash: List[int], i: int, j: int) -> int:
            if i == 0:
                return hash[j]

            return (hash[j] - hash[i - 1] * base_with_power_of[j - i + 1]) % MOD

        def is_palindrome(i: int, j: int) -> bool:
            reversed_s_i = N - j - 1
            reversed_s_j = N - i - 1
            return calculate_hash(hash_s, i, j) == calculate_hash(hash_reversed_s, reversed_s_i, reversed_s_j)

        lf = 0
        rg = N + 1
        start_of_maximum_even_palindrome = 0
        while rg - lf > 2:
            mid = (rg + lf) // 2
            if mid % 2 != 0:
                mid += 1

            palindrome_exists = False
            for i in range(N - mid + 1):
                if is_palindrome(i, i + mid - 1):
                    start_of_maximum_even_palindrome = i
                    palindrome_exists = True
                    break

            if palindrome_exists:
                lf = mid
            else:
                rg = mid

        maximum_even_palindrome_length = lf

        lf = 0
        rg = N + 1
        start_of_maximum_odd_palindrome = 0
        while rg - lf > 2:
            mid = (rg + lf) // 2
            if mid % 2 != 1:
                mid += 1

            palindrome_exists = False
            for i in range(N - mid + 1):
                if is_palindrome(i, i + mid - 1):
                    start_of_maximum_odd_palindrome = i
                    palindrome_exists = True
                    break

            if palindrome_exists:
                lf = mid
            else:
                rg = mid

        maximum_odd_palindrome_length = lf
        print(maximum_odd_palindrome_length, maximum_even_palindrome_length)

        if maximum_odd_palindrome_length > maximum_even_palindrome_length:
            return s[start_of_maximum_odd_palindrome:start_of_maximum_odd_palindrome + maximum_odd_palindrome_length]

        return s[start_of_maximum_even_palindrome:start_of_maximum_even_palindrome + maximum_even_palindrome_length]


if __name__ == '__main__':
    sol = Solution()
    s = "a"
    result = sol.longestPalindrome(s)
    print(result)
