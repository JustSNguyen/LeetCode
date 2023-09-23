import bisect
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        character_positions = defaultdict(list)
        for i, char in enumerate(t):
            character_positions[char].append(i)

        min_position_to_search = 0
        for char in s:
            index = bisect.bisect_left(character_positions[char], min_position_to_search)
            if index == len(character_positions[char]):
                return False
            min_position_to_search = character_positions[char][index] + 1

        return True

if __name__ == '__main__':
    sol = Solution()
    s = "a"
    t = "a"
    result = sol.isSubsequence(s, t)
    print(result)
