from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = defaultdict(int)
        for char in s1:
            need[char] += 1

        cnt = defaultdict(int)
        i = 0
        for j in range(len(s2)):
            cnt[s2[j]] += 1
            if j - i + 1 > len(s1):
                cnt[s2[i]] -= 1
                i += 1

            if j - i + 1 == len(s1):
                found = True
                for char in need:
                    if need[char] != cnt[char]:
                        found = False
                        break

                if found:
                    return True

        return False
