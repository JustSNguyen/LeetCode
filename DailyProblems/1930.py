import bisect
from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        positions = defaultdict(list)
        for i, char in enumerate(s):
            positions[char].append(i)

        result = 0

        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if len(positions[char]) < 2:
                continue

            first_pos = positions[char][0]
            last_pos = positions[char][-1]
            for j in range(ord('a'), ord('z') + 1):
                mid_char = chr(j)
                if len(positions[mid_char]) == 0:
                    continue

                mid_pos_index = bisect.bisect_right(positions[mid_char], first_pos)
                if mid_pos_index == len(positions[mid_char]):
                    continue

                mid_pos = positions[mid_char][mid_pos_index]
                if first_pos < mid_pos < last_pos:
                    result += 1

        return result

if __name__ == '__main__':
    sol = Solution()
    s = "aabca"
    print(sol.countPalindromicSubsequence(s))


