from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        j = 0
        max_length = 0
        for i, char in enumerate(s):
            cnt[char] += 1
            while (i - j + 1) - max(cnt.values()) > k:
                cnt[s[j]] -= 1
                j += 1

            max_length = max(max_length, i - j + 1)

        return max_length
