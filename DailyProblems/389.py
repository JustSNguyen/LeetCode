from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_char_count = defaultdict(int)
        t_char_count = defaultdict(int)

        for char in s:
            s_char_count[char] += 1

        for char in t:
            t_char_count[char] += 1

        for char in t_char_count:
            if t_char_count[char] == s_char_count[char] + 1:
                return char

if __name__ == '__main__':
    sol = Solution()
    s = "adc"
    t = "cdda"
    print(sol.findTheDifference(s, t))