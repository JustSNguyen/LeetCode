class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i = 0
        j = 0

        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1

            if j == len(t):
                return False

            i += 1
            j += 1

        return True
