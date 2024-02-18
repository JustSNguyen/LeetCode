from typing import List 

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        n = len(s)
        words_set = set(words)
        
        dp = [False for _ in range(n + 1)]
        dp[n] = True 

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                word = s[i:j + 1]
                if word in words_set and dp[j + 1]:
                    dp[i] = True 
                    break 
        
        return dp[0]
