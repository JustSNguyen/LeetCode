from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        @lru_cache(maxsize=N*N)
        def is_palindrome(i, j):
            if i >= j:
                return True

            if s[i] != s[j]:
                return False

            return is_palindrome(i + 1, j - 1)

        count = 0
        for i in range(N):
            for j in range(i, N):
                if is_palindrome(i, j):
                    count += 1

        return count