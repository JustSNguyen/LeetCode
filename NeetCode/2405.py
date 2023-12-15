from collections import defaultdict

class Solution:
    def partitionString(self, s: str) -> int:
        char_count = defaultdict(int)
        result = 1

        for i in range(len(s)):
            cur_char = s[i]

            if char_count[cur_char] == 1:
                for char in char_count:
                    char_count[char] = 0

                result += 1

            char_count[cur_char] = 1

        return result

if __name__ == '__main__':
    sol = Solution()
    s = "abacaba"
    result = sol.partitionString(s)
    print(result)