from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def get_length(char, count):
            if char == "" or count == 0:
                return 0

            if count == 1:
                return 1

            if count < 10:
                return 2

            if count < 100:
                return 3

            return 4

        N = len(s)

        all_same = True
        prev = s[0]
        for i in range(1, N):
            if s[i] != prev:
                all_same = False
                break

            prev = s[i]

        if all_same:
            return get_length(s[0], N - k)

        @lru_cache(maxsize=None)
        def dp(i, k, prev_char, count_prev_char):
            if i == N:
                return get_length(prev_char, count_prev_char)

            cur_char = s[i]
            if k == 0:
                if cur_char == prev_char:
                    return dp(i + 1, 0, cur_char, min(count_prev_char + 1, 10))

                return dp(i + 1, 0, cur_char, 1) + get_length(prev_char, count_prev_char)

            option1 = dp(i + 1, k - 1, prev_char, count_prev_char)
            option2 = dp(i + 1, k, cur_char, min(count_prev_char + 1, 10))
            if cur_char != prev_char:
                option2 = dp(i + 1, k, cur_char, 1) + get_length(prev_char, count_prev_char)

            return min(option1, option2)

        return dp(0, k, "", 0)

if __name__ == '__main__':
    sol = Solution()
    s = "a"
    k = 1
    result = sol.getLengthOfOptimalCompression(s, k)
    print(result)