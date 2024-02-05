from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        max_length = 0
        j = 0
        for i, char in enumerate(s):
            count[char] += 1
            while count[char] > 1:
                count[s[j]] -= 1
                j += 1
            max_length = max(max_length, i - j + 1 )

        return max_length

