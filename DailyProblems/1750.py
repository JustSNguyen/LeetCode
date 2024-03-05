class Solution:
    def minimumLength(self, s: str) -> int:
        lf = 0
        rg = len(s) - 1
        while lf < rg:
            if s[lf] != s[rg]:
                break

            while lf + 1 < rg and s[lf + 1] == s[lf]:
                lf += 1

            while lf < rg - 1 and s[rg - 1] == s[rg]:
                rg -= 1

            lf += 1
            rg -= 1

        return rg - lf + 1