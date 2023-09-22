import bisect
from typing import List
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        character_positions = defaultdict(list)
        for i, char in enumerate(s):
            character_positions[char].append(i)
        def is_subsequence(word: str) -> bool:
            min_position_to_search = 0
            for char in word:
                index = bisect.bisect_left(character_positions[char], min_position_to_search)
                if index == len(character_positions[char]):
                    return False
                min_position_to_search = character_positions[char][index] + 1

            return True

        number_of_subsequences = 0
        for word in words:
            if is_subsequence(word):
                number_of_subsequences += 1

        return number_of_subsequences

if __name__ == '__main__':
    sol = Solution()
    s = "dsahjpjauf"
    words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    print(sol.numMatchingSubseq(s, words))