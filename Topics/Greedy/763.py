from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = dict()

        for i, char in enumerate(s):
            last_pos[char] = i

        result = []
        lf = 0
        rg = 0
        i = 0
        while i < len(s):
            rg = max(rg, last_pos[s[i]])
            if i == rg:
                result.append(rg - lf + 1)
                rg += 1
                lf = rg

            i += 1

        return result

if __name__ == '__main__':
    sol = Solution()
    str = "aaaa"
    result = sol.partitionLabels(str)
    print(result)