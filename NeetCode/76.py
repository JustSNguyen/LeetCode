from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        expected_char_count = defaultdict(int)
        for char in t:
            expected_char_count[char] += 1

        def is_valid(cur_char_count):
            for char in expected_char_count:
                if expected_char_count[char] > cur_char_count[char]:
                    return False

            return True

        cur_char_count = defaultdict(int)

        i = 0
        j = 0
        start = -1
        end = -1
        min_window = len(s) + 1

        while j < len(s):
            char = s[j]
            cur_char_count[char] += 1

            while is_valid(cur_char_count) and i < len(s):
                new_length = j - i + 1

                if new_length < min_window:
                    min_window = new_length
                    start = i
                    end = j

                cur_char_count[s[i]] -= 1
                i += 1

            j += 1

        if min_window == len(s) + 1:
            return ""

        return s[start: end + 1]

if __name__ == '__main__':
    sol = Solution()
    s = "ABCDEF"
    t = "ABCDEF"
    result = sol.minWindow(s, t)
    print(result)
