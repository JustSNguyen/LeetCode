from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        max_cnt = 0
        longest = 0 

        for i, char in enumerate(s):
            cnt[char] += 1 
            max_cnt = max(max_cnt, cnt[char])

            if longest + 1 - max_cnt <= k:
                longest += 1
            else:
                j = i - longest
                cnt[s[j]] -= 1 
        
        return longest 