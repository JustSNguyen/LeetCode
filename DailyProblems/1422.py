class Solution:
    def maxScore(self, s: str) -> int:
        max_result = 0 
        if s[0] == "0":
            max_result += 1 
        if s[1] == "1":
            max_result += 1 

        for i in range(len(s) - 1):
            if s[i] == "1":
                max_result += 1

        return max_result

